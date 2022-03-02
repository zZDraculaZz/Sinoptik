from aiogram import types, Dispatcher
from aiogram.types import KeyboardButton

from keyboards import agree_or_not, choose_time, menu, buttons_day, greeting_or_cancel, male_or_female, \
    buttons_settings_menu, buttons_with_language, remove
from states import user_state
from texts import CHOOSE_TIME, COMMON_TEXT, R_MENU, REGISTRATION, LANGUAGES, A_SETTINGS, R_SETTINGS, A_MENU
from functions import save_location, check_requested_date, weather_advice, set_language, set_gender, check_gender, \
    take_language
from create_bot import bot


# Хендлер для установления языка пользователя
async def reaction_on_choice_language(message: types.Message):
    text = message.text
    chat_id = str(message.chat.id)
    language = take_language(chat_id)

    if text in LANGUAGES:
        set_language(chat_id=chat_id, language=text)
        language = take_language(chat_id)

        await user_state.registration.accept_registration.set()
        await bot.send_message(message.from_user.id, text=REGISTRATION["language_set"][language],
                               reply_markup=greeting_or_cancel(language))

    else:
        await bot.send_message(message.from_user.id, text=REGISTRATION["language_not_found"][language])


# Хендлер отмены действий
async def reaction_on_cancel(message: types.Message):
    chat_id = str(message.chat.id)
    language = take_language(chat_id)
    await bot.send_message(message.from_user.id, text=REGISTRATION["pained"][language], reply_markup=remove)


# Хендлер принятия пользователем регистрации
async def agree_registration(message: types.Message):
    chat_id = str(message.chat.id)
    language = take_language(chat_id)

    await user_state.registration.gender_choice.set()
    await bot.send_message(message.from_user.id, text=REGISTRATION["gender_selection"][language],
                           reply_markup=male_or_female(language))


# Хендлер установки пола пользователя
async def reaction_on_choice_gender(message: types.Message):
    chat_id = str(message.chat.id)
    language = take_language(chat_id)
    text = message.text
    if text in REGISTRATION["male"] or text in REGISTRATION["female"]:
        set_gender(chat_id=chat_id, gender=text)

        await user_state.registration.loc_request.set()
        await bot.send_message(message.from_user.id, text=REGISTRATION["location_request"][language],
                               reply_markup=agree_or_not(language))

    else:
        await bot.send_message(message.from_user.id, text=REGISTRATION["gender_not_found"][language].format(text))


# Ловим сообщение с локацией от пользователя
async def reaction_on_location(message: types.Message):
    chat_id = str(message.chat.id)
    language = take_language(chat_id)
    lat = str(message.location.latitude)
    lon = str(message.location.longitude)

    save_location(chat_id=chat_id, lat=lat, lon=lon)
    await user_state.registered.main_menu.set()
    await bot.send_message(message.from_user.id, text=REGISTRATION["location_confirm"][language],
                           reply_markup=menu(language))


# # # Хендлеры главного меню (Ловим сообщения с менюшки)
async def reaction_on_prediction(message: types.Message):
    chat_id = str(message.chat.id)
    language = take_language(chat_id)

    await user_state.registered.choice_day.set()
    await bot.send_message(message.from_user.id, text=A_MENU["prediction"][language],
                           reply_markup=buttons_day(chat_id, language))


async def in_settings_menu(message: types.Message):
    chat_id = str(message.chat.id)
    language = take_language(chat_id)
    await user_state.registered.settings_menu.set()
    await bot.send_message(message.from_user.id, text=A_MENU["in_settings"][language],
                           reply_markup=buttons_settings_menu(language))


async def list_of_commands(message: types.Message):
    chat_id = str(message.chat.id)
    language = take_language(chat_id)
    await bot.send_message(message.from_user.id, text=A_MENU["list_of_commands"][language])


# # # Хендлеры меню настроек
async def reaction_on_change_location(message: types.Message):
    chat_id = str(message.chat.id)
    language = take_language(chat_id)
    lat = str(message.location.latitude)
    lon = str(message.location.longitude)

    save_location(chat_id=chat_id, lat=lat, lon=lon)
    await bot.send_message(message.from_user.id, text=A_SETTINGS["location_changed"][language])


async def reaction_on_change_gender(message: types.Message):
    chat_id = str(message.chat.id)
    language = take_language(chat_id)
    gender = check_gender(chat_id)
    if gender == REGISTRATION["male"][language]:
        set_gender(chat_id, gender=REGISTRATION["female"][language])
        await bot.send_message(message.from_user.id,
                               text=A_SETTINGS["gender_changed"][language].format(gender,
                                                                                  REGISTRATION["female"][language]))
    else:
        set_gender(chat_id, gender=REGISTRATION["male"][language])
        await bot.send_message(message.from_user.id,
                               text=A_SETTINGS["gender_changed"][language].format(gender,
                                                                                  REGISTRATION["male"][language]))


async def reaction_on_change_language(message: types.Message):
    chat_id = str(message.chat.id)
    language = take_language(chat_id)
    await user_state.registered.change_language.set()
    await bot.send_message(message.from_user.id, text=A_SETTINGS["choose_language"][language],
                           reply_markup=buttons_with_language()
                           .row(KeyboardButton(R_SETTINGS["return_in_settings"][language])))


