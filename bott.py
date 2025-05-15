from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from dataset_loader import load_dataset


TOKEN = "8073936334:AAHHTXBLiCZfGuneD5Z2IV9WRDafXii_UQE"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print("دستور /start دریافت شد ✅")
    await update.message.reply_text("سلام! \n"
            "دستورهای قابل استفاده:\n"
            "/start - شروع\n"
            "/help - راهنما\n"
            "/about - درباره ربات\n"
            "/dataset - نمایش نمونه‌ای از دیتاست\n"
            "/search <نام اپلیکیشن> - جستجوی اپلیکیشن\n\n"
            "مثال:\n/search Instagram")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print("دستور /help دریافت شد ✅")
    await update.message.reply_text(
        "📌 راهنما:\n"
        "/start - شروع به کار بات\n"
        "/help - نمایش این راهنما\n"
        "/about - درباره بات\n"
        "/dataset - نمایش نمونه‌ای از دیتاست\n"
        "/search <نام اپلیکیشن> - جستجوی اطلاعات اپ مورد نظر\n\n"
        "مثال:\n/search Instagram"
    )

async def about_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print("دستور /about دریافت شد ✅")
    await update.message.reply_text(
        "این بات برای آنالیز اطلاعات اپلیکیشن‌های گوگل پلی ساخته شده است. 🎉"
    )
async def dataset(update: Update, context: ContextTypes.DEFAULT_TYPE):
    df = load_dataset()
    sample = df[['App', 'Category', 'Rating']].head(3).to_string(index=False)
    await update.message.reply_text(f"📊 نمونه‌ای از دیتاست:\n\n{sample}")

async def search(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("❗ لطفاً نام اپلیکیشن مورد نظر را بنویسید.\nمثال:\n/search Instagram")
        return

    query = " ".join(context.args).lower()
    df = load_dataset()

    result = df[df['App'].str.lower() == query]

    if result.empty:
        await update.message.reply_text("❌ اپلیکیشنی با این نام پیدا نشد.")
    else:
        app_info = result.iloc[0]
        name = app_info['App']
        category = app_info['Category']
        rating = app_info['Rating']
        installs = app_info['Installs'] if 'Installs' in app_info else 'نامشخص'
        await update.message.reply_text(
            f"🔍 نتیجه جستجو:\n"
            f"📱 نام: {name}\n"
            f"🏷️ دسته: {category}\n"
            f"⭐ امتیاز: {rating}\n"
            f"⬇️ نصب‌ها: {installs}"
        )


app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("about", about_command))
app.add_handler(CommandHandler("dataset", dataset))
app.add_handler(CommandHandler("search", search))



print("🚀 Bot is running...")
app.run_polling()