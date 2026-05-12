from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

TOKEN = "8297614142:AAFtxrsxgBoZuW6gUjdHAQhR9_Y8I-XUnsY"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    keyboard = [
        ["❤️ سوالات قلب", "🌬 سوالات تنفس"],
        ["📚 جزوه ها", "☎️ پشتیبانی"]
    ]

    reply_markup = ReplyKeyboardMarkup(
        keyboard,
        resize_keyboard=True
    )

    await update.message.reply_text(
        "سلام 👋\nچطور میتونم کمکتون کنم؟",
        reply_markup=reply_markup
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = update.message.text

    if text == "❤️ سوالات قلب":
        await update.message.reply_text(
            "1- قلب چند حفره دارد؟\n2- وظیفه قلب چیست؟"
        )

    elif text == "🌬 سوالات تنفس":
        await update.message.reply_text(
            "1- ریه چه کاری انجام میدهد؟"
        )

    elif text == "📚 جزوه ها":
        await update.message.reply_text(
            "جزوه ها به زودی اضافه میشوند"
        )

    elif text == "☎️ پشتیبانی":
        await update.message.reply_text(
            "@yourid"
        )

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))

app.add_handler(
    MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message)
)

print("Bot running...")

app.run_polling()

