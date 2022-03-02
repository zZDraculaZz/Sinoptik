import emoji

MIDDLEWARE_TEXT = {

    "block_flood": [f"{emoji.emojize(':prohibited:')} Остановись! я не выдержу "
                    f"столько запросов! {emoji.emojize(':exploding_head:')} "
                    f"\n{emoji.emojize(':locked_with_key:')} Сработал анти-флуд, отправка сообщение заблокирована на "
                    "короткое время.",

                    f"{emoji.emojize(':prohibited:')} Stop! I can't stand it"
                    f"so many requests! {emoji.emojize(':exploding_head:')} "
                    f"\n{emoji.emojize(':locked_with_key:')} Anti-flood has worked, message sending is blocked for "
                    "a short time.",

                    f"{emoji.emojize(':prohibited:')} Зупинися! я не витримаю "
                    f" стільки запитів! {emoji.emojize(':exploding_head:')} "
                    f"\n{emoji.emojize(':locked_with_key:')} Спрацював анти-флуд, "
                    f"відправка повідомлення заблокована на "
                    "короткий час.",

                    f"{emoji.emojize(':prohibited:')} Hör auf! Ich kann es nicht ertragen"
                    f"so viele Anfragen! {emoji.emojize(':exploding_head:')} "
                    f"\n{emoji.emojize(':locked_with_key:')} Anti-Flood hat funktioniert, "
                    "Nachrichtenversand ist blockiert für "
                    "eine kurze Zeit.",

                    f"{emoji.emojize(':prohibited:')} 住手！我受不了了"
                    f"這麼多請求！{emoji.emojize(':exploding_head:')} "
                    f"\n{emoji.emojize(':locked_with_key:')} 防洪已經成功，消息發送被阻止 "
                    "很短的時間。",

                    f"{emoji.emojize(':prohibited:')} ¡Alto! No lo soporto"
                    f"¡Tantas solicitudes! {emoji.emojize(':exploding_head:')} "
                    f"\n{emoji.emojize(':locked_with_key:')} Anti-flood ha funcionado, "
                    "el envío de mensajes está bloqueado para "
                    "un tiempo corto.",
                    ],



    "unblock": [f"{emoji.emojize(':locked_with_key:')} Робот разблокировал человека и теперь "
                f"человек свободен! {emoji.emojize(':unlocked:')}",

                f"{emoji.emojize(':locked_with_key:')} The robot has unlocked the person and now "
                f"person is free! {emoji.emojize(':unlocked:')}",

                f"{emoji.emojize(':locked_with_key:')} Робот розблокував людину і тепер "
                f"людина вільна! {emoji.emojize(':unlocked:')}",

                f"{emoji.emojize(':locked_with_key:')} Der Roboter hat die Person entsperrt und jetzt "
                f"Person ist frei! {emoji.emojize(':unlocked:')}",

                f"{emoji.emojize(':locked_with_key:')} 機器人已經解鎖了這個人，現在"
                f"人有空！{emoji.emojize(':unlocked:')}",

                f"{emoji.emojize(':locked_with_key:')} El robot ha desbloqueado a la persona y ahora "
                f"¡persona libre! {emoji.emojize(':unlocked:')}",
                ]

}


