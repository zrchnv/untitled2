import requests
import datetime
from pprint import pprint
from config import open_weather_token


def get_weather(city, open_weather_token):

    code_to_smile = {
        "Clear": "Ясно \U00002600",
        "Clouds": "Облачно \U00002601",
        "Rain": "Дождик \U00002614",
        "Drizzle": "Ясно \U00002614",
        "Snow": "Снег \U0001F328",
        "Mist": "туман \U0001F32B",
        "Thunderzone": "Гроза \U000026A1",
        "Thunderzone": "Гроза \U000026A1",
    }

    try:
        r = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={open_weather_token}&units=metric"
        )
        data = r.json()
        #pprint(data)

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

        print(f"***{datetime.datetime.now().strftime('%d-%M-%y')}***\n"
            f"Погода в городе: {city}\nТемпература: {cur_weather}с° {wd}\n"
            f"Влажность: {humidity}\nДавление: {pressure} мм\nВетер {wind}m/s\n"
            f"восход солнца: {sunrise_timestamp}\nзакат солнца: {sunset_timestamp}\nПродолжительность дня: {lengh_of_the_day}\n"
            f"\U0001F974	 Котков лох"
              )


    except Exception as ex:
        print(ex)
        print("Проверьте название города")


def main():
    city = input("Введите город:")
    get_weather(city, open_weather_token)

if __name__ == '__main__':
    main()


