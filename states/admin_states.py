from aiogram.dispatcher.filters.state import StatesGroup, State


class admin_state(StatesGroup):
    admin_menu = State()