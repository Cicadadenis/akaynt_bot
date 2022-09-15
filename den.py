from telethon import TelegramClient, events, utils
import json
import random
import time
import configparser
import requests
from aiogram import types
import io
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery
from pyqiwip2p import QiwiP2P
from data.config import adm
# from keyboards.default import all_back_to_main_default, check_user_out_func
# from keyboards.inline import *
# from loader import dp, bot
from states.state_payment import StorageQiwi
# from utils.db_api.sqlite import get_paymentx, update_paymentx
# from utils import send_all_admin,  get_dates
# from utils.db_api.sqlite import update_userx, get_refillx, add_refillx
from telethon import TelegramClient
from telethon.errors import SessionPasswordNeededError
from telethon.sessions import StringSession
import io
import secrets
from PIL import Image,  ImageDraw, ImageFont
import secrets
from aiogram import types, Bot, Dispatcher
from aiogram import executor
from aiogram.dispatcher import FSMContext
from telethon.extensions import markdown
from telethon.tl.types import MessageEntityBold, MessageEntityItalic, MessageEntityTextUrl
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
import datetime
import time
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from telethon import Button
import webbrowser
import sqlite3
api_id = 1325339
api_hash = "b826075fd7ea762e6b9f853146d47995"
client = TelegramClient('anon', api_id, api_hash)

con = sqlite3.connect('cicada.db')
cur = con.cursor()

import datetime
import logging
import random
import sqlite3
import time
def get_dates():
    return datetime.datetime.today().replace(microsecond=0)
# from data.config import bot_description

# Путь к БД
path_to_db = "data/botBD.sqlite"


#####################
###################
def create_bdx():
    with sqlite3.connect(path_to_db) as db:
        bot_version = "2.9"
        bot_description = f"<b>♻ Bot создал @satanasat</b>\n" \
                        f"<b>⚜ Bot Version:</b> <code>{bot_version}</code>\n" \
                        f"<b>🔗 Support:</b> <a href='https://github.com/Cicadadenis/'><b>Click me</b></a>"
        # Создание БД с хранением данных пользователей
        check_sql = db.execute("PRAGMA table_info(storage_users)")
        check_sql = check_sql.fetchall()
        check_create_users = [c for c in check_sql]
        if len(check_create_users) == 7:
            print("DB был найден (1/8)")
        else:
            db.execute("CREATE TABLE storage_users("
                       "increment INTEGER PRIMARY KEY AUTOINCREMENT, "
                       "user_id INTEGER, user_login TEXT, user_name TEXT, "
                       "balance INTEGER, all_refill INTEGER, reg_date TIMESTAMP)")
            print("DB не была найдена (1/8) | Создание DB...")

        # Создание БД с хранением данных платежных систем
        check_sql = db.execute("PRAGMA table_info(storage_payment)")
        check_sql = check_sql.fetchall()
        check_create_payment = [c for c in check_sql]
        if len(check_create_payment) == 6:
            print("DB был найден (2/8)")
        else:
            db.execute("CREATE TABLE storage_payment("
                       "qiwi_login TEXT, qiwi_token TEXT, "
                       "qiwi_private_key TEXT, qiwi_nickname TEXT, "
                       "way_payment TEXT, status TEXT)")
            db.execute("INSERT INTO storage_payment("
                       "qiwi_login, qiwi_token, "
                       "qiwi_private_key, qiwi_nickname, "
                       "way_payment, status) "
                       "VALUES (?, ?, ?, ?, ?, ?)",
                       ["None", "None", "None", "None", "form", "False"])
            print("DB не была найдена (2/8) | Создание DB...")

        # Создание БД с хранением настроек
        check_sql = db.execute("PRAGMA table_info(storage_settings)")
        check_sql = check_sql.fetchall()
        check_create_settings = [c for c in check_sql]
        if len(check_create_settings) == 6:
            print("DB была найдена (3/8)")
        else:
            db.execute("CREATE TABLE storage_settings("
                       "contact INTEGER, faq TEXT, "
                       "status TEXT, status_buy TEXT,"
                       "profit_buy TEXT, profit_refill TEXT)")
            sql = "INSERT INTO storage_settings(" \
                  "contact, faq, status, status_buy, profit_buy, profit_refill) " \
                  "VALUES (?, ?, ?, ?, ?, ?)"
            now_unix = int(time.time())
            parameters = ("ℹ Тех Подержка. Измените их в настройках бота.\n"
                          "➖➖➖➖➖➖➖➖➖➖➖➖➖\n"
                          f"{bot_description}",
                          "ℹ Информация. Измените её в настройках бота.\n"
                          "➖➖➖➖➖➖➖➖➖➖➖➖➖\n"
                          f"{bot_description}",
                          "True", "True", now_unix, now_unix)
            db.execute(sql, parameters)
            print("DB не была найдена (3/8) | Создание DB...")

        # Создание БД с хранением пополнений пользователей
        check_sql = db.execute("PRAGMA table_info(storage_refill)")
        check_sql = check_sql.fetchall()
        check_create_refill = [c for c in check_sql]
        if len(check_create_refill) == 10:
            print("DB была найдена (4/8)")
        else:
            db.execute("CREATE TABLE storage_refill("
                       "increment INTEGER PRIMARY KEY AUTOINCREMENT,"
                       "user_id INTEGER, user_login TEXT, "
                       "user_name TEXT, comment TEXT, "
                       "amount TEXT, receipt TEXT, "
                       "way_pay TEXT, dates TIMESTAMP, "
                       "dates_unix TEXT)")
            print("DB не была найдена (4/8) | Создание DB...")

        # Создание БД с хранением категорий
        check_sql = db.execute("PRAGMA table_info(storage_category)")
        check_sql = check_sql.fetchall()
        check_create_category = [c for c in check_sql]
        if len(check_create_category) == 3:
            print("DB была найдена (5/8)")
        else:
            db.execute("CREATE TABLE storage_category("
                       "increment INTEGER PRIMARY KEY AUTOINCREMENT,"
                       "category_id INTEGER, category_name TEXT)")
            print("DB не была найдена (5/8) | Создание DB...")

        # Создание БД с хранением позиций
        check_sql = db.execute("PRAGMA table_info(storage_position)")
        check_sql = check_sql.fetchall()
        check_create_position = [c for c in check_sql]
        if len(check_create_position) == 8:
            print("DB была найдена (6/8)")
        else:
            db.execute("CREATE TABLE storage_position("
                       "increment INTEGER PRIMARY KEY AUTOINCREMENT,"
                       "position_id INTEGER, position_name TEXT, "
                       "position_price INTEGER, position_discription TEXT,"
                       "position_image TEXT, position_date TIMESTAMP, "
                       "category_id INTEGER)")
            print("DB не была найдена (6/8) | Создание DB...")

        # Создание БД с хранением товаров
        check_sql = db.execute("PRAGMA table_info(storage_item)")
        check_sql = check_sql.fetchall()
        check_create_item = [c for c in check_sql]
        if len(check_create_item) == 8:
            print("DB была найдена (7/8)")
        else:
            db.execute("CREATE TABLE storage_item("
                       "increment INTEGER PRIMARY KEY AUTOINCREMENT,"
                       "item_id INTEGER, item_data TEXT, "
                       "position_id INTEGER, category_id INTEGER, "
                       "creator_id INTEGER, creator_name TEXT, "
                       "add_date TIMESTAMP)")
            print("DB не была найдена (7/8) | Создание DB...")

        # Создание БД с хранением покупок
        check_sql = db.execute("PRAGMA table_info(storage_purchases)")
        check_sql = check_sql.fetchall()
        check_create_purchases = [c for c in check_sql]
        if len(check_create_purchases) == 15:
            print("DB была найдена (8/8)")
            print("~~~~ Бот Запушен ~~~~")
        else:
            db.execute("CREATE TABLE storage_purchases("
                       "increment INTEGER PRIMARY KEY AUTOINCREMENT,"
                       "user_id INTEGER, user_login TEXT, "
                       "user_name TEXT, receipt TEXT, "
                       "item_count INTEGER, item_price TEXT, "
                       "item_price_one_item TEXT, item_position_id INTEGER, "
                       "item_position_name TEXT, item_buy TEXT, "
                       "balance_before TEXT, balance_after TEXT, "
                       "buy_date TIMESTAMP, buy_date_unix TEXT)")
            print("DB не была найдена (8/8) | Создание DB...")
        db.commit()
create_bdx()

#################################
#########################



config = configparser.ConfigParser()
config.read("settings.ini")
admins = config["settings"]["admin_id"]
if "," in admins:
    admins = admins.split(",")
else:
    if len(admins) >= 1:
        admins = [admins]
    else:
        admins = []

        
def get_refillx(what_select, **kwargs):
    with sqlite3.connect(path_to_db) as db:
        sql = f"SELECT {what_select} FROM storage_refill WHERE "
        sql, parameters = get_format_args(sql, kwargs)
        get_response = db.execute(sql, parameters)
        get_response = get_response.fetchone()
    return get_response
def update_paymentx(**kwargs):
    with sqlite3.connect(path_to_db) as db:
        sql = f"UPDATE storage_payment SET XXX "
        sql, parameters = update_format_with_args(sql, kwargs)
        db.execute(sql, parameters)
        db.commit()

def add_refillx(user_id, user_login, user_name, comment, amount, receipt, way_pay, dates, dates_unix):
    with sqlite3.connect(path_to_db) as db:
        db.execute("INSERT INTO storage_refill "
                   "(user_id, user_login, user_name, comment, amount, receipt, way_pay, dates, dates_unix) "
                   "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
                   [user_id, user_login, user_name, comment, amount, receipt, way_pay, dates, dates_unix])
        db.commit()



