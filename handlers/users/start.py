import requests
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove

from keyboards.default.kurs import menukurs
from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Salom, {message.from_user.full_name}!",reply_markup=menukurs)


@dp.message_handler(Command('about'), states=None)
async def b(message: Message):
    await message.answer("Admin: @Sarvarssssc ☎ \nBot 7 ta kurslarni aniqlab beradi️\nHar kuni Yangilanib boriladi \nSizga albatta foydasi tegadi 😉")


API_KEY =  'f4d35ae73feeb7cc4a466814'




@dp.message_handler(text='USD')
async def send_link(message: Message):
    currency = 'USD'
    url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/pair/{currency}/UZS"
    response = requests.get(url)
    # print(response.status_code)
    # print(response.json())
    jsondata = response.json()
    kurs = response.json()['conversion_rate']
    await message.answer(f"Bugungi kurs: 1 AQSH dollari = {kurs} so'm", reply_markup=menukurs)

@dp.message_handler(text='EUR')
async def send_link(message: Message):
    currency = 'EUR'
    url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/pair/{currency}/UZS"
    response = requests.get(url)
    # print(response.status_code)
    # print(response.json())
    jsondata = response.json()
    kurs = response.json()['conversion_rate']
    await message.answer(f"Bugungi kurs: 1-Euro = {kurs} so'm", reply_markup=menukurs)

@dp.message_handler(text='UAE Dirham')
async def send_link(message: Message):
    currency = 'AED'
    url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/pair/{currency}/UZS"
    response = requests.get(url)
    # print(response.status_code)
    # print(response.json())
    jsondata = response.json()
    kurs = response.json()['conversion_rate']
    await message.answer(f"Bugungi kurs: 1-Dirham = {kurs} so'm", reply_markup=menukurs)

@dp.message_handler(text='India Rupee')
async def send_link(message: Message):
    currency = 'INR'
    url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/pair/{currency}/UZS"
    response = requests.get(url)
    # print(response.status_code)
    # print(response.json())
    jsondata = response.json()
    kurs = response.json()['conversion_rate']
    await message.answer(f"Bugungi kurs: 1-Rupee = {kurs} so'm", reply_markup=menukurs)

@dp.message_handler(text='Japan Yen')
async def send_link(message: Message):
    currency = 'JPY'
    url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/pair/{currency}/UZS"
    response = requests.get(url)
    # print(response.status_code)
    # print(response.json())
    jsondata = response.json()
    kurs = response.json()['conversion_rate']
    await message.answer(f"Bugungi kurs: 1-Yen = {kurs} so'm", reply_markup=menukurs)

@dp.message_handler(text='Tenge')
async def send_link(message: Message):
    currency = 'KZT'
    url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/pair/{currency}/UZS"
    response = requests.get(url)
    # print(response.status_code)
    # print(response.json())
    jsondata = response.json()
    kurs = response.json()['conversion_rate']
    await message.answer(f"Bugungi kurs: 1-Tenge = {kurs} so'm", reply_markup=menukurs)

@dp.message_handler(text='Turkish Lira')
async def send_link(message: Message):
    currency = 'TRY'
    url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/pair/{currency}/UZS"
    response = requests.get(url)
    # print(response.status_code)
    # print(response.json())
    jsondata = response.json()
    kurs = response.json()['conversion_rate']
    await message.answer(f"Bugungi kurs: 1-Lira = {kurs} so'm", reply_markup=menukurs)

@dp.message_handler(text='Log Out')
async def send_link(message: Message):
    await message.answer("Foydalanganingiz Uchun Rahmat 😊😊😊 ", reply_markup=ReplyKeyboardRemove())

