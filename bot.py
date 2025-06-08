import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

load_dotenv()
TOKEN = os.getenv("TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print("دستور /start دریافت شد ✅")
    await update.message.reply_text("سلام! خوش آمدید به ربات ما.")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))

print("🚀 Bot is running...")
app.run_polling()