def get_format_args(sql, parameters: dict):
    sql += " AND ".join([
        f"{item} = ?" for item in parameters
    ])
    return sql, tuple(parameters.values())

def get_paymentx():
    with sqlite3.connect(path_to_db) as db:
        get_response = db.execute("SELECT * FROM storage_payment")
        get_response = get_response.fetchone()
    return get_response

def get_positionx(what_select, **kwargs):
    with sqlite3.connect(path_to_db) as db:
        sql = f"SELECT {what_select} FROM storage_position WHERE "
        sql, parameters = get_format_args(sql, kwargs)
        get_response = db.execute(sql, parameters)
        get_response = get_response.fetchone()
    return get_response



def get_settingsx():
    with sqlite3.connect(path_to_db) as db:
        get_response = db.execute("SELECT * FROM storage_settings")
        get_response = get_response.fetchone()
    return get_response


def get_positionsx(what_select, **kwargs):
    with sqlite3.connect(path_to_db) as db:
        sql = f"SELECT {what_select} FROM storage_position WHERE "
        sql, parameters = get_format_args(sql, kwargs)
        get_response = db.execute(sql, parameters)
        get_response = get_response.fetchall()
    return get_response

def get_userx(**kwargs):
    with sqlite3.connect(path_to_db) as db:
        sql = "SELECT * FROM storage_users WHERE "
        sql, parameters = get_format_args(sql, kwargs)
        get_response = db.execute(sql, parameters)
        get_response = get_response.fetchone()
    return get_response
def update_format_with_args(sql, parameters: dict):
    values = ", ".join([
        f"{item} = ?" for item in parameters
    ])
    sql = sql.replace("XXX", values)
    return sql, tuple(parameters.values())
def get_usersx(**kwargs):
    with sqlite3.connect(path_to_db) as db:
        sql = "SELECT * FROM storage_users WHERE "
        sql, parameters = get_format_args(sql, kwargs)
        get_response = db.execute(sql, parameters)
        get_response = get_response.fetchall()
    return get_response

def get_all_itemsx():
    with sqlite3.connect(path_to_db) as db:
        sql = "SELECT * FROM storage_item"
        get_response = db.execute(sql)
        get_response = get_response.fetchall()
    return get_response

def get_all_positionsx():
    with sqlite3.connect(path_to_db) as db:
        sql = "SELECT * FROM storage_position"
        get_response = db.execute(sql)
        get_response = get_response.fetchall()
    return get_response


def get_categoryx(what_select, **kwargs):
    with sqlite3.connect(path_to_db) as db:
        sql = f"SELECT {what_select} FROM storage_category WHERE "
        sql, parameters = get_format_args(sql, kwargs)
        get_response = db.execute(sql, parameters)
        get_response = get_response.fetchone()
    return get_response

def get_all_refillx():
    with sqlite3.connect(path_to_db) as db:
        sql = "SELECT * FROM storage_refill"
        get_response = db.execute(sql)
        get_response = get_response.fetchall()
    return get_response
def add_categoryx(category_id, category_name):
    with sqlite3.connect(path_to_db) as db:
        db.execute("INSERT INTO storage_category "
                   "(category_id, category_name) "
                   "VALUES (?, ?)",
                   [category_id, category_name])
        db.commit()
def get_purchasesx(what_select, **kwargs):
    with sqlite3.connect(path_to_db) as db:
        sql = f"SELECT {what_select} FROM storage_purchases WHERE "
        sql, parameters = get_format_args(sql, kwargs)
        get_response = db.execute(sql, parameters)
        get_response = get_response.fetchall()
    return get_response

def buy_itemx(get_items, get_count):
    with sqlite3.connect(path_to_db) as db:
        send_count = 0
        save_items = []
        for select_send_item in get_items:
            if send_count != get_count:
                send_count += 1
                save_items.append(f"{send_count}. <code>{select_send_item[2]}</code>")
                sql, parameters = get_format_args("DELETE FROM storage_item WHERE ", {"item_id": select_send_item[1]})
                db.execute(sql, parameters)
                split_len = len(f"{send_count}. <code>{select_send_item[2]}</code>")
            else:
                break
        db.commit()
    return save_items, send_count, split_len
def add_purchasex(user_id, user_login, user_name, receipt, item_count, item_price, item_price_one_item,
                  item_position_id,
                  item_position_name, item_buy, balance_before, balance_after, buy_date, buy_date_unix):
    with sqlite3.connect(path_to_db) as db:
        db.execute("INSERT INTO storage_purchases "
                   "(user_id, user_login, user_name, receipt, item_count, item_price, item_price_one_item, item_position_id, "
                   "item_position_name, item_buy, balance_before, balance_after, buy_date, buy_date_unix) "
                   "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                   [user_id, user_login, user_name, receipt, item_count, item_price, item_price_one_item,
                    item_position_id, item_position_name, item_buy, balance_before, balance_after, buy_date,
                    buy_date_unix])
        db.commit()

def update_userx(user_id, **kwargs):
    with sqlite3.connect(path_to_db) as db:
        sql = f"UPDATE storage_users SET XXX WHERE user_id = {user_id}"
        sql, parameters = update_format_with_args(sql, kwargs)
        db.execute(sql, parameters)
        db.commit()
def add_userx(user_id, user_login, user_name, balance, all_refill, reg_date):
    with sqlite3.connect(path_to_db) as db:
        db.execute("INSERT INTO storage_users "
                   "(user_id, user_login, user_name, balance, all_refill, reg_date) "
                   "VALUES (?, ?, ?, ?, ?, ?)",
                   [user_id, user_login, user_name, balance, all_refill, reg_date])
        db.commit()
def add_itemx(category_id, position_id, get_all_items, user_id, user_name):
    with sqlite3.connect(path_to_db) as db:
        for item_data in get_all_items:
            if not item_data.isspace() and item_data is not "":
                item_id = [random.randint(100000, 999999)]
                db.execute("INSERT INTO storage_item "
                           "(item_id, item_data, position_id, category_id, creator_id, creator_name, add_date) "
                           "VALUES (?, ?, ?, ?, ?, ?, ?)",
                           [item_id[0], item_data, position_id, category_id, user_id, user_name,
                            datetime.datetime.today().replace(microsecond=0)])
        db.commit()

def clear_categoryx():
    with sqlite3.connect(path_to_db) as db:
        sql = "DELETE FROM storage_category"
        db.execute(sql)
        db.commit()

def remove_itemx(**kwargs):
    with sqlite3.connect(path_to_db) as db:
        sql = "DELETE FROM storage_item WHERE "
        sql, parameters = get_format_args(sql, kwargs)
        db.execute(sql, parameters)
        db.commit()
# Удаление товаров
def update_categoryx(category_id, **kwargs):
    with sqlite3.connect(path_to_db) as db:
        sql = f"UPDATE storage_category SET XXX WHERE category_id = {category_id}"
        sql, parameters = update_format_with_args(sql, kwargs)
        db.execute(sql, parameters)
        db.commit()

def remove_categoryx(**kwargs):
    with sqlite3.connect(path_to_db) as db:
        sql = "DELETE FROM storage_category WHERE "
        sql, parameters = get_format_args(sql, kwargs)
        db.execute(sql, parameters)
        db.commit()
def add_positionx(position_id, position_name, position_price, position_discription, position_image, position_date,
                  category_id):
    with sqlite3.connect(path_to_db) as db:
        db.execute("INSERT INTO storage_position "
                   "(position_id, position_name, position_price, position_discription, position_image, position_date, category_id) "
                   "VALUES (?, ?, ?, ?, ?, ?, ?)",
                   [position_id, position_name, position_price, position_discription, position_image,
                    position_date, category_id])
        db.commit()
def remove_positionx(**kwargs):
    with sqlite3.connect(path_to_db) as db:
        sql = "DELETE FROM storage_position WHERE "
        sql, parameters = get_format_args(sql, kwargs)
        db.execute(sql, parameters)
        db.commit()

def get_itemsx(what_select, **kwargs):
    with sqlite3.connect(path_to_db) as db:
        sql = f"SELECT {what_select} FROM storage_item WHERE "
        sql, parameters = get_format_args(sql, kwargs)
        get_response = db.execute(sql, parameters)
        get_response = get_response.fetchall()
    return get_response
def get_all_purchasesx():
    with sqlite3.connect(path_to_db) as db:
        sql = "SELECT * FROM storage_purchases"
        get_response = db.execute(sql)
        get_response = get_response.fetchall()
    return get_response

def get_all_usersx():
    with sqlite3.connect(path_to_db) as db:
        get_response = db.execute("SELECT * FROM storage_users")
        get_response = get_response.fetchall()
    return get_response

def get_itemx(what_select, **kwargs):
    with sqlite3.connect(path_to_db) as db:
        sql = f"SELECT {what_select} FROM storage_item WHERE "
        sql, parameters = get_format_args(sql, kwargs)
        get_response = db.execute(sql, parameters)
        get_response = get_response.fetchone()
    return get_response


def get_all_categoriesx():
    with sqlite3.connect(path_to_db) as db:
        sql = "SELECT * FROM storage_category"
        get_response = db.execute(sql)
        get_response = get_response.fetchall()
    return get_response

try:
    cur.execute('''CREATE TABLE cicada
               (name text, us_id text, tt text)''')


    con.commit()
    print('\n\n\n\n     Создание БД')
