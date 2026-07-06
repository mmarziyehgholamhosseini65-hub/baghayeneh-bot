from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ConversationHandler, ContextTypes

NAME, PHONE, MESSAGE = range(3)

BOT_TOKEN = "YOUR_BOT_TOKEN"
ADMIN_ID = 123456789

user_data = {}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🌿 به باغ آینه خوش آمدید\nنام خود را وارد کنید:")
    return NAME

async def get_name(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.chat_id
    user_data[user_id] = {"name": update.message.text}

    keyboard = [[KeyboardButton("📱 ارسال شماره", request_contact=True)]]
    await update.message.reply_text(
        "شماره خود را ارسال کنید:",
        reply_markup=ReplyKeyboardMarkup(keyboard, one_time_keyboard=True)
    )
    return PHONE

async def get_phone(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.chat_id
    user_data[user_id]["phone"] = update.message.contact.phone_number

    await update.message.reply_text("پیام یا درخواست خود را بنویسید:")
    return MESSAGE

async def get_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.chat_id
    user_data[user_id]["message"] = update.message.text

    info = user_data[user_id]

    await update.message.reply_text("✅ درخواست شما ثبت شد")

    await context.bot.send_message(
        chat_id=ADMIN_ID,
        text=f"""
📥 درخواست جدید

👤 نام: {info['name']}
📞 شماره: {info['phone']}
💬 پیام: {info['message']}
"""
    )

    return ConversationHandler.END

app = Application.builder().token(BOT_TOKEN).build()

conv = ConversationHandler(
    entry_points=[CommandHandler("start", start)],
    states={
        NAME: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_name)],
        PHONE: [MessageHandler(filters.CONTACT, get_phone)],
        MESSAGE: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_message)],
    },
    fallbacks=[]
)

app.add_handler(conv)

app.run_polling()from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ConversationHandler, ContextTypes

NAME, PHONE, MESSAGE = range(3)

BOT_TOKEN = "YOUR_BOT_TOKEN"
ADMIN_ID = 123456789

user_data = {}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🌿 به باغ آینه خوش آمدید\nنام خود را وارد کنید:")
    return NAME

async def get_name(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.chat_id
    user_data[user_id] = {"name": update.message.text}

    keyboard = [[KeyboardButton("📱 ارسال شماره", request_contact=True)]]
    await update.message.reply_text(
        "شماره خود را ارسال کنید:",
        reply_markup=ReplyKeyboardMarkup(keyboard, one_time_keyboard=True)
    )
    return PHONE

async def get_phone(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.chat_id
    user_data[user_id]["phone"] = update.message.contact.phone_number

    await update.message.reply_text("پیام یا درخواست خود را بنویسید:")
    return MESSAGE

async def get_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.chat_id
    user_data[user_id]["message"] = update.message.text

    info = user_data[user_id]

    await update.message.reply_text("✅ درخواست شما ثبت شد")

    await context.bot.send_message(
        chat_id=ADMIN_ID,
        text=f"""
📥 درخواست جدید

👤 نام: {info['name']}
📞 شماره: {info['phone']}
💬 پیام: {info['message']}
"""
    )

    return ConversationHandler.END

app = Application.builder().token(BOT_TOKEN).build()

conv = ConversationHandler(
    entry_points=[CommandHandler("start", start)],
    states={
        NAME: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_name)],
        PHONE: [MessageHandler(filters.CONTACT, get_phone)],
        MESSAGE: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_message)],
    },
    fallbacks=[]
)

app.add_handler(conv)

app.run_polling()
