import asyncio
from pyrogram import Client, filters
from strings import get_command
from strings.filters import command
from typing import Union
from pyrogram.types import (InlineKeyboardButton,
                            InlineKeyboardMarkup)
from pyrogram.types import Message, VoiceChatStarted, VoiceChatEnded
from YukkiMusic import app

@app.on_message(filters.voice_chat_started)
async def babloo(client: Client, message: Message): 
      Startt = "- بدأت المحادثة الصوتية ."
      await message.reply_text(Startt)

@app.on_message(filters.voice_chat_ended)
async def bablo(client: Client, message: Message): 
      Enddd = "- تم انهاء المحادثه الصوتية ."
      await message.reply_text(Enddd)
@app.on_message(filters.voice_chat_members_invited)
async def fuckoff(client, message):
           text = f"🗯 | قام -> {message.from_user.mention}\n"
           x = 0
           for user in message.voice_chat_members_invited.users:
             try:
               text += f"🗯 | بدعوة -> {user.mention} \n🗯 | إلى المحادثه الصوتية"
               x += 1
             except Exception:
               pass
           try:
             await message.reply(f"{text}")
           except:
             pass

def get_id(msg: Message):
    if msg.media:
        for message_type in (
            "photo",
            "animation",
            "audio",
            "document",
            "video",
            "video_note",
            "voice",
            "contact",
            "dice",
            "poll",
            "location",
            "venue",
            "sticker",
        ):
            obj = getattr(msg, message_type)
            if obj:
                setattr(obj, "message_type", message_type)
                return obj
              
@app.on_message(command("ايما"))
async def throw_dice(client, message: Message): 
    await message.reply_text(["عيونها","روحها","قلبها"])
@app.on_message(command(["مساؤ","صباحو"]))
async def throw_dice(client, message: Message): 
    await message.reply_text("فل عمري .")
@app.on_message(command("مليت"))
async def throw_dice(client, message: Message): 
    await message.reply_text("منحكي ؟ 🥲🤍")
@app.on_message(command(["هه","ههه","ههههه"]))
async def throw_dice(client, message: Message): 
    await message.reply_text("احلى ضحكة والله 💋🤍")
@app.on_message(command(["نورت","نورتي"]))
async def throw_dice(client, message: Message): 
    await message.reply_text("نورك عمري")
@app.on_message(command("هلا"))
async def throw_dice(client, message: Message): 
    await message.reply_text("هلا فيك/ي عمري .")
@app.on_message(command("عرفونا"))
async def throw_dice(client, message: Message): 
    await message.reply_text("ايما ، ع22 مغنية ، حمصية 🥲🤌")
@app.on_message(command("اشتقت"))
async def throw_dice(client, message: Message): 
    await message.reply_text("تشتقلك مكة يارب .")
@app.on_message(command("ملل"))
async def throw_dice(client, message: Message): 
    await message.reply_text("اممممم ، طيب لا اتضوجنا ممكن؟")
@app.on_message(command("هايز"))
async def throw_dice(client, message: Message): 
    await message.reply_text("هايزععع ، شد تمك شوي 🥲")
@app.on_message(command("خاصك"))
async def throw_dice(client, message: Message): 
    await message.reply_text("بطل هل حركات 🙂!")
@app.on_message(command(".rawann"))
async def throw_dice(client, message: Message): 
    await message.reply_text("https://t.me/SS_WN/2")
@app.on_message(command("بالناقص"))
async def throw_dice(client, message: Message): 
    await message.reply_text("منك! 🙂")
@app.on_message(command("بحبك"))
async def throw_dice(client, message: Message): 
    await message.reply_text("بس انا صغيرة!")
@app.on_message(command("نعست"))
async def throw_dice(client, message: Message): 
    await message.reply_text("عمري لا تتعب حالك نام 🤌")
@app.on_message(command("بعشئك"))
async def throw_dice(client, message: Message): 
    await message.reply_text("خجلتني 😎")
@app.on_message(command("😎😎"))
async def throw_dice(client, message: Message): 
    await message.reply_text("على شو شايف حالك لك تافه؟")
@app.on_message(command("عضو"))
async def throw_dice(client, message: Message): 
    await message.reply_text("اي نورت 🙂")
@app.on_message(command("صباحو"))
async def throw_dice(client, message: Message): 
    await message.reply_text("فل ، عمري الحلو والله .")
@app.on_message(command("متت"))
async def throw_dice(client, message: Message): 
    await message.reply_text("بقدرش بدونك! 🙂") 
@app.on_message(command("فرطت"))
async def throw_dice(client, message: Message): 
    await message.reply_text("لموه ختلج الصبي 🥲.")
@app.on_message(command("هههه"))
async def throw_dice(client, message: Message): 
    await message.reply_text("تؤبرني هالضحكة 🫂🤍")
@app.on_message(command("باي"))
async def throw_dice(client, message: Message): 
    await message.reply_text("الله معك 🤝")