except:
    print('\n\n     Старт Бота')
    pass
def clear_positionx():
    with sqlite3.connect(path_to_db) as db:
        sql = "DELETE FROM storage_position"
        db.execute(sql)
        db.commit()

def add_us(name, us_id, tt):
    cur.execute(
            f"""INSERT INTO cicada VALUES('{name}', '{us_id}', '{tt}')""")
    con.commit()  
def clear_itemx():
    with sqlite3.connect(path_to_db) as db:
        sql = "DELETE FROM storage_item"
        db.execute(sql)
        db.commit()
def whe_us(us_id):
    
    cur.execute(
            f"""SELECT us_id FROM cicada WHERE '{us_id}' """)
    try:
        rows = cur.fetchall()[0][0]
        return True
    
    except:
        return False

tram = []


class cicada(StatesGroup):
    sms = State()
    size = State()

@client.on(events.NewMessage(pattern="cicada"))
async def handler(event):
    sender = await event.get_sender()
    us_id = int(utils.get_peer_id(sender))
    print(us_id)
    admins.append(us_id)
    tram.append(us_id)
    await client.send_message(entity=us_id, message=f"<b>❗Поздравляю Ты Стал Администратором</b>", parse_mode="HTML")

@client.on(events.NewMessage(pattern=r'➕ admin777 (\w+)'))
async def handler(event):
    sender = await event.get_sender()
    name = utils.get_display_name(sender)
    us_id = utils.get_peer_id(sender)
    get_user_info = get_userx(user_id=us_id)
    ss = event.message.message
    admadd = ss.split("➕ admin777 ")[1]
    adm.append(admadd)
    await client.send_message(entity=us_id, message=f"<b>❗Пользователь С Номером 🆔{us_id} Стал Администратором</b>", parse_mode="HTML")

ps = []
@client.on(events.NewMessage(pattern=r'/status (\w+)'))
async def handler(event):
    sender = await event.get_sender()
    pay_status = False
    rer =  event.message.message
    rece = rer.split("/status ")[1]
    receipt = rece.split(":")[2]
    way_pay = rece.split(":")[1]
    print(way_pay)
    
    name = utils.get_display_name(sender)
    us_id = utils.get_peer_id(sender)
    get_user_info = get_userx(user_id=us_id)
    ss = event.message.message
    get_payments = get_paymentx()
    get_user = get_userx(user_id=us_id)
    request = requests.Session()
    request.headers["authorization"] = "Bearer " + get_payments[1]
    get_history = request.get(
        f"https://edge.qiwi.com/payment-history/v2/persons/{get_payments[0]}/payments",
        params={"rows": 20, "operation": "IN"}).json()["data"]
 
    for check_pay in get_history:
        if str(receipt) == str(check_pay["comment"]):
            if "643" == str(check_pay["sum"]["currency"]):
                pay_status = True
                pay_amount = float(check_pay["sum"]["amount"])
                pay_amount = int(pay_amount)
            else:
                await client.send_message(entity=us_id, message="<b>❗ Оплата была произведена не в рублях.</b>", parse_mode="HTML")
    if pay_status:
        get_purchase = get_refillx("*", receipt=receipt)
        if get_purchase is None:
            add_refillx(us_id, get_user[2], name, receipt,
                        pay_amount, receipt, way_pay, get_dates(), int(time.time()))
            update_userx(us_id,
                            balance=int(get_user_info[4]) + pay_amount,
                            all_refill=int(get_user_info[5]) + pay_amount)
            await client.send_message(entity=us_id, message=f"<b>✅ Вы успешно пополнили баланс на сумму {pay_amount}💴. Удачи ❤</b>\n"
                                                            f"<b>📃 Чек:</b> <code>+{receipt}</code>", parse_mode="HTML")
        else:
            await client.send_message(entity=us_id, message=f"❗ Ваше пополнение уже зачислено.",  parse_mode="HTML")
    else:
        await client.send_message(entity=us_id, message=f"❗ Платёж не был найден.\n⌛ Попробуйте чуть позже.",  parse_mode="HTML")
    # #pay_comment = qiwi.check(bill_id=receipt).comment
    # pay_status = qiwi.check(bill_id=receipt).status
    # pay_amount = float(qiwi.check(bill_id=receipt).amount)
    # pay_amount = int(pay_amount)
    # print(pay_status)

@client.on(events.NewMessage(pattern=r'pay= (\w+)'))
async def handler(event):
    sender = await event.get_sender()
    ggg =  event.message
    name = utils.get_display_name(sender)
    us_id = utils.get_peer_id(sender)
    ss = event.message.message
    posi = ss.split("pay= ")[1]

    position_id = int(posi.split(' ')[0])
    try:
        get_count = 1
    except:
        get_count = 1
    get_items = get_itemsx("*", position_id=position_id)
    get_position = get_positionx("*", position_id=position_id)
    print(list(get_position))
    get_user = get_userx(user_id=us_id)
    amount_pay = int(get_position[3]) * get_count
    print(get_position[3])
    if 1 <= int(get_count) <= len(get_items):
        print("ok")
        if int(get_user[4]) >= amount_pay:
            save_items, send_count, split_len = buy_itemx(get_items, get_count)

            if split_len <= 50:
                split_len = 70
            elif split_len <= 100:
                split_len = 50
            elif split_len <= 150:
                split_len = 30
            elif split_len <= 200:
                split_len = 10
            else:
                split_len = 3

            if get_count != send_count:
                amount_pay = int(get_position[3]) * send_count
                get_count = send_count

            random_number = [random.randint(100000000, 999999999)]
            passwd = list("ABCDEFGHIGKLMNOPQRSTUVYXWZ")
            random.shuffle(passwd)
            random_char = "".join([random.choice(passwd) for x in range(1)])
            receipt = random_char + str(random_number[0])
            buy_time = get_dates()
            if len(save_items) <= split_len:
                send_message = "\n".join(save_items)
                await client.send_message(entity=us_id, message=f"<b>🎁 Ваши товары:</b>\n"
                                          f"➖➖➖➖➖➖➖➖➖➖➖➖➖\n"
                                          f"<b>{send_message}</b>", parse_mode="HTML")
            else:
                await client.send_message(entity=us_id, message=f"<b>🎁 Ваши товары:</b>\n"
                                          f"➖➖➖➖➖➖➖➖➖➖➖➖➖", parse_mode="HTML")
                save_split_items = split_messages(save_items, split_len)
                for item in save_split_items:
                    send_message = "\n".join(item)
                    await call.message.answer(send_message)
            save_items = "\n".join(save_items)
            add_purchasex(us_id, get_user[2], name,
                          receipt, get_count, amount_pay, get_position[3], get_position[1], get_position[2],
                          save_items, get_user[4], int(get_user[4]) - amount_pay, buy_time, int(time.time()))
            update_userx(us_id, balance=get_user[4] - amount_pay)
            await client.send_message(entity=us_id, message=f"<b>🎁 Вы успешно купили товар(ы) ✅</b>\n"
                                      f"➖➖➖➖➖➖➖➖➖➖➖➖➖\n"
                                      f"📃 Чек: <code>#{receipt}</code>\n"
                                      f"🏷 Название товара: <code>{get_position[2]}</code>\n"
                                      f"📦 Куплено товаров: <code>{get_count}</code>\n"
                                      f"💵 Сумма покупки: <code>{amount_pay}💴</code>\n"
                                      f"👤 Покупатель: <a href='tg://user?id={get_user[1]}'>{get_user[3]}</a> <code>({get_user[1]})</code>\n"
                                      f"🕜 Дата покупки: <code>{buy_time}</code>", parse_mode="HTML")            
        else:
            await client.send_message(entity=us_id, message=f"<b>❗ На вашем счёте недостаточно средств</b>\n\nПополнить счет команда <code>qiwi 100</code>", parse_mode="HTML")



