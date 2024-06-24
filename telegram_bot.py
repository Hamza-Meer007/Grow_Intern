
from api import Token
from telegram.ext import CommandHandler, Application
from telegram import Update
import logging

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logging.getLogger("httpx").setLevel(logging.WARNING)
logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)


async def start(update, context):
    await update.message.reply_text("Hello! Welcome to Code Bot")


async def help(update, context):
    await update.message.reply_text(
        f"""
    /start  --> Welcome to Code Bot
    /help   --> This particular message
    /content --> Various Languages Available
    /Python --> First video of Python language tutorial
    /SQL --> First video of SQL language tutorial
    /HTML --> First video of HTML language tutorial
    /C --> First video of C language tutorial
    /Java --> First video of Java language tutorial
    /Javascript --> First video of Javascript language tutorial
    /contact --> Conatct Information"""
    )


async def content(update, context):
    await update.message.reply_text(
        "We have a collection of various programming languages"
    )


async def contact(update, context):
    await update.message.reply_text(
        f"You can contact me on LinkedIn https://www.linkedin.com/in/hamza-meer"
    )


async def Python(update, context):
    await update.message.reply_text(
        "First tutorial Link :https://youtu.be/UrsmFxEIp5k?si=pU1b3liIvv1BLKDr"
    )


async def SQL(update, context):
    await update.message.reply_text(
        "First tutorial Link :https://youtu.be/hlGoQC332VM?si=1Y9spEJaC0LNIgAs"
    )


async def HTML(update, context):
    await update.message.reply_text(
        "First tutorial Link :https://youtu.be/BsDoLVMnmZs?si=p3lO6wRw49pDb5tI"
    )


async def CSS(update, context):
    await update.message.reply_text(
        "First tutorial Link :https://youtu.be/ESnrn1kAD4E?si=VKQlA2kvBdKrHwpu"
    )


async def C(update, context):
    await update.message.reply_text(
        "First tutorial Link :https://youtube.com/playlist?list=PLxgZQoSe9cg1drBnejUaDD9GEJBGQ5hMt&si=ooblOWVNjYIqs5aW"
    )


async def Jave(update, context):
    await update.message.reply_text(
        "First tutorial Link :https://youtube.com/playlist?list=PLu0W_9lII9agS67Uits0UnJyrYiXhDS6q&si=HJTAsBIPc5D9PXjg"
    )


async def Javascript(update, context):
    await update.message.reply_text(
        "First tutorial Link :https://youtube.com/playlist?list=PLGjplNEQ1it_oTvuLRNqXfz_v_0pq6unW&si=w_H-aCejiBRNqWT9"
    )


async def SQL(update, context):
    await update.message.reply_text(
        "First tutorial Link :https://youtu.be/hlGoQC332VM?si=1Y9spEJaC0LNIgAs"
    )


application = Application.builder().token(Token).build()

application.add_handler(CommandHandler("start", start))
application.add_handler(CommandHandler("help", help))
application.add_handler(CommandHandler("Python", Python))
application.add_handler(CommandHandler("SQL", SQL))
application.add_handler(CommandHandler("HTML", HTML))
application.add_handler(CommandHandler("CSS", CSS))
application.add_handler(CommandHandler("C", C))
application.add_handler(CommandHandler("Java", Jave))
application.add_handler(CommandHandler("Javascript", Javascript))
application.add_handler(CommandHandler("contact", contact))

application.run_polling(allowed_updates=Update.ALL_TYPES)
