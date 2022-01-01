from aiogram import types, Dispatcher
from create_bot import bot


#@dp.message_handler()
async def reaction_on_unknown_command(message: types.Message):
    chat_id = message.chat.id
    text = message.text
    await bot.send_message(chat_id=chat_id, text=f"Ты уж прости, но я не знаю команду:  \"{text}\"."
                                                 "\nНо не унывай, я всё-таки робот и никогда не брошу человека в беде,"
                                                 " воспользуйся командой /help")


def register_handlers_echo(dp: Dispatcher):
    dp.register_message_handler(reaction_on_unknown_command)