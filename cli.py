from telethon import TelegramClient, events, utils

from telethon import TelegramClient
from telethon.errors import SessionPasswordNeededError
from telethon.sessions import StringSession

import secrets
from PIL import Image,  ImageDraw, ImageFont
import secrets
from aiogram import types, Bot, Dispatcher
from aiogram import executor
from aiogram.dispatcher import FSMContext
from aiogram import Dispatcher
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import CallbackQuery, Message
import random, time
from aiogram.dispatcher.filters import ChatTypeFilter
from datetime import datetime, timedelta
from aiogram.dispatcher import FSMContext
from aiogram import Dispatcher
from aiogram.dispatcher.filters import ChatTypeFilter
from aiogram.types import (ChatType, ContentTypes, InlineKeyboardButton,
                           InlineKeyboardMarkup, Message)

from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from telethon import Button
import webbrowser
import sqlite3
from datetime import datetime, timedelta
from telethon import TelegramClient
import secrets


con = sqlite3.connect('cicada.db')
cur = con.cursor()
tt = datetime.now()

bazaa = open('baza.txt', 'r', encoding='utf-8').read()


api_id = 1325339
api_hash = "b826075fd7ea762e6b9f853146d47995"

client = TelegramClient('auth_key', api_id, api_hash)
client.connect()
me = client.get_me()

client.send_message(1144785510, '+')
class cicada(StatesGroup):
    sms = State()
    size = State()
    jaloba = State()
    ppp = State()
    tex = State()
    delit = State()



try:
    cur.execute('''CREATE TABLE cicada
               (name text, us_id text, data text)''')


    con.commit()
    print('\n\n\n\n     Создание БД')
except:
    print('\n\n     Старт Бота')
    pass

def add_us(name, us_id, tt):
    cur.execute(
            f"""INSERT INTO cicada VALUES('{name}', '{us_id}', '{balance}', {tt}')""")
    con.commit()    

def whe_us(name):
    cur.execute(
            f"""SELECT name FROM cicada WHERE '{name}' """)
    rows = cur.fetchone()
    #for row in rows:
    print(rows)
client.parse_mode = 'html'

@client.on(events.NewMessage())
def handler(event):
    print(event)

    
    


    entity = int(1144785510)

    

#    async for dialog in client.iter_dialogs():
#       # print(dialog)
##        print('{:>1}: {}'.format(dialog.message.chat_id))
 #   msg = (f"{name} <b>Написал</b> {event.text} !")
 #   
    client.send_message(entity, obr)
    #
    #entity = input(1144785510)
    #chat = 1144785510
    ##client.forward_messages(entity, messages)
    #client.forward_messages()


client.start()
client.run_until_disconnected()