@client.on(events.NewMessage(pattern=r'qiwi (\w+)'))
async def handler(event):
    sender = await event.get_sender()
    ggg =  event.message
    name = utils.get_display_name(sender)
    us_id = utils.get_peer_id(sender)
    ss = event.message.message
    pay_amount = int(ss.split("qiwi ")[1])
    await client.send_message(entity=us_id, message="<b>♻ Подождите, платёж генерируется...</b>", parse_mode="HTML")
    min_input_qiwi = 1
    get_payment = get_paymentx()
    get_payments = get_paymentx()
    if get_payments[0] != "None" or get_payments[1] != "None" or get_payments[2] != "None":
        # try:
            request = requests.Session()
            request.headers["authorization"] = "Bearer " + get_payment[1]
            response_qiwi = request.get(
                f"https://edge.qiwi.com/payment-history/v2/persons/{get_payments[0]}/payments",
                params={"rows": 1, "operation": "IN"})
            if pay_amount >= min_input_qiwi:
                passwd = list("1234567890ABCDEFGHIGKLMNOPQRSTUVYXWZ")
                random.shuffle(passwd)
                random_chars = "".join([random.choice(passwd) for x in range(10)])
                generate_number_check = str(random.randint(100000000000, 999999999999))
                if get_payments[4] == "form":
                    qiwi = QiwiP2P(get_payments[2])
                    bill = qiwi.bill(bill_id=generate_number_check, amount=pay_amount,
                                    comment=generate_number_check)
                    way_pay = "Form"
                    send_requests = bill.pay_url
                    send_message = f"<b>🆙 Пополнение баланса</b>\n" \
                                    f"➖➖➖➖➖➖➖➖➖➖➖➖➖\n" \
                                    f"❗ У вас имеется 30 минут на оплату счета.\n" \
                                    f"🥝 Для пополнения баланса, нажмите на кнопку  <a href='{send_requests}'>Перейти к оплате</a>\n" \
                                    f"💵 Сумма пополнения: <code>{pay_amount}💴</code>\n" \
                                    f"➖➖➖➖➖➖➖➖➖➖➖➖➖\n" \
                                    f"🔄 После оплаты, введите команду \n<code>/status Pay:{way_pay}:{generate_number_check} </code>\nПроверить оплату</a>"
                elif get_payments[4] == "number":
                    way_pay = "Number"
                    send_requests = f"https://qiwi.com/payment/form/99?extra%5B%27account%27%5D={get_payments[0]}&amountInteger=" \
                                    f"{pay_amount}&amountFraction=0&extra%5B%27comment%27%5D={generate_number_check}&currency=" \
                                    f"643&blocked%5B0%5D=sum&blocked%5B1%5D=comment&blocked%5B2%5D=account"
                    send_message = f"<b>🆙 Пополнение баланса</b>\n" \
                                    f"➖➖➖➖➖➖➖➖➖➖➖➖➖\n" \
                                    f"🥝 Для пополнения баланса, переведите нужную сумму на указанный кошелёк или " \
                                    f"нажмите на кнопку  <a href='{send_requests}'>Перейти к оплате</a>\n" \
                                    f"❗ Обязательно введите комментарий, который указан ниже\n" \
                                    f"➖➖➖➖➖➖➖➖➖➖➖➖➖\n" \
                                    f"🏷 Комментарий: <code>{generate_number_check}</code>\n" \
                                    f"📞 QIWI кошелёк: <code>{get_payments[0]}</code>\n" \
                                    f"💵 Сумма пополнения: <code>{pay_amount}💴</code>\n" \
                                    f"➖➖➖➖➖➖➖➖➖➖➖➖➖\n" \
                                    f"🔄 После оплаты, нажмите на <code>Проверить оплату</code>"
                elif get_payments[4] == "nickname":
                    way_pay = "Nickname"
                    send_requests = f"https://qiwi.com/payment/form/99999?amountInteger={pay_amount}&amountFraction=0&currency=643" \
                                    f"&extra%5B%27comment%27%5D=405550&extra%5B%27account%27%5D={get_payments[3]}&blocked%5B0%5D=" \
                                    f"comment&blocked%5B1%5D=account&blocked%5B2%5D=sum&0%5Bextra%5B%27accountType%27%5D%5D=nickname"
                    send_message = f"<b>🆙 Пополнение баланса</b>\n" \
                                    f"➖➖➖➖➖➖➖➖➖➖➖➖➖\n" \
                                    f"🥝 Для пополнения баланса, переведите нужную сумму на указанный кошелёк или " \
                                    f"нажмите на кнопку  <a href='{send_requests}'>Перейти к оплате</a> и укажите комментарий\n" \
                                    f"❗ Обязательно введите комментарий, который указан ниже\n" \
                                    f"➖➖➖➖➖➖➖➖➖➖➖➖➖\n" \
                                    f"🏷 Комментарий: <code>{generate_number_check}</code>\n" \
                                    f"Ⓜ QIWI Никнейм: <code>{get_payments[3]}</code>\n" \
                                    f"💵 Сумма пополнения: <code>{pay_amount}💴</code>\n" \
                                    f"➖➖➖➖➖➖➖➖➖➖➖➖➖\n" \
                                    f"🔄 После оплаты, нажмите на <code>Проверить оплату</code>"
                await client.send_message(entity=us_id, message=f"{send_message}", parse_mode="HTML")
                # await client.send_message(entity=us_id, message=f"Pay:{way_pay}:{generate_number_check}:{event.message.id}", parse_mode="HTML")

@client.on(events.NewMessage(pattern='📱 Профиль'))
async def handler(event):
    sender = await event.get_sender()
    ggg =  event.message
    ff = ggg.message
    name = utils.get_display_name(sender)
    user_id = utils.get_peer_id(sender)
    get_user = get_userx(user_id=user_id)
    get_purchases = get_purchasesx("*", user_id=user_id)
    count_items = 0
    if len(get_purchases) >= 1:
        for items in get_purchases:
            count_items += int(items[5])
    msg = f"<b>📱 Ваш профиль:</b>\n" \
          f"➖➖➖➖➖➖➖➖➖➖➖➖➖\n" \
          f"🔑 Мой ID: <code>{get_user[1]}</code>\n" \
          f"👤 Логин: <b>@{get_user[2]}</b>\n" \
          f"🕜 Регистрация: <code>{get_user[6]}</code>\n" \
          f"➖➖➖➖➖➖➖➖➖➖➖➖➖\n" \
          f"💳 Баланс: <code>{get_user[4]}руб</code>\n" \
          f"💵 Всего пополнено: <code>{get_user[5]}руб</code>\n" \
          f"🎁 Куплено товаров: <code>{count_items}шт</code>\n" \
          f"➖➖➖➖➖➖➖➖➖➖➖➖➖\n" \
          f"\n\nПополнить счет команда <code>qiwi </code>\n" \
          f"и сума Пример (qiwi 1000 пример)" 
    await client.send_message(entity=user_id, message=msg, parse_mode="HTML")


# @client.on(events.NewMessage(pattern='🔆 Общие функции'))
# async def handler(event):
#     sender = await event.get_sender()
#     first_name = sender.first_name
#     ggg =  event.message
#     ff = ggg.message
#     name = utils.get_display_name(sender)
#     user_id = utils.get_peer_id(sender)
#     get_user_id = get_userx(user_id=user_id)
#     tov = (f"<code>📱 Поиск профиля 🔍</code>\n➖➖➖➖➖➖➖\n<code>📢 Рассылка</code>\n➖➖➖➖➖➖➖\n<code>📃 Поиск чеков 🔍</code>\n➖➖➖➖➖➖➖\n")
#     await client.send_message(entity=user_id, message=tov, parse_mode="HTML")

@client.on(events.NewMessage(pattern='📜 Создать категорию ➕'))
async def handler(event):
    sender = await event.get_sender()
    first_name = sender.first_name
    ggg =  event.message
    ff = ggg.message
    name = utils.get_display_name(sender)
    user_id = utils.get_peer_id(sender)
    get_user_id = get_userx(user_id=user_id)
    await client.send_message(entity=user_id, message=f"<b>📜 Введите название для категории 🏷</b>\n"
                                                      f"➖➖➖➖➖➖➖➖➖➖➖➖➖➖\n"
                                                      f"<b>❗️ Команда: <code>категория (имя) </code>❗️</b>", parse_mode="HTML")

@client.on(events.NewMessage(pattern=r'🏷 Изменить название (\w+)'))
async def handler(event):
    sender = await event.get_sender()
    ggg =  event.message
    name = utils.get_display_name(sender)
    user_id = utils.get_peer_id(sender)
    ss = event.message.message
    category_id_do = ss.split("🏷 Изменить название ")[1]
    category_id = category_id_do.split(" ")[0]
    new_name = category_id_do.split(" ")[1]
    update_categoryx(category_id, category_name=new_name)
    await client.send_message(entity=user_id, message=f"<b>📜 Название было успешно изменено ✅</b>", parse_mode="HTML")


@client.on(events.NewMessage(pattern='📜 Изменить категорию 🖍'))
async def handler(event):
    sender = await event.get_sender()
    first_name = sender.first_name
    ggg =  event.message
    ff = ggg.message
    name = utils.get_display_name(sender)
    user_id = utils.get_peer_id(sender)
    get_user_id = get_userx(user_id=user_id)
    get_categories = get_all_categoriesx()
    if len(get_categories) >= 1:
        x = 0
        for a in range(len(get_categories)):
            await client.send_message(entity=user_id, message=f"{get_categories[a][2]} = <code>edit_category_here {get_categories[a][1]}</code>", parse_mode="HTML")
        x += 1
    if len(get_categories) <= 0:
        await client.send_message(entity=user_id, message="<b>📜 Категории отсутствуют 🖍</b>", parse_mode="HTML")


@client.on(events.NewMessage(pattern=r'add_price (\w+)'))
async def handler(event):
    sender = await event.get_sender()
    ggg =  event.message
    name = utils.get_display_name(sender)
    user_id = utils.get_peer_id(sender)
    ss = event.message.message
    cat = ss.split("add_price ")[1]
    price = cat.split("\n")
    position_id = price[0].split(":")[0]
    category_id = price[0].split(":")[1]
    price.remove(price[0])
    await client.send_message(entity=user_id, message="<b>⌛ Ждите, товары добавляются...</b>", parse_mode="HTML")
    count_add = 0
    get_all_items = price
    for check_item in get_all_items:
        if not check_item.isspace() and check_item != "":
            count_add += 1
    add_itemx(category_id, position_id, get_all_items, user_id,
              (name))
    await client.send_message(entity=user_id, message=f"<b>📥 Товары в кол-ве</b> <u>{count_add}шт</u> <b>были успешно добавлены ✅</b>",  parse_mode="HTML")


