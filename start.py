from aiogram.utils import executor

from create_bot import dp, bot
from middlewares import throttling
from handlers import commands, user, echo, admin
from config import ADMINS_ID
from texts import FOR_ADMINS


async def on_startup(_):
    for admin_id in ADMINS_ID:
        await bot.send_message(chat_id=admin_id, text=FOR_ADMINS["bot_activated"])


throttling.register_throttling(dp)
commands.register_handlers_commands(dp)
admin.register_handlers_admin(dp)
user.register_handlers_user(dp)
echo.register_handlers_echo(dp)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)