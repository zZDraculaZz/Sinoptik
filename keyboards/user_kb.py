# Вот тут то и начинается кузня кнопочек!! БУ-ГА-ГА!!
from aiogram import types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from functions import get_dates
from texts import CHOOSE_TIME, COMMON_TEXT, R_MENU, LANGUAGES, REGISTRATION, R_SETTINGS


# Создаем кнопочки
# Регистрация
def greeting(language):
    button = KeyboardButton(REGISTRATION["greeting"][language])
    return button


def cancel(language):
    button = KeyboardButton(REGISTRATION["cancel"][language])
    return button


def ok(language):
    button = KeyboardButton(REGISTRATION["agree"][language], request_location=True)
    return button


def male(language):
    button = KeyboardButton(REGISTRATION["male"][language])
    return button


def female(language):
    button = KeyboardButton(REGISTRATION["female"][language])
    return button


# Главное меню
def prediction(language):
    button = KeyboardButton(R_MENU["prediction"][language])
    return button


def settings_menu(language):
    button = KeyboardButton(R_MENU["settings"][language])
    return button


def list_of_commands(language):
    button = KeyboardButton(R_MENU["list_of_commands"][language])
    return button


# Меню настроек
def change_coordinates(language):
    button = KeyboardButton(R_SETTINGS["change_coordinates"][language], request_location=True)
    return button


def change_gender(language):
    button = KeyboardButton(R_SETTINGS["change_gender"][language])
    return button


def change_language(language):
    button = KeyboardButton(R_SETTINGS["change_language"][language])
    return button


def backspace_menu(language):
    button = KeyboardButton(COMMON_TEXT["backspace_in_menu"][language])
    return button


# Времена суток
def night(language):
    button = KeyboardButton(CHOOSE_TIME["night"][language])
    return button


def morning(language):
    button = KeyboardButton(CHOOSE_TIME["morning"][language])
    return button


def midday(language):
    button = KeyboardButton(CHOOSE_TIME["midday"][language])
    return button


def evening(language):
    button = KeyboardButton(CHOOSE_TIME["evening"][language])
    return button


def backspace_choice(language):
    button = KeyboardButton(COMMON_TEXT["backspace_in_choice"][language])
    return button


# удалить кнопки с экрана
remove = types.ReplyKeyboardRemove()


# Выдать пользователю кнопки с доступными языками.
def buttons_with_language():
    choose_language = ReplyKeyboardMarkup(resize_keyboard=True)
    for language in LANGUAGES:
        choose_language = choose_language.row(KeyboardButton(language))
    return choose_language


# Объеденяем кнопочки
def greeting_or_cancel(language):
    buttons = ReplyKeyboardMarkup(resize_keyboard=True).row(greeting(language)).row(cancel(language))
    return buttons


def agree_or_not(language):
    buttons = ReplyKeyboardMarkup(resize_keyboard=True).row(ok(language)).row(cancel(language))
    return buttons


def male_or_female(language):
    buttons = ReplyKeyboardMarkup(resize_keyboard=True).row(male(language)).row(female(language))
    return buttons


def menu(language):
    buttons = ReplyKeyboardMarkup(resize_keyboard=True).row(prediction(language)).row(list_of_commands(language))\
                                                       .row(settings_menu(language))
    return buttons


def buttons_settings_menu(language):
    buttons = ReplyKeyboardMarkup(resize_keyboard=True).row(change_coordinates(language)).row(change_gender(language))\
                                                    .row(change_language(language)).row(backspace_menu(language))
    return buttons


# Выдать пользователю кнопочки от его текущей даты.
def buttons_day(chat_id, language):
    days = get_dates(chat_id, language)
    choose_day = ReplyKeyboardMarkup(resize_keyboard=True).row(KeyboardButton(days[0]), KeyboardButton(days[4]))\
                                                          .row(KeyboardButton(days[1]), KeyboardButton(days[5]))\
                                                          .row(KeyboardButton(days[2]), KeyboardButton(days[6]))\
                                                          .row(KeyboardButton(days[3]), backspace_menu(language))
    return choose_day


def choose_time(language):
    buttons = ReplyKeyboardMarkup(resize_keyboard=True).row(morning(language)).row(midday(language))\
                                                       .row(evening(language)).row(night(language))\
                                                       .row(backspace_choice(language))
    return buttons