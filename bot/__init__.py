#https://t.me/Shadow_Garden_Bots

from aiohttp import web
from plugins import web_server

import pyromod
import pyromod.listen
import pyromod.listen
from pyrogram import Client
from pyrogram.enums import ParseMode
import sys
from datetime import datetime

from config import API_HASH, APP_ID, LOGGER, TG_BOT_TOKEN, TG_BOT_WORKERS, FORCE_SUB_CHANNEL, CHANNEL_ID, PORT, STRING_SESSION


if STRING_SESSION != "None":
    try:
        Ubot = Client("ubot", session_string=STRING_SESSION, api_id=APP_ID, api_hash=API_HASH,plugins={
                "root": "plugins"},max_concurrent_transmissions =4)
        Bot = Client("ubot",workers=TG_BOT_WORKERS,bot_token=TG_BOT_TOKEN, api_id=APP_ID, api_hash=API_HASH,plugins={
                "root": "plugins"
            })
        print("❤️ UBot Connected")
        print("❤️ Bot Connected")
    except Exception as e:
        print('😞 Error While Connecting To UBot')    
        print(e)
        sys.exit() 

