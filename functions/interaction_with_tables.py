import datetime
import time

import requests

from config import server_timezone, WEATHER_TOKEN
from db_connection import cursor_on, cursor_off
from texts import CHOOSE_DAY, FUNCTION_TEXT


# (Реакция на \start)Проверка существования пользователя в базе данных
def search_user(chat_id, username):
    cursor = cursor_on()
    # Создаём переменную для указания существования пользователя
    user_detected = False

    cursor.execute("select chat_id from bot_users where chat_id = %s", (chat_id,))
    table = cursor.fetchall()
    # Если есть хоть 1 такой пользователь, меняем переменную на True
    if len(table) > 0:
        user_detected = True

    # Сохранение пользователя в базе данных, если его там нет.
    if not user_detected:
        cursor.execute("INSERT INTO bot_users (chat_id, user_name) "
                       "VALUES (%s, %s);",
                       (chat_id, username))

    cursor_off(cursor=cursor)


# Запрос к API oneweathermap.org
def url_request(lat, lon):
    precipitation = ""
    temperatures = ""
    humidity = ""
    wind_speed = ""
    times_of_day = ["morn", "day", "eve", "night"]
    updates = requests.get(FUNCTION_TEXT["url_for_request"].format(lat, lon, WEATHER_TOKEN)).json()
    timezone = int(updates["timezone_offset"])
    request_day = str(int(updates["daily"][0]["dt"]) + timezone)

    for day in range(8):
        precipitation += (updates["daily"][day]["weather"][0]["description"]) + ", "
        humidity += str((updates["daily"][day]["humidity"])) + ", "
        wind_speed += str((updates["daily"][day]["wind_speed"])) + ", "

        for day_time in times_of_day:
            temperatures += (str(updates["daily"][day]["temp"][day_time])) + " "

    return request_day, temperatures, precipitation, timezone, humidity, wind_speed


# Сохранение локации, когда пользователь предоставляеет её нам.
def save_location(chat_id, lat, lon):
    cursor = cursor_on()
    cursor.execute("select chat_id from coordinates where chat_id = %s", (chat_id,))
    table = cursor.fetchall()
    # Создаём переменную для указания существования координат в базе данных
    loc_detected = False
    # Если есть такой пользователь, меняем переменную на True
    if len(table) > 0:
        loc_detected = True

    # Если не найден, то сохраняем локацию
    if not loc_detected:
        cursor.execute("INSERT INTO coordinates (chat_id, lat, lon) "
                       "VALUES (%s, %s, %s);",
                       (chat_id, lat, lon))

    # Если  найден, то обновляем данные о локации пользователя
    if loc_detected:
        cursor.execute("UPDATE coordinates SET lat=%s, lon=%s WHERE chat_id=%s", (lat, lon, chat_id))

        request_day, temperatures, precipitation, timezone, humidity, wind_speed = url_request(lat=lat, lon=lon)

        cursor.execute("UPDATE weathers SET request_day=%s, temperatures=%s, precipitation=%s, timezone=%s,"
                       "humidity=%s, wind_speed=%s"
                       "WHERE chat_id=%s",
                       (request_day, temperatures, precipitation, timezone, humidity, wind_speed, chat_id))
    cursor_off(cursor=cursor)


# Проверка регистрации пользователя
def user_registration_check(chat_id):
    cursor = cursor_on()
    cursor.execute("select chat_id from coordinates where chat_id = %s", (chat_id,))
    table = cursor.fetchall()
    cursor_off(cursor)
    # Создаём переменную для указания существования регистрации пользователя
    user_registered = False
    # Если есть такой пользователь, меняем переменную на True
    if len(table) > 0:
        user_registered = True
    return user_registered


