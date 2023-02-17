import asyncio
from pyrogram import Client, filters
from strings import get_command
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from YukkiMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from typing import Union
from pyrogram.types import InlineKeyboardButton

from config import GITHUB_REPO, SUPPORT_CHANNEL, SUPPORT_GROUP, OWNER_ID
from YukkiMusic import app
from config import BANNED_USERS, MUSIC_BOT_NAME
from YukkiMusic.misc import SUDOERS
from YukkiMusic.utils.decorators import AdminRightsCheck

import re
import sys
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

BOT_USERNAME = getenv("BOT_USERNAME")

IMG_DEV1 = getenv("IMG_DEV1")

OWNER_ID = getenv("OWNER_ID")

BOTID = getenv("BOTID")




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
    command(["المطور","المبرمج","مطور"])
    & filters.group
    & ~filters.edited
)
async def khalid(client: Client, message: Message, OWNER: Union[bool, int] = None):
    usr = await client.get_users(5791673201)
    name = usr.first_name
    async for photo in client.iter_profile_photos(5791673201, limit=1):
                    await message.reply_photo(photo.file_id,   caption="ترا أنا بتخطى بسرعة، بس بحب ساوي دراما : @D_33_D",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"tg://user?id=5791673201")
                ],[
                    InlineKeyboardButton(
                        "‹ ضيفني لكروبك ›", url=f"https://t.me/EmCaMusicBot?startgroup=true"),
                ],
            ]
        ),
    )
