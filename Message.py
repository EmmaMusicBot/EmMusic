import telebot 
from telepot.loop import MessageLoop 
from YukkiMusic import app
bot=telebot.Bot('5769323463:AAFMHSF4rQ3sfMJarIQa_eOkBntQGIo5hJI')

def action(msg): 

  chat_id=msg['chat']['id'] 

  if ('new_chat_member' in msg): 

    name=msg['new_chat_member']['first_name'] 

    bot.sendMessage(chat_id, 'مرحبا بك يا '+name+' جزيل الشكر انك دخلت المجموعة')

MessageLoop(bot, action).run_as_thread() 

while 1: 

  pass
