import asyncio

from aiogram import types, Dispatcher
from aiogram.dispatcher.handler import CancelHandler, current_handler
from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram.utils.exceptions import Throttled

from create_bot import bot
from functions import take_language
from texts import MIDDLEWARE_TEXT


class ThrottlingMiddleware(BaseMiddleware):
    """
    Simple middleware
    """

    def __init__(self, limit=0.3, key_prefix='antiflood_'):
        self.rate_limit = limit
        self.prefix = key_prefix
        super(ThrottlingMiddleware, self).__init__()

    # noinspection PyUnusedLocal
    async def on_process_message(self, message: types.Message, data: dict):
        handler = current_handler.get()
        dispatcher = Dispatcher.get_current()
        if handler:
            limit = getattr(handler, 'throttling_rate_limit', self.rate_limit)
            key = getattr(handler, 'throttling_key', f"{self.prefix}_{handler.__name__}")
        else:
            limit = self.rate_limit
            key = f"{self.prefix}_message"
        try:
            await dispatcher.throttle(key, rate=limit)
        except Throttled as t:
            await self.message_throttled(message, t)
            raise CancelHandler()

    async def message_throttled(self, message: types.Message, throttled: Throttled):
        handler = current_handler.get()
        dispatcher = Dispatcher.get_current()
        language = take_language(str(message.chat.id))
        if handler:
            key = getattr(handler, 'throttling_key', f"{self.prefix}_{handler.__name__}")
        else:
            key = f"{self.prefix}_message"
        delta = throttled.rate - throttled.delta
        if throttled.exceeded_count <= 2:
            await bot.send_message(message.from_user.id, MIDDLEWARE_TEXT["block_flood"][language])
        await asyncio.sleep(delta)
        thr = await dispatcher.check_key(key)
        if thr.exceeded_count == throttled.exceeded_count:
            await bot.send_message(message.from_user.id, MIDDLEWARE_TEXT["unblock"][language])


def register_throttling(dp: Dispatcher):
    dp.middleware.setup(ThrottlingMiddleware())