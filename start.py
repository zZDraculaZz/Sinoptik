from aiogram.utils import executor

from create_bot import dp, bot
from handlers import commands, user, echo
from config import ADMINS_ID


async def on_startup(_):
    for admin_id in ADMINS_ID:
        await bot.send_message(chat_id=admin_id, text="Я снова ожил! Вот блин, сколько же дел невыполненных...")


commands.register_handlers_commands(dp)
user.register_handlers_user(dp)
echo.register_handlers_echo(dp)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
