from aiogram.dispatcher.filters.state import StatesGroup, State


class user_state(StatesGroup):
    class registration(StatesGroup):
        start = State()
        accept_registration = State()
        gender_choice = State()
        loc_request = State()

    class registered(StatesGroup):
        main_menu = State()
        choice_day = State()
        choice_time = State()
        settings_menu = State()
        change_language = State()