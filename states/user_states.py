from aiogram.dispatcher.filters.state import StatesGroup, State


class user_state(StatesGroup):
    start = State()
    loc_request = State()
    menu = State()
    choice_day = State()
    choice_time = State()