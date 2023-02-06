from dotenv import load_dotenv

import os


################setTime################
from datetime import datetime
now = datetime.now()

import logging
from colorlog import ColoredFormatter

################logColoringSettings################
LOG_LEVEL = logging.DEBUG
LOGFORMAT = " %(log_color)s%(levelname)-8s%(reset)s | %(log_color)s%(message)s%(reset)s"

logging.root.setLevel(LOG_LEVEL)
formatter = ColoredFormatter(LOGFORMAT)
stream = logging.StreamHandler()
stream.setLevel(LOG_LEVEL)
stream.setFormatter(formatter)
log = logging.getLogger('pythonConfig')
log.setLevel(LOG_LEVEL)
log.addHandler(stream)

################colorPalette################
class Style():
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'
    
################TOKENandDEVTHINGS################
load_dotenv()
TOKEN = os.environ["DISCORD_BOT_TOKEN"]
APPLICATION_ID = os.environ["DISCORD_APPLICATION_ID"]
GUILD_ID = os.environ["DISCORD_GUILD_ID"]

################music################
FFMPEG_OPTIONS = {
    'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
    'options': '-vn'
    }
YDL_OPTIONS = {
    'format':'bestaudio',
     'quiet': True, 
     'default_search':"ytsearch", 
     'noplaylist':'True'
    }

################sourceCodeGithub################
GITHUB_LINK = "https://github.com/Tutu-Inc/REINHARD"
################createMainVoice################
TEMP_MAIN_CHANNEL = "➕〡CREATE CHANNEL"
TEMP_MAIN_CATEGORY = "──༺VOICECHANNEL༻──"
################createSchuleVoice################
TEMP_SCHULE_CHANNEL = "➕〡LEARNING ROOM"
TEMP_SCHULE_CATEGORY = "─────༺TGM༻─────"
################channels################
MUSICCHANNEL = "musik"
RULEROLECHANNEL = "regeln"
################roles################
MODERATOR_ROLE_NAME = "Moderatoren"
