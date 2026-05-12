from telegram import ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

TOKEN = "8297614142:AAFtxrsxgBoZuW6gUjdHAQhR9_Y8I-XUnsY"

# استارت
def start(update, context):

    keyboard = [
        ["❤️ سوالات قلب", "🌬 سوالات تنفس"],
        ["📚 جزوه ها", "☎️ پشتیبانی"]
    ]

    reply_markup = ReplyKeyboardMarkup(
        keyboard,
        resize_keyboard=True
    )

    update.message.reply_text(
        "سلام 👋\nچطور میتونم کمکتون کنم؟",
        reply_markup=reply_markup
    )

# دکمه ها
def handle_message(update, context):

    text = update.message.text

    if text == "❤️ سوالات قلب":
        update.message.reply_text(
            "1- قلب چند حفره دارد؟\n2- وظیفه قلب چیست؟"
        )

    elif text == "🌬 سوالات تنفس":
        update.message.reply_text(
            "1- ریه چه کاری انجام میدهد؟"
        )

    elif text == "📚 جزوه ها":
        update.message.reply_text(
            "جزوه ها به زودی اضافه میشوند"
        )

    elif text == "☎️ پشتیبانی":
        update.message.reply_text(
            "@yourid"
        )

# اجرای بات
updater = Updater(TOKEN, use_context=True)

dp = updater.dispatcher

dp.add_handler(CommandHandler("start", start))
dp.add_handler(MessageHandler(Filters.text, handle_message))

print("Bot running...")

updater.start_polling()
updater.idle()
