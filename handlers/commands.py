from aiogram import types, Dispatcher

from config import ADMINS_ID
from functions import search_user, user_registration_check, take_language
from keyboards import menu, buttons_with_language, admin_panel
from states import user_state, admin_state
from texts import COMMAND_TEXT


# команды для бота
async def process_start_command(message: types.Message):
    chat_id = str(message.chat.id)
    search_user(chat_id=chat_id, username=message.chat.username)
    language = take_language(chat_id)

    await user_state.registration.start.set()
    await message.reply(COMMAND_TEXT["start"][language], reply_markup=buttons_with_language())


async def process_help_command(message: types.Message):
    chat_id = str(message.chat.id)
    language = take_language(chat_id)

    await message.reply(COMMAND_TEXT["help"][language])


async def process_advice_command(message: types.Message):
    chat_id = str(message.chat.id)
    user_registered = user_registration_check(chat_id)
    language = take_language(chat_id)

    if user_registered:
        await user_state.registered.main_menu.set()
        await message.reply(COMMAND_TEXT["menu"][language], reply_markup=menu(language))
    else:
        await message.reply(COMMAND_TEXT["user_not_registered"][language])


async def process_info_command(message: types.Message):
    chat_id = str(message.chat.id)
    language = take_language(chat_id)

    await message.reply(COMMAND_TEXT["info"][language])


async def process_admin_command(message: types.Message):
    chat_id = str(message.chat.id)
    language = take_language(chat_id)

    if chat_id in ADMINS_ID:
        await admin_state.admin_menu.set()
        await message.reply(COMMAND_TEXT["admin"][language], reply_markup=admin_panel(language))
    else:
        await message.reply(COMMAND_TEXT["not_admin"], language)


def register_handlers_commands(dp: Dispatcher):
    dp.register_message_handler(process_start_command, commands=["start"],
                                state="*")
    dp.register_message_handler(process_help_command, commands=["help"],
                                state="*")
    dp.register_message_handler(process_advice_command, commands=["menu"],
                                state="*")
    dp.register_message_handler(process_info_command, commands=["info"],
                                state="*")
    dp.register_message_handler(process_admin_command, commands=["admin"],
                                state="*")