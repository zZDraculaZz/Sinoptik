from aiogram import types, Dispatcher

from create_bot import bot
from functions import take_language
from states import user_state

from texts import COMMON_TEXT


async def reaction_on_error_time(message: types.Message):
    chat_id = message.chat.id
    language = take_language(str(chat_id))
    text = message.text
    await bot.send_message(chat_id=chat_id, text=COMMON_TEXT["error_time"][language].format(text))


async def reaction_on_error_dates(message: types.Message):
    chat_id = message.chat.id
    language = take_language(str(chat_id))
    text = message.text
    await bot.send_message(chat_id=chat_id, text=COMMON_TEXT["error_date"][language].format(text))


async def reaction_on_unknown_command(message: types.Message):
    chat_id = message.chat.id
    language = take_language(str(chat_id))
    text = message.text
    await bot.send_message(chat_id=chat_id, text=COMMON_TEXT["command_not_found"][language].format(text))


def register_handlers_echo(dp: Dispatcher):
    dp.register_message_handler(reaction_on_error_time, state=user_state.registered.choice_time)
    dp.register_message_handler(reaction_on_error_dates, state=user_state.registered.choice_day)
    dp.register_message_handler(reaction_on_unknown_command, state="*")