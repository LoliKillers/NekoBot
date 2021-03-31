from telegram import ParseMode, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import CommandHandler
from telegram.ext.dispatcher import run_async

from Bot.modules import help_and_utils, anilist, lewd
from Bot import LOGGER, dispatcher, updater


@run_async
def start(update, context):
    PM_START_TEXT = """
Hewwo, Ohayoo >_<.
Tap on /help to know all my commands!
"""
    keyboard = [
        [
            InlineKeyboardButton("Maintained by", url="t.me/RikonAsw"),
            InlineKeyboardButton("Help", callback_data="help"),
        ]
    ]

    if update.effective_chat.type == "private":
        args = context.args
        update.effective_message.reply_photo(
            "https://telegra.ph/file/981f776678ac4980d39fd.png",
            PM_START_TEXT,
            timeout=60,
            parse_mode=ParseMode.MARKDOWN,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(keyboard),
        )
    else:
        update.effective_message.reply_text("Ohayooo!")


def main():
    dispatcher.add_handler(CommandHandler("start", start))


if __name__ == "__main__":
    LOGGER.info("Using long polling.")
    main()
    updater.start_polling(timeout=15, read_latency=4)
    updater.idle()
