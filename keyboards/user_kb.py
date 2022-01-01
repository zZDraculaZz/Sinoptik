# Вот тут то и начинается кузня кнопочек!! БУ-ГА-ГА!!
from aiogram import types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from texts import TIME_TO_CHOICE, COMMON_TEXT

# Создаем кнопочки
button_greeting = KeyboardButton(COMMON_TEXT["greeting"])
button_cancel = KeyboardButton(COMMON_TEXT["cancel"])

button_ok = KeyboardButton(COMMON_TEXT["agree"], request_location=True)

button_morning = KeyboardButton(TIME_TO_CHOICE["morning"])
button_midday = KeyboardButton(TIME_TO_CHOICE["midday"])
button_evening = KeyboardButton(TIME_TO_CHOICE["evening"])

# удалить кнопки с экрана
remove_buttons = types.ReplyKeyboardRemove()

# Объеденяем кнопочки
greeting_or_cancel = ReplyKeyboardMarkup(resize_keyboard=True).row(button_greeting).row(button_cancel)


agree_or_not = ReplyKeyboardMarkup(resize_keyboard=True).row(button_ok).row(button_cancel)


time_to_choice = ReplyKeyboardMarkup(resize_keyboard=True).row(button_morning).row(button_midday).row(button_evening)