# Смена языка
async def language_changed(message: types.Message):
    text = message.text
    chat_id = str(message.chat.id)
    language = take_language(chat_id)

    if text in LANGUAGES:
        set_language(chat_id=chat_id, language=text)
        language = take_language(chat_id)
        await bot.send_message(message.from_user.id, text=A_SETTINGS["language_changed"][language],
                               reply_markup=buttons_with_language()
                               .row(KeyboardButton(R_SETTINGS["return_in_settings"][language])))

    elif text in R_SETTINGS["return_in_settings"]:
        await user_state.registered.settings_menu.set()
        await bot.send_message(message.from_user.id, text=COMMON_TEXT["return"][language],
                               reply_markup=buttons_settings_menu(language))

    else:
        await bot.send_message(message.from_user.id, text=A_SETTINGS["language_not_found"][language])


# Реакция на возвращение в главное меню
async def return_in_menu(message: types.Message):
    chat_id = str(message.chat.id)
    language = take_language(chat_id)
    await user_state.registered.main_menu.set()
    await bot.send_message(message.from_user.id, text=COMMON_TEXT["return"][language], reply_markup=menu(language))


# Реакция на выбранный день
async def reaction_on_choose_day(message: types.Message):
    text = message.text[4:14]
    chat_id = str(message.chat.id)
    language = take_language(chat_id)
    date_available, precipitation, humidity, wind_speed = check_requested_date(text, chat_id, language)

    if date_available:
        await user_state.registered.choice_time.set()
        await bot.send_message(message.from_user.id, text=COMMON_TEXT["day_selected"][language]
                               .format(text, precipitation, humidity, wind_speed), reply_markup=choose_time(language))
    else:
        await bot.send_message(message.from_user.id, text=COMMON_TEXT["error_date"][language].format(message.text))


# # # # # Ловим ключевые слова с временем суток и возвращением в меню выбора дня
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
    language = take_language(chat_id)
    await user_state.registered.choice_day.set()
    await bot.send_message(message.from_user.id, text=COMMON_TEXT["return"][language],
                           reply_markup=buttons_day(chat_id, language))


# регистрируем все хендлеры
def register_handlers_user(dp: Dispatcher):

    # Регистрация
    dp.register_message_handler(reaction_on_choice_language, state=user_state.registration.start)
    dp.register_message_handler(reaction_on_cancel, lambda message: message.text in REGISTRATION["cancel"],
                                state=user_state.registration)
    dp.register_message_handler(agree_registration, lambda message: message.text in REGISTRATION["greeting"],
                                state=user_state.registration.accept_registration)
    dp.register_message_handler(reaction_on_choice_gender, state=user_state.registration.gender_choice)
    dp.register_message_handler(reaction_on_location, content_types=['location'],
                                state=user_state.registration.loc_request)

    # Меню
    dp.register_message_handler(reaction_on_prediction, lambda message: message.text in R_MENU["prediction"],
                                state=user_state.registered.main_menu)
    dp.register_message_handler(in_settings_menu, lambda message: message.text in R_MENU["settings"],
                                state=user_state.registered.main_menu)
    dp.register_message_handler(list_of_commands, lambda message: message.text in R_MENU["list_of_commands"],
                                state=user_state.registered.main_menu)

    # Настройки
    dp.register_message_handler(reaction_on_change_location, content_types=['location'],
                                state=user_state.registered.settings_menu)
    dp.register_message_handler(reaction_on_change_gender, lambda message: message.text in R_SETTINGS["change_gender"],
                                state=user_state.registered.settings_menu)
    dp.register_message_handler(reaction_on_change_language,
                                lambda message: message.text in R_SETTINGS["change_language"],
                                state=user_state.registered.settings_menu)
    dp.register_message_handler(language_changed, state=user_state.registered.change_language)

    # Возврат в главное меню
    dp.register_message_handler(return_in_menu, lambda message: message.text in COMMON_TEXT["backspace_in_menu"],
                                state=user_state.registered)

    # Выбор дня
    dp.register_message_handler(reaction_on_choose_day, lambda message: 9 < len(message.text) < 30,
                                state=user_state.registered.choice_day)
    # Выбор времени суток или возврат к выбору дня
    dp.register_message_handler(reaction_night, lambda message: message.text in CHOOSE_TIME["night"],
                                state=user_state.registered.choice_time)
    dp.register_message_handler(reaction_morning, lambda message: message.text in CHOOSE_TIME["morning"],
                                state=user_state.registered.choice_time)
    dp.register_message_handler(reaction_midday, lambda message: message.text in CHOOSE_TIME["midday"],
                                state=user_state.registered.choice_time)
    dp.register_message_handler(reaction_evening, lambda message: message.text in CHOOSE_TIME["evening"],
                                state=user_state.registered.choice_time)
    dp.register_message_handler(return_in_choice_day, lambda message:
                                message.text in COMMON_TEXT["backspace_in_choice"],
                                state=user_state.registered.choice_time)