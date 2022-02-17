# Вот тут то и начинается кузня кнопочек!! БУ-ГА-ГА!!
from aiogram import types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from functions import get_dates
from texts import CHOOSE_TIME, COMMON_TEXT, MENU


# Создаем кнопочки
class buttons:
    greeting = KeyboardButton(COMMON_TEXT["greeting"])
    cancel = KeyboardButton(COMMON_TEXT["cancel"])
    backspace_choice = KeyboardButton(COMMON_TEXT["backspace_in_choice"])
    backspace_menu = KeyboardButton(COMMON_TEXT["backspace_in_menu"])

    ok = KeyboardButton(COMMON_TEXT["agree"], request_location=True)

    prediction = KeyboardButton(MENU["prediction"])
    change_coordinates = KeyboardButton(MENU["change_coordinates"], request_location=True)
    list_of_commands = KeyboardButton(MENU["list_of_commands"])

    night = KeyboardButton(CHOOSE_TIME["night"])
    morning = KeyboardButton(CHOOSE_TIME["morning"])
    midday = KeyboardButton(CHOOSE_TIME["midday"])
    evening = KeyboardButton(CHOOSE_TIME["evening"])

    # удалить кнопки с экрана
    remove = types.ReplyKeyboardRemove()


# Объеденяем кнопочки
greeting_or_cancel = ReplyKeyboardMarkup(resize_keyboard=True).row(buttons.greeting).row(buttons.cancel)

agree_or_not = ReplyKeyboardMarkup(resize_keyboard=True).row(buttons.ok).row(buttons.cancel)

menu = ReplyKeyboardMarkup(resize_keyboard=True).row(buttons.prediction).row(buttons.change_coordinates)\
                                                       .row(buttons.list_of_commands)


def buttons_day(chat_id):
    days = get_dates(chat_id)
    choose_day = ReplyKeyboardMarkup(resize_keyboard=True).row(KeyboardButton(days[0]), KeyboardButton(days[4]))\
                                                          .row(KeyboardButton(days[1]), KeyboardButton(days[5]))\
                                                          .row(KeyboardButton(days[2]), KeyboardButton(days[6]))\
                                                          .row(KeyboardButton(days[3]), buttons.backspace_menu)
    return choose_day


choose_time = ReplyKeyboardMarkup(resize_keyboard=True).row(buttons.night).row(buttons.morning)\
                                                       .row(buttons.midday).row(buttons.evening)\
                                                       .row(buttons.backspace_choice)