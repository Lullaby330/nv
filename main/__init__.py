#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = config("6216349", default=None, cast=int)
API_HASH = config("5c7418e9f3df6db931caa7354521c55f", default=None)
BOT_TOKEN = config("6614032202:AAEtY2CZRXX0GD-EgP2KxXc_eKBv3t7XL_A", default=None)
SESSION = config("AQBJMNojMub-86MHKkemO3LqWzra79oLIPXgYeGsQ3yl3rk0wnmB9STk_--ETseV_xlmpVyshizF9Sj5p-IaByYpmXrLZ4JBSQ1Iwa_ep_efwBEyVKBNHD8o61iXDeHZ7mf7OBbyvznYFeAwQr5d8XSySOh2ATnEXc2yHyk4CdkpZZF2EZHWJzYVGt6aAv3nghsVWiXPCpptbFPCseWnKur0waFCisAC9PHEhfnLDJE6rXpQ0flbT7_mDXCWtX87mPQ7H1K4rvVVT_wr5T4_pK5DcilPOELuoumcYPysjK7C84PKov_eTPhVXD-CHvnK6dXdrArGhkKUf_qDgUJhgWDWAAAAAYtBvCAA", default=None)
FORCESUB = config("svcntn", default=None)
AUTH = config("6631308320", default=None, cast=int)

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client("saverestricted", session_string=SESSION, api_hash=API_HASH, api_id=API_ID) 

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
