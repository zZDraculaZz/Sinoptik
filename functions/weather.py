# здесь лежат все функции
import requests
import xlrd3
import pandas as pd

from config import WEATHER_TOKEN, base_location
from texts import EXPERIENCE, COMMON_TEXT, FUNCTION_TEXT

# функция поиска айдишника пользователя в базе данных
def search_id(chat_id):

    lat = ''
    lon = ''
    id_present = False

    wb = xlrd3.open_workbook(base_location)
    sheet = wb.sheet_by_index(0)  # выбор листа
    vals = [sheet.row_values(rownum) for rownum in range(sheet.nrows)]  # получаем список из всех записей

    for i in vals[1:]:
        if int(chat_id) == int(i[0]):
            lat = str(i[1])
            lon = str(i[2])
            id_present = True
            break
    return lat, lon, id_present


# функция реакции на температуру
def temperature_reaction(temperature, weather):

    if temperature > 23:
        my_experience = EXPERIENCE["23+"]

    elif 17 < temperature < 23:
        my_experience = EXPERIENCE["23"]

    elif 10 < temperature < 17:
        my_experience = EXPERIENCE["17"]

    elif 0 < temperature < 10:
        my_experience = EXPERIENCE["10"]

    elif -15 < temperature < 0:
        my_experience = EXPERIENCE["0"]

    else:
        my_experience = EXPERIENCE["-15"]

    text_answer = FUNCTION_TEXT["weather_answer"].format(my_experience, temperature, weather)

    return text_answer


# функция(ответ) на нажатие кнопки "Утром! 06:00-12:00"
def morning(chat_id):
    lat, lon, id_present = search_id(chat_id)
    text_answer = COMMON_TEXT["location_not_found"]

    if id_present == False:
        return text_answer

    else:

        updates = requests.get(FUNCTION_TEXT["url_for_request"].format(lat, lon, WEATHER_TOKEN)).json()
        update_time = int(updates["list"][0]['dt_txt'][11:13])
        number = 2
        repeat_number = True

        for i in range(0, 22, 3):
            if update_time == i:
                temperature = float(updates['list'][number]['main']['temp_min'])
                weather = str(updates['list'][number]['weather'][0]['description'])
                text_answer = temperature_reaction(temperature=temperature, weather=weather)
                break

            elif number == 1 and repeat_number == True:
                repeat_number = False
                continue

            elif number == 0:
                number = 6
                continue

            elif number != 0:
                number -= 1

        return text_answer


# функция(ответ) на нажатие кнопки "Днём! 12:00-18:00"
def midday(chat_id):
    lat, lon, id_present = search_id(chat_id)
    text_answer = COMMON_TEXT["location_not_found"]

    if id_present == False:
        return text_answer

    else:

        updates = requests.get(FUNCTION_TEXT["url_for_request"].format(lat, lon, WEATHER_TOKEN)).json()
        update_time = int(updates["list"][0]['dt_txt'][11:13])
        number = 4
        repeat_number = True

        for i in range(0, 22, 3):
            if update_time == i:
                temperature = float(updates['list'][number]['main']['temp_min'])
                weather = str(updates['list'][number]['weather'][0]['description'])
                text_answer = temperature_reaction(temperature=temperature, weather=weather)
                break

            elif number == 1 and repeat_number == True:
                repeat_number = False
                continue

            elif number == 0:
                number = 6
                continue

            elif number != 0:
                number -= 1

        return text_answer


# функция(ответ) на нажатие кнопки "Вечером! 18:00-24:00"
def evening(chat_id):
    lat, lon, id_present = search_id(chat_id)
    text_answer = COMMON_TEXT["location_not_found"]

    if id_present == False:
        return text_answer

    else:

        updates = requests.get(FUNCTION_TEXT["url_for_request"].format(lat, lon, WEATHER_TOKEN)).json()
        update_1_hours = int(updates["list"][0]['dt_txt'][11:13])
        number = 6

        for i in range(0, 22, 3):
            if update_1_hours == i:
                temperature = float(updates['list'][number]['main']['temp_min'])
                weather = str(updates['list'][number]['weather'][0]['description'])
                text_answer = temperature_reaction(temperature=temperature, weather=weather)
                break

            elif number != 0:
                number -= 1

        return text_answer


# функция запоминания локации
def save_location(chat_id, lat, lon):

    wb = xlrd3.open_workbook(base_location)
    sheet = wb.sheet_by_index(0)  # выбор листа
    vals = [sheet.row_values(rownum) for rownum in range(sheet.nrows)]  # получаем список из всех записей

    amount = 0
    chat_ids = []  # создаем списки,что бы потом в них запоминать уже имеющиеся данные
    lats = []
    lons = []

    # читаем имеющиеся айдишники с локациями и запоминаем их
    for i in vals[1:]:
        chat_ids.append(i[0])
        lats.append(i[1])
        lons.append(i[2])

        # если находим совпадение,то удаляем его из имеющихся данных,что бы потом добавить в конец списка
        if i[0] == chat_id:
            del chat_ids[amount]
            del lats[amount]
            del lons[amount]

        amount += 1

    chat_ids.append(chat_id)  # добавляем новые данные к нашим спискам
    lats.append(lat)
    lons.append(lon)

    # а вот и "замечательная" вещь которая стала женой моему мозгу (сохраняем айдишники с локациями)
    save_location = pd.DataFrame({'chat_id': chat_ids, 'lat': lats, 'lon': lons})
    save_location.to_excel(base_location, index=False)
    pass