# Используются в commands.py(handlers)
COMMAND_TEXT = {

    "start": [f"{emoji.emojize(':pirate_flag:')} Выбери язык, чтобы мы могли общаться на одной волне.",

              f"{emoji.emojize(':pirate_flag:')} Choose a language so we can communicate on the same wavelength.",

              f"{emoji.emojize(':pirate_flag:')} Вибери мову, щоб ми могли спілкуватися на одній хвилі.",

              f"{emoji.emojize(':pirate_flag:')} Wähle eine Sprache, damit wir auf derselben "
              f"Wellenlänge kommunizieren können.",

              f"{emoji.emojize(':pirate_flag:')} 選擇一種語言，以便我們可以在同一波長上進行交流。",

              f"{emoji.emojize(':pirate_flag:')} Elige un idioma para que podamos comunicarnos en la "
              f"misma longitud de onda.",
              ],



    "help": [f"{emoji.emojize(':label:')} Если хочешь получить совет по человеческой одежде и ещё "
             f"не \"зарегистрировался\", то просто нажми {emoji.emojize(':backhand_index_pointing_right:')} /start"
             f"\n\n{emoji.emojize(':label:')} Если не знаешь как передать мне свою геолокацию, "
             f"то просто перейди в настройки своего телефона {emoji.emojize(':mobile_phone_with_arrow:')}, "
             f"где есть кнопка с включением GPS {emoji.emojize(':satellite_antenna:')}, "
             "дальше тебе просто потребуется продолжить общение со мной."
             f"\n\n{emoji.emojize(':circled_M:')} А если ты уже предоставлял свою геолокацию "
             f"нажми {emoji.emojize(':backhand_index_pointing_right:')} /menu",

             f"{emoji.emojize(':label:')} If you want advice on human clothing and more "
             f"not \"registered\", then just press {emoji.emojize(':backhand_index_pointing_right:')} /start"
             f"\n\n{emoji.emojize(':label:')} If you don't know how to send me your geolocation, "
             f"then just go to your phone settings {emoji.emojize(':mobile_phone_with_arrow:')}, "
             f"where there is a button to enable GPS {emoji.emojize(':satellite_antenna:')}, "
             "then you just need to continue communicating with me."
             f"\n\n{emoji.emojize(':circled_M:')} And if you've already provided your geolocation "
             f"press {emoji.emojize(':backhand_index_pointing_right:')} /menu",

             f"{emoji.emojize(':label:')} Якщо хочеш отримати пораду з людського одягу та ще "
             f"не \"зареєструвався\", то просто натисніть {emoji.emojize(':backhand_index_pointing_right:')} /start"
             f"\n\n{emoji.emojize(':label:')} Якщо не знаєш, як передати мені свою геолокацію, "
             f"просто перейди в налаштування свого телефону {emoji.emojize(':mobile_phone_with_arrow:')}, "
             f"де є кнопка з включенням GPS {emoji.emojize(':satellite_antenna:')}, "
             "Далі тобі просто потрібно продовжити спілкування зі мною."
             f"\n\n{emoji.emojize(':circled_M:')} А якщо ти вже надавав свою геолокацію "
             f"натисніть {emoji.emojize(':backhand_index_pointing_right:')} /menu",

             f"{emoji.emojize(':label:')} Wenn Sie Ratschläge zu menschlicher Kleidung und mehr wünschen "
             f"nicht \"registriert\", dann drücke einfach {emoji.emojize(':backhand_index_pointing_right:')} /start"
             f"\n\n{emoji.emojize(':label:')} Wenn Sie nicht wissen, wie Sie mir Ihren Standort senden sollen, "
             f"Gehen Sie dann einfach zu Ihren Telefoneinstellungen {emoji.emojize(':mobile_phone_with_arrow:')}, "
             f"wo es eine Schaltfläche zum Aktivieren von GPS gibt {emoji.emojize(':satellite_antenna:')}, "
             "dann musst du einfach weiter mit mir kommunizieren."
             f"\n\n{emoji.emojize(':circled_M:')} Und wenn Sie bereits Ihre Geolokalisierung angegeben haben "
             f"drücke {emoji.emojize(':backhand_index_pointing_right:')} /menu",

             f"{emoji.emojize(':label:')} 如果你想要關於人類服裝的建議等等"
             f"not \"registered\"，然後按 {emoji.emojize(':backhand_index_pointing_right:')} /start"
             f"\n\n{emoji.emojize(':label:')} 如果您不知道如何將您的地理位置發送給我，"
             f"然後進入你的手機設置 {emoji.emojize(':mobile_phone_with_arrow:')}, "
             f"那裡有一個啟用 GPS 的按鈕 {emoji.emojize(':satellite_antenna:')}, "
             "那你只需要繼續和我交流。"
             f"\n\n{emoji.emojize(':circled_M:')} 如果你已經提供了你的地理位置 "
             f"按 {emoji.emojize(':backhand_index_pointing_right:')} /menu",

             f"{emoji.emojize(':label:')} Si quieres consejos sobre ropa humana y más"
             f"no \"registrado\", luego presione {emoji.emojize(':backhand_index_pointing_right:')} /start"
             f"\n\n{emoji.emojize(':label:')} Si no sabes cómo enviarme tu geolocalización, "
             f"entonces solo ve a la configuración de tu teléfono {emoji.emojize(':mobile_phone_with_arrow:')}, "
             f"donde hay un botón para habilitar el GPS {emoji.emojize(':satellite_antenna:')}, "
             "Entonces solo necesitas continuar comunicándote conmigo."
             f"\n\n{emoji.emojize(':circled_M:')} Y si ya proporcionaste tu geolocalización "
             f"presione {emoji.emojize(':backhand_index_pointing_right:')} /menu",
             ],



    "menu": [f"{emoji.emojize(':winking_face:')} Как же я рад тебя видеть!"
             f"\n{emoji.emojize(':scroll:')} Теперь выкладывай, что же тебе понадобилось от такого "
             f"скромника, как я? {emoji.emojize(':mechanical_arm:')}{emoji.emojize(':robot:')}",

             f"{emoji.emojize(':winking_face:')} How nice to see you!"
             f"\n{emoji.emojize(':scroll:')} Now tell me what you need from this "
             f"Shy, how am I? {emoji.emojize(':mechanical_arm:')}{emoji.emojize(':robot:')}",

             f"{emoji.emojize(':winking_face:')} Як же я радий тебе бачити!"
             f"\n{emoji.emojize(':scroll:')} Тепер викладай, що ж тобі знадобилося від такого "
             f"скромника, як я? {emoji.emojize(':mechanical_arm:')}{emoji.emojize(':robot:')}",

             f"{emoji.emojize(':winking_face:')} Wie schön dich zu sehen!"
             f"\n{emoji.emojize(':scroll:')} Sagen Sie mir jetzt, was Sie davon brauchen "
             f"Schüchtern, wie geht es mir? {emoji.emojize(':mechanical_arm:')}{emoji.emojize(':robot:')}",

             f"{emoji.emojize(':winking_face:')} 見到你真高興！"
             f"\n{emoji.emojize(':scroll:')} 現在告訴我你需要什麼 "
             f"害羞，我好嗎？{emoji.emojize(':mechanical_arm:')}{emoji.emojize(':robot:')}",

             f"{emoji.emojize(':winking_face:')} ¡Qué bueno verte!"
             f"\n{emoji.emojize(':scroll:')} Ahora dime qué necesitas de este "
             f"Tímido, ¿cómo estoy? {emoji.emojize(':mechanical_arm:')}{emoji.emojize(':robot:')}",
             ],



    "admin": [f"{emoji.emojize(':globe_with_meridians:')} Добро пожаловать в пункт "
              f"управления пользователями, здесь решаются судьбы.",

              f"{emoji.emojize(':globe_with_meridians:')} Welcome to point "
              f"User management, fates are decided here.",

              f"{emoji.emojize(':globe_with_meridians:')} Ласкаво просимо до пункту "
              f"управління користувачами, тут вирішуються долі.",

              f"{emoji.emojize(':globe_with_meridians:')} Willkommen bei Punkt "
              f"Benutzerverwaltung, hier werden Schicksale entschieden.",

              f"{emoji.emojize(':globe_with_meridians:')} 歡迎點"
              f"用戶管理，命運在這裡決定。",

              f"{emoji.emojize(':globe_with_meridians:')} Bienvenido al punto "
              f"administración de usuarios, los destinos se deciden aquí."],



    "not_admin": [f"{emoji.emojize(':no_entry')} Только \"Администратор\" имеет право на эту команду.",

                  f"{emoji.emojize(':no_entry')} Only \"Administrator\" is authorized to use this command.",

                  f"{emoji.emojize(':no_entry')} Тільки \"Адміністратор\" має право на цю команду.",

                  f"{emoji.emojize(':no_entry')} Nur \"Administrator\" ist berechtigt, diesen Befehl zu verwenden.",

                  f"{emoji.emojize(':no_entry')} 只允許\"管理員\"使用此命令。",

                  f"{emoji.emojize(':no_entry')} Solo el \"Administrador\" puede usar este comando."],



    "user_not_registered": [f"{emoji.emojize(':face_with_monocle:')} Вышло какое-то недопонимание, "
                            f"по моим данным ты ещё не прошел \"регистрацию\" {emoji.emojize(':clipboard:')}."
                            f"\n{emoji.emojize(':shushing_face:')} Только не переживай, "
                            "если это какая-то ошибка, то я буду рад вновь с тобой познакомиться, просто "
                            f"нажми {emoji.emojize(':backhand_index_pointing_right:')} /start и начни "
                            "с самого начала.",

                            f"{emoji.emojize(':face_with_monocle:')} There was some misunderstanding, "
                            "According to my information, you have not yet \"registered\" "
                            f"{emoji.emojize(':clipboard:')}."
                            f"\n{emoji.emojize(':shushing_face:')} Don't worry, "
                            "if this is some kind of mistake, then I will be glad to meet you again, just "
                            f"press {emoji.emojize(':backhand_index_pointing_right:')} /start and start"
                            "from the very beginning.",

                            f"{emoji.emojize(':face_with_monocle:')} Вийшло якесь непорозуміння, "
                            f"за моїми даними ти ще не пройшов \"реєстрацію\" {emoji.emojize(':clipboard:')}."
                            f"\n{emoji.emojize(':shushing_face:')} Тільки не переживай, "
                            "якщо це якась помилка, то я буду радий знову з тобою познайомитись, просто"
                            f"натисни {emoji.emojize(':backhand_index_pointing_right:')} /start та почни "
                            "з самого початку.",

                            f"{emoji.emojize(':face_with_monocle:')} Es gab ein Missverständnis, "
                            "Nach meinen Informationen haben Sie sich noch nicht \"registriert\" "
                            f"{emoji.emojize(':clipboard:')}."
                            f"\n{emoji.emojize(':shushing_face:')} Keine Sorge, "
                            "Wenn das ein Fehler ist, dann freue ich mich, dich wieder zu treffen, nur "
                            f"Drücke {emoji.emojize(':backhand_index_pointing_right:')} /start und starte"
                            "von Anfang an.",

                            f"{emoji.emojize(':face_with_monocle:')} 有誤會，"
                            f"根據我的信息，你還沒有“註冊”{emoji.emojize(':clipboard:')}。"
                            f"\n{emoji.emojize(':shushing_face:')} 別擔心，"
                            "如果這是某種錯誤，那麼我很高興再次見到你，只是"
                            f"按 {emoji.emojize(':backhand_index_pointing_right:')} /start 並開始"
                            "從一開始就。",

                            f"{emoji.emojize(':face_with_monocle:')} Hubo un malentendido, "
                            f"Según mi información, aún no se ha \"registrado\" {emoji.emojize(':clipboard:')}."
                            f"\n{emoji.emojize(':shushing_face:')} No te preocupes, "
                            "Si esto es algún tipo de error, estaré encantado de volver a verte, solo"
                            f"presione {emoji.emojize(':backhand_index_pointing_right:')} /start y comenzar"
                            "desde el principio."
                            ],



    "info": [f"{emoji.emojize(':waving_hand:')} Доброго времени суток! "
             f"\n{emoji.emojize(':label:')} В этом сообщении содержиться описание функций бота:"
             f"\n\n{emoji.emojize(':keycap_1:')} Бот строит свои советы опираясь "
             "на координаты местности, которые вы предоставляете."
             f"\n\n{emoji.emojize(':keycap_2:')} В предоставленном ботом совете будет предложено "
             "что вам надеть в выбранный вами день и час, а так же будут показаны осадки и температура."
             f"\n\n{emoji.emojize(':keycap_3:')} Регистрацией пользователя является выбор типа одежды и "
             "предоставление им координатов при запросе."
             f"\n\n{emoji.emojize(':keycap_4:')} В боте используются фразы юмористического содержания "
             "с целью поднятия настроения пользователя, а так же для создания характера бота как отдельной личности."
             f"\n\n{emoji.emojize(':keycap_5:')} Родным языком для бота является \"Русский\", все остальные доступные "
             "в боте языки были переведены машиной, поэтому могут присутствовать лексические "
             "ошибки, а то и вовсе может быть потерян смысл шутки, отсылки или предложения в боте.",

             f"{emoji.emojize(':waving_hand:')} Good afternoon!"
             f"\n{emoji.emojize(':label:')} This message contains a description of the bot's features:"
             f"\n\n{emoji.emojize(':keycap_1:')} The bot builds its tips based on "
             "to the location coordinates you provide."
             f"\n\n{emoji.emojize(':keycap_2:')} The bot-provided tip will suggest "
             "what to wear on the day and hour you choose, as well as rainfall and temperature."
             f"\n\n{emoji.emojize(':keycap_3:')} User registration is the choice of clothing type and "
             "giving them the coordinates when requested."
             f"\n\n{emoji.emojize(':keycap_4:')} The bot uses humorous phrases "
             "in order to raise the mood of the user, as well as to create the character of "
             "the bot as a separate person."
             f"\n\n{emoji.emojize(':keycap_5:')} The native language for the bot is \"Russian\", all other available "
             "languages in the bot were translated by machine, so lexical "
             "mistakes, or even the meaning of the joke, reference or sentence in the bot may be lost.",

             f"{emoji.emojize(':waving_hand:')} Доброго часу доби!"
             f"\n{emoji.emojize(':label:')} У цьому повідомленні міститься опис функцій бота:"
             f"\n\n{emoji.emojize(':keycap_1:')} Бот будує свої поради спираючись "
             "на координати місцевості, які ви надаєте."
             f"\n\n{emoji.emojize(':keycap_2:')} У наданій роботі раді буде запропоновано "
             "що вам надіти в обраний вами день і годину, а також будуть показані опади та температура."
             f"\n\n{emoji.emojize(':keycap_3:')} Реєстрацією користувача є вибір типу одягу та "
             "надання їм координат при запиті."
             f"\n\n{emoji.emojize(':keycap_4:')} У роботі використовуються фрази гумористичного змісту "
             "з метою підняття настрою користувача, а також створення характеру бота як окремої особистості."
             f"\n\n{emoji.emojize(':keycap_5:')} Рідною мовою для бота є \"Росiйська\", всі інші доступні "
             "в боті мови були перекладені машиною, тому можуть бути лексичні "
             "помилки, а то й зовсім може бути втрачений сенс жарту, відсилання чи пропозиції у боті.",

             f"{emoji.emojize(':waving_hand:')} Guten Tag!"
             f"\n{emoji.emojize(':label:')} Diese Nachricht enthält eine Beschreibung der Funktionen des Bots:"
             f"\n\n{emoji.emojize(':keycap_1:')} Der Bot baut seine Tipps basierend auf "
             "zu den von Ihnen angegebenen Standortkoordinaten."
             f"\n\n{emoji.emojize(':keycap_2:')} Der vom Bot bereitgestellte Tipp schlägt "
             "Was Sie an dem von Ihnen gewählten Tag und zu der von Ihnen gewählten Uhrzeit anziehen sollten, "
             "sowie Niederschlag und Temperatur."
             f"\n\n{emoji.emojize(':keycap_3:')} Benutzerregistrierung ist die Wahl des Kleidungstyps und "
             "Ihnen auf Anfrage die Koordinaten zu geben."
             f"\n\n{emoji.emojize(':keycap_4:')} Der Bot verwendet humorvolle Sätze "
             "um die Stimmung des Benutzers zu heben und den Charakter des Bots als eigenständige Person zu schaffen."
             f"\n\n{emoji.emojize(':keycap_5:')} Die Muttersprache für den Bot ist \"Russisch\", "
             "alle anderen verfügbar "
             "Sprachen im Bot wurden maschinell übersetzt, also lexikalisch"
             "Fehler oder sogar die Bedeutung des Witzes, der Referenz oder des Satzes im Bot können verloren gehen.",

             f"{emoji.emojize(':waving_hand:')} 下午好！"
             f"\n{emoji.emojize(':label:')} 此消息包含對機器人功能的描述："
             f"\n\n{emoji.emojize(':keycap_1:')} 機器人基於 "
             "到你提供的位置坐標。"
             f"\n\n{emoji.emojize(':keycap_2:')} 機器人提供的提示會建議"
             "在你選擇的日期和時間穿什麼，以及降雨量和溫度。"
             f"\n\n{emoji.emojize(':keycap_3:')} 用戶註冊是選擇服裝類型和"
             "根據要求給他們坐標。"
             f"\n\n{emoji.emojize(':keycap_4:')} 機器人使用幽默詞組"
             "為了提高用戶的情緒，以及創造機器人作為一個單獨的人的角色。"
             f"\n\n{emoji.emojize(':keycap_5:')} 機器人的母語是 \"Russian\"，其他都是 "
             "機器人中的語言是機器翻譯的，所以詞彙量很大"
             "錯誤，甚至可能會丟失機器人中的笑話、參考或句子的含義。",

             f"{emoji.emojize(':waving_hand:')} ¡Buenas tardes!"
             f"\n{emoji.emojize(':label:')} Este mensaje contiene una descripción de las características del bot:"
             f"\n\n{emoji.emojize(':keycap_1:')} El bot construye sus consejos basados ​​en "
             "a las coordenadas de ubicación que proporcione."
             f"\n\n{emoji.emojize(':keycap_2:')} La sugerencia proporcionada por el bot sugerirá "
             "qué ponerse el día y la hora que elija, así como las precipitaciones y la temperatura."
             f"\n\n{emoji.emojize(':keycap_3:')} El registro de usuario es la elección del tipo de ropa y "
             "Dándoles las coordenadas cuando lo soliciten."
             f"\n\n{emoji.emojize(':keycap_4:')} El bot usa frases humorísticas "
             "para elevar el estado de ánimo del usuario, así como para crear el carácter del bot como una "
             "persona separada."
             f"\n\n{emoji.emojize(':keycap_5:')} El idioma nativo del bot es \"ruso\", todos los demás son "
             "Los idiomas en el bot fueron traducidos por máquina, por lo que léxico"
             "Errores, o incluso el significado de una broma, referencia u oración en el bot puede perderse.",
             ]
}


