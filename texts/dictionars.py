import emoji

# ответы на температуру, от -15 до бесконечного минуса) и в другом углу ринга от 23 до бесконечного пекла
# Используется в weather.py(functions)
EXPERIENCE = {

    "-15": f"{emoji.emojize(':scroll:')} С таким холодом и водного охлаждения не нужно, надевай на:"
           f"\n\n{emoji.emojize(':crown:')} Голову: шапку-ушанку."
           f"\n{emoji.emojize(':scarf:')} Шею: шарфик (тёплый)."
           f"\n{emoji.emojize(':coat:')} Торс: майку, шерстяной свитер, тёплую дублёнку."
           f"\n{emoji.emojize(':gloves:')} Руки: любые тёплые перчатки."
           f"\n{emoji.emojize(':jeans:')} Талию: подштанники, штаны."
           f"\n{emoji.emojize(':hiking_boot:')} Ноги: шерстяные носки, валенки.",

    "0": f"{emoji.emojize(':scroll:')} Морозная погодка, человек, ты уверен что хочешь гулять? "
         "Хотя кого я спрашиваю..."
         "\nНадевай на: "
         f"\n\n{emoji.emojize(':crown:')} Голову: шапку."
         f"\n{emoji.emojize(':scarf:')} Шею: тёплый шарфик."
         f"\n{emoji.emojize(':coat:')} Торс: майку, шерстяной свитер, стёганную куртку."
         f"\n{emoji.emojize(':gloves:')} Руки: зимние кожаные перчатки."
         f"\n{emoji.emojize(':jeans:')} Талию: подштанники, штаны."
         f"\n{emoji.emojize(':hiking_boot:')} Ноги: тёплые носки, ботинки.",

    "10": f"{emoji.emojize(':scroll:')} Холодновато у вас тут, был бы на твоем месте, то надел на:"
          f"\n\n{emoji.emojize(':crown:')} Голову: шапку."
          f"\n{emoji.emojize(':coat:')} Торс: майку, лёгкий свитер, курточку."
          f"\n{emoji.emojize(':jeans:')} Талию: лёгкие подштанники, штаны."
          f"\n{emoji.emojize(':hiking_boot:')} Ноги: носки, кроссовки.",

    "17": f"{emoji.emojize(':scroll:')} Прохладновато нынче на улице, был бы я твоей робомамой, "
          "то сказал бы надеть на:"
          f"\n\n{emoji.emojize(':coat:')} Торс: футболку, по желанию лёгкий свитер, куртку."
          f"\n{emoji.emojize(':jeans:')} Талию: штаны."
          f"\n{emoji.emojize(':hiking_boot:')} Ноги: носки, кроссовки.",

    "23": f"{emoji.emojize(':scroll:')} Замечательная температура, можно и в робобол сыграть, надевай на:"
          f"\n\n{emoji.emojize(':coat:')} Торс: майку, спортивную курточку."
          f"\n{emoji.emojize(':jeans:')} Талию: джинсы."
          f"\n{emoji.emojize(':hiking_boot:')} Ноги: носки, кеды (любую другую лёгкую обувь).",

    "23+": f"{emoji.emojize(':scroll:')} Слушай такую жару даже мой радиатор не выдерживает, сказал бы идти "
           "в трусах, но где мои робоманеры, надевай на:"
           f"\n\n{emoji.emojize(':crown:')} Голову: модные очки (по желанию)"
           f"\n{emoji.emojize(':coat:')} Торс:майку. "
           f"\n{emoji.emojize(':jeans:')} Талию:шорты (юбку)."
           f"\n{emoji.emojize(':hiking_boot:')} Ноги: любую свободную для ног обувь.",
}