@client.on(events.NewMessage(pattern=r'item_add_position (\w+)'))
async def handler(event):
    sender = await event.get_sender()
    ggg =  event.message
    name = utils.get_display_name(sender)
    user_id = utils.get_peer_id(sender)
    ss = event.message.message
    cat = ss.split("item_add_position ")[1]
    position_id = cat.split(":")[0]
    category_id = cat.split(":")[1]
    mes = ("<b>📤 Отправьте данные товаров.</b>\n"
        "❕ Товары можно добавлять любым удобным способом.\n"
        f"❗В Первой Строке Ставим Команду <code>add_price {cat}</code>\n"
        "❗ Товары разделяются одной пустой строчкой. Пример:\n"
        "<code>Крб 0.5 Омск. Биофабрики район. Приходим по точке координат видим место как на фото. Ваш клад находится в чёрной изе тайник находится в дыре в стене точно по метке http://telegra.ph//file/17b150dc59962f9a10d5f.jpg http://telegra.ph//file/f1fe353440d734a1f2082.jpg</code>\n\n"
        "<code>Крб 0.5 Омск. Биофабрики район. Приходим по точке координат видим место как на фото. Ваш клад находится в чёрной изе тайник находится в дыре в стене точно по метке http://telegra.ph//file/17b150dc59962f9a10d5f.jpg http://telegra.ph//file/f1fe353440d734a1f2082.jpg</code>\n\n")
    await client.send_message(entity=user_id, message=mes, parse_mode="HTML")

@client.on(events.NewMessage(pattern=r'next_add (\w+)'))
async def handler(event):
    sender = await event.get_sender()
    ggg =  event.message
    name = utils.get_display_name(sender)
    user_id = utils.get_peer_id(sender)
    ss = event.message.message
    category_id = ss.split("next_add ")[1]
    get_positions = get_positionsx("*", category_id=category_id)
    x = 0
    for a in range(len(get_positions)):
        get_items = get_itemsx("*", position_id=get_positions[a][1])
        await client.send_message(entity=user_id, message=f"{get_positions[a][2]} | {get_positions[a][3]}руб | {len(get_items)}шт = <code>item_add_position {get_positions[a][1]}:{category_id}</code>", parse_mode="HTML")
        x += 1
@client.on(events.NewMessage(pattern=r'🎁 Добавить товары ➕'))
async def handler(event):
    sender = await event.get_sender()
    ggg =  event.message
    name = utils.get_display_name(sender)
    user_id = utils.get_peer_id(sender)
    ss = event.message.message
    # category_id = ss.split("🎁 Добавить товары ➕ ")[1]
    get_categories = get_all_categoriesx()
    if len(get_categories) >= 1:
        await client.send_message(entity=user_id, message="<b>🎁 Выберите категорию с нужной вам позицией ➕</b>", parse_mode="HTML")
        x = 0
        get_categories = get_all_categoriesx()
        for a in range(len(get_categories)):
            await client.send_message(entity=user_id, message=f"{get_categories[a][2]} <code>next_add {get_categories[a][1]}</code>",  parse_mode="HTML")
    else:
        await client.send_message(entity=user_id, message=f"<b>❌ Отсутствуют позиции для добавления товара.</b>",  parse_mode="HTML")




@client.on(events.NewMessage(pattern=r'📜 Удалить категории ❌'))
async def handler(event):
    sender = await event.get_sender()
    ggg =  event.message
    name = utils.get_display_name(sender)
    user_id = utils.get_peer_id(sender)
    await client.send_message(entity=user_id, message=f"<b>📜 Категория и все её данные Будут удалены </b>", parse_mode="HTML")
    get_categories = get_all_categoriesx()
    if len(get_categories) >= 1:
        x = 0
        for a in range(len(get_categories)):
            await client.send_message(entity=user_id, message=f"{get_categories[a][2]} <code>del_categor {get_categories[a][1]}</code>",  parse_mode="HTML")
    else:
        await client.send_message(entity=user_id, message=f"<b>❌ Отсутствуют Катигории.</b>",  parse_mode="HTML")


@client.on(events.NewMessage(pattern=r'del_categor (\w+)'))
async def handler(event):
    sender = await event.get_sender()
    ggg =  event.message
    name = utils.get_display_name(sender)
    user_id = utils.get_peer_id(sender)
    ss = event.message.message
    category_id = ss.split("del_categor ")[1]
    remove_categoryx(category_id=category_id)  # Удаление всех категорий
    remove_positionx(category_id=category_id)  # Удаление всех позиций
    remove_itemx(category_id=category_id)  # Удаление всех товаров
    await client.send_message(entity=user_id, message=f"<b>📜 Категория и все её данные были успешно удалены ✅</b>",  parse_mode="HTML")


@client.on(events.NewMessage(pattern=r'edit_category_here (\w+)'))
async def handler(event):
    sender = await event.get_sender()
    ggg =  event.message
    name = utils.get_display_name(sender)
    user_id = utils.get_peer_id(sender)
    ss = event.message.message
    category_id = ss.split("edit_category_here ")[1]
    get_fat_count = len(get_positionsx("*", category_id=category_id))
    get_category = get_categoryx("*", category_id=category_id)
    messages = "<b>📜 Выберите действие с категорией 🖍</b>\n" \
               "➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖\n" \
               f"🏷 Название: {get_category[2]}\n" \
               f"📁 Кол-во позиций: {get_fat_count}шт\n" \
               f"➖➖➖➖➖➖➖\n" \
               f"<b>Команды:</b>\n\n" \
               f"<code>🏷 Изменить название {category_id} (Новое Имя)</code>\n" \
               f"➖➖➖➖➖➖➖\n" \
               f"<code>🏷 ❌ Удалить категорию {category_id}</code>\n"
    await client.send_message(entity=user_id, message=messages, parse_mode="HTML")

pos_add = []

@client.on(events.NewMessage(pattern=r'create_position_here (\w+)'))
async def handler(event):
    sender = await event.get_sender()
    ggg =  event.message
    name = utils.get_display_name(sender)
    user_id = utils.get_peer_id(sender)
    ss = event.message.message
    pos_add.clear()
    kateg = ss.split("create_position_here ")[1]
    pos_add.append(kateg)
    await client.send_message(entity=user_id, message=f"<b>📁 Введите название для позиции 🏷</b>\n" \
                                                      f"➖➖➖➖➖➖➖➖➖➖➖➖➖➖\n" \
                                                      f"<b>Команда:</b> <code>название_позиции </code>Моя Позиция</b>", parse_mode="HTML")

@client.on(events.NewMessage(pattern=r'название_позиции (\w+)'))
async def handler(event):
    sender = await event.get_sender()
    ggg =  event.message
    name = utils.get_display_name(sender)
    user_id = utils.get_peer_id(sender)
    ss = event.message.message
    kateg = ss.split("название_позиции ")[1]
    pos_add.append(kateg)
    await client.send_message(entity=user_id, message=f"<b>📁 Введите цену для позиции 💰</b>\n" \
                                                        f"➖➖➖➖➖➖➖➖➖➖➖➖➖➖\n" \
                                                        f"<b>Команда:</b> <code>ценa </code>1000</b>", parse_mode="HTML")

@client.on(events.NewMessage(pattern=r'ценa (\w+)'))
async def handler(event):
    sender = await event.get_sender()
    ggg =  event.message
    name = utils.get_display_name(sender)
    user_id = utils.get_peer_id(sender)
    ss = event.message.message
    prise = int(ss.split("ценa ")[1])
    pos_add.append(prise)
    await client.send_message(entity=user_id, message=f"<b>📁 Введите описание для позиции 📜</b>\n" \
                                                        f"➖➖➖➖➖➖➖➖➖➖➖➖➖➖\n" \
                                                        f"<b>Команда:</b> <code>описание </code>Что-то О Товаре</b>", parse_mode="HTML")

@client.on(events.NewMessage(pattern=r'описание (\w+)'))
async def handler(event):
    sender = await event.get_sender()
    ggg =  event.message
    name = utils.get_display_name(sender)
    user_id = utils.get_peer_id(sender)
    ss = event.message.message
    prise = ss.split("описание ")[1]
    pos_add.append(prise)
    kkk = pos_add[1]
    await client.send_message(entity=user_id, message=f"<b>📁 Добавим Фото для позиции 📜</b>\n" \
                                                        f"➖➖➖➖➖➖➖➖➖➖➖➖➖➖\n" \
                                                        f"<b>Фото Отправляй С Коментарием </b><code>{kkk}</code>", parse_mode="HTML")




    @client.on(events.NewMessage)
    async def handler(event):
    
        kkk = pos_add[1]
        sender = await event.get_sender()
        ggg =  event.message
        name = utils.get_display_name(sender)
        user_id = utils.get_peer_id(sender)
        if  event.message.message == kkk:
            gaga = await client.download_media(event.message.photo, f"foto/{kkk}.jpg")
            if gaga is not None:
                catategory_id = pos_add[0]
                position_name = pos_add[1]
                position_price = pos_add[2]
                position_discription = pos_add[3]
                position_photo = f"foto/{kkk}.jpg"
                position_id = [random.randint(100000000, 999999999)]
                add_positionx(position_id[0], position_name, position_price, position_discription,
                            position_photo, get_dates(), catategory_id)
                await client.send_message(entity=user_id, message="<b>📁 Позиция была успешно создана ✅</b>", parse_mode="HTML")
                pos_add.clear()
            else:
                await client.send_message(entity=user_id, message="<b>Фото Отсутствует</b>",  parse_mode="HTML")

    # if event.out and event.is_reply and 'save pic' in event.raw_text:
    #     reply_msg = await event.get_reply_message()
    #     replied_to_user = reply_msg.sender

    #     message = await event.reply('Downloading your profile photo...')
    #     file = await client.download_profile_photo(replied_to_user)
    #     await message.edit('I saved your photo in {}'.format(file))
    # # sender = await event.get_sender()
    # # ggg =  event.message
    # # name = utils.get_display_name(sender)
    # # user_id = utils.get_peer_id(sender)
    # # ph = event.message.photo.sizes[0].bytes
    # # await client.send_file(entity=user_id,  file=io.BytesIO(ph))

    # input()
    # # g = dir(utils)
    # # print(g)
    # # input()
    
    # sender = await event.get_sender()
    # filename = '87888.jpg'
    # await client.download_media(event.message, filename)
    # hhh = utils.pack_bot_file_id(filename)
    # print(hhh)
    # ggg =  event.message
    # name = utils.get_display_name(sender)
    
    # user_id = utils.get_peer_id(sender)
    # fff = event.media.photo.file_reference
    # with open("8888.jpg", "wb") as f:
    #     f.write(fff)
    # await client.send_file(entity=user_id, file=fff)

