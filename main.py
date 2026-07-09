import os
import logging

from telegram import (
    Update,
    ReplyKeyboardMarkup,
    KeyboardButton,
)
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    ConversationHandler,
    filters,
)

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = int(os.getenv("ADMIN_ID"))

(
    FULLNAME,
    PHONE,
    ADDRESS,
    DESCRIPTION,
) = range(4)

MAIN_KEYBOARD = ReplyKeyboardMarkup(
    [
        ["👴 مراقبت سالمند", "👶 مراقبت کودک"],
        ["💰 اطلاع از هزینه", "📝 ثبت درخواست"],
        ["🏢 درباره ما", "📞 تماس با ما"],
    ],
    resize_keyboard=True,
)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "🌹 به ربات باغ آینه خوش آمدید.\n\n"
        "لطفاً یکی از گزینه‌های زیر را انتخاب کنید."
    )

    await update.message.reply_text(
        text,
        reply_markup=MAIN_KEYBOARD,
    )


async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "👴 مراقبت سالمند":
        await update.message.reply_text(
            "خدمات مراقبت سالمند به صورت شبانه‌روزی، روزانه و ساعتی ارائه می‌شود."
        )

    elif text == "👶 مراقبت کودک":
        await update.message.reply_text(
            "خدمات مراقبت کودک توسط نیروهای مجرب و قابل اعتماد انجام می‌شود."
        )

    elif text == "💰 اطلاع از هزینه":
        await update.message.reply_text(
            "هزینه خدمات با توجه به شرایط، ساعات کاری تعیین می‌شود."
        )

    elif text == "🏢 درباره ما":
        await update.message.reply_text(
            "باغ آینه ارائه‌دهنده خدمات مراقبت از سالمند و کودک با نیروهای آموزش‌دیده است."
        )

    elif text == "📞 تماس با ما":
        await update.message.reply_text(
            "شماره تماس:\n09191398300"
        )

    elif text == "📝 ثبت درخواست":
        await update.message.reply_text(
            "لطفاً نام و نام خانوادگی خود را وارد کنید:"
        )
        return FULLNAME

    return ConversationHandler.END


async def fullname(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["fullname"] = update.message.text

    await update.message.reply_text(
        "شماره تماس خود را وارد کنید:"
    )

    return PHONE


async def phone(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["phone"] = update.message.text

    await update.message.reply_text(
        "محدوده آدرس را وارد کنید:"
    )

    return ADDRESS


async def address(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["address"] = update.message.text

    await update.message.reply_text(
        "لطفاً توضیحی درباره شرایط سالمند یا کودک بنویسید:"
    )

    return DESCRIPTION


async def description(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["description"] = update.message.text

    message = f"""
📥 درخواست جدید

👤 نام:
{context.user_data['fullname']}

📞 شماره تماس:
{context.user_data['phone']}

📍 محدوده:
{context.user_data['address']}

📝 توضیحات:
{context.user_data['description']}
"""

    await context.bot.send_message(
        chat_id=ADMIN_ID,
        text=message,
    )

    await update.message.reply_text(
        "✅ درخواست شما با موفقیت ثبت شد.\nبه‌زودی با شما تماس خواهیم گرفت.",
        reply_markup=MAIN_KEYBOARD,
    )

    return ConversationHandler.END


async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "عملیات لغو شد.",
        reply_markup=MAIN_KEYBOARD,
    )

    return ConversationHandler.END


def main():
    app = Application.builder().token(TOKEN).build()

    conv = ConversationHandler(
        entry_points=[
            MessageHandler(
                filters.Regex("^📝 ثبت درخواست$"),
                menu,
            )
        ],
        states={
            FULLNAME: [
                MessageHandler(filters.TEXT & ~filters.COMMAND, fullname)
            ],
            PHONE: [
                MessageHandler(filters.TEXT & ~filters.COMMAND, phone)
            ],
            ADDRESS: [
                MessageHandler(filters.TEXT & ~filters.COMMAND, address)
            ],
            DESCRIPTION: [
                MessageHandler(filters.TEXT & ~filters.COMMAND, description)
            ],
        },
        fallbacks=[
            CommandHandler("cancel", cancel)
        ],
    )

    app.add_handler(CommandHandler("start", start))
    app.add_handler(conv)

    app.add_handler(
        MessageHandler(
            filters.TEXT & ~filters.COMMAND,
            menu,
        )
    )

    app.run_polling()


if __name__ == "__main__":
    main()
