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
*NEKO* [.](https://telegra.ph/file/981f776678ac4980d39fd.png)
- /neko: Sending a Random SFW Neko source Image.
- /feet: Sending Random Anime Foot Images.
- /yuri: Sends Random Yuri's source Image.
- /trap: Sends a Random Trap source Image.
- /futanari: Sends Random Futanari source Images.
- /hololewd: Sends Random Holo Lewds.
  - /lewdkemo: Sending Random Chemo Lewds.
- /sologif: Send a Random Solo GIF.
- /cumgif: Sending Random Cum GIFs.
- /erokemo: Sending Random Ero-Chemo Images.
- /lesbian: Sending Random Les Source Images.
- /wallpaper: Send Random Wallpaper.
- /lewdk: Sends Random Kitsune Lewds.
- /ngif: Sending Random Neko GIFs.
- /tickle: Sends a Random Tickle GIF.
- /lewd: Send random (?)
- /feed: Sends a Random Feeding GIF.
- /eroyuri: Sending a Random Ero-Yuri source Image.
- /eron: Sending Random Ero-Neko source images.
- /cum: Sending Random Cum Images.
- /bjgif: Sending Shuffle Worker GIF.
- /bj: Sending Random Worker Source Image.
- /nekonsfw: Sending a Random NSFW Neko source Image.
- /solo: Send a Random Neko NSFW GIF.
- /kemonomimi: Sending a Random KemonoMimi source Image.
- /poke: Sends Random Poke GIFs.
- /anal: Sending Random Anal GIFs.
- /hentai: Sending Random Hentai source Images.
- /erofeet: Sends a Random Ero-Feet source Image.
- /holo: Sends a Random Holo source Image.
- /tits: Sends 99 Random source Images.
- /pussygif: Sending ...... Random.
- /holoero: Sends a Random Ero-Holo source Image.
- /pussy: Sends Random source Image.
- /hentaigif: Sending Random Hentai GIFs.
- /classic: Send Random Classic Hentai GIFs.
- /kuni: Sending a random kuni Lick GIF.
- /kiss: Send a Random Kiss GIF.
- /femdom: Sends a Random Femdom source Image.
- /cuddle: Sends a Random Cuddle GIF.
- /erok: Sends a Random Ero-Kitsune source Image.
- /foxgirl: Sending a Random FoxGirl source Image.
- /titsgif: Sends 99 Random GIFs.
- /ero: Sends a Random Ero source image.
- /smug: Sends a Random Snob GIF.
- /baka: Sends a random Baka Shout GIF.
- /dva: Sends a Random D.VA source Image.
 
  * Pinging *
- /ping: Displays signal strength / ping.

  * AniList *
- /anime: search for anime
- /character: search character
- /manga: search for manga
-/airing: get anime broadcast status
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
        update.effective_message.reply_text("Everything is in pm dear")


# Kanged from PaperPlane Extended userbot
def speed_convert(size):
    """
    Hey man, you can't read the bytes?
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
