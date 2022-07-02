import datetime

import requests

city_ = input("Enter city: ")
days_ = input("Enter day: ")


def get_weather(city, days):
    url = "http://api.openweathermap.org/data/2.5/forecast/" \
          f"daily?q={city}&cnt={days}&units=metric&appid=f9ada9efec6a3934dad5f30068fdcbb8"
    response = requests.get(url)
    return response.json()


def convert_weather(weather_json):
    title = "Date        Day temp  Night temp\n"
    weather_text_list = [title]

    for day in weather_json["list"]:
        date_obj = datetime.datetime.fromtimestamp(day["dt"])
        date = date_obj.strftime("%d-%m-%Y")
        day_temp = day["temp"]["day"]
        night_temp = day["temp"]["night"]
        string = f"{date}  {day_temp}     {night_temp}\n"
        weather_text_list.append(string)

    return weather_text_list


def write_weather_to_file(weather_list_text, city_name, days_count):
    file_name = f"{city_name}_{days_count}_days_forecast.txt"

    with open(file_name, "w") as file:
        file.writelines(weather_list_text)


weather = get_weather(city_, days_)
weather_list = convert_weather(weather)
write_weather_to_file(weather_list, city_, days_)
