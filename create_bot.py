from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.redis import RedisStorage2

from config import BOT_TOKEN


bot = Bot(token=BOT_TOKEN)
storage = RedisStorage2()

dp = Dispatcher(bot, storage=storage)