# Проверка таймзоны пользователя
def timezone_check(chat_id):
    cursor = cursor_on()
    cursor.execute("select timezone from weathers where chat_id = %s", (chat_id,))
    timezone = cursor.fetchall()

    # Проверка установлена ли таймзона у пользователя по его координатам и если нет, то делаем запрос на погоду
    if len(timezone) == 0:
        cursor.execute("select lat, lon from coordinates where chat_id = %s", (chat_id,))
        lat, lon = cursor.fetchall()[0]

        request_day, temperatures, precipitation, timezone, humidity, wind_speed = url_request(lat=lat, lon=lon)

        cursor.execute("INSERT INTO weathers(chat_id, request_day, temperatures, precipitation, timezone, selected_day,"
                       "humidity, wind_speed)"
                       "VALUES (%s, %s, %s, %s, %s, %s, %s, %s);",
                       (chat_id, request_day, temperatures, precipitation, timezone, -1, humidity, wind_speed))

    # Если установлена, то просто запоминаем
    else:
        timezone = timezone[0][0]

    cursor_off(cursor=cursor)
    return timezone


# Выдать дату смотря на таймзону пользователя
def get_dates(chat_id):
    timezone = timezone_check(chat_id)
    time_now = (int(time.time()) - server_timezone) + timezone
    one_day = 86400
    value = []
    for day in CHOOSE_DAY:
        value.append(CHOOSE_DAY[day].format(datetime.datetime.fromtimestamp(time_now).strftime('%d-%m-%Y')))
        time_now += one_day
    return value


# Запрос на погоду для пользователя, если данные устарели
def weather_request(chat_id):
    cursor = cursor_on()
    cursor.execute("select lat, lon from coordinates where chat_id = %s", (chat_id,))
    lat, lon = cursor.fetchall()[0]

    request_day, temperatures, precipitation, timezone, humidity, wind_speed = url_request(lat=lat, lon=lon)

    cursor.execute("UPDATE weathers SET request_day=%s, temperatures=%s, precipitation=%s, timezone=%s"
                   "humidity=%s, wind_speed=%s "
                   "WHERE chat_id=%s",
                   (request_day, temperatures, precipitation, timezone, humidity, wind_speed, chat_id))

    cursor_off(cursor)


# Функция для для взятия погодных условий из базы для пользователя, а так же запомнить положение в списке,выбранного дня
def take_predict_on_day(chat_id, selected_day):
    cursor = cursor_on()
    cursor.execute("select precipitation from weathers where chat_id = %s", (chat_id,))
    precipitation = cursor.fetchall()[0][0].split(", ")[selected_day]
    cursor.execute("select humidity from weathers where chat_id = %s", (chat_id,))
    humidity = cursor.fetchall()[0][0].split(", ")[selected_day]
    cursor.execute("select wind_speed from weathers where chat_id = %s", (chat_id,))
    wind_speed = cursor.fetchall()[0][0].split(", ")[selected_day]
    cursor.execute("UPDATE weathers SET selected_day=%s WHERE chat_id=%s", (selected_day, chat_id))
    cursor_off(cursor)
    return precipitation, humidity, wind_speed


# Проверить на наличие запрашиваемую пользователем дату
def check_requested_date(text, chat_id):
    cursor = cursor_on()
    cursor.execute("select request_day from weathers where chat_id = %s", (chat_id,))
    request_day = int(cursor.fetchall()[0][0])
    cursor_off(cursor)

    precipitation = ""
    humidity = ""
    wind_speed = ""
    selected_day = 0
    one_day = 86400
    date_available = False

    for day in range(8):
        if text == (datetime.datetime.fromtimestamp(request_day).strftime('%d-%m-%Y')):
            date_available = True
            precipitation, humidity, wind_speed = take_predict_on_day(chat_id, selected_day)
            break
        selected_day += 1
        request_day += one_day

    if not date_available:
        selected_day = 0
        dates = get_dates(chat_id)
        for day in dates:
            if day == text:
                date_available = True
                weather_request(chat_id)
                precipitation, humidity, wind_speed = take_predict_on_day(chat_id, selected_day)
                break
            selected_day += 1

    return date_available, precipitation, humidity, wind_speed