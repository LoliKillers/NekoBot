from Bot.config import Development as Config
import logging
import sys
import telegram.ext as tg
import pymongo
import time
import os

BLACK='\033[0;30m'
BLUE='\033[0;34m'
GREEN='\033[0;32m'
CYAN='\033[0;36m'
RED='\033[0;31m'
PURPLE='\033[0;35m'
BROWN='\033[0;33m'
LGRAY='\033[0;37m'
DGRAY='\033[1;30m'
LBLUE='\033[1;34m'
LGREEN='\033[1;32m'
LCYAN='\033[1;36m'
LRED='\033[1;31m'
LPURPLE='\033[1;35m'
YELLOW='\033[1;33m'
WHITE='\033[1;37m'
NC='\033[om'

os.system("clear")
StartTime = time.time()

# enable logging
logging.basicConfig(
    format="\033[1;31%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

LOGGER = logging.getLogger(__name__)
LOGGER.info("\033[0;34mNeko \033[0;32mis \033[0;36mnow \033[0;31monline\n\033[1;36m[\033[0;33m+\033[1;36m]======================================================\033[1;36m[\033[0;33m+\033[1;36m]\n\033[1;36m[\033[0;33m+\033[1;36m]\033[1;33m       _   _ \033[1;35m    \033[1;31m _\033[1;36m          \033[1;34m____    \033[1;37m    _            \033[1;36m[\033[0;33m+\033[1;36m]\n\033[1;36m[\033[0;33m+\033[1;36m]\033[1;33m      | \ | |\033[1;35m ___\033[1;31m| | __\033[1;36m___\033[1;34m  | __ ) \033[1;32m ___\033[1;37m | |_          \033[1;36m[\033[0;33m+\033[1;36m]\n\033[1;36m[\033[0;33m+\033[1;36m]\033[1;33m      |  \| |\033[1;35m/ _ \ \033[1;31m|/ / \033[1;36m_ \ \033[1;34m|  _ \ \033[1;32m/ _ \\\033[1;37m| __|         \033[1;36m[\033[0;33m+\033[1;36m]\n\033[1;36m[\033[0;33m+\033[1;36m]\033[1;33m      | |\  | \033[1;35m __/  \033[1;31m <\033[1;36m (_) |\033[1;34m| |_) |\033[1;32m (_) \033[1;37m| |_          \033[1;36m[\033[0;33m+\033[1;36m]\n\033[1;36m[\033[0;33m+\033[1;36m]\033[1;33m      |_| \_|\033[1;35m\___|\033[1;31m_|\_\\\033[1;36m___\033[0;37m(_)\033[1;34m____/ \033[1;32m\___/\033[1;37m \__|         \033[1;36m[\033[0;33m+\033[1;36m]\n\033[1;36m[\033[0;33m+\033[1;36m]======================================================\033[1;36m[\033[0;33m+\033[1;36m]\n\033[1;36m[\033[0;33m+\033[1;36m]\033[1;37m Created \033[1;32m :\033[1;37m NekoId                                    \033[1;36m[\033[0;33m+\033[1;36m]\n\033[1;36m[\033[0;33m+\033[1;36m]\033[1;37m Github  \033[1;32m :\033[1;37m https://github.com/NekoId                 \033[1;36m[\033[0;33m+\033[1;36m]\n\033[1;36m[\033[0;33m+\033[1;36m]\033[1;37m Telegram\033[1;32m :\033[1;37m https://t.me/Nekoid                       \033[1;36m[\033[0;33m+\033[1;36m]\n\033[1;36m[\033[0;33m+\033[1;36m]======================================================\033[1;36m[\033[0;33m+\033[1;36m]")

# if version < 3.6, stop bot.
if sys.version_info[0] < 3 or sys.version_info[1] < 6:
    LOGGER.error(
        "You MUST have python version at least 3.6!  Several features depend on this.  Bot stop."
    )
    quit(1)

TOKEN = Config.TOKEN
MONGO_CLIENT = pymongo.MongoClient(Config.MONGO_URI)

updater = tg.Updater(TOKEN, use_context=True)
dispatcher = updater.dispatcher