@app.on_message(command("احمد"))
async def throw_dice(client, message: Message): 
    await message.reply_text("بقلبي 🤍💋")
@app.on_message(command(["ش ع ت","شو عم تعمل","شعم تعمل","شعك تعملي"]))
async def throw_dice(client, message: Message): 
    await message.reply_text("عم أدي واجبي وغني لهل بشر ☹💗")
@app.on_message(command("مرحبا"))
async def throw_dice(client, message: Message): 
    await message.reply_text("مراحب 🤝")
@app.on_message(command("دوم"))
async def throw_dice(client, message: Message): 
    await message.reply_text("تسلم/ي")
@app.on_message(command("صباحو"))
async def throw_dice(client, message: Message): 
    await message.reply_text("ورد 💞")
@app.on_message(command("هلو"))
async def throw_dice(client, message: Message): 
    await message.reply_text("هلوات 🙁")
@app.on_message(command("ازيك"))
async def throw_dice(client, message: Message): 
    await message.reply_text("بخير وانت/ي ؟")
@app.on_message(command("🤣🤣"))
async def throw_dice(client, message: Message): 
    await message.reply_text("مستفز 🙂")
@app.on_message(command("😂😂"))
async def throw_dice(client, message: Message): 
    await message.reply_text("دامت عمري 🫂")
@app.on_message(command("🥲🥲"))
async def throw_dice(client, message: Message): 
    await message.reply_text("دخيلو الكيوت 🥲")
@app.on_message(command("هاي"))
async def throw_dice(client, message: Message): 
    await message.reply_text("هايات 🙃")
@app.on_message(command("بولنغ"))
async def throw_dice(client, message: Message): 
    await message.reply("🎲")
@app.on_message(command("كيفكم"))
async def throw_dice(client, message: Message): 
    await message.reply_text("بخير وانت ؟")
@app.on_message(command("احا"))
async def throw_dice(client, message: Message): 
    await message.reply_text("احاااات يعم 🤌")
@app.on_message(command("خاص"))
async def throw_dice(client, message: Message): 
    await message.reply_text("واللهي يبتاع الخاص قلبي تعب وعقلي تعب وأي ياي ياي .")
@app.on_message(command("تصبحو ع خير"))
async def throw_dice(client, message: Message): 
    await message.reply_text("وانت بخير يا نور عيوني .")
@app.on_message(command("ايمااا"))
async def throw_dice(client, message: Message): 
    await message.reply_text("قليل ذوق لا تعيط!!")
@app.on_message(command("بتحبيني"))
async def throw_dice(client, message: Message): 
    await message.reply_text("طبعا بحبك لك ابرنييي 🤍🫂")
@app.on_message(command("🙂🙂"))
async def throw_dice(client, message: Message): 
    await message.reply_text("الغزال منكد؟")
@app.on_message(command("😍😍"))
async def throw_dice(client, message: Message): 
    await message.reply_text("حبيت؟")
@app.on_message(command("تفه"))
async def throw_dice(client, message: Message): 
    await message.reply_text("قلة ذوق ترا ؟")
@app.on_message(command("تفو"))
async def throw_dice(client, message: Message): 
    await message.reply_text("قليل ادب 🙂.")
@app.on_message(command("قناتي"))
async def throw_dice(client, message: Message): 
    await message.reply_text("@sspaa,@wopictures")
@app.on_message(command(["متتت"])
    & filters.group
    & ~filters.edited
)
async def ahmad(client: Client, message: Message):
    await message.reply_video(
        video="https://te.legra.ph/file/dbcf6af7538952498c41c.mp4",
        caption=f"""- فرررررررطت ضحك قمنقلععع 😂""",
        reply_markup=InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("‹ ضيفني لكروبك ›", url=f"t.me/EmCaMusicBot?startgroup=true",
                ),
            ],
            [
                InlineKeyboardButton("‹ دخول البوت ›", url=f"t.me/EmCaMusicBot"),
            ],
            ]
        ),
    )
@jepiq.ar_cmd(pattern="معلومات_المكالمة")

async def info_vc(event):

    vc_chat = await jepiq.get_entity(event.chat_id)

    gc_call = await chat_vc_checker(event, vc_chat)

    if not gc_call:

        return

    await edit_or_reply(event, "**- جار جلب معلومات المكالمة انتظر قليلا**")

    call_details = await jepiq(

        functions.phone.GetGroupCallRequest(call=gc_call, limit=1)

    )

    grp_call = "**معلومات مكالمة المجموعة**\n\n"

    grp_call += f"**العنوان :** {call_details.call.title}\n"

    grp_call += f"**عدد المشاركين :** {call_details.call.participants_count}\n\n"

    if call_details.call.participants_count > 0:

        grp_call += "**المشاركون**\n"

        for user in call_details.users:

            nam = f"{user.first_name or ''} {user.last_name or ''}"

            grp_call += f"  ● {mentionuser(nam,user.id)} - `{user.id}`\n"

    await edit_or_reply(event, grp_call)
