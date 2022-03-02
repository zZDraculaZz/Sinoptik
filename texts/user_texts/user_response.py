import emoji


WEEK_DAY = {
    0: [f"{emoji.emojize(':spiral_calendar:')} Пн",

        f"{emoji.emojize(':spiral_calendar:')} Mon",

        f"{emoji.emojize(':spiral_calendar:')} Пн",

        f"{emoji.emojize(':spiral_calendar:')} Mon",

        f"{emoji.emojize(':spiral_calendar:')} 週一",

        f"{emoji.emojize(':spiral_calendar:')} Lun",
        ],



    1: [f"{emoji.emojize(':spiral_calendar:')} Вт",

        f"{emoji.emojize(':spiral_calendar:')} Tue",

        f"{emoji.emojize(':spiral_calendar:')} Вв",

        f"{emoji.emojize(':spiral_calendar:')} Die",

        f"{emoji.emojize(':spiral_calendar:')} 週二",

        f"{emoji.emojize(':spiral_calendar:')} Mar",
        ],



    2: [f"{emoji.emojize(':spiral_calendar:')} Ср",

        f"{emoji.emojize(':spiral_calendar:')} Wed",

        f"{emoji.emojize(':spiral_calendar:')} Ср",

        f"{emoji.emojize(':spiral_calendar:')} Mit",

        f"{emoji.emojize(':spiral_calendar:')} 週三",

        f"{emoji.emojize(':spiral_calendar:')} Mie",
        ],



    3: [f"{emoji.emojize(':spiral_calendar:')} Чт",

        f"{emoji.emojize(':spiral_calendar:')} Thu",

        f"{emoji.emojize(':spiral_calendar:')} Чт",

        f"{emoji.emojize(':spiral_calendar:')} Don",

        f"{emoji.emojize(':spiral_calendar:')} 週四",

        f"{emoji.emojize(':spiral_calendar:')} Jue",
        ],



    4: [f"{emoji.emojize(':spiral_calendar:')} Пт",

        f"{emoji.emojize(':spiral_calendar:')} Fri",

        f"{emoji.emojize(':spiral_calendar:')} Пт",

        f"{emoji.emojize(':spiral_calendar:')} Fre",

        f"{emoji.emojize(':spiral_calendar:')} 星期五",

        f"{emoji.emojize(':spiral_calendar:')} Vie",
        ],



    5: [f"{emoji.emojize(':spiral_calendar:')} Сб",

        f"{emoji.emojize(':spiral_calendar:')} Sat",

        f"{emoji.emojize(':spiral_calendar:')} Сб",

        f"{emoji.emojize(':spiral_calendar:')} Sam",

        f"{emoji.emojize(':spiral_calendar:')} 週六",

        f"{emoji.emojize(':spiral_calendar:')} Sáb",
        ],



    6: [f"{emoji.emojize(':spiral_calendar:')} Вс",

        f"{emoji.emojize(':spiral_calendar:')} Sun",

        f"{emoji.emojize(':spiral_calendar:')} Нд",

        f"{emoji.emojize(':spiral_calendar:')} Son",

        f"{emoji.emojize(':spiral_calendar:')} 星期日",

        f"{emoji.emojize(':spiral_calendar:')} Dom",
        ],

    7: [f"{emoji.emojize(':spiral_calendar:')} Вс",

        f"{emoji.emojize(':spiral_calendar:')} Sun",

        f"{emoji.emojize(':spiral_calendar:')} Нд",

        f"{emoji.emojize(':spiral_calendar:')} Son",

        f"{emoji.emojize(':spiral_calendar:')} 星期日",

        f"{emoji.emojize(':spiral_calendar:')} Dom",
        ]
}


# {day} {WEEK_DAY}
CHOOSE_DAY = {

    "first": f"{emoji.emojize(':keycap_1:')} "
             "{} {}",

    "second": f"{emoji.emojize(':keycap_2:')} "
              "{} {}",

    "third": f"{emoji.emojize(':keycap_3:')} "
             "{} {}",

    "fourth": f"{emoji.emojize(':keycap_4:')} "
              "{} {}",

    "fifth": f"{emoji.emojize(':keycap_5:')} "
             "{} {}",

    "sixth": f"{emoji.emojize(':keycap_6:')} "
             "{} {}",

    "seventh": f"{emoji.emojize(':keycap_7:')} "
               "{} {}",

    "eight": f"{emoji.emojize(':keycap_8:')} "
             "{} {}"
}


