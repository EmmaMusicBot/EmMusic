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
from config import BANNED_USERS, MUSIC_BOT_NAME
from YukkiMusic.misc import SUDOERS

import re
import sys
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

BOT_USERNAME = getenv("BOT_USERNAME")

OWNER_ID = getenv("OWNER_ID")

ID_BOT1 = getenv("ID_BOT1")

NAME_BOT = getenv("NAME_BOT")

DEV = getenv("DEV")

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

    command(["بوت"])

    & filters.group

    & ~filters.edited

)

async def khalid(client: Client, message: Message):

    usr = await client.get_users(6292399606)

    name = usr.first_name

    async for photo in client.iter_profile_photos(6292399606, limit=1):

                    await message.reply_photo(photo.file_id,       caption=f"- هلا عمري {message.from_user.mention}\n- اسمي ايما ، أضغط على الزر لتشوف اوامري.", 

        reply_markup=InlineKeyboardMarkup(

            [

                [

                    InlineKeyboardButton(

                      "- الأوامر .", url=f"https://t.me/@mCaMusicBot?start=help") 

                ],[

                    InlineKeyboardButton(

                       "- ضيفني لكروبك .", url=f"https://t.me/EmCaMusicBot?startgroup=true"),

                ],

            ]

        ),

    )

                