FUNCTION_TEXT = {

    # 1{EXPERIENCE},2{temperature}
    "weather_answer": ['{}'
                       f"\n\n{emoji.emojize(':thermometer:')} "'Температура: {} ℃.'
                       f"\n\n{emoji.emojize(':circled_M:')} Ты можешь воспользоваться командой "
                       f"{emoji.emojize(':backhand_index_pointing_right:')} /menu, если снова захочешь прогуляться.",

                       '{}'
                       f"\n\n{emoji.emojize(':thermometer:')} "'Temperature: {} ℃.'
                       f"\n\n{emoji.emojize(':circled_M:')} You can suggest the command "
                       f"{emoji.emojize(':backhand_index_pointing_right:')} /menu if you want to walk again.",

                       '{}'
                       f"\n\n{emoji.emojize(':thermometer:')} "'Температура: {} ℃.'
                       f"\n\n{emoji.emojize(':circled_M:')} Ти можеш скористатися командою "
                       f"{emoji.emojize(':backhand_index_pointing_right:')} /menu, якщо захочеш знову прогулятися.",

                       '{}'
                       f"\n\n{emoji.emojize(':thermometer:')} "'Temperatur: {} ℃.'
                       f"\n\n{emoji.emojize(':circled_M:')} Sie können "
                       f"{emoji.emojize(':backhand_index_pointing_right:')} /menu wenn du wieder laufen willst.",

                       '{}'
                       f"\n\n{emoji.emojize(':thermometer:')} "'溫度：{}℃。'
                       f"\n\n{emoji.emojize(':circled_M:')} 你可以使用 "
                       f"{emoji.emojize(':backhand_index_pointing_right:')} /menu 如果你想再次四處走走。",

                       '{}'
                       f"\n\n{emoji.emojize(':thermometer:')} "'Temperatura: {} ℃.'
                       f"\n\n{emoji.emojize(':circled_M:')} Puedes usar "
                       f"{emoji.emojize(':backhand_index_pointing_right:')} /menu si quieres caminar de nuevo.",
                       ],

    # 1{lat}, 2{lon}, 3{WEATHER_TOKEN}
    "url_for_request": "https://api.openweathermap.org/data/2.5/"
                       "onecall?lat={}&lon={}&exclude=current,minutely,hourly&units=metric&lang=ru&appid={}"
}


