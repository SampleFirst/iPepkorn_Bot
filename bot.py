import os
import math
import logging
import pytz
import logging.config
import asyncio
from datetime import date, datetime
 
from pyrogram.errors import BadRequest, Unauthorized
from pyrogram.raw.all import layer
from pyrogram import Client, __version__, types

from database.ia_filterdb import Media
from database.users_chats_db import db
from utils import temp
from typing import Union, Optional, AsyncGenerator
from plugins import web_server
from aiohttp import web
from Script import script

from info import API_ID, API_HASH, BOT_TOKEN, ADMINS, LOG_CHANNEL, UPTIME, WEBHOOK

# Get logging configurations
logging.config.fileConfig("logging.conf")
logging.getLogger().setLevel(logging.INFO)
logging.getLogger("cinemagoer").setLevel(logging.ERROR)
logger = logging.getLogger(__name__)


class Bot(Client):

    def __init__(self):
        super().__init__(
            name="Professor-Bot",
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
            workers=200,
            plugins={"root": "plugins"},
            sleep_threshold=10,
        )

    async def start(self):
        b_users, b_chats = await db.get_banned()
        temp.BANNED_USERS = b_users
        temp.BANNED_CHATS = b_chats
        await super().start()
        await Media.ensure_indexes()
        me = await self.get_me()
        temp.U_NAME = me.username
        temp.B_NAME = me.first_name
        self.id = me.id
        self.name = me.first_name
        self.mention = me.mention
        self.username = me.username
        self.log_channel = LOG_CHANNEL
        self.uptime = UPTIME
        curr = datetime.datetime.now(pytz.timezone("Asia/Kolkata"))
        date = curr.strftime('%d %B, %Y')
        time = curr.strftime('%I:%M:%S %p')
        logging.info(f"{me.first_name} with for Pyrogram v{__version__} (Layer {layer}) started on {me.username}.")
        try:
            await self.send_message(LOG_CHANNEL, text=script.RESTART_TXT.format(
                a=date, 
                b=time, 
                c=temp.U_NAME
            )
        )
        except Exception as e:
            logger.warning(f"Bot Isn't Able To Send Message To LOG_CHANNEL \n{e}")

        for admin_id in ADMINS:
            try:
                await self.send_message(admin_id, text=f"Bot started successfully at {date}, {time}.\nsend command /start")
            except Exception as e:
                logger.warning(f"Bot Isn't Able To Send Message To Admin {admin_id} \n{e}")

        if WEBHOOK is True:
            app = web.AppRunner(await web_server())
            await app.setup()
            await web.TCPSite(app, "0.0.0.0", 8080).start()
            logger.info("Web Response Is Running......🕸️")

        # Add a job to send a message at 11:59 PM daily
        await self.send_report_message()

    async def send_report_message(self):
        while True:
            tz = pytz.timezone('Asia/Kolkata')
            today = date.today()
            now = datetime.now(tz)
            formatted_date_1 = now.strftime("%d-%B-%Y")
            formatted_date_2 = today.strftime("%d %b")
            time = now.strftime("%H:%M:%S %p")

            total_users = await db.total_users_count()
            total_chats = await db.total_chat_count()
            today_users = await db.daily_users_count(today) + 1
            today_chats = await db.daily_chats_count(today) + 1

            if now.hour == 23 and now.minute == 59:
                await self.send_message(
                    chat_id=LOG_CHANNEL,
                    text=script.REPORT_TXT.format(
                        a=formatted_date_1,
                        b=formatted_date_2,
                        c=time,
                        d=total_users,
                        e=total_chats,
                        f=today_users,
                        g=today_chats,
                        h=temp.U_NAME
                    )
                )
                # Sleep for 1 minute to avoid sending multiple messages
                await asyncio.sleep(60)
            else:
                # Sleep for 1 minute and check again
                await asyncio.sleep(60)

    async def iter_messages(self, chat_id: Union[int, str], limit: int, offset: int = 0) -> Optional[
        AsyncGenerator["types.Message", None]]:
        current = offset
        while True:
            new_diff = min(200, limit - current)
            if new_diff <= 0:
                return
            messages = await self.get_messages(chat_id, list(range(current, current + new_diff + 1)))
            for message in messages:
                yield message
                current += 1

    async def stop(self, *args):
        await super().stop()
        me = await self.get_me()
        logger.info(f"{me.first_name} is_...  ♻️Restarting...")


Bot().run()

