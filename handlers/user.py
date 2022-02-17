from aiogram import types, Dispatcher

from keyboards import agree_or_not, choose_time, menu, buttons_day, buttons
from states import user_state
from texts import CHOOSE_TIME, COMMON_TEXT, MENU
from functions import save_location, check_requested_date, weather_advice
from create_bot import bot


# # Далее хендлеры для отлова ключевых слов
async def reaction_on_cancel(message: types.Message):
    await bot.send_message(message.from_user.id, text=COMMON_TEXT["pained"], reply_markup=buttons.remove)


async def reaction_on_hello(message: types.Message):
    await user_state.loc_request.set()
    await bot.send_message(message.from_user.id, text=COMMON_TEXT["location_request"], reply_markup=agree_or_not)


# Ловим сообщение с локацией от пользователя
async def reaction_on_location(message: types.Message):
    chat_id = str(message.chat.id)
    lat = str(message.location.latitude)
    lon = str(message.location.longitude)

    save_location(chat_id=chat_id, lat=lat, lon=lon)
    await user_state.menu.set()
    await bot.send_message(message.from_user.id, text=COMMON_TEXT["location_confirm"], reply_markup=menu)


# # # Хендлеры меню (Ловим сообщения с менюшки)
async def reaction_on_prediction(message: types.Message):
    chat_id = str(message.chat.id)

    await user_state.choice_day.set()
    await bot.send_message(message.from_user.id, text=COMMON_TEXT["prediction"], reply_markup=buttons_day(chat_id))


async def reaction_on_change_location(message: types.Message):
    chat_id = str(message.chat.id)
    lat = str(message.location.latitude)
    lon = str(message.location.longitude)

    save_location(chat_id=chat_id, lat=lat, lon=lon)
    await bot.send_message(message.from_user.id, text=COMMON_TEXT["location_changed"])


async def list_of_commands(message: types.Message):
    await bot.send_message(message.from_user.id, text=COMMON_TEXT["list_of_commands"])


async def return_in_menu(message: types.Message):

    await user_state.menu.set()
    await bot.send_message(message.from_user.id, text=COMMON_TEXT["return"], reply_markup=menu)


async def reaction_on_choose_day(message: types.Message):
    if len(message.text) == 14:
        text = message.text[4:]
    else:
        text = message.text

    chat_id = str(message.chat.id)
    date_available, precipitation, humidity, wind_speed = check_requested_date(text, chat_id)

    if date_available:
        await user_state.choice_time.set()
        await bot.send_message(message.from_user.id, text=COMMON_TEXT["day_selected"]
                               .format(text, precipitation, humidity, wind_speed), reply_markup=choose_time)
    else:
        await bot.send_message(message.from_user.id, text=COMMON_TEXT["error_date"].format(message.text))


# # # # Ловим ключевые слова с временем суток
async def reaction_night(message: types.Message):
    chat_id = str(message.chat.id)
    text_answer = weather_advice(chat_id, 3)
    await bot.send_message(message.from_user.id, text=text_answer)


async def reaction_morning(message: types.Message):
    chat_id = str(message.chat.id)
    text_answer = weather_advice(chat_id, 0)
    await bot.send_message(message.from_user.id, text=text_answer)


async def reaction_midday(message: types.Message):
    chat_id = str(message.chat.id)
    text_answer = weather_advice(chat_id, 1)
    await bot.send_message(message.from_user.id, text=text_answer)


async def reaction_evening(message: types.Message):
    chat_id = str(message.chat.id)
    text_answer = weather_advice(chat_id, 2)
    await bot.send_message(message.from_user.id, text=text_answer)


async def return_in_choice_day(message: types.Message):
    chat_id = str(message.chat.id)
    await user_state.choice_day.set()
    await bot.send_message(message.from_user.id, text=COMMON_TEXT["return"], reply_markup=buttons_day(chat_id))


# регистрируем все хендлеры
def register_handlers_user(dp: Dispatcher):
    dp.register_message_handler(reaction_on_cancel, lambda message: message.text == COMMON_TEXT["cancel"],
                                state="*")

    dp.register_message_handler(reaction_on_hello, lambda message: message.text == COMMON_TEXT["greeting"],
                                state=user_state.start)

    dp.register_message_handler(reaction_on_location, content_types=['location'],
                                state=user_state.loc_request)

    dp.register_message_handler(reaction_on_prediction, lambda message: message.text == MENU["prediction"],
                                state=user_state.menu)

    dp.register_message_handler(reaction_on_change_location, content_types=['location'],
                                state=user_state.menu)

    dp.register_message_handler(list_of_commands, lambda message: message.text == MENU["list_of_commands"],
                                state=user_state.menu)

    dp.register_message_handler(return_in_menu, lambda message: message.text == COMMON_TEXT["backspace_in_menu"],
                                state=user_state.choice_day)

    dp.register_message_handler(reaction_on_choose_day, lambda message: len(message.text) == 10
                                or len(message.text) == 14, state=user_state.choice_day)

    dp.register_message_handler(reaction_night, lambda message: message.text == CHOOSE_TIME["night"],
                                state=user_state.choice_time)

    dp.register_message_handler(reaction_morning, lambda message: message.text == CHOOSE_TIME["morning"],
                                state=user_state.choice_time)

    dp.register_message_handler(reaction_midday, lambda message: message.text == CHOOSE_TIME["midday"],
                                state=user_state.choice_time)

    dp.register_message_handler(reaction_evening, lambda message: message.text == CHOOSE_TIME["evening"],
                                state=user_state.choice_time)

    dp.register_message_handler(return_in_choice_day, lambda message:
                                message.text == COMMON_TEXT["backspace_in_choice"], state=user_state.choice_time)