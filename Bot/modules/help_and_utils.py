import html
import importlib
import json
import re
import time
import traceback
from typing import Optional

from telegram import Message, Chat, User
from telegram import ParseMode, InlineKeyboardMarkup, InlineKeyboardButton, Update
from telegram.ext import (
    CommandHandler,
    Filters,
    MessageHandler,
    CallbackQueryHandler,
    CallbackContext,
)
from telegram.ext.dispatcher import run_async, DispatcherHandlerStop
from telegram.utils.helpers import escape_markdown

from Bot import (
    dispatcher,
    updater,
)

StartTime = time.time()




help_text = """
⛦ *L.K Botz* ⛦

⌬ *SFW & NSFW MENU*
▹ /neko
▹ /feet
▹ /yuri
▹ /trap
▹ /futanari
▹ /hololewd
▹ /lewdkemo
▹ /sologif
▹ /cumgif
▹ /erokemo
▹ /lesbian
▹ /wallpaper
▹ /lewdk
▹ /ngif
▹ /tickle
▹ /lewd
▹ /feed
▹ /eroyuri
▹ /eron
▹ /cum
▹ /bjgif
▹ /bj
▹ /nekonsfw
▹ /solo
▹ /kemonomimi
▹ /poke
▹ /anal
▹ /hentai
▹ /erofeet
▹ /holo
▹ /tits
▹ /pussygif
▹ /holoero
▹ /pussy
▹ /hentaigif
▹ /classic
▹ /kuni
▹ /kiss
▹ /femdom
▹ /cuddle
▹ /erok
▹ /foxgirl
▹ /titsgif
▹ /ero
▹ /smug
▹ /baka
▹ /dva
 
 ⌬ *PINGING*
▹ /ping

 ⌬ *ANILIST*
▹ /anime
▹ /character
▹ /manga
▹ /airing
 """


@run_async
def edit_msg(update, context):
    update.effective_message.delete()
    update.effective_message.reply_text(help_text, parse_mode=ParseMode.MARKDOWN)


@run_async
def help(update, context):
    if update.effective_chat.type == "private":
        args = context.args
        update.effective_message.reply_text(
            help_text,
            parse_mode=ParseMode.MARKDOWN,
            timeout=60,
            disable_web_page_preview=False,
        )
    else:
        update.effective_message.reply_text("Semuanya ada di pm sayang")

def speed_convert(size):
    """
    Anda tidak bisa membaca byte?
    """
    power = 2 ** 10
    zero = 0
    units = {0: "", 1: "Kb/s", 2: "Mb/s", 3: "Gb/s", 4: "Tb/s"}
    while size > power:
        size /= power
        zero += 1
    return f"{round(size, 2)} {units[zero]}"


def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time


def ping(update: Update, context: CallbackContext):
    msg = update.effective_message

    start_time = time.time()
    message = msg.reply_text("Pinging...")
    end_time = time.time()
    telegram_ping = str(round((end_time - start_time) * 1000, 3)) + " ms"
    uptime = get_readable_time((time.time() - StartTime))

    message.edit_text(
        "PONG!!\n"
        "<b>Time Taken:</b> <code>{}</code>\n"
        "<b>Service uptime:</b> <code>{}</code>".format(telegram_ping, uptime),
        parse_mode=ParseMode.HTML,
    )

help_handler = CommandHandler("help", help, pass_args=True)
CALLBACK_QUERY_HANDLER = CallbackQueryHandler(edit_msg, pattern="help")
PING_HANDLER = CommandHandler("ping", ping)
dispatcher.add_handler(help_handler)
dispatcher.add_handler(CALLBACK_QUERY_HANDLER)
dispatcher.add_handler(PING_HANDLER)
