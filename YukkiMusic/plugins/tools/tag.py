import os, logging, asyncio
from telethon import Button
from telethon import TelegramClient, events
from telethon.tl.types import ChannelParticipantAdmin
from telethon.tl.types import ChannelParticipantCreator
from telethon.tl.functions.channels import GetParticipantRequest
from telethon.errors import UserNotParticipantError
from YukkiMusic import app

logging.basicConfig(
    level=logging.INFO,
    format='%(name)s - [%(levelname)s] - %(message)s'
)
LOGGER = logging.getLogger(__name__)

api_id = int(os.environ.get("APP_ID","8288457"))
api_hash = os.environ.get("API_HASH","583ce464b47ed1b7b26e80e3fd278714")
bot_token = os.environ.get("TOKEN","6292399606:AAGFU4pS1xl0iYl1IHub6azDSh6WHEDwwwA")
client = TelegramClient('client', api_id, api_hash).start(bot_token=bot_token)
spam_chats = []

@client.on(events.NewMessage(pattern="^/emmastartemma$"))
async def start(event):
  await event.reply(
    "__**𝐈'𝐦 𝐓𝐚𝐠𝐀𝐥𝐥 𝐁𝐨𝐭**, 𝐢 𝐂𝐚𝐧 𝐌𝐞𝐧𝐭𝐢𝐨𝐧 𝐀𝐥𝐥 𝐌𝐞𝐦𝐛𝐞𝐫𝐬 𝐈𝐧 𝐆𝐫𝐨𝐮𝐩 𝐎𝐫 𝐂𝐡𝐚𝐧𝐧𝐞𝐥 👻\n𝐂𝐥𝐢𝐜𝐤 **/help** 𝐅𝐨𝐫 𝐌𝐨𝐫𝐞 𝐈𝐧𝐟𝐨𝐫𝐦𝐚𝐭𝐢𝐨𝐧__\n\n 𝐅𝐨𝐥𝐥𝐨𝐰 [𝗗𝗘𝗩𝗜𝗟 𝗛𝗔𝗖𝗞𝗘𝗥](https://t.me/JaiHindChatting) 𝗢𝗻 𝐓𝐞𝐥𝐞𝐆𝐫𝐚𝐦",
    link_preview=False,
    buttons=(
      [
        Button.url('✨𝙎𝙐𝙋𝙋𝙊𝙍𝙏', 'https://t.me/JaiHindChatting'),
        Button.url('📦 𝙎𝙊𝙐𝙍𝘾𝙀', 'https://github.com/rakeshyt/DevilTagAllBot')
      ]
    )
  )
@client.on(events.NewMessage(pattern="^/all ?(.*)"))
async def all(event):
  chat_id = event.chat_id
  if event.is_private:
    return await event.respond("__يمكن استخدام هذا الأمر في المجموعات والقنوات  @EmCaMusicbot !__")
  
  is_admin = False
  try:
    partici_ = await client(GetParticipantRequest(
      event.chat_id,
      event.sender_id
    ))
  except UserNotParticipantError:
    is_admin = False
  else:
    if (
      isinstance(
        partici_.participant,
        (
          ChannelParticipantAdmin,
          ChannelParticipantCreator
        )
      )
    ):
      is_admin = True
  if not is_admin:
    return await event.respond("__فقط الأدمن يستطيع عمل تاك !__")
  
  if event.pattern_match.group(1) and event.is_reply:
    return await event.respond("__أعطني حجة واحدة !__")
  elif event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.is_reply:
    mode = "text_on_reply"
    msg = await event.get_reply_message()
    if msg == None:
        return await event.respond("__استطيع عمل تاك الى اعضاء المجموعة__")
  else:
    return await event.respond("__قم بالرد على رسالة أو أعطني بعض النص لأذكر الآخرين!__")
  
  spam_chats.append(chat_id)
  usrnum = 0
  usrtxt = ''
  async for usr in client.iter_participants(chat_id):
    if not chat_id in spam_chats:
      break
    usrnum += 1
    usrtxt += f"[{usr.first_name}](tg://user?id={usr.id}) "
    if usrnum == 5:
      if mode == "text_on_cmd":
        txt = f"{usrtxt}\n\n{msg}\n\n - بواسطة : @EmCaMusicBot ."
        await client.send_message(chat_id, txt)
      elif mode == "text_on_reply":
        await msg.reply(usrtxt)
      await asyncio.sleep(2)
      usrnum = 0
      usrtxt = ''
  try:
    spam_chats.remove(chat_id)
  except:
    pass

@client.on(events.NewMessage(pattern="توقف"))
async def cancel_spam(event):
  if not event.chat_id in spam_chats:
    return await event.respond('__لا يوجد مشكلة...__')
  else:
    try:
      spam_chats.remove(event.chat_id)
    except:
      pass
    return await event.respond('__تم الايقاف.__')

print(">> انضم الى قناة البوت : @D_33_D<<")
client.run_until_disconnected()