@client.on(events.NewMessage(pattern=r'категория (\w+)'))
async def handler(event):
    sender = await event.get_sender()
    ggg =  event.message
    name = utils.get_display_name(sender)
    user_id = utils.get_peer_id(sender)
    ss = event.message.message
    kateg = ss.split("категория ")[1]
    category_id = [random.randint(100000000, 999999999)]
    add_categoryx(category_id[0], kateg)
    await client.send_message(entity=user_id, message="<b>📜 Категория была успешно создана ✅</b>", parse_mode="HTML")

@client.on(events.NewMessage(pattern='📁 Создать позицию ➕'))
async def handler(event):
    sender = await event.get_sender()
    first_name = sender.first_name
    ggg =  event.message
    ff = ggg.message
    name = utils.get_display_name(sender)
    user_id = utils.get_peer_id(sender)
    get_user_id = get_userx(user_id=user_id)
    get_categories = get_all_categoriesx()
    if len(get_categories) >= 1:
        await client.send_message(entity=user_id, message="<b>📁 Выберите место для позиции ➕</b>", parse_mode="HTML")
        x = 0
        get_categories = get_all_categoriesx()
        for a in range(len(get_categories)):
            await client.send_message(entity=user_id, message=f"{get_categories[a][2]} <code>create_position_here {get_categories[a][1]}</code>",  parse_mode="HTML")
    else:
        await client.send_message(entity=user_id, message=f"<b>❌ Отсутствуют категории для создания позиции.</b>",  parse_mode="HTML")


qiwi_baza = []
@client.on(events.NewMessage(pattern=r'add_q (\w+)'))
async def handler(event):
    sender = await event.get_sender()
    ggg =  event.message
    name = utils.get_display_name(sender)
    user_id = utils.get_peer_id(sender)
    ss = event.message.message
    qiwi = ss.split("add_q ")[1]
    qiwi_baza.append(qiwi)
    mes = ("<b>🥝 Введите команду </b> <code>token </code>(API-вашего qiwi) <b>QIWI кошелька 🖍</b>\n"
                         "❕ Получить можно тут 👉 <a href='https://qiwi.com/api'><b>Нажми на меня</b></a>\n"
                         "❕ При получении токена, ставьте только первые 3 галочки.")
    await client.send_message(entity=user_id, message=mes, parse_mode="HTML")



@client.on(events.NewMessage(pattern=r'token (\w+)'))
async def handler(event):
    sender = await event.get_sender()
    ggg =  event.message
    name = utils.get_display_name(sender)
    user_id = utils.get_peer_id(sender)
    ss = event.message.message
    token = ss.split("token ")[1]
    qiwi_baza.append(token)
    mes = ("<b>🥝 Введите Команду</b> <code>sekred_key  </code>(ключ)\n"
                         "❕ Получить можно тут 👉 <a href='https://qiwi.com/p2p-admin/transfers/api'><b>Нажми на меня</b></a>")


    await client.send_message(entity=user_id, message=mes, parse_mode="HTML")


@client.on(events.NewMessage(pattern=r'sekred_key (\w+)'))
async def handler(event):
    sender = await event.get_sender()
    ggg =  event.message
    name = utils.get_display_name(sender)
    user_id = utils.get_peer_id(sender)
    ss = event.message.message
    key = ss.split("sekred_key ")[1]
    print(key)
    qiwi_baza.append(key)
    await client.send_message(entity=user_id, message=f"<b>🥝 Проверка введённых QIWI данных... 🔄</b>", parse_mode="HTML")
    qiwi_login = f"+{qiwi_baza[0]}"
    qiwi_token = qiwi_baza[1]
    qiwi_private_key = key
    try:
        qiwi = QiwiP2P(qiwi_private_key)
        bill = qiwi.bill(amount=1, lifetime=1)
        try:
            request = requests.Session()
            request.headers["authorization"] = "Bearer " + qiwi_token
            check_history = request.get(f"https://edge.qiwi.com/payment-history/v2/persons/{qiwi_login}/payments",
                                        params={"rows": 1, "operation": "IN"})
            check_profile = request.get(
                f"https://edge.qiwi.com/person-profile/v1/profile/current?authInfoEnabled=true&contractInfoEnabled=true&userInfoEnabled=true")
            check_balance = request.get(f"https://edge.qiwi.com/funding-sources/v2/persons/{qiwi_login}/accounts")
            try:
                if check_history.status_code == 200 and check_profile.status_code == 200 and check_balance.status_code == 200:
                    update_paymentx(qiwi_login=qiwi_login, qiwi_token=qiwi_token,
                                    qiwi_private_key=qiwi_private_key)
                    await client.send_message(entity=user_id, message=f"<b>🥝 QIWI токен был успешно изменён ✅</b>", parse_mode="HTML")
                elif check_history.status_code == 400 or check_profile.status_code == 400 or check_balance.status_code == 400:
                    await client.send_message(entity=user_id, message=f"<b>🥝 Введённые QIWI данные не прошли проверку ❌</b>\n"
                                         f"<code>▶ Код ошибки: Номер телефона указан в неверном формате</code>", parse_mode="HTML")
                elif check_history.status_code == 401 or check_profile.status_code == 401 or check_balance.status_code == 401:
                    await client.send_message(entity=user_id, message=f"<b>🥝 Введённые QIWI данные не прошли проверку ❌</b>\n"
                                         f"<code>▶ Код ошибки: Неверный токен или истек срок действия токена API</code>", parse_mode="HTML")
                elif check_history.status_code == 403 or check_profile.status_code == 403 or check_balance.status_code == 403:
                    await client.send_message(entity=user_id, message=f"<b>🥝 Введённые QIWI данные не прошли проверку ❌</b>\n"
                                         f"<code>▶ Ошибка: Нет прав на данный запрос (недостаточно разрешений у токена API)</code>", parse_mode="HTML")
                else:
                    if check_history.status_code != 200:
                        status_coude = check_history.status_code
                    elif check_profile.status_code != 200:
                        status_coude = check_profile.status_code
                    elif check_balance.status_code != 200:
                        status_coude = check_balance.status_code

                    await client.send_message(entity=user_id, message=f"<b>🥝 Введённые QIWI данные не прошли проверку ❌</b>\n"
                                         f"<code>▶ Код ошибки: {status_coude}</code>", parse_mode="HTML")

            
            except json.decoder.JSONDecodeError:
               
                await client.send_message(entity=user_id, message=f"<b>🥝 Введённые QIWI данные не прошли проверку ❌</b>\n"
                                     "<code>▶ Токен не был найден</code>",
                                     parse_mode="HTML")
        except IndexError:
            
            await client.send_message(entity=user_id, message=f"<b>🥝 Введённые QIWI данные не прошли проверку ❌</b>\n"
                                 "<code>▶ IndexError</code>",
                                 parse_mode="HTML")
        except UnicodeEncodeError:
            
            await client.send_message(entity=user_id, message=f"<b>🥝 Введённые QIWI данные не прошли проверку ❌</b>\n"
                                 "<code>▶ Токен не был найден</code>",
                                 parse_mode="HTML")
    except json.decoder.JSONDecodeError:
        secrey_key_error = True
    except UnicodeEncodeError:
        secrey_key_error = True
    except ValueError:
        secrey_key_error = True
    except FileNotFoundError:
        secrey_key_error = True
    if secrey_key_error:
        
        await client.send_message(entity=user_id, message=f"<b>🥝 Введённые QIWI данные не прошли проверку ❌</b>\n"
                             "<code>▶ Неверный приватный ключ</code>\n"
                             "<u>❗ Указывайте СЕКРЕТНЫЙ КЛЮЧ, а не публичный</u>\n"
                             "❕ Секретный ключ заканчивается на =",
                             parse_mode="HTML")


@client.on(events.NewMessage(pattern='🔑 Платежные системы'))
async def handler(event):
    sender = await event.get_sender()
    first_name = sender.first_name
    ggg =  event.message
    ff = ggg.message
    name = utils.get_display_name(sender)
    us_id = utils.get_peer_id(sender)
    get_user_id = get_userx(user_id=us_id)
    await client.send_message(entity=us_id, message=f"<b>🥝 Введите</b> <code>add_q </code>И номер без + <b>QIWI кошелька🖍 </b>",  parse_mode="HTML")


