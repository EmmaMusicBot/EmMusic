import asyncio
from pyrogram import Client, filters
from strings import get_command
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from YukkiMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from typing import Union
from pyrogram.types import InlineKeyboardButton

from config import GITHUB_REPO, SUPPORT_CHANNEL, SUPPORT_GROUP
from YukkiMusic import app
from YukkiMusic.misc import SUDOERS

import re
import sys
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

BOT_USERNAME = getenv("BOT_USERNAME")

IMG_DEV1 = getenv("IMG_DEV1")

OWNER = getenv("OWNER")





def get_file_id(msg: Message):
    if msg.media:
        for message_type in (
            "photo",
            "animation",
            "audio",
            "document",
            "video",
            "video_note",
            "voice",
            # "contact",
            # "dice",
            # "poll",
            # "location",
            # "venue",
            "sticker",
        ):
            obj = getattr(msg, message_type)
            if obj:
                setattr(obj, "message_type", message_type)
                return obj



@app.on_message(
    command(["ايدي","ا","رتبتي"])
    & filters.group
    & ~filters.edited
)
async def madison(client: Client, message: Message):
    if message.from_user.id in SUDOERS:
        await message.reply_text(f"⤶ أسمك : {message.from_user.mention}\n⤶ آيديك : ```{message.from_user.id}``` .\n⤶ رتبتبك : مطور بوت ايما .")
    else:
        await message.reply_text(f"⤶ أسمك : {message.from_user.mention}\n⤶ آيديك : ```{message.from_user.id}``` .\n⤶ رتبتبك : مطور بوت ايما .")
        
@app.on_message(
    command(["رتبتي","ايدي","ا"])
    & filters.group
    & ~filters.edited
)
async def ruteb(client: Client, message: Message):
    if message.from_user.id in AUTH:
        await message.reply_text(f"⤶ أسمك : {message.from_user.mention}\n⤶ آيديك : ```{message.from_user.id}``` .\n⤶ رتبتبك : عضو في بوت ايما .")
    else:
        await message.reply_text(f"⤶ أسمك : {message.from_user.mention}\n⤶ آيديك : ```{message.from_user.id}``` .\n⤶ رتبتبك : عضو في بوت ايما .")
