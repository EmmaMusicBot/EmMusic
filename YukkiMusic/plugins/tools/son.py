from utlis.rank import setrank,isrank,remrank,remsudos,setsudo, GPranks,IDrank
from utlis.send import send_msg, BYusers, GetLink,Name,Glang
from utlis.locks import st,getOR
from utlis.tg import Bot
from config import *
from YukkiMusic import app
import threading, requests, time, random, re, json
import importlib

from os import listdir
from os.path import isfile, join
def updateMsgs(client, message,redis):
  userID = message.from_user.id
  chatID = message.chat.id
  userFN = message.from_user.first_name
  rank = isrank(redis,userID,chatID)
  text = message.text
    if (rank is not False or rank is not  0 or rank != "vip"):
     if text and text == "غنيلي" :
       client.copy_message(chatID,"Teamsulta",random.randint(2, 552),reply_to_message_id=message.message_id)