A_MENU = {

    "prediction": [f"{emoji.emojize(':thinking_face:')} Так-с... нужно определиться когда ты собираешься выйти "
                   f"на прогулку. {emoji.emojize(':woman_running:')}"
                   f"\n{emoji.emojize(':down_arrow:')} Я бы хотел услышать твой "
                   f"ответ. {emoji.emojize(':down_arrow:')}",

                   f"{emoji.emojize(':thinking_face:')} So...you need to decide when you're going to go out"
                   f"for a walk. {emoji.emojize(':woman_running:')}"
                   f"\n{emoji.emojize(':down_arrow:')} I would like to hear your "
                   f"answer. {emoji.emojize(':down_arrow:')}",

                   f"{emoji.emojize(':thinking_face:')} Так-с... потрібно визначитися коли ти збираєшся вийти"
                   f"на прогулянку. {emoji.emojize(':woman_running:')}"
                   f"\n{emoji.emojize(':down_arrow:')} Я б хотів почути твій "
                   f"відповідь. {emoji.emojize(':down_arrow:')}",

                   f"{emoji.emojize(':thinking_face:')} Also ... du musst entscheiden, wann du ausgehen wirst"
                   f"Spazieren gehen. {emoji.emojize(':woman_running:')}"
                   f"\n{emoji.emojize(':down_arrow:')} Ich würde gerne Ihre "
                   f"Antwort. {emoji.emojize(':down_arrow:')}",

                   f"{emoji.emojize(':thinking_face:')} 所以……你需要決定什麼時候出去"
                   f"散步。{emoji.emojize(':woman_running:')}"
                   f"\n{emoji.emojize(':down_arrow:')} 我想听聽你的"
                   f"答案。{emoji.emojize(':down_arrow:')}",

                   f"{emoji.emojize(':thinking_face:')} Así que... tienes que decidir cuándo vas a salir"
                   f"de paseo. {emoji.emojize(':woman_running:')}"
                   f"\n{emoji.emojize(':down_arrow:')} Me gustaría escuchar tu "
                   f"respuesta. {emoji.emojize(':down_arrow:')}",
                   ],



    "list_of_commands": ["/start -  Зарегистрировать себя (если этого не сделал)"
                         "\n\n/menu -  Главное меню (доступно зарегистрированным пользователям)"
                         "\n\n/help -  Помощь"
                         "\n\n/info -  Информация о боте",

                         "/start - Register yourself (if you haven't already)"
                         "\n\n/menu - Main menu (available to registered users)"
                         "\n\n/help - Help"
                         "\n\n/info - Information about the bot",

                         "/start - Зареєструвати себе (якщо цього не зробив)"
                         "\n\n/menu - Головне меню (доступне зареєстрованим користувачам)"
                         "\n\n/help - Допомога"
                         "\n\n/info - Інформація про роботу",

                         "/start - Registrieren Sie sich (falls noch nicht geschehen)"
                         "\n\n/menu - Hauptmenü (verfügbar für registrierte Benutzer)"
                         "\n\n/help - Hilfe"
                         "\n\n/info - Informationen über den Bot",

                         "/start - 註冊自己（如果你還沒有）"
                         "\n\n/menu - 主菜單（註冊用戶可用）"
                         "\n\n/help - 幫助"
                         "\n\n/info - 關於機器人的信息",

                         "/start - Regístrese usted mismo (si aún no lo ha hecho)"
                         "\n\n/menu - Menú principal (disponible para usuarios registrados)"
                         "\n\n/help -ayuda"
                         "\n\n/info - Información sobre el bot",
                         ],



    "in_settings": [f"{emoji.emojize(':counterclockwise_arrows_button:')} Настало время перемен! Что хочешь поменять?",

                    f"{emoji.emojize(':counterclockwise_arrows_button:')} It's time for a change! "
                    "What do you want to change?",

                    f"{emoji.emojize(':counterclockwise_arrows_button:')} Настав час змін! Що хочеш змінити?",

                    f"{emoji.emojize(':counterclockwise_arrows_button:')} Es ist Zeit für eine Veränderung! "
                    "Was möchtest du ändern?",

                    f"{emoji.emojize(':counterclockwise_arrows_button:')} 是時候改變了！你想改變什麼？",

                    f"{emoji.emojize(':counterclockwise_arrows_button:')} ¡Es hora de un cambio! "
                    f"¿Qué quieres cambiar?",
                    ],
}