CHOOSE_TIME = {

    "morning": [f"{emoji.emojize(':cityscape:')} Утром! 00:00-12:00",

                f"{emoji.emojize(':cityscape:')} Morning! 00:00-12:00",

                f"{emoji.emojize(':cityscape:')} Вранці! 00:00-12:00",

                f"{emoji.emojize(':cityscape:')} Morgens! 00:00-12:00",

                f"{emoji.emojize(':cityscape:')} 早上！00:00-12:00",

                f"{emoji.emojize(':cityscape:')} Mañana! 00:00-12:00"],



    "midday": [f"{emoji.emojize(':national_park:')} Днём! 12:00-17:00",

               f"{emoji.emojize(':national_park:')} Daytime! 12:00-17:00",

               f"{emoji.emojize(':national_park:')} Вдень! 12:00-17:00",

               f"{emoji.emojize(':national_park:')} Tagsüber! 12:00-17:00",

               f"{emoji.emojize(':national_park:')} 白天！12:00-17:00",

               f"{emoji.emojize(':national_park:')} Día! 12:00-17:00",
               ],



    "evening": [f"{emoji.emojize(':sunset:')} Вечером! 17:00-24:00",

                f"{emoji.emojize(':sunset:')} Evening! 17:00-20:00",

                f"{emoji.emojize(':sunset:')} Увечері! 17:00-24:00",

                f"{emoji.emojize(':sunset:')} Abend! 17:00-20:00",

                f"{emoji.emojize(':sunset:')} 晚上！17:00-24:00",

                f"{emoji.emojize(':sunset:')} Por la tarde! 17:00-20:00"],



    "night": [f"{emoji.emojize(':night_with_stars:')} Ночью! 20:00-24:00",

              f"{emoji.emojize(':night_with_stars:')} At night! 20:00-24:00",

              f"{emoji.emojize(':night_with_stars:')} Вночі! 20:00-24:00",

              f"{emoji.emojize(':night_with_stars:')} Nachts! 20:00-24:00",

              f"{emoji.emojize(':night_with_stars:')} 晚上！20:00-24:00",

              f"{emoji.emojize(':night_with_stars:')} ¡Por la noche! 20:00-24:00"]
}


R_MENU = {

    "prediction": [f"{emoji.emojize(':speaking_head:')} Робот, дай совет что надеть!",

                   f"{emoji.emojize(':speaking_head:')} Robot, give me advice on what to wear!",

                   f"{emoji.emojize(':speaking_head:')} Робот, дай пораду що вдягнути!",

                   f"{emoji.emojize(':speaking_head:')} Roboter, gib mir einen Rat, was ich anziehen soll!",

                   f"{emoji.emojize(':speaking_head:')} 機器人，給我建議穿什麼！",

                   f"{emoji.emojize(':speaking_head:')} ¡Robot, aconséjame qué ponerme!",
                   ],



    "settings": [f"{emoji.emojize(':gear:')} Настройки",

                 f"{emoji.emojize(':gear:')} Settings",

                 f"{emoji.emojize(':gear:')} Налаштування",

                 f"{emoji.emojize(':gear:')} Einstellungen",

                 f"{emoji.emojize(':gear:')} 設置",

                 f"{emoji.emojize(':gear:')} Configuración",
                 ],



    "list_of_commands": [f"{emoji.emojize(':open_book:')} Покажи список команд!",

                         f"{emoji.emojize(':open_book:')} Show command list!",

                         f"{emoji.emojize(':open_book:')} Покажи список команд!",

                         f"{emoji.emojize(':open_book:')} Befehlsliste anzeigen!",

                         f"{emoji.emojize(':open_book:')} 顯示命令列表！",

                         f"{emoji.emojize(':open_book:')} ¡Mostrar lista de comandos!",
                         ]
}


R_SETTINGS = {
    "change_coordinates": [f"{emoji.emojize(':world_map:')} Сменить координаты",

                           f"{emoji.emojize(':world_map:')} Change coordinates",

                           f"{emoji.emojize(':world_map:')} Змінити координати",

                           f"{emoji.emojize(':world_map:')} Koordinaten ändern",

                           f"{emoji.emojize(':world_map:')} 改變坐標",

                           f"{emoji.emojize(':world_map:')} Cambiar coordenadas",
                           ],



    "change_gender": [f"{emoji.emojize(':restroom:')} Сменить тип одежды",

                      f"{emoji.emojize(':restroom:')} Change clothing type",

                      f"{emoji.emojize(':restroom:')} Змінити тип одягу",

                      f"{emoji.emojize(':restroom:')} Kleidungstyp ändern",

                      f"{emoji.emojize(':restroom:')} 改變服裝類型",

                      f"{emoji.emojize(':restroom:')} Cambiar tipo de ropa",
                      ],



    "change_language": [f"{emoji.emojize(':pirate_flag:')} Сменить язык",

                        f"{emoji.emojize(':pirate_flag:')} Change language",

                        f"{emoji.emojize(':pirate_flag:')} Змінити мову",

                        f"{emoji.emojize(':pirate_flag:')} Sprache ändern",

                        f"{emoji.emojize(':pirate_flag:')} 更改語言",

                        f"{emoji.emojize(':pirate_flag:')} Cambiar idioma",
                        ],



    "return_in_settings": [f"{emoji.emojize(':BACK_arrow:')} Верни в настройки!",

                           f"{emoji.emojize(':BACK_arrow:')} Go back to settings!",

                           f"{emoji.emojize(':BACK_arrow:')} Поверни в налаштування!",

                           f"{emoji.emojize(':BACK_arrow:')} Zurück zu den Einstellungen!",

                           f"{emoji.emojize(':BACK_arrow:')} 回到設置！",

                           f"{emoji.emojize(':BACK_arrow:')} ¡Vuelve a la configuración!",
                           ]
}