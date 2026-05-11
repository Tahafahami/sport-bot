from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
)

TOKEN = "8297614142:AAFtxrsxgBoZuW6gUjdHAQhR9_Y8I-XUnsY"

# دستور استارت
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text(
        "سلام 👋\n"
        "چطور می‌تونم کمکتون کنم؟"
    )

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))

print("Bot running...")

app.run_polling()
git init
git add .
git commit -m "first bot"