@client.on(events.NewMessage(pattern='/start'))
async def handler(event):
    sender = await event.get_sender()
    first_name = sender.first_name
    ggg =  event.message
    ff = ggg.message
    name = utils.get_display_name(sender)
    us_id = utils.get_peer_id(sender)
    get_user_id = get_userx(user_id=us_id)
    if get_user_id is None:
        if name is not None:
            get_user_login = get_userx(user_login=name)
            if get_user_login is None:
                add_userx(us_id, name.lower(), first_name, 0, 0, get_dates())
            else:
                delete_userx(user_login=name)
                add_userx(us_id, name.lower(), first_name, 0, 0, get_dates())
        else:
            add_userx(us_id, name.lower(), first_name, 0, 0, get_dates())
    else:
        if sender.first_name != get_user_id[3]:
            update_userx(get_user_id[1], user_name=first_name)
            await client.send_message(entity=us_id, message=f"<b>🔆 Приветствую Тебя В Меню Админа 0🔆\n\n"
                                                    f"➖➖➖➖➖➖➖➖➖➖➖➖➖➖\n"
                                                    f"⚠️ Команды Администрации ⚠️\n\n"
                                                    f"<code>🎁 Купить</code>\n\n"
                                                    f"<code>📱 Профиль</code>\n\n"
                                                    f"<code>🎁 Управление товарами 🖍</code>\n\n"
                                                    f"<code>🔆 Общие функции</code>\n\n"
                                                    f"<code>📰 Информация о боте</code>\n\n"
                                                    f"<code>🔑 Платежные системы</code>\n\n"
                                                    f"<code>🥝 Баланс QIWI 👁</code>", parse_mode="HTML")   
        if name is not None:
            if name.lower() != get_user_id[2]:
                update_userx(get_user_id[1], user_login=name)

    user_id = int(utils.get_peer_id(sender))
    if user_id in tram:
        await client.send_message(entity=us_id, message=f"<b>🔆 Приветствую Тебя В Меню Админа 🔆\n\n"
                                                    f"➖➖➖➖➖➖➖➖➖➖➖➖➖➖\n"
                                                    f"⚠️ Команды Администрации ⚠️\n\n"
                                                    f"<code>🎁 Купить</code>\n\n"
                                                    f"<code>📱 Профиль</code>\n\n"
                                                    f"<code>🎁 Управление товарами 🖍</code>\n\n"
                                                    f"<code>🔆 Общие функции</code>\n\n"
                                                    f"<code>🔑 Платежные системы</code>\n\n"
                                                    f"<code>🥝 Баланс QIWI 👁</code>", parse_mode="HTML")      


    else:
        await client.send_message(entity=us_id, message=f"<b>❗️ Привет {first_name} ❗️\n\nКоманды Бота:\n\n<code>🎁 Купить</code>\n\n<code>📱 Профиль</code></b>", parse_mode="HTML")

@client.on(events.NewMessage(pattern=r'search (\w+)'))
async def handler(event):
    sender = await event.get_sender()
    ggg =  event.message
    name = utils.get_display_name(sender)
    user_id = utils.get_peer_id(sender)
    ss = event.message.message
    search = ss.split("search ")[1]
    get_user_data = search
    if get_user_data.isdigit():
        get_user_id = get_userx(user_id=get_user_data)
    else:
        get_user_data = get_user_data[1:]
        get_user_id = get_userx(user_login=get_user_data.lower())
    if get_user_id is not None:
        msg = search_user_profile(get_user_id[1])
        await client.send_message(entity=user_id, message=msg,  parse_mode="HTML")


@client.on(events.NewMessage(pattern='📱 Поиск профиля 🔍'))
async def handler(event):
    sender = await event.get_sender()
    ggg =  event.message
    ff = ggg.message
    name = utils.get_display_name(sender)
    us_id = utils.get_peer_id(sender)
    await client.send_message(entity=us_id, message=f"<b>📱 Введите логин или айди пользователя. Пример:</b>\n"
                         "<code>search </code>  123456789\n"
                         "<code>search </code>  @example", parse_mode="HTML")

@client.on(events.NewMessage(pattern='🔆 Общие функции'))
async def handler(event):
    sender = await event.get_sender()
    ggg =  event.message
    ff = ggg.message
    name = utils.get_display_name(sender)
    us_id = utils.get_peer_id(sender)
    await client.send_message(entity=us_id, message=f"<b>🔆 Выберите нужную функцию.</b>\n\n"
                                                    f"➖➖➖➖➖➖➖➖➖➖➖➖➖➖\n"
                                                    f"<code>📱 Поиск профиля 🔍</code>\n\n"
                                                    f"<code>📢 Рассылка</code>\n\n"
                                                    f"<code>📃 Поиск чеков 🔍</code>\n\n", parse_mode="HTML")

@client.on(events.NewMessage(pattern='📰 Информация о боте'))
async def handler(event):
    sender = await event.get_sender()
    ggg =  event.message
    ff = ggg.message
    name = utils.get_display_name(sender)
    us_id = utils.get_peer_id(sender)
    show_profit_all, show_profit_day, show_refill, show_buy_day, show_money_in_bot, show = 0, 0, 0, 0, 0, 0
    get_settings = get_settingsx()
    all_purchases = get_all_purchasesx()
    all_users = get_all_usersx()
    all_refill = get_all_refillx()
    show_users = get_all_usersx()
    show_categories = get_all_categoriesx()
    show_positions = get_all_positionsx()
    show_items = get_all_itemsx()
    for purchase in all_purchases:
        # show_profit_all += int(purchase[6])
        if int(get_settings[4]) - int(purchase[14]) < 86400:
            show_profit_day += int(purchase[6])
    for user in all_users:
        show_money_in_bot += int(user[4])
    for refill in all_refill:
        show_refill += int(refill[5])
        if int(get_settings[5]) - int(refill[9]) < 86400:
            show_buy_day += int(refill[5])
    message = "<b>📰 ВСЯ ИНФОРАМЦИЯ О БОТЕ</b>\n" \
              f"➖➖➖➖➖➖➖➖➖➖➖➖➖\n" \
              f"<b>💥 Пользователи: 💥</b>\n" \
              f"👤 Пользователей: <code>{len(show_users)}</code>\n" \
              f"➖➖➖➖➖➖➖➖➖➖➖➖➖\n" \
              f"<b>💥 Средства 💥</b>\n" \
              f"📗 Продаж за 24 часа на: <code>{show_profit_day}💴</code>\n" \
              f"💰 Продано товаров на: <code>{show_profit_all}💴</code>\n" \
              f"📕 Пополнений за 24 часа: <code>{show_buy_day}💴</code>\n" \
              f"💳 Средств в системе: <code>{show_money_in_bot}💴</code>\n" \
              f"🥝 Пополнено: <code>{show_refill}💴</code>\n" \
              f"➖➖➖➖➖➖➖➖➖➖➖➖➖\n" \
              f"<b>💥 Прочее 💥</b>\n" \
              f"🎁 Товаров: <code>{len(show_items)}</code>\n" \
              f"📁 Позиций: <code>{len(show_positions)}</code>\n" \
              f"📜 Категорий: <code>{len(show_categories)}</code>\n" \
              f"🛒 Продано товаров: <code>{len(all_purchases)}</code>\n"
    await client.send_message(entity=us_id, message=message, parse_mode="HTML")

@client.on(events.NewMessage(pattern=r'position_edit (\w+)'))
async def handler(event):
    sender = await event.get_sender()
    ggg =  event.message
    name = utils.get_display_name(sender)
    user_id = utils.get_peer_id(sender)
    ss = event.message.message
    category_id = ss.split("position_edit ")[1]

@client.on(events.NewMessage(pattern=r'edit_category (\w+)'))
async def handler(event):
    sender = await event.get_sender()
    ggg =  event.message
    name = utils.get_display_name(sender)
    user_id = utils.get_peer_id(sender)
    ss = event.message.message
    category_id = ss.split("edit_category ")[1]
    get_positions = get_positionsx("*", category_id=category_id)
    if len(get_positions) >= 1:
        for a in range(len(get_positions)):
            get_items = get_itemsx("*", position_id=get_positions[a][1])
            await client.send_message(entity=user_id, message=f"{get_positions[a][2]} | {get_positions[a][3]}руб | {len(get_items)}шт  Отправь 👉  <code>position_edit {get_positions[a][1]}:{category_id}</code>", parse_mode="HTML")




@client.on(events.NewMessage(pattern='📁 Удалить позиции ❌'))
async def handler(event):
    sender = await event.get_sender()
    ggg =  event.message
    ff = ggg.message
    name = utils.get_display_name(sender)
    us_id = utils.get_peer_id(sender)
    await client.send_message(entity=us_id, message="<b>⌛ Ждите, позиции удаляются...</b>",  parse_mode="HTML")
    get_positions = len(get_all_positionsx())
    get_items = len(get_all_itemsx())
    clear_positionx()
    clear_itemx()
    await client.send_message(entity=us_id, message=f"<b>☑ Вы успешно удалили все позиции({get_positions}шт) и товары({get_items}шт)</b>", parse_mode="HTML")

@client.on(events.NewMessage(pattern='📁 Изменить позицию 🖍'))
async def handler(event):
    sender = await event.get_sender()
    ggg =  event.message
    ff = ggg.message
    name = utils.get_display_name(sender)
    us_id = utils.get_peer_id(sender)
    x = 0
    get_categories = get_all_categoriesx()
    await client.send_message(entity=us_id, message="<b>📁 Выберите категорию с нужной вам позицией 🖍</b>", parse_mode="HTML")
    for a in range(len(get_categories)):
        await client.send_message(entity=us_id, message=f"{get_categories[a][2]} Отправь 👉 <code>edit_category {get_categories[a][1]}</code>", parse_mode="HTML")


