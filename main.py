import os
import logging

from telegram import Update, ReplyKeyboardMarkup from telegram.ext import ( Application, CommandHandler, MessageHandler, ContextTypes, ConversationHandler, filters, )

logging.basicConfig( format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO )

TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = int(os.getenv("ADMIN_ID"))

( FULLNAME, PHONE, ADDRESS, DESCRIPTION, CHILD_AGE, CHILD_TIME, CHILD_PLACE, CHILD_DESC, OLD_AGE, OLD_HEALTH, OLD_TIME, OLD_PLACE, OLD_DESC, INTRO_CHOICE, INTRO_NAME, ) = range(15)

MAIN_KEYBOARD = ReplyKeyboardMarkup( [ ["👴 مراقبت سالمند", "👶 مراقبت کودک"], ["💚 اطلاع از هزینه‌ها", "📝 ثبت درخواست"], ["🏢 درباره ما", "📞 تماس با ما"], ["🤝 معرفی نیرو"], ], resize_keyboard=True )

async def send_admin(context, text): try: await context.bot.send_message( chat_id=ADMIN_ID, text=text ) logging.info("Message sent to admin")
except Exception as e:       logging.error(f"Admin send error: {e}")   
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
text = """   
سلام و وقت بخیر 🌿

به مؤسسه باغ آینه خوش آمدید 💚

اینجا کنار شما هستیم تا با معرفی نیروهای دلسوز، مطمئن و مسئولیت‌پذیر برای نگهداری از سالمند، کودک و بیمار، آرامش و اطمینان خاطر را برای شما فراهم کنیم.

لطفاً درخواست خود را ثبت کنید تا همکاران ما در اولین فرصت راهنمایی‌تان کنند. """
await update.message.reply_text(       text,       reply_markup=MAIN_KEYBOARD   )   
async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
text = update.message.text     if text == "🏢 درباره ما":        await update.message.reply_text(   
""" درباره مؤسسه باغ آینه 🌿

در باغ آینه، ما باور داریم مراقبت از عزیزان نیازمند چیزی فراتر از یک نیروی کار است؛ نیازمند اعتماد، مسئولیت و دلسوزی است.

ما با هدف کمک به خانواده‌ها و مراکز درمانی، نیروهای متعهد و قابل اعتماد را برای نگهداری از سالمندان، کودکان و بیماران معرفی می‌کنیم.

تلاش ما این است که با شناخت نیاز شما، انتخابی مطمئن و مناسب را فراهم کنیم تا با آرامش خاطر، مراقبت از عزیزانتان را به افراد شایسته بسپارید.

باغ آینه؛ پلی میان اعتماد شما و مراقبتی شایسته 💚 """ )
   return ConversationHandler.END     elif text == "💚 اطلاع از هزینه‌ها":        await update.message.reply_text(  
""" 💚 دریافت مشاوره و اطلاع از هزینه خدمات

انتخاب یک همراه مطمئن برای مراقبت از عزیزانتان، تصمیمی مهم است. ما در باغ آینه قبل از اعلام هزینه، شرایط و نیاز شما را به‌دقت بررسی می‌کنیم تا مناسب‌ترین خدمت را پیشنهاد دهیم.

هزینه‌ها بر اساس نوع مراقبت، میزان نیاز، زمان همکاری و شرایط فردی شما تعیین می‌شود؛ تا هم کیفیت خدمات حفظ شود و هم انتخابی مناسب و منصفانه داشته باشید.

🌿 برای دریافت مشاوره رایگان و اطلاع از هزینه دقیق، درخواست خود را ثبت کنید. کارشناسان باغ آینه همراه شما هستند تا بهترین انتخاب را داشته باشید. """ )
   return ConversationHandler.END     elif text == "📞 تماس با ما":        await update.message.reply_text(  
""" 📞 تماس با مؤسسه باغ آینه

۰۹۱۹۱۳۹۸۳۰۰

۰۹۳۶۶۰۷۷۳۷۸ """ )
   return ConversationHandler.END     elif text == "📝 ثبت درخواست":        await update.message.reply_text(           "لطفاً نام و نام خانوادگی خود را وارد کنید:"       )        return FULLNAME     elif text == "👶 مراقبت کودک":        await update.message.reply_text(           "👶 سن کودک را وارد کنید:"       )        return CHILD_AGE     elif text == "👴 مراقبت سالمند":        await update.message.reply_text(           "👵👴 سن سالمند را وارد کنید:"       )        return OLD_AGE     elif text == "🤝 معرفی نیرو":        await update.message.reply_text(           "آیا معرف دارید؟ (بله یا خیر)"       )        return INTRO_CHOICE     return ConversationHandler.END  