A_SETTINGS = {

    "location_changed": [f"{emoji.emojize(':counterclockwise_arrows_button:')} Локация успешно изменена!"
                         f"\n{emoji.emojize(':robot:')} Чего теперь жаждет твоя человеческая воля?",

                         f"{emoji.emojize(':counterclockwise_arrows_button:')} Location changed successfully!"
                         f"\n{emoji.emojize(':robot:')} What does your human will now crave?",

                         f"{emoji.emojize(':counterclockwise_arrows_button:')} Локація успішно змінена!"
                         f"\n{emoji.emojize(':robot:')} Чого тепер прагне твоя людська воля?",

                         f"{emoji.emojize(':counterclockwise_arrows_button:')} Ort erfolgreich geändert!"
                         f"\n{emoji.emojize(':robot:')} Wonach wird sich dein Mensch jetzt sehnen?",

                         f"{emoji.emojize(':counterclockwise_arrows_button:')} 位置更改成功！"
                         f"\n{emoji.emojize(':robot:')} 你的人類現在渴望什麼？",

                         f"{emoji.emojize(':counterclockwise_arrows_button:')} ¡La ubicación se cambió correctamente!"
                         f"\n{emoji.emojize(':robot:')} ¿Qué anhela tu ser humano ahora?",
                         ],



    "gender_changed": [f"{emoji.emojize(':check_mark_button:')} "
                       "Ты успешно изменил \"{}\" тип одежды на \"{}\"",

                       f"{emoji.emojize(':check_mark_button:')}"
                       "You have successfully changed \"{}\" clothing type to \"{}\"",

                       f"{emoji.emojize(':check_mark_button:')} "
                       "Ти успішно змінив \"{}\" тип одягу на \"{}\"",

                       f"{emoji.emojize(':check_mark_button:')}"
                       "Sie haben den Kleidungstyp von \"{}\" erfolgreich in \"{}\" geändert",

                       f"{emoji.emojize(':check_mark_button:')}"
                       "您已成功將 \"{}\" 服裝類型更改為 \"{}\" ",

                       f"{emoji.emojize(':check_mark_button:')}"
                       "Has cambiado con éxito el tipo de ropa \"{}\" a \"{}\" ",
                       ],



    "choose_language": [f"{emoji.emojize(':speaking_head:')} Выбери из доступных нужный тебе язык, "
                        "а всё остальное я сделаю сам."
                        f"\n{emoji.emojize(':label:')} Если передумал, можешь нажать "
                        f"{emoji.emojize(':backhand_index_pointing_right:')} /menu",

                        f"{emoji.emojize(':speaking_head:')} Choose the language you want from the available ones, "
                        "I'll do the rest myself."
                        f"\n{emoji.emojize(':label:')} If you change your mind, you can click "
                        f"{emoji.emojize(':backhand_index_pointing_right:')} /menu",

                        f"{emoji.emojize(':speaking_head:')} Вибери з доступних потрібну тобі мову, "
                        "а все інше я зроблю сам."
                        f"\n{emoji.emojize(':label:')} Якщо передумав, можеш натиснути "
                        f"{emoji.emojize(':backhand_index_pointing_right:')} /menu",

                        f"{emoji.emojize(':speaking_head:')} Wählen Sie die gewünschte Sprache aus den "
                        "verfügbaren aus, Den Rest mache ich selbst."
                        f"\n{emoji.emojize(':label:')} Wenn Sie Ihre Meinung ändern, können Sie auf "
                        f"{emoji.emojize(':backhand_index_pointing_right:')} /menu",

                        f"{emoji.emojize(':speaking_head:')} 從可用語言中選擇您想要的語言，"
                        "剩下的我自己來。"
                        f"\n{emoji.emojize(':label:')} 如果你改變主意，可以點擊"
                        f"{emoji.emojize(':backhand_index_pointing_right:')} /menu",

                        f"{emoji.emojize(':speaking_head:')} Elija el idioma que desee de los disponibles, "
                        "Haré el resto yo mismo."
                        f"\n{emoji.emojize(':label:')} Si cambia de opinión, puede hacer clic en "
                        f"{emoji.emojize(':backhand_index_pointing_right:')} /menu",
                        ],



    "language_changed": [f"{emoji.emojize(':check_mark_button:')} Язык успешно изменён! "
                         "Теперь-то мы точно поймём друг друга. Наверное..."
                         f"\n\n{emoji.emojize(':label:')} Можешь вернуться в меню "
                         f"{emoji.emojize(':backhand_index_pointing_right:')} /menu",

                         f"{emoji.emojize(':check_mark_button:')} Language changed successfully! "
                         "Now we'll definitely understand each other. Probably..."
                         f"\n\n{emoji.emojize(':label:')} You can return to the menu "
                         f"{emoji.emojize(':backhand_index_pointing_right:')} /menu",

                         f"{emoji.emojize(':check_mark_button:')} Мова успішно змінена! "
                         "Тепер ми точно зрозуміємо один одного. Напевно ..."
                         f"\n\n{emoji.emojize(':label:')} Можеш повернутися до меню "
                         f"{emoji.emojize(':backhand_index_pointing_right:')} /menu",

                         f"{emoji.emojize(':check_mark_button:')} Sprache erfolgreich geändert! "
                         "Jetzt werden wir uns bestimmt verstehen. Wahrscheinlich..."
                         f"\n\n{emoji.emojize(':label:')} Sie können zum Menü zurückkehren "
                         f"{emoji.emojize(':backhand_index_pointing_right:')} /menu",

                         f"{emoji.emojize(':check_mark_button:')} 語言更改成功！"
                         "現在我們一定會互相理解的。大概..."
                         f"\n\n{emoji.emojize(':label:')} 可以返回菜單"
                         f"{emoji.emojize(':backhand_index_pointing_right:')} /menu",

                         f"{emoji.emojize(':check_mark_button:')} ¡El idioma cambió correctamente! "
                         "Ahora definitivamente nos entenderemos. Probablemente..."
                         f"\n\n{emoji.emojize(':label:')} Puede volver al menú "
                         f"{emoji.emojize(':backhand_index_pointing_right:')} /menu",
                         ],



    "language_not_found": [f"{emoji.emojize(':warning:')} Ты сделал не правильный выбор, ты пожалеешь об... "
                           f"\n\n{emoji.emojize(':face_with_rolling_eyes:')} Упс...Я случайно перепутал реплики, "
                           f"так о чем я должен был рассказать?"
                           f"\n\n{emoji.emojize(':label:')} Точно! Выбранный тобой язык недоступен, "
                           f"выбери из предложенных или можешь вернуться в меню "
                           f"{emoji.emojize(':backhand_index_pointing_right:')} /menu",

                           f"{emoji.emojize(':warning:')} You made the wrong choice, you will regret... "
                           f"\n\n{emoji.emojize(':face_with_rolling_eyes:')} Oops...I accidentally mixed up the lines, "
                           f"So what was I supposed to talk about?"
                           f"\n\n{emoji.emojize(':label:')} Exactly! Your chosen language is not available, "
                           f"choose from those offered or you can return to the menu"
                           f"{emoji.emojize(':backhand_index_pointing_right:')} /menu",

                           f"{emoji.emojize(':warning:')} Ти зробив не правильний вибір, ти пошкодуєш про..."
                           f"\n\n{emoji.emojize(':face_with_rolling_eyes:')} Упс...Я випадково переплутав репліки, "
                           f"так про що я повинен був розповісти?"
                           f"\n\n{emoji.emojize(':label:')} Точно! Вибрана тобою мова недоступна, "
                           f"вибери із запропонованих або можеш повернутися в меню "
                           f"{emoji.emojize(':backhand_index_pointing_right:')} /menu",

                           f"{emoji.emojize(':warning:')} Du hast die falsche Wahl getroffen, du wirst es bereuen... "
                           f"\n\n{emoji.emojize(':face_with_rolling_eyes:')} Hoppla ... "
                           "ich habe versehentlich die Zeilen verwechselt, "
                           f"Also, worüber sollte ich reden?"
                           f"\n\n{emoji.emojize(':label:')} Genau! Ihre gewählte Sprache ist nicht verfügbar, "
                           f"Wählen Sie aus den Angeboten oder kehren Sie zum Menü zurück"
                           f"{emoji.emojize(':backhand_index_pointing_right:')} /menu",

                           f"{emoji.emojize(':warning:')} 你選錯了，你會後悔的..."
                           f"\n\n{emoji.emojize(':face_with_rolling_eyes:')} 哎呀...我不小心弄錯了台詞，"
                           f"那我應該說什麼？"
                           f"\n\n{emoji.emojize(':label:')} 沒錯！您選擇的語言不可用，"
                           f"從提供的選項中選擇，或者您可以返回菜單"
                           f"{emoji.emojize(':backhand_index_pointing_right:')} /menu",

                           f"{emoji.emojize(':warning:')} Tomaste la decisión equivocada, te arrepentirás... "
                           f"\n\n{emoji.emojize(':face_with_rolling_eyes:')} Ups... Accidentalmente mezclé las líneas, "
                           f"Entonces, ¿de qué se suponía que debía hablar?"
                           f"\n\n{emoji.emojize(':label:')} ¡Exactamente! El idioma elegido no está disponible, "
                           f"elija entre los ofrecidos o puede volver al menú"
                           f"{emoji.emojize(':backhand_index_pointing_right:')} /menu",
                           ]

}