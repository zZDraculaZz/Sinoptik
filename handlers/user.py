from aiogram import types, Dispatcher

from keyboards import remove_buttons, agree_or_not, time_to_choice
from texts import TIME_TO_CHOICE, COMMON_TEXT
from functions import morning, midday, evening, save_location
from create_bot import bot


# # Далее хендлеры для отлова ключевых слов
# @dp.message_handler(lambda message: message.text == COMMON_TEXT["cancel"])
async def reaction_on_cancel(message: types.Message):
    await bot.send_message(message.from_user.id, text=COMMON_TEXT["pained"], reply_markup=remove_buttons)


# @dp.message_handler(lambda message: message.text == COMMON_TEXT["greeting"])
async def reaction_on_hello(message: types.Message):
    await message.reply(COMMON_TEXT["location_request"], reply_markup=agree_or_not)


# Ловим сообщение с локацией от пользователя
# @dp.message_handler(content_types=['location'])
async def reaction_on_location(message: types.Message):

    chat_id = message.chat.id
    lat = message.location.latitude
    lon = message.location.longitude

    save_location(chat_id=chat_id, lat=lat, lon=lon)

    await message.reply(COMMON_TEXT["location_confirm"], reply_markup=time_to_choice)


# # # Ловим ключевые слова с временем суток
# @dp.message_handler(lambda message: message.text == TIME_TO_CHOICE["morning"])
async def reaction_morning(message: types.Message):

    text_answer = morning(chat_id=message.chat.id)

    await bot.send_message(message.from_user.id, text=text_answer, reply_markup=remove_buttons)


# @dp.message_handler(lambda message: message.text == TIME_TO_CHOICE["midday"])
async def reaction_midday(message: types.Message):

    text_answer = midday(chat_id=message.chat.id)

    await bot.send_message(message.from_user.id, text=text_answer, reply_markup=remove_buttons)


# @dp.message_handler(lambda message: message.text == TIME_TO_CHOICE["evening"])
async def reaction_evening(message: types.Message):

    text_answer = evening(chat_id=message.chat.id)

    await bot.send_message(message.from_user.id, text=text_answer, reply_markup=remove_buttons)


# регистрируем все хендлеры
def register_handlers_user(dp: Dispatcher):
    dp.register_message_handler(reaction_on_cancel, lambda message: message.text == COMMON_TEXT["cancel"])
    dp.register_message_handler(reaction_on_hello, lambda message: message.text == COMMON_TEXT["greeting"])
    dp.register_message_handler(reaction_on_location, content_types=['location'])
    dp.register_message_handler(reaction_morning, lambda message: message.text == TIME_TO_CHOICE["morning"])
    dp.register_message_handler(reaction_midday, lambda message: message.text == TIME_TO_CHOICE["midday"])
    dp.register_message_handler(reaction_evening, lambda message: message.text == TIME_TO_CHOICE["evening"])