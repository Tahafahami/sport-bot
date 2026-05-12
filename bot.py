from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = "8297614142:AAFtxrsxgBoZuW6gUjdHAQhR9_Y8I-XUnsY"

# سوالات
QUESTIONS = [
    {
        "q": "قلب چند حفره دارد؟",
        "options": ["2", "3", "4", "5"],
        "answer": "4"
    },

    {
        "q": "وظیفه قلب چیست؟",
        "options": ["تنفس", "پمپاژ خون", "هضم غذا", "دیدن"],
        "answer": "پمپاژ خون"
    }
]

# ذخیره وضعیت کاربران
user_score = {}
user_index = {}

# استارت
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.from_user.id

    user_score[user_id] = 0
    user_index[user_id] = 0

    await send_question(update, context)

# ارسال سوال
async def send_question(update, context):
    user_id = update.effective_user.id
    index = user_index[user_id]

    if index >= len(QUESTIONS):
        score = user_score[user_id]

        await update.message.reply_text(
            f"🎉 امتحان تمام شد\nنمره شما: {score} از {len(QUESTIONS)}"
        )
        return

    q = QUESTIONS[index]

    keyboard = [
        [InlineKeyboardButton(opt, callback_data=opt)]
        for opt in q["options"]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        f"سوال {index+1}:\n{q['q']}",
        reply_markup=reply_markup
    )

# بررسی جواب
async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    user_id = query.from_user.id
    index = user_index[user_id]

    q = QUESTIONS[index]

    if query.data == q["answer"]:
        user_score[user_id] += 1
        text = "✔ جواب درست"
    else:
        text = f"❌ غلط\nجواب صحیح: {q['answer']}"

    user_index[user_id] += 1

    await query.edit_message_text(text)

    if user_index[user_id] < len(QUESTIONS):

        next_q = QUESTIONS[user_index[user_id]]

        keyboard = [
            [InlineKeyboardButton(opt, callback_data=opt)]
            for opt in next_q["options"]
        ]

        reply_markup = InlineKeyboardMarkup(keyboard)

        await context.bot.send_message(
            chat_id=user_id,
            text=f"سوال {user_index[user_id]+1}:\n{next_q['q']}",
            reply_markup=reply_markup
        )

    else:
        score = user_score[user_id]

        await context.bot.send_message(
            chat_id=user_id,
            text=f"🏁 امتحان تمام شد\nنمره شما: {score} از {len(QUESTIONS)}"
        )

# اجرای بات
app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(button))

print("Bot running...")

app.run_polling()