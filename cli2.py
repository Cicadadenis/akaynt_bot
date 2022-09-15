from telethon import TelegramClient, events

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
import webbrowser

api_id = 1325339
api_hash = "b826075fd7ea762e6b9f853146d47995"
client = TelegramClient('anon', api_id, api_hash)



class cicada(StatesGroup):
    sms = State()
    size = State()
    jaloba = State()
    ppp = State()
    tex = State()
    delit = State()


ff = []
ps = []
adm = []

@client.on(events.NewMessage)
async def my_event_handler(event):

    ps.clear()
    chat_id = message.chat.id
    imya = message.chat.first_name
    password = secrets.token_urlsafe(3)
    ps.append(password)
    im = Image.open('dropbox-logo@2x.jpg')
    draw_text = ImageDraw.Draw(im)
    font = ImageFont.truetype('Carnivale.ttf', size=170)
    draw_text.text(
        (220,120),
        password,
        font=font,
        fill=('green'),
        colors='green'
        )
    im.save('new_pic.jpg')
    pp = open("new_pic.jpg", 'rb').read()
    text = (f"<b>Введите код с картинки 👆</b>\n"
           f" ➖➖➖➖➖➖➖➖➖\n"
           f"<b>Чтобы вернуться в меню и начать</b>\n"
           f"<b>Oтправьте 👉 /start</b>")
    user_id=message.from_user.id
    if str(user_id) in admins:
        await message.answer(f'<b>Приветствую тебя {imya}\nЭто Меня Админа</b>', reply_markup=check_user_out_func(message.from_user.id))
    else:
        await bot.send_photo(chat_id, photo=pp, caption=text)
    await cicada.sms.set()

@dp.message_handler(state=cicada.sms)
async def bot2(message: Message, state):

    chat_id = message.chat.id
    imya = message.chat.first_name
    pas = message.text
    if pas == ps[0]:
        ps.clear()
        await message.answer(f"<b>Привет ! {imya} \nОпишете суть вашего обращения</b>\n"
                             f"<b>И мы Отправим Ваше Обращение</b>\n"
                             f"<b>Первому свободному Оператору</b>\n"
                             f"<b>В течении 3-х минут С Вами Свяжеться Тех-Подержка</b>")
        await cicada.jaloba.set()
    else:
        ps.clear()
        await message.answer("<b>Неверно Введена Капча\nПопробуйте Снова</b>")
        await start_command(message, state="*")

    await state.finish()
    await event.reply('<a href="http://t.me/gbbdhdhdifbvfhub_bot>Наш Магазин</a>')

client.start()
client.run_until_disconnected()