# Используются в commands.py(handlers)
COMMAND_TEXT = {

    "start": f"{emoji.emojize(':robot:')} Привет, человек!"
             f"\n{emoji.emojize(':newspaper:')} Хочешь получить от меня совет по одежде?",

    "help": f"{emoji.emojize(':label:')} Если хочешь получить совет по человеческой одежде и ещё "
            f"не \"зарегистрировался\", то просто нажми {emoji.emojize(':backhand_index_pointing_right:')} /start"
            f"\n\n{emoji.emojize(':label:')} Если не знаешь как передать мне свою геолокацию, "
            f"то просто перейди в настройки своего телефона {emoji.emojize(':mobile_phone_with_arrow:')}, "
            f"где есть кнопка с включением GPS {emoji.emojize(':satellite_antenna:')}, "
            "дальше тебе просто потребуется продолжить общение со мной."
            f"\n\n{emoji.emojize(':circled_M:')} А если ты уже предоставлял свою геолокацию "
            f"нажми {emoji.emojize(':backhand_index_pointing_right:')} /menu",

    "menu": f"{emoji.emojize(':winking_face:')} Как же я рад тебя видеть!"
            f"\n{emoji.emojize(':scroll:')} Теперь выкладывай, что же тебе понадобилось от такого "
            f"скромника как я? {emoji.emojize(':mechanical_arm:')}{emoji.emojize(':robot:')}",

    "user_not_registered": f"{emoji.emojize(':face_with_monocle:')} Вышло какое-то недопонимание, "
                           f"по моим данным ты ещё не прошел \"регистрацию\" {emoji.emojize(':clipboard:')}."
                           f"\n{emoji.emojize(':shushing_face:')} Только не переживай, "
                           "если это какая-то ошибка, то я буду рад вновь с тобой познакомиться, просто "
                           f"нажми {emoji.emojize(':backhand_index_pointing_right:')} /start и начни с самого начала.",

    "info": f"{emoji.emojize(':waving_hand:')} Доброго времени суток! "
            f"\n{emoji.emojize(':label:')} В этом сообщении содержиться описание функций бота:"
            f"\n\n{emoji.emojize(':keycap_1:')} Бот строит свои советы опираясь "
            "на координаты местности, которые вы предоставляете."
            f"\n\n{emoji.emojize(':keycap_2:')} В предоставленном ботом совете будет предложено "
            "что вам надеть в выбранный вами день и час, а так же будут показаны осадки и температура."
            f"\n\n{emoji.emojize(':keycap_3:')} Регистрацией пользователя является "
            "предоставление им координат при запросе."
            f"\n\n{emoji.emojize(':keycap_4:')} В боте используются фразы юмористического содержания "
            "с целью поднятия настроения пользователя, а так же для создания характера бота как отдельной личности."
}


MENU = {

    "prediction": f"{emoji.emojize(':speaking_head:')}Робот, дай совет что надеть!",

    "change_coordinates": f"{emoji.emojize(':world_map:')} Поменяй мои координаты!",

    "list_of_commands": f"{emoji.emojize(':open_book:')} Покажи список команд!"
}


# {day}
CHOOSE_DAY = {

    "first": f"{emoji.emojize(':keycap_1:')} "
             "{}",

    "second": f"{emoji.emojize(':keycap_2:')} "
              "{}",

    "third": f"{emoji.emojize(':keycap_3:')} "
             "{}",

    "fourth": f"{emoji.emojize(':keycap_4:')} "
              "{}",

    "fifth": f"{emoji.emojize(':keycap_5:')} "
             "{}",

    "sixth": f"{emoji.emojize(':keycap_6:')} "
             "{}",

    "seventh": f"{emoji.emojize(':keycap_7:')} "
               "{}",

    "eighth": f"{emoji.emojize(':keycap_8:')} "
              "{}"
}


CHOOSE_TIME = {

    "morning": f"{emoji.emojize(':cityscape:')} Утром! 05:00-12:00",

    "midday": f"{emoji.emojize(':national_park:')} Днём! 12:00-17:00",

    "evening": f"{emoji.emojize(':sunset:')} Вечером! 17:00-24:00",

    "night": f"{emoji.emojize(':night_with_stars:')} Ночью! 00:00-05:00"
}


