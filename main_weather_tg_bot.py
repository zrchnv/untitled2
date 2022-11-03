import requests
import datetime
from config import tg_bot_token, open_weather_token
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

bot = Bot(token=tg_bot_token)
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    await message.reply("Напиши город")


@dp.message_handler()
async def get_weather(message: types.Message):
    code_to_smile = {
        "Clear": "Ясно \U00002600",
        "Clouds": "Облачно \U00002601",
        "Rain": "Дождик \U00002614",
        "Drizzle": "Ясно \U00002614",
        "Snow": "Снег \U0001F328",
        "Mist": "туман \U0001F32B",
    }

    try:
        r = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={open_weather_token}&units=metric"
        )
        data = r.json()

        city = data["name"]
        cur_weather = data["main"]["temp"]

        weather_description = data["weather"][0]["main"]
        if weather_description in code_to_smile:
            wd = code_to_smile[weather_description]
        else: "Неведомая погода происходит"

        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"] # что то не то
        wind = data["wind"]["speed"]
        sunrise_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
        sunset_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunset"])
        lengh_of_the_day = datetime.datetime.fromtimestamp(data["sys"]["sunset"]) - datetime.datetime.fromtimestamp(
            data["sys"]["sunrise"])

        await message.reply(f"***{datetime.datetime.now().strftime('%d-%m-%y')}***\n"
            f"Погода в городе: {city}\nТемпература: {cur_weather}с° {wd}\n"
            f"Влажность: {humidity}\nДавление: {pressure} мм\nВетер {wind}m/s\n"
            f"восход солнца: {sunrise_timestamp}\nзакат солнца: {sunset_timestamp}\nПродолжительность дня: {lengh_of_the_day}\n"
            f"\U0001F974	 Котков лох"
              )


    except:
        await message.reply("\U00002620Проверьте название города")

if __name__ == '__main__':
    executor.start_polling(dp)
