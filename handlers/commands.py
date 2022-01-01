from aiogram import types, Dispatcher

from keyboards import greeting_or_cancel, time_to_choice
from texts import COMMAND_TEXT


# команды для бота
# @dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply(COMMAND_TEXT["start"], reply_markup=greeting_or_cancel)  #выдаем пользователю кнопочки с ответами

# @dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply(COMMAND_TEXT["help"])

# @dp.message_handler(commands=['advice'])
async def process_advice_command(message: types.Message):
    await message.reply(COMMAND_TEXT["advice"], reply_markup=time_to_choice)


def register_handlers_commands(dp: Dispatcher):
    dp.register_message_handler(process_start_command, commands=["start"])
    dp.register_message_handler(process_help_command, commands=["help"])
    dp.register_message_handler(process_advice_command, commands=["advice"])