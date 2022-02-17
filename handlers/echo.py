from aiogram import types, Dispatcher

from create_bot import bot
from states import user_state

from texts import COMMON_TEXT


async def reaction_on_error_time(message: types.Message):
    chat_id = message.chat.id
    text = message.text
    await bot.send_message(chat_id=chat_id, text=COMMON_TEXT["error_time"].format(text))


async def reaction_on_error_dates(message: types.Message):
    chat_id = message.chat.id
    text = message.text
    await bot.send_message(chat_id=chat_id, text=COMMON_TEXT["error_date"].format(text))


async def reaction_on_unknown_command(message: types.Message):
    chat_id = message.chat.id
    text = message.text
    await bot.send_message(chat_id=chat_id, text=COMMON_TEXT["command_not_found"].format(text))


def register_handlers_echo(dp: Dispatcher):
    dp.register_message_handler(reaction_on_error_time, state=user_state.choice_time)
    dp.register_message_handler(reaction_on_error_dates, state=user_state.choice_day)
    dp.register_message_handler(reaction_on_unknown_command, state="*")