async def fullname(update: Update, context: ContextTypes.DEFAULT_TYPE):
context.user_data["fullname"] = update.message.text    await update.message.reply_text(       "📞 شماره تماس خود را وارد کنید:"   )    return PHONE   
async def phone(update: Update, context: ContextTypes.DEFAULT_TYPE):
context.user_data["phone"] = update.message.text    await update.message.reply_text(       "📍 محدوده آدرس را وارد کنید:"   )    return ADDRESS   
async def address(update: Update, context: ContextTypes.DEFAULT_TYPE):
context.user_data["address"] = update.message.text    await update.message.reply_text(       "📝 توضیحات درخواست خود را وارد کنید:"   )    return DESCRIPTION   
async def description(update: Update, context: ContextTypes.DEFAULT_TYPE):
context.user_data["description"] = update.message.text     message = f"""   
📥 درخواست جدید

👤 نام: {context.user_data.get('fullname')}

📞 شماره تماس: {context.user_data.get('phone')}

📍 محدوده: {context.user_data.get('address')}

📝 توضیحات: {context.user_data.get('description')} """
await send_admin(       context,       message   )     await update.message.reply_text(       "✅ درخواست شما با موفقیت ثبت شد.\n"       "کارشناسان باغ آینه به‌زودی با شما تماس می‌گیرند.",       reply_markup=MAIN_KEYBOARD   )     return ConversationHandler.END   
async def child_age(update: Update, context: ContextTypes.DEFAULT_TYPE):
context.user_data["child_age"] = update.message.text    await update.message.reply_text(       "⏰ ساعت و روزهای مورد نیاز را وارد کنید:"   )    return CHILD_TIME   
async def child_time(update: Update, context: ContextTypes.DEFAULT_TYPE):
context.user_data["child_time"] = update.message.text    await update.message.reply_text(       "📍 محل خدمت را وارد کنید:"   )    return CHILD_PLACE   
async def child_place(update: Update, context: ContextTypes.DEFAULT_TYPE):
context.user_data["child_place"] = update.message.text    await update.message.reply_text(       "📝 توضیحات و نیازهای خاص کودک را وارد کنید:"   )    return CHILD_DESC   
async def child_desc(update: Update, context: ContextTypes.DEFAULT_TYPE):
context.user_data["child_desc"] = update.message.text     message = f"""   
🌸 درخواست نگهداری کودک

👶 سن کودک: {context.user_data.get('child_age')}

⏰ ساعت و روزهای مورد نیاز: {context.user_data.get('child_time')}

📍 محل خدمت: {context.user_data.get('child_place')}

📝 توضیحات: {context.user_data.get('child_desc')} """
await send_admin(       context,       message   )     await update.message.reply_text(       "✅ درخواست شما ثبت شد.\n"       "کارشناسان باغ آینه به‌زودی با شما تماس می‌گیرند.",       reply_markup=MAIN_KEYBOARD   )     return ConversationHandler.END   
async def old_age(update: Update, context: ContextTypes.DEFAULT_TYPE):
context.user_data["old_age"] = update.message.text    await update.message.reply_text(       "🩺 وضعیت جسمی و نیازهای مراقبتی سالمند را وارد کنید:"   )    return OLD_HEALTH   
async def old_health(update: Update, context: ContextTypes.DEFAULT_TYPE):
context.user_data["old_health"] = update.message.text    await update.message.reply_text(       "⏰ ساعت و نوع همکاری مورد نیاز را وارد کنید:"   )    return OLD_TIME   
async def old_time(update: Update, context: ContextTypes.DEFAULT_TYPE):
context.user_data["old_time"] = update.message.text    await update.message.reply_text(       "📍 محل خدمت را وارد کنید:"   )    return OLD_PLACE   
async def old_place(update: Update, context: ContextTypes.DEFAULT_TYPE):
context.user_data["old_place"] = update.message.text    await update.message.reply_text(       "📝 توضیحات تکمیلی درباره شرایط سالمند را وارد کنید:"   )    return OLD_DESC 
async def old_desc(update: Update, context: ContextTypes.DEFAULT_TYPE):

context.user_data["old_desc"] = update.message.text  

message = f"""

🌿 درخواست نگهداری سالمند

👵👴 سن سالمند:
{context.user_data.get('old_age')}

🩺 وضعیت جسمی و نیازهای مراقبتی:
{context.user_data.get('old_health')}

⏰ ساعت و نوع همکاری:
{context.user_data.get('old_time')}

📍 محل خدمت:
{context.user_data.get('old_place')}

📝 توضیحات تکمیلی:
{context.user_data.get('old_desc')}
"""

await send_admin(  
    context,  
    message  
)  