COMMON_TEXT = {

    "greeting": f"{emoji.emojize(':waving_hand:')} Привет, да!",

    "cancel": f"{emoji.emojize(':anger_symbol:')} Проваливай жестянка!",

    "backspace_in_menu": f"{emoji.emojize(':BACK_arrow:')} Верни в меню!",

    "backspace_in_choice": f"{emoji.emojize(':BACK_arrow:')} Хочу перевыбрать день!",

    "agree": f"{emoji.emojize(':OK_hand:')} Я согласен, милый робот.",

    "pained": f"{emoji.emojize(':pleading_face:')} Было бы обидно, если бы я был человеком..."
              f"\n{emoji.emojize(':lying_face:')} Но я всегда с радостью дам тебе еще один шанс!"
              f"\n{emoji.emojize(':label:')} Можешь без угрызения совести "
              f"нажимать {emoji.emojize(':backhand_index_pointing_right:')} /start",

    "location_request": f"{emoji.emojize(':OK_hand:')} Хорошо!"
                        f"\n{emoji.emojize(':alien:')} Но мне нужна твоя преле...кхм, геолокация.",

    "location_confirm": f"{emoji.emojize(':pager:')} Данные успешно получены!"
                        f"\n{emoji.emojize(':robot:')} Чего теперь жаждет твоя человеческая воля?",

    "location_changed": f"{emoji.emojize(':counterclockwise_arrows_button:')} Локация успешно изменена!"
                        f"\n{emoji.emojize(':robot:')} Чего теперь жаждет твоя человеческая воля?",

    "list_of_commands": "/start -  Зарегистрировать себя (если этого не сделал)"
                        "\n\n/menu -  Главное меню (доступно зарегистрированным пользователям)"
                        "\n\n/help -  Помощь"
                        "\n\n/info -  Информация о боте",

    "return": f"{emoji.emojize(':face_screaming_in_fear:')} Ты сделал невозможное! Ты повернул время вспять!",

    # {text}
    "command_not_found": f"{emoji.emojize(':pensive_face:')} ""Ты уж прости, но я не знаю команду:  \"{}\"."
                         f"\n{emoji.emojize(':robot:')} Но не унывай, я всё-таки робот "
                         "и никогда не брошу человека в беде. "
                         f"\n{emoji.emojize(':label:')} Воспользуйся "
                         f"командой {emoji.emojize(':backhand_index_pointing_right:')} /help",
    # {text}
    "error_date": f"{emoji.emojize(':warning:')} ""Вышла какая-то ошибка, выбранная тобой дата \"{}\" неверная."
                  f"\n{emoji.emojize(':hourglass_done:')} Возможно ты выбрал устаревшую дату или ввёл неверную."
                  f"\n\n{emoji.emojize(':circled_M:')} Для избежания этой проблемы советую "
                  f"нажать {emoji.emojize(':backhand_index_pointing_right:')} /menu, "
                  "тогда тебя вернёт в начальное меню и при следующем запросе, список обновиться. "
                  f"\n\n{emoji.emojize(':label:')} Можешь попробовать выбрать другую дату",

    "prediction": f"{emoji.emojize(':thinking_face:')} Так-с... нужно определиться когда ты собираешься выйти "
                  f"на прогулку. {emoji.emojize(':woman_running:')}"
                  f"\n{emoji.emojize(':down_arrow:')} Я бы хотел услышать твой ответ. {emoji.emojize(':down_arrow:')}",

    # {text}, {precipitation}
    "day_selected": f"{emoji.emojize(':newspaper:')} "
                    "Нашел кое-какую информация на \"{}\", думаю ты будешь рад её услышать:"
                    f"\n\n{emoji.emojize(':pager:')} ""В этот день будет: {}."
                    f"\n{emoji.emojize(':droplet:')} ""Влажность: {}%."
                    f"\n{emoji.emojize(':wind_face:')} ""Скорость ветра: {} метров в секунду."
                    f"\n\n{emoji.emojize(':scroll:')} Ну теперь осталось дело за малым, "
                    "если хочешь получить совет то скажи, когда собираешься поразмять косточки?",

    "error_time": f"{emoji.emojize(':warning:')} Я не являюсь эспертом времени суток, мой создатель этого не учёл..."
                  "\nПоэтому я не могу понять что значит \"{}\"."
                  f"\n\n{emoji.emojize(':label:')} Прошу выбери из предложенного времени и нажми."
                  f"\n\n{emoji.emojize(':circled_M:')} Или могу предложить вернуться "
                  f"в главное меню {emoji.emojize(':backhand_index_pointing_right:')} /menu"
}

FUNCTION_TEXT = {

    # 1{EXPERIENCE},2{temperature}
    "weather_answer": '{}'
                      f"\n\n{emoji.emojize(':thermometer:')} "'Температура: {} ℃.'
                      f"\n\n{emoji.emojize(':circled_M:')} Ты можешь воспользоваться командой "
                      f"{emoji.emojize(':backhand_index_pointing_right:')} /menu, если снова захочешь прогуляться.",

    # 1{lat}, 2{lon}, 3{WEATHER_TOKEN}
    "url_for_request": "https://api.openweathermap.org/data/2.5/"
                       "onecall?lat={}&lon={}&exclude=current,minutely,hourly&units=metric&lang=ru&appid={}"
}


MIDDLEWARE_TEXT = {

    "block_flood": f"{emoji.emojize(':prohibited:')} Остановись! я не выдержу "
                   f"столько запросов! {emoji.emojize(':exploding_head:')} "
                   f"\n{emoji.emojize(':locked_with_key:')} Сработал анти-флуд, отправка сообщение заблокирована на "
                   "короткое время.",

    "unblock": f"{emoji.emojize(':locked_with_key:')} Робот разблокировал человека и теперь "
               f"человек свободен! {emoji.emojize(':unlocked:')}"

}