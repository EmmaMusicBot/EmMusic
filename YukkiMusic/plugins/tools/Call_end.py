import asyncio
from pyrogram import Client, filters
from strings import get_command
from strings.filters import command
from pyrogram.types import Message, VoiceChatStarted, VoiceChatEnded
from YukkiMusic import app

@app.on_message(filters.voice_chat_started)
async def babloo(client: Client, message: Message): 
      Startt = "- صعدوا نسمع أغاني 🥲"
      await message.reply_text(Startt)

@app.on_message(filters.voice_chat_ended)
async def bablo(client: Client, message: Message): 
      Enddd = "- أصلاً مليت 🙂"
      await message.reply_text(Enddd)

      
@app.on_message(command("ايما"))
async def throw_dice(client, message: Message): 
    await message.reply_text("عيونها")
@app.on_message(command("ايدي"))
async def throw_dice(client, message: Message): 
    await message.reply_text(f"ايدي الكروب :```{message.chat.id}```")
@app.on_message(command("بالناقص"))
async def throw_dice(client, message: Message): 
    await message.reply_text("منك! 🙂")
@app.on_message(command("بحبك"))
async def throw_dice(client, message: Message): 
    await message.reply_text("بس انا صغيرة!")
@app.on_message(command("احمد"))
async def throw_dice(client, message: Message): 
    await message.reply_text("ده مطوري")
@app.on_message(command("باي"))
async def throw_dice(client, message: Message): 
    await message.reply_text("الله معك")
@app.on_message(command("مرحبا"))
async def throw_dice(client, message: Message): 
    await message.reply_text("مرحبتين")
@app.on_message(command("دوم"))
async def throw_dice(client, message: Message): 
    await message.reply_text("تسلم/ي")
@app.on_message(command("صباحو"))
async def throw_dice(client, message: Message): 
    await message.reply_text("ورد")
@app.on_message(command("صلاح"))
async def throw_dice(client, message: Message): 
    await message.reply_text("ده صحبي")
@app.on_message(command("لجين"))
async def throw_dice(client, message: Message): 
    await message.reply_text("دي بنتي")
@app.on_message(command("ابو سليمان"))
async def throw_dice(client, message: Message): 
    await message.reply_text("ده حبيبي")
@app.on_message(command("ايمن"))
async def throw_dice(client, message: Message): 
    await message.reply_text("طنبخة")
@app.on_message(command("هاي"))
async def throw_dice(client, message: Message): 
    await message.reply_text("هايات")
@app.on_message(command("بولنغ"))
async def throw_dice(client, message: Message): 
    await message.reply_text("🎲")
@app.on_message(command("كيفكم"))
async def throw_dice(client, message: Message): 
    await message.reply_text("بخير وانت")
@app.on_message(command("رنا"))
async def throw_dice(client, message: Message): 
    await message.reply_text("دي عمري")
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
