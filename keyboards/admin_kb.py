from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

from texts.admin_texts import R_ADMIN


def all_users(language):
    button = KeyboardButton(R_ADMIN["all_users"][language])
    return button


def number_of_registered(language):
    button = KeyboardButton(R_ADMIN["number_of_registered"][language])
    return button


def admin_panel(language):
    buttons = ReplyKeyboardMarkup(resize_keyboard=True).row(all_users(language)).row(number_of_registered(language))
    return buttons