await update.message.reply_text(  
    "✅ درخواست شما ثبت شد.\n"  
    "کارشناسان باغ آینه به‌زودی با شما تماس می‌گیرند.",  
    reply_markup=MAIN_KEYBOARD  
)  

return ConversationHandler.END

async def intro_choice(update: Update, context: ContextTypes.DEFAULT_TYPE):

answer = update.message.text.lower()  

if answer in ["بله", "بلی", "اره", "آره"]:  

    await update.message.reply_text(  
        "لطفاً نام و نام خانوادگی معرف را وارد کنید:"  
    )  

    return INTRO_NAME  

else:  

    message = f"""

🤝 معرفی نیرو

👤 نام:
{update.effective_user.full_name}

🆔 شناسه کاربر:
{update.effective_user.id}

❌ معرف ندارد
"""

await send_admin(  
        context,  
        message  
    )  

    await update.message.reply_text(  
        "✅ اطلاعات شما ثبت شد.",  
        reply_markup=MAIN_KEYBOARD  
    )  

    return ConversationHandler.END

async def intro_name(update: Update, context: ContextTypes.DEFAULT_TYPE):

context.user_data["intro_name"] = update.message.text  

message = f"""

🤝 معرفی نیرو

👤 نام درخواست کننده:
{update.effective_user.full_name}

🆔 شناسه کاربر:
{update.effective_user.id}

👥 نام معرف:
{context.user_data.get('intro_name')}
"""

await send_admin(  
    context,  
    message  
)  

await update.message.reply_text(  
    "✅ اطلاعات معرف ثبت شد.",  
    reply_markup=MAIN_KEYBOARD  
)  

return ConversationHandler.END

async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE):

await update.message.reply_text(  
    "عملیات لغو شد.",  
    reply_markup=MAIN_KEYBOARD  
)  

return ConversationHandler.END

async def error_handler(update, context):

logging.error(  
    "خطا در ربات:",  
    exc_info=context.error  
)

def main():

app = Application.builder().token(TOKEN).build()  


conv = ConversationHandler(  

    entry_points=[  
        MessageHandler(  
            filters.Regex("^📝 ثبت درخواست$"),  
            menu  
        ),  

        MessageHandler(  
            filters.Regex("^👶 مراقبت کودک$"),  
            menu  
        ),  

        MessageHandler(  
            filters.Regex("^👴 مراقبت سالمند$"),  
            menu  
        ),  

        MessageHandler(  
            filters.Regex("^🤝 معرفی نیرو$"),  
            menu  
        ),  
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


        CHILD_AGE: [  
            MessageHandler(filters.TEXT & ~filters.COMMAND, child_age)  
        ],  

        CHILD_TIME: [  
            MessageHandler(filters.TEXT & ~filters.COMMAND, child_time)  
        ],  

        CHILD_PLACE: [  
            MessageHandler(filters.TEXT & ~filters.COMMAND, child_place)  
        ],  

        CHILD_DESC: [  
            MessageHandler(filters.TEXT & ~filters.COMMAND, child_desc)  
        ],  


        OLD_AGE: [  
            MessageHandler(filters.TEXT & ~filters.COMMAND, old_age)  
        ],  

        OLD_HEALTH: [  
            MessageHandler(filters.TEXT & ~filters.COMMAND, old_health)  
        ],  

        OLD_TIME: [  
            MessageHandler(filters.TEXT & ~filters.COMMAND, old_time)  
        ],  

        OLD_PLACE: [  
            MessageHandler(filters.TEXT & ~filters.COMMAND, old_place)  
        ],  

        OLD_DESC: [  
            MessageHandler(filters.TEXT & ~filters.COMMAND, old_desc)  
        ],  


        INTRO_CHOICE: [  
            MessageHandler(filters.TEXT & ~filters.COMMAND, intro_choice)  
        ],  

        INTRO_NAME: [  
            MessageHandler(filters.TEXT & ~filters.COMMAND, intro_name)  
        ],  
    },  


    fallbacks=[  
        CommandHandler("cancel", cancel)  
    ],  
)  


app.add_handler(  
    CommandHandler(  
        "start",  
        start  
    )  
)  


app.add_handler(conv)  


app.add_handler(  
    MessageHandler(  
        filters.TEXT & ~filters.COMMAND,  
        menu  
    )  
)  


app.add_error_handler(  
    error_handler  
)  async def fullname(update: Update, context: ContextTypes.DEFAULT_TYPE):

     context.user_data["fullname"] = update.message.text
 
     await update.message.reply_text(
         "📞 شماره تماس خود را وارد کنید:"
    ) 
     return PHONE


logging.info(  
    "BOT STARTED"  
)  


app.run_polling(  
    drop_pending_updates=True  
)

if name == "main":
main()
