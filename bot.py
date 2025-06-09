import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

load_dotenv()
TOKEN = os.getenv("TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print("دستور /start دریافت شد ✅")
    await update.message.reply_text(
"سلام! خوش آمدید به ربات ما."
"برای دیدن راهنمای دستورات، لطفاً از دستور /help استفاده کنید. 📋")

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


app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("help", help_command))

print("🚀 Bot is running...")
app.run_polling()
