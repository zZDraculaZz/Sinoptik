from aiogram import types, Dispatcher
from create_bot import bot
from texts import COMMON_TEXT


# @dp.message_handler()
async def reaction_on_unknown_command(message: types.Message):
    chat_id = message.chat.id
    text = message.text
    await bot.send_message(chat_id=chat_id, text=COMMON_TEXT["command_not_found"].format(text))


def register_handlers_echo(dp: Dispatcher):
    dp.register_message_handler(reaction_on_unknown_command)