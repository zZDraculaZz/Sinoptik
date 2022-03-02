from db_connection import cursor_on, cursor_off
from texts import EXPERIENCE, FUNCTION_TEXT, LANGUAGES


# Функция реакции на температуру
def temperature_reaction(temperature, gender, language):

    if temperature > 23:
        my_experience = EXPERIENCE["23+"][gender][language]

    elif 17 < temperature < 23:
        my_experience = EXPERIENCE["23"][gender][language]

    elif 10 < temperature < 17:
        my_experience = EXPERIENCE["17"][gender][language]

    elif 0 < temperature < 10:
        my_experience = EXPERIENCE["10"][gender][language]

    elif -15 < temperature < 0:
        my_experience = EXPERIENCE["0"][gender][language]

    else:
        my_experience = EXPERIENCE["-15"][gender][language]

    text_answer = FUNCTION_TEXT["weather_answer"][language].format(my_experience, temperature)

    return text_answer


# Функция ответа на выбранное пользователем время
def weather_advice(chat_id, number_time):
    cursor = cursor_on()
    cursor.execute("select selected_day from weathers where chat_id = %s", (chat_id,))
    selected_day = cursor.fetchall()[0][0]
    cursor.execute("select temperatures from weathers where chat_id = %s", (chat_id,))
    value = cursor.fetchall()[0][0].split()
    cursor.execute("select gender from bot_users where chat_id = %s", (chat_id,))
    gender = int(cursor.fetchall()[0][0])
    cursor.execute("select language from bot_users where chat_id = %s", (chat_id,))
    language = LANGUAGES.index(cursor.fetchall()[0][0])
    cursor_off(cursor)

    temperatures = []
    count_temperatures = 0

    for day in range(selected_day+1):
        temperatures.append([])
        for times_of_day in range(4):
            temperatures[day].append(float(value[count_temperatures]))
            count_temperatures += 1

    temperature = temperatures[selected_day][number_time]
    text_answer = temperature_reaction(temperature, gender, language)

    return text_answer