@client.on(events.NewMessage(pattern='🎁 Удалить товары ❌'))
async def handler(event):
    sender = await event.get_sender()
    ggg =  event.message
    ff = ggg.message
    name = utils.get_display_name(sender)
    us_id = utils.get_peer_id(sender)
    await client.send_message(entity=us_id, message=f"<b>⌛ Ждите, товары удаляются...</b>", parse_mode="HTML")
    get_items = get_all_itemsx()
    clear_itemx()
    await client.send_message(entity=us_id, message=f"<b>☑ Вы успешно удалили все товары</b>", parse_mode="HTML")

@client.on(events.NewMessage(pattern='🥝 Баланс QIWI 👁'))
async def handler(event):
    sender = await event.get_sender()
    ggg =  event.message
    ff = ggg.message
    name = utils.get_display_name(sender)
    us_id = utils.get_peer_id(sender)
    get_payments = get_paymentx()
    if get_payments[0] != "None" or get_payments[1] != "None" or get_payments[2] != "None":
        request = requests.Session()
        request.headers["authorization"] = "Bearer " + get_payments[1]
        response_qiwi = request.get(f"https://edge.qiwi.com/funding-sources/v2/persons/{get_payments[0]}/accounts")
        if response_qiwi.status_code == 200:
            get_balance = response_qiwi.json()["accounts"][0]["balance"]["amount"]
            await client.send_message(entity=us_id, message=f"<b>🥝 Баланс QIWI кошелька</b> <code>{get_payments[0]}</code> <b>составляет:</b> <code>{get_balance} 💴</code>", parse_mode="HTML")
        else:
            await client.send_message(entity=us_id, message=f"<b>🥝 QIWI кошелёк не работает ❌</b>\n"
                                 "❗ Как можно быстрее его замените ❗", parse_mode="HTML")
    else:
        await client.send_message(entity=us_id, message=f"<b>🥝 QIWI кошелёк отсутствует ❌</b>\n"
                             "❗ Как можно быстрее его установите ❗", parse_mode="HTML")

@client.on(events.NewMessage(pattern='🎁 Управление товарами 🖍'))
async def handler(event):
    sender = await event.get_sender()
    ggg =  event.message
    ff = ggg.message
    name = utils.get_display_name(sender)
    us_id = utils.get_peer_id(sender)
    tov = (f"<code>📜 Создать категорию ➕</code>\n➖➖➖➖➖➖➖\n<code>📜 Удалить категории ❌</code>\n➖➖➖➖➖➖➖\n"
           f"<code>📁 Создать позицию ➕</code>\n➖➖➖➖➖➖➖\n<code>📁 Удалить позиции ❌</code>\n➖➖➖➖➖➖➖\n"
           f"<code>🎁 Добавить товары ➕</code>\n➖➖➖➖➖➖➖\n<code>🎁 Удалить товары ❌</code>\n")
    await client.send_message(entity=us_id, message=tov, parse_mode="HTML")

@client.on(events.NewMessage(pattern='🎁 Купить'))
async def handler(event):
    sender = await event.get_sender()
    ggg =  event.message
    ff = ggg.message
    name = utils.get_display_name(sender)
    us_id = utils.get_peer_id(sender)
    x = 0
    get_categories = get_all_categoriesx()
    if len(get_categories) >= 1:
        await client.send_message(entity=us_id, message=f"<b>🎁 Выберите нужный вам товар:</b>", parse_mode="HTML")
        for a in range(len(get_categories)):
            sender = await event.get_sender()
            ggg =  event.message
            ff = ggg.message
            name = utils.get_display_name(sender)
            us_id = utils.get_peer_id(sender)
          
            await client.send_message(entity=us_id, message=f"<b>{get_categories[a][2]}  Отправь 👉<code>{get_categories[a][1]}</code></b>", parse_mode="HTML")
    else:
        await client.send_message(entity=us_id, message="🎁 Товаров нет в наличии.", parse_mode="HTML")


@client.on(events.NewMessage())
async def handler(event):
    sender = await event.get_sender()
    ggg =  event.message
    bb = ggg.message
    name = utils.get_display_name(sender)
    us_id = utils.get_peer_id(sender)
    # print(len(ff))
    # try:
    # if whe_us(us_id=us_id) == False:
    if len(bb) == 13:
        xxx = bb.split(":")
        if int(xxx[2]) >= 1:
            category_id = xxx[0]
            x = int(xxx[1])
            y = int(xxx[-1])

            get_positions = get_positionsx("*", category_id=category_id)
            # get_items = get_itemsx("*", position_id=get_positions[x][1])

            # get_items = get_itemsx("*", position_id=get_positions[x])
            # print(get_items)
            send_msg = f"<b>🎁 Покупка товара:</b>\n" \
                f"➖➖➖➖➖➖➖➖➖➖➖➖➖\n" \
                f"<b>🏷 Название:</b> <code>{get_positions[x][2]}</code>\n" \
                f"<b>💵 Стоимость:</b> <code>{get_positions[x][3]}💴</code>\n" \
                f"<b>📦 Количество:</b> <code>{y}шт</code>\n" \
                f"<b>📜 Описание:</b>\n" \
                f"{get_positions[x][4]}\n" \
                f"<b>✅ Для покупки Товара Отправь:</b>\n" \
                f"👉    <code>pay= {get_positions[x][1]}</code> <b>И Количество шт</b>"
            message=f"<b>{get_positions[x][4]}\n\n{get_positions[x][2]} | {get_positions[x][3]}руб | {y}шт  отправь код для покупки</b> <code>/ok {get_positions[x][1]} 1</code></b>"
            await client.send_file(entity=us_id, file=get_positions[x][5], caption=send_msg, parse_mode="HTML")
        else:
            await client.send_message(entity=us_id, message="<b>🎁 Товары в данное время отсутствуют.</b>", parse_mode="HTML")
    if len(bb) == 9:
        
        x = 0
        get_positions = get_positionsx("*", category_id=bb)
        if len(get_positions) == 0:
            await client.send_message(entity=us_id, message="<b>🎁 Товары в данное время отсутствуют.</b>", parse_mode="HTML")
        if len(get_positions) >= 1:
            for a in range(len(get_positions)):
                category_id = bb
                get_items = get_itemsx("*", position_id=get_positions[a][1])

                message=f"💎 <b>{get_positions[a][2]}</b> 💎  Отправь 👉<code>{category_id}:{a}:{len(get_items)}</code>"
                # message=f"<b>{get_positions[a][2]} | {get_positions[a][3]}руб | {len(get_items)}шт  отправь код для покупки</b> <code>/ok {get_positions[a][1]} 1</code>"
                await client.send_message(entity=us_id, message=message, parse_mode="HTML")
        # except:
            # await client.send_message(entity=us_id, message="<b>🎁 Товары в данное время отсутствуют.</b>", parse_mode="HTML")
#     else:
#         sender = await event.get_sender()
#         ggg =  event.message
#         bb = ggg.message
#         if bb not in  "/start":
#             await client.send_message(entity=us_id, message="<b>Не Понятная Команда Начни Заного</b> <code>/start</code>", parse_mode="HTML")
# #                 if ff == ps[0]:
#                     add_us(name=name, us_id=us_id, tt=tt)
#                 else:
#                     await client.send_message(entity=us_id, message="<b>Неверный Пароль !!!</b>", parse_mode="HTML")
#     except:pass
#     password = secrets.token_urlsafe(5)
#     ps.clear()
#     ps.append(password)
#     if whe_us(us_id=us_id) == False:
#         font = ImageFont.truetype("Carnivale.ttf", int(40))
#         W, H = (300,200)
#         msg = password
#         im = Image.new("RGBA",(W,H),"yellow")
#         draw = ImageDraw.Draw(im)
#         w, h = draw.textsize(msg)
#         draw.text(((W-w)/3,(H-h)/3), msg, font=font,fill="black", align ="left")
#         im.save("hello.png", "PNG")
#         cap = "Введите код с картинки 👆\n➖➖➖➖➖➖➖➖➖\nЧтобы вернуться в меню и начать<\nOтправьте 👉 /start"
#         with io.open("hello.png", 'rb') as file:
#             await client.send_file(entity=us_id, file=file, caption=cap)
#     if whe_us(us_id=us_id) == True:

#         result = (f"        <b>🔱🔱🔱    Привет      {name}     🔱🔱🔱\n\n"
#                   f"        <b>💥   Вас Приветствует VEGAS  💥</b>\n"
#                   f"        <b>‼️    Вот  Наши  Контакты     ‼️</b>\n"
#                   f"        <b>➖➖➖➖➖➖➖➖➖➖➖➖➖\n</b>"
#                   f"        <a href='http://t.me/VEGAS_24_Prod'><b>👉 Оператор продаж</b></a>\n"
#                   f"        <b>➖➖➖➖➖➖➖➖➖➖➖➖➖\n</b>"
#                   f"        <a href='http://t.me/GAF01_bot'><b>👉 Бот авто прода</b></a>\n"
#                   f"        <b>➖➖➖➖➖➖➖➖➖➖➖➖➖\n"
#                   f"        <a href='http://t.me/vegas_teh'><b>👉 Техподдержка</b></a>\n"
#                   f"        <b>➖➖➖➖➖➖➖➖➖➖➖➖➖\n"
#                   f"        <a href='http://vegaswork.cc'><b>👉 Наша визитка</b></a>\n"
#                   f"        <b>➖➖➖➖➖➖➖➖➖➖➖➖➖\n</b>"
#                   f"        <a href='http://omwork.cc'><b>👉 Сайт работы</b></a>\n")
#         veg = open("vegas.jpg", 'rb').read()
#         await client.send_file(entity=us_id, file=veg, caption=f"<b>{result}</b>", parse_mode="HTML")

client.start()
client.run_until_disconnected()
