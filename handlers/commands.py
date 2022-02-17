from aiogram import types, Dispatcher

from functions import search_user, user_registration_check
from keyboards import greeting_or_cancel, menu
from states import user_state
from texts import COMMAND_TEXT


# команды для бота
async def process_start_command(message: types.Message):

    search_user(chat_id=str(message.chat.id), username=message.chat.username)

    await user_state.start.set()
    await message.reply(COMMAND_TEXT["start"], reply_markup=greeting_or_cancel)


async def process_help_command(message: types.Message):
    await message.reply(COMMAND_TEXT["help"])


async def process_advice_command(message: types.Message):
    chat_id = str(message.chat.id)
    user_registered = user_registration_check(chat_id)
    if user_registered:
        await user_state.menu.set()
        await message.reply(COMMAND_TEXT["menu"], reply_markup=menu)
    else:
        await message.reply(COMMAND_TEXT["user_not_registered"])


async def process_info_command(message: types.Message):
    await message.reply(COMMAND_TEXT["info"])


def register_handlers_commands(dp: Dispatcher):
    dp.register_message_handler(process_start_command, commands=["start"],
                                state="*")
    dp.register_message_handler(process_help_command, commands=["help"],
                                state="*")
    dp.register_message_handler(process_advice_command, commands=["menu"],
                                state="*")
    dp.register_message_handler(process_info_command, commands=["info"],
                                state="*")