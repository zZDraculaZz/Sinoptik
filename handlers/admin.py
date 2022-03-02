from aiogram import Dispatcher, types

from create_bot import bot
from functions import take_language, amount_users, amount_registered_users
from states import admin_state
from texts.admin_texts import R_ADMIN, A_ADMIN


async def count_users(message: types.Message):
    chat_id = str(message.chat.id)
    language = take_language(chat_id)
    await bot.send_message(message.from_user.id, text=A_ADMIN["all_users"][language].format(amount_users()))


async def count_registered_users(message: types.Message):
    chat_id = str(message.chat.id)
    language = take_language(chat_id)
    await bot.send_message(message.from_user.id, text=A_ADMIN["number_of_registered"][language]
                           .format(amount_registered_users()))


def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(count_users, lambda message: message.text in R_ADMIN["all_users"],
                                state=admin_state.admin_menu)
    dp.register_message_handler(count_registered_users, lambda message: message.text in R_ADMIN["number_of_registered"],
                                state=admin_state.admin_menu)