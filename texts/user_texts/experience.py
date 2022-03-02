import emoji
# ответы на температуру, от -15 до бесконечного минуса) и в другом углу ринга от 23 до бесконечного пекла
# Используется в weather.py(functions)
EXPERIENCE = {

    "-15": [[f"{emoji.emojize(':scroll:')} С таким холодом и водного охлаждения не нужно, надевай на"
             f"\n\n{emoji.emojize(':crown:')} Голову: шапку-ушанку."
             f"\n{emoji.emojize(':scarf:')} Шею: шарфик (тёплый)."
             f"\n{emoji.emojize(':coat:')} Торс: майку, шерстяной свитер, шубу."
             f"\n{emoji.emojize(':gloves:')} Руки: любые тёплые перчатки."
             f"\n{emoji.emojize(':jeans:')} Талию: тёплые колготы, штаны."
             f"\n{emoji.emojize(':hiking_boot:')} Ноги: шерстяные носки, валенки.",

             f"{emoji.emojize(':scroll:')} With this cold, you don't need water cooling, put it on"
             f"\n\n{emoji.emojize(':crown:')} Head: warm hat."
             f"\n{emoji.emojize(':scarf:')} Neck: warm scarf."
             f"\n{emoji.emojize(':coat:')} Torso: T-shirt, wool sweater, fur coat."
             f"\n{emoji.emojize(':gloves:')} Hands: any warm gloves."
             f"\n{emoji.emojize(':jeans:')} Waist: warm tights, pants."
             f"\n{emoji.emojize(':hiking_boot:')} Feet: woolen socks, felt boots.",

             f"{emoji.emojize(':scroll:')} З таким холодом і водного охолодження не потрібно, одягай на"
             f"\n\n{emoji.emojize(':crown:')} Голову: шапку-вушанку."
             f"\n{emoji.emojize(':scarf:')} Шию: шарфик (теплий)."
             f"\n{emoji.emojize(':coat:')} Торс: майку, вовняний светр, шубу."
             f"\n{emoji.emojize(':gloves:')} Руки: будь-які теплі рукавички."
             f"\n{emoji.emojize(':jeans:')} Талію: теплі колготи, штани."
             f"\n{emoji.emojize(':hiking_boot:')} Ноги: вовняні шкарпетки, валянки.",

             f"{emoji.emojize(':scroll:')} Bei dieser Erkältung brauchst du keine Wasserkühlung, zieh sie an"
             f"\n\n{emoji.emojize(':crown:')} Kopf: Hut mit Ohrenklappen."
             f"\n{emoji.emojize(':scarf:')} Hals: Schal (warm)."
             f"\n{emoji.emojize(':coat:')} Oberkörper: T-Shirt, Wollpullover, Pelzmantel."
             f"\n{emoji.emojize(':gloves:')} Hände: alle warmen Handschuhe."
             f"\n{emoji.emojize(':jeans:')} Taille: warme Strumpfhose, Hose."
             f"\n{emoji.emojize(':hiking_boot:')} Füße: Wollsocken, Filzstiefel.",

             f"{emoji.emojize(':scroll:')} 這麼冷就不用水冷了，裝上吧"
             f"\n\n{emoji.emojize(':crown:')} 頭：帶耳罩的帽子。"
             f"\n{emoji.emojize(':scarf:')} 脖子：圍巾（暖色）。"
             f"\n{emoji.emojize(':coat:')} 軀幹：T 卹、羊毛衫、皮草大衣。"
             f"\n{emoji.emojize(':gloves:')} 手：任何溫暖的手套。"
             f"\n{emoji.emojize(':jeans:')} 腰部：保暖緊身衣、褲子。"
             f"\n{emoji.emojize(':hiking_boot:')} 腿：羊毛襪，氈靴。",

             f"{emoji.emojize(':scroll:')} Con este frio no hace falta enfriar con agua, pontelo"
             f"\n\n{emoji.emojize(':crown:')} Cabeza: gorro con orejerass."
             f"\n{emoji.emojize(':scarf:')} Cuello: bufanda (caliente)."
             f"\n{emoji.emojize(':coat:')} Torso: camiseta, suéter de lana, abrigo de piel."
             f"\n{emoji.emojize(':gloves:')} Manos: cualquier guante caliente."
             f"\n{emoji.emojize(':jeans:')} Cintura: medias cálidas, pantalones."
             f"\n{emoji.emojize(':hiking_boot:')} Piernas: calcetines de lana, botas de fieltro.",
             ],



            [f"{emoji.emojize(':scroll:')} С таким холодом и водного охлаждения не нужно, надевай на"
             f"\n\n{emoji.emojize(':crown:')} Голову: шапку-ушанку."
             f"\n{emoji.emojize(':scarf:')} Шею: шарфик (тёплый)."
             f"\n{emoji.emojize(':coat:')} Торс: майку, шерстяной свитер, тёплую дублёнку."
             f"\n{emoji.emojize(':gloves:')} Руки: любые тёплые перчатки."
             f"\n{emoji.emojize(':jeans:')} Талию: тёплые подштанники, брюки."
             f"\n{emoji.emojize(':hiking_boot:')} Ноги: шерстяные носки, валенки.",

             f"{emoji.emojize(':scroll:')} With this cold, you don't need water cooling, put it on"
             f"\n\n{emoji.emojize(':crown:')} Head: warm hat."
             f"\n{emoji.emojize(':scarf:')} Neck: warm scarf."
             f"\n{emoji.emojize(':coat:')} Torso: T-shirt, wool sweater, warm sheepskin coat."
             f"\n{emoji.emojize(':gloves:')} Hands: any warm gloves."
             f"\n{emoji.emojize(':jeans:')} Waist: warm underpants, trousers."
             f"\n{emoji.emojize(':hiking_boot:')} Feet: woolen socks, felt boots.",

             f"{emoji.emojize(':scroll:')} З таким холодом і водного охолодження не потрібно, одягай на"
             f"\n\n{emoji.emojize(':crown:')} Голову: шапку-вушанку."
             f"\n{emoji.emojize(':scarf:')} Шию: шарфик (теплий)."
             f"\n{emoji.emojize(':coat:')} Торс: майку, вовняний светр, теплу дублянку."
             f"\n{emoji.emojize(':gloves:')} Руки: будь-які теплі рукавички."
             f"\n{emoji.emojize(':jeans:')} Талія: теплі підштанники, штани."
             f"\n{emoji.emojize(':hiking_boot:')} Ноги: вовняні шкарпетки, валянки.",

             f"{emoji.emojize(':scroll:')} Bei dieser Erkältung brauchst du keine Wasserkühlung, zieh sie an"
             f"\n\n{emoji.emojize(':crown:')} Kopf: Hut mit Ohrenklappen."
             f"\n{emoji.emojize(':scarf:')} Hals: Schal (warm)."
             f"\n{emoji.emojize(':coat:')} Oberkörper: T-Shirt, Wollpullover, warmer Schaffellmantel."
             f"\n{emoji.emojize(':gloves:')} Hände: alle warmen Handschuhe."
             f"\n{emoji.emojize(':jeans:')} Taille: warme Unterhose, Hose."
             f"\n{emoji.emojize(':hiking_boot:')} Füße: Wollsocken, Filzstiefel.",

             f"{emoji.emojize(':scroll:')} 這麼冷就不用水冷了，裝上吧"
             f"\n\n{emoji.emojize(':crown:')} 頭：帶耳罩的帽子。"
             f"\n{emoji.emojize(':scarf:')} 脖子：圍巾（暖色）。"
             f"\n{emoji.emojize(':coat:')} 軀幹：T卹、羊毛衫、保暖羊皮大衣。"
             f"\n{emoji.emojize(':gloves:')} 手：任何溫暖的手套。"
             f"\n{emoji.emojize(':jeans:')} 腰部：保暖內褲、長褲。"
             f"\n{emoji.emojize(':hiking_boot:')} 腿：羊毛襪，氈靴。",

             f"{emoji.emojize(':scroll:')} Con este frio no hace falta enfriar con agua, pontelo"
             f"\n\n{emoji.emojize(':crown:')} Cabeza: gorro con orejeras."
             f"\n{emoji.emojize(':scarf:')} Cuello: bufanda (caliente)."
             f"\n{emoji.emojize(':coat:')} Torso: camiseta, suéter de lana, abrigo cálido de piel de oveja."
             f"\n{emoji.emojize(':gloves:')} Manos: cualquier guante caliente."
             f"\n{emoji.emojize(':jeans:')} Cintura: calzoncillos cálidos, pantalones."
             f"\n{emoji.emojize(':hiking_boot:')} Piernas: calcetines de lana, botas de fieltro.",
             ]],


    "0": [[f"{emoji.emojize(':scroll:')} Морозная погодка, человек, ты уверен что хочешь гулять? "
           "Хотя кого я спрашиваю..."
           "\nНадевай на "
           f"\n\n{emoji.emojize(':crown:')} Голову: шапку."
           f"\n{emoji.emojize(':scarf:')} Шею: тёплый шарфик."
           f"\n{emoji.emojize(':coat:')} Торс: майку, блузку, шубу или пальто."
           f"\n{emoji.emojize(':gloves:')} Руки: зимние кожаные перчатки."
           f"\n{emoji.emojize(':jeans:')} Талию: тёплые колготы, брюки."
           f"\n{emoji.emojize(':hiking_boot:')} Ноги: тёплые носки, ботинки.",

           f"{emoji.emojize(':scroll:')} It's freezing, human, are you sure you want to go out?"
           "Though who am I to ask..."
           "\nPut on "
           f"\n\n{emoji.emojize(':crown:')} Head: warm hat."
           f"\n{emoji.emojize(':scarf:')} Neck: warm scarf."
           f"\n{emoji.emojize(':coat:')} Torso: T-shirt, blouse, fur coat or coat."
           f"\n{emoji.emojize(':gloves:')} Hands: Winter leather gloves."
           f"\n{emoji.emojize(':jeans:')} Waist: warm tights, trousers."
           f"\n{emoji.emojize(':hiking_boot:')} Legs: warm socks, boots.",

           f"{emoji.emojize(':scroll:')} Морозна погода, людина, ти впевнений, що хочеш гуляти?"
           "Хоча кого я питаю..."
           "\nВдягай на "
           f"\n\n{emoji.emojize(':crown:')} Голову: шапку."
           f"\n{emoji.emojize(':scarf:')} Шию: теплий шарфик."
           f"\n{emoji.emojize(':coat:')} Торс: майку, блузку, шубу або пальто."
           f"\n{emoji.emojize(':gloves:')} Руки: зимові шкіряні рукавички."
           f"\n{emoji.emojize(':jeans:')} Талію: теплі колготи, штани."
           f"\n{emoji.emojize(':hiking_boot:')} Ноги: теплі шкарпетки, черевики.",

           f"{emoji.emojize(':scroll:')} Es ist eiskalt, Mann, willst du wirklich ausgehen?"
           "Aber wen soll ich fragen..."
           "\nAnziehen"
           f"\n\n{emoji.emojize(':crown:')} Kopf: Hut."
           f"\n{emoji.emojize(':scarf:')} Hals: warmer Schal."
           f"\n{emoji.emojize(':coat:')} Oberkörper: T-Shirt, Bluse, Pelzmantel oder Mantel."
           f"\n{emoji.emojize(':gloves:')} Hände: Winterlederhandschuhe."
           f"\n{emoji.emojize(':jeans:')} Taille: warme Strumpfhose, Hose."
           f"\n{emoji.emojize(':hiking_boot:')} Beine: warme Socken, Stiefel.",

           f"{emoji.emojize(':scroll:')} 好冷，伙計，你確定要出去嗎  ?"
           "雖然我要問誰..."
           "\n穿上"
           f"\n\n{emoji.emojize(':crown:')} 頭：帽子。"
           f"\n{emoji.emojize(':scarf:')} 脖子：溫暖的圍巾。"
           f"\n{emoji.emojize(':coat:')} 軀幹：T 卹、襯衫、毛皮大衣或大衣。"
           f"\n{emoji.emojize(':gloves:')} 手：冬季皮手套。"
           f"\n{emoji.emojize(':jeans:')} 腰部：保暖緊身衣、長褲。"
           f"\n{emoji.emojize(':hiking_boot:')} 腿：保暖襪、靴子。",

           f"{emoji.emojize(':scroll:')} Hace mucho frío, tío, ¿estás seguro de que quieres salir?"
           "Aunque quién soy yo para preguntar..."
           "\nPonte"
           f"\n\n{emoji.emojize(':crown:')} Cabeza: gorro."
           f"\n{emoji.emojize(':scarf:')} Cuello: cálida bufanda."
           f"\n{emoji.emojize(':coat:')} Torso: camiseta, blusa, abrigo de piel o abrigo."
           f"\n{emoji.emojize(':gloves:')} Manos: Guantes de cuero de invierno."
           f"\n{emoji.emojize(':jeans:')} Cintura: medias cálidas, pantalones."
           f"\n{emoji.emojize(':hiking_boot:')} Piernas: calcetines cálidos, botas.",
           ],



          [f"{emoji.emojize(':scroll:')} Морозная погодка, человек, ты уверен что хочешь гулять? "
           "Хотя кого я спрашиваю..."
           "\nНадевай на "
           f"\n\n{emoji.emojize(':crown:')} Голову: шапку."
           f"\n{emoji.emojize(':scarf:')} Шею: тёплый шарфик."
           f"\n{emoji.emojize(':coat:')} Торс: футболку, шерстяной свитер, стёганную куртку."
           f"\n{emoji.emojize(':gloves:')} Руки: зимние кожаные перчатки."
           f"\n{emoji.emojize(':jeans:')} Талию: тёплые подштанники, брюки."
           f"\n{emoji.emojize(':hiking_boot:')} Ноги: тёплые носки, ботинки.",

           f"{emoji.emojize(':scroll:')} It's freezing, human, are you sure you want to go out?"
           "Though who am I to ask..."
           "\nPut on "
           f"\n\n{emoji.emojize(':crown:')} Head: warm hat."
           f"\n{emoji.emojize(':scarf:')} Neck: warm scarf."
           f"\n{emoji.emojize(':coat:')} Torso: T-shirt, wool sweater, quilted jacket."
           f"\n{emoji.emojize(':gloves:')} Hands: Winter leather gloves."
           f"\n{emoji.emojize(':jeans:')} Waist: warm underpants, trousers."
           f"\n{emoji.emojize(':hiking_boot:')} Legs: warm socks, boots.",

           f"{emoji.emojize(':scroll:')} Морозна погода, людина, ти впевнений, що хочеш гуляти?"
           "Хоча кого я питаю..."
           "\nВдягай на "
           f"\n\n{emoji.emojize(':crown:')} Голову: шапку."
           f"\n{emoji.emojize(':scarf:')} Шию: теплий шарфик."
           f"\n{emoji.emojize(':coat:')} Торс: футболку, вовняний светр, стьобану куртку."
           f"\n{emoji.emojize(':gloves:')} Руки: зимові шкіряні рукавички."
           f"\n{emoji.emojize(':jeans:')} Талію: теплі підштанники, штани."
           f"\n{emoji.emojize(':hiking_boot:')} Ноги: теплі шкарпетки, черевики.",

           f"{emoji.emojize(':scroll:')} Es ist eiskalt, Mann, willst du wirklich ausgehen?"
           "Aber wen soll ich fragen..."
           "\nAnziehen"
           f"\n\n{emoji.emojize(':crown:')} Kopf: Hut."
           f"\n{emoji.emojize(':scarf:')} Hals: warmer Schal."
           f"\n{emoji.emojize(':coat:')} Oberkörper: T-Shirt, Wollpullover, Steppjacke."
           f"\n{emoji.emojize(':gloves:')} Hände: Winterlederhandschuhe."
           f"\n{emoji.emojize(':jeans:')} Taille: warme Unterhose, Hose."
           f"\n{emoji.emojize(':hiking_boot:')} Beine: warme Socken, Stiefel.",

           f"{emoji.emojize(':scroll:')} 好冷，伙計，你確定要出去嗎?"
           "雖然我要問誰..."
           "\n穿上"
           f"\n\n{emoji.emojize(':crown:')} 頭：帽子。"
           f"\n{emoji.emojize(':scarf:')} 脖子：溫暖的圍巾。"
           f"\n{emoji.emojize(':coat:')} 軀幹：T 卹、羊毛衫、絎縫夾克。"
           f"\n{emoji.emojize(':gloves:')} 手：冬季皮手套。"
           f"\n{emoji.emojize(':jeans:')} 腰部：保暖內褲、長褲。"
           f"\n{emoji.emojize(':hiking_boot:')} 腿：保暖襪、靴子。",

           f"{emoji.emojize(':scroll:')} Hace mucho frío, tío, ¿estás seguro de que quieres salir?"
           "Aunque quién soy yo para preguntar..."
           "\nPonte"
           f"\n\n{emoji.emojize(':crown:')} Cabeza: gorro."
           f"\n{emoji.emojize(':scarf:')} Cuello: cálida bufanda."
           f"\n{emoji.emojize(':coat:')} Torso: camiseta, jersey de lana, chaqueta acolchada."
           f"\n{emoji.emojize(':gloves:')} Manos: Guantes de cuero de invierno."
           f"\n{emoji.emojize(':jeans:')} Cintura: calzoncillos cálidos, pantalones."
           f"\n{emoji.emojize(':hiking_boot:')} Piernas: calcetines cálidos, botas.",
           ]],


    "10": [[f"{emoji.emojize(':scroll:')} Холодновато у вас тут, был бы на твоем месте, то надел на"
            f"\n\n{emoji.emojize(':crown:')} Голову: шапку."
            f"\n{emoji.emojize(':coat:')} Торс: блузку, лёгкий свитер, курточку."
            f"\n{emoji.emojize(':jeans:')} Талию: лёгкие колготы, джинсы."
            f"\n{emoji.emojize(':hiking_boot:')} Ноги: носки, кроссовки.",

            f"{emoji.emojize(':scroll:')} It's a bit cold here, if I were you, I'd put it on"
            f"\n\n{emoji.emojize(':crown:')} Head: hat."
            f"\n{emoji.emojize(':coat:')} Torso: blouse, light sweater, jacket."
            f"\n{emoji.emojize(':jeans:')} Waist: light tights, jeans."
            f"\n{emoji.emojize(':hiking_boot:')} Legs: socks, sneakers.",

            f"{emoji.emojize(':scroll:')} Холодно у вас тут, був би на твоєму місці, то надів на"
            f"\n\n{emoji.emojize(':crown:')} Голову: шапку."
            f"\n{emoji.emojize(':coat:')} Торс: блузку, легкий светр, курточку."
            f"\n{emoji.emojize(':jeans:')} Талію: легкі колготи, джинси."
            f"\n{emoji.emojize(':hiking_boot:')} Ноги: шкарпетки, кросівки.",

            f"{emoji.emojize(':scroll:')} Es ist ein bisschen kalt hier, wenn ich du wäre, würde ich es anziehen"
            f"\n\n{emoji.emojize(':crown:')} Kopf: Hut."
            f"\n{emoji.emojize(':coat:')} Oberkörper: Bluse, leichter Pullover, Jacke."
            f"\n{emoji.emojize(':jeans:')} Taille: leichte Strumpfhose, Jeans."
            f"\n{emoji.emojize(':hiking_boot:')} Beine: Socken, Turnschuhe.",

            f"{emoji.emojize(':scroll:')}這裡有點冷，如果我是你，我會穿上它"
            f"\n\n{emoji.emojize(':crown:')} 頭：帽子。"
            f"\n{emoji.emojize(':coat:')} 軀幹：襯衫、薄毛衣、夾克。"
            f"\n{emoji.emojize(':jeans:')} 腰圍：緊身褲，牛仔褲。"
            f"\n{emoji.emojize(':hiking_boot:')} 腿：襪子、運動鞋。",

            f"{emoji.emojize(':scroll:')} Aquí hace un poco de frío, yo en tu lugar me lo pondría"
            f"\n\n{emoji.emojize(':crown:')} Cabeza: gorro."
            f"\n{emoji.emojize(':coat:')} Torso: blusa, suéter ligero, chaqueta."
            f"\n{emoji.emojize(':jeans:')} Cintura: medias ligeras, jeans."
            f"\n{emoji.emojize(':hiking_boot:')} Piernas: calcetines, tenis.",
            ],



           [f"{emoji.emojize(':scroll:')} Холодновато у вас тут, был бы на твоем месте, то надел на"
            f"\n\n{emoji.emojize(':crown:')} Голову: шапку."
            f"\n{emoji.emojize(':coat:')} Торс: футболку, лёгкий свитер, курточку."
            f"\n{emoji.emojize(':jeans:')} Талию: лёгкие подштанники, брюки."
            f"\n{emoji.emojize(':hiking_boot:')} Ноги: носки, кроссовки.",

            f"{emoji.emojize(':scroll:')} It's a bit cold here, if I were you, I'd put it on"
            f"\n\n{emoji.emojize(':crown:')} Head: hat."
            f"\n{emoji.emojize(':coat:')} Torso: T-shirt, light sweater, jacket."
            f"\n{emoji.emojize(':jeans:')} Waist: light underpants, trousers."
            f"\n{emoji.emojize(':hiking_boot:')} Legs: socks, sneakers.",

            f"{emoji.emojize(':scroll:')} Холодно у вас тут, був би на твоєму місці, то надів на"
            f"\n\n{emoji.emojize(':crown:')} Голову: шапку."
            f"\n{emoji.emojize(':coat:')} Торс: футболку, легкий светр, курточку."
            f"\n{emoji.emojize(':jeans:')} Талію: легкі підштанники, штани."
            f"\n{emoji.emojize(':hiking_boot:')} Ноги: шкарпетки, кросівки.",

            f"{emoji.emojize(':scroll:')} Es ist ein bisschen kalt hier, wenn ich du wäre, würde ich es anziehen"
            f"\n\n{emoji.emojize(':crown:')} Kopf: Hut."
            f"\n{emoji.emojize(':coat:')} Oberkörper: T-Shirt, leichter Pullover, Jacke."
            f"\n{emoji.emojize(':jeans:')} Taille: leichte Unterhose, Hose."
            f"\n{emoji.emojize(':hiking_boot:')} Beine: Socken, Turnschuhe.",

            f"{emoji.emojize(':scroll:')}這裡有點冷，如果我是你，我會穿上它"
            f"\n\n{emoji.emojize(':crown:')} 頭：帽子。"
            f"\n{emoji.emojize(':coat:')} 軀幹：T 卹、輕便毛衣、夾克。"
            f"\n{emoji.emojize(':jeans:')} 腰：輕內褲、長褲。"
            f"\n{emoji.emojize(':hiking_boot:')} 腿：襪子、運動鞋。",

            f"{emoji.emojize(':scroll:')} Aquí hace un poco de frío, yo en tu lugar me lo pondría"
            f"\n\n{emoji.emojize(':crown:')} Cabeza: gorro."
            f"\n{emoji.emojize(':coat:')} Torso: camiseta, suéter ligero, chaqueta."
            f"\n{emoji.emojize(':jeans:')} Cintura: calzoncillos ligeros, pantalones."
            f"\n{emoji.emojize(':hiking_boot:')} Piernas: calcetines, tenis.",
            ]],


    "17": [[f"{emoji.emojize(':scroll:')} Прохладненько нынче на улице, был бы я твоей робомамой, "
            "то сказал бы надеть на"
            f"\n\n{emoji.emojize(':coat:')} Торс: блузку-футболку, кофту, куртку."
            f"\n{emoji.emojize(':jeans:')} Талию: джинсы или брюки (по желанию лёгкие колготы)."
            f"\n{emoji.emojize(':hiking_boot:')} Ноги: носки, кроссовки.",

            f"{emoji.emojize(':scroll:')} It's cool outside today, if I were your robot mom, "
            "I would say put on"
            f"\n\n{emoji.emojize(':coat:')} Torso: T-shirt blouse, blouse, jacket."
            f"\n{emoji.emojize(':jeans:')} Waistline: jeans or trousers (optional light tights)."
            f"\n{emoji.emojize(':hiking_boot:')} Legs: socks, sneakers.",

            f"{emoji.emojize(':scroll:')} Прохолодно нині на вулиці, був би я твоєю робомамою, "
            "то сказав би надіти на"
            f"\n\n{emoji.emojize(':coat:')} Торс: блузку-футболку, кофту, куртку."
            f"\n{emoji.emojize(':jeans:')} Талію: джинси або штани (за бажанням легкі колготи)."
            f"\n{emoji.emojize(':hiking_boot:')} Ноги: шкарпетки, кросівки.",

            f"{emoji.emojize(':scroll:')} Es ist heute cool draußen, wenn ich deine Robotermama wäre, "
            "Ich würde sagen anziehen"
            f"\n\n{emoji.emojize(':coat:')} Oberkörper: T-Shirt-Bluse, Bluse, Jacke."
            f"\n{emoji.emojize(':jeans:')} Taille: Jeans oder Hose (optional leichte Strumpfhose)."
            f"\n{emoji.emojize(':hiking_boot:')} Beine: Socken, Turnschuhe.",

            f"{emoji.emojize(':scroll:')} 今天外面很酷，如果我是你的機器人媽媽，"
            "我會說穿上"
            f"\n\n{emoji.emojize(':coat:')} 軀幹：T 恤衫、襯衫、夾克。"
            f"\n{emoji.emojize(':jeans:')} 腰圍：牛仔褲或長褲（可選輕便緊身衣）。"
            f"\n{emoji.emojize(':hiking_boot:')} 腿：襪子、運動鞋。",

            f"{emoji.emojize(':scroll:')} Hoy hace buen tiempo afuera, si yo fuera tu mamá robot, "
            "Yo diría que se ponga"
            f"\n\n{emoji.emojize(':coat:')} Torso: Camiseta blusa, blusa, chaqueta."
            f"\n{emoji.emojize(':jeans:')} Cintura: jeans o pantalones (medias ligeras opcionales)."
            f"\n{emoji.emojize(':hiking_boot:')} Piernas: calcetines, tenis.",
            ],



           [f"{emoji.emojize(':scroll:')} Прохладненько нынче на улице, был бы я твоей робомамой, "
            "то сказал бы надеть на"
            f"\n\n{emoji.emojize(':coat:')} Торс: футболку, по желанию лёгкий свитер, куртку."
            f"\n{emoji.emojize(':jeans:')} Талию: джинсы или брюки (по желанию лёгкие подштанники)."
            f"\n{emoji.emojize(':hiking_boot:')} Ноги: носки, кроссовки.",

            f"{emoji.emojize(':scroll:')} It's cool outside today, if I were your robot mom, "
            "I would say put on"
            f"\n\n{emoji.emojize(':coat:')} Torso: t-shirt, optional light sweater, jacket."
            f"\n{emoji.emojize(':jeans:')} Waistline: Jeans or trousers (optional light underpants)."
            f"\n{emoji.emojize(':hiking_boot:')} Legs: socks, sneakers.",

            f"{emoji.emojize(':scroll:')} Прохолодно нині на вулиці, був би я твоєю робомамою, "
            "то сказав би надіти на"
            f"\n\n{emoji.emojize(':coat:')} Торс: футболку, за бажанням легкий светр, куртку."
            f"\n{emoji.emojize(':jeans:')} Талію: джинси або штани (за бажанням легкі підштанники)."
            f"\n{emoji.emojize(':hiking_boot:')} Ноги: шкарпетки, кросівки.",

            f"{emoji.emojize(':scroll:')} Es ist heute cool draußen, wenn ich deine Robotermama wäre, "
            "Ich würde sagen anziehen"
            f"\n\n{emoji.emojize(':coat:')} Oberkörper: T-Shirt-Bluse, Bluse, Jacke."
            f"\n{emoji.emojize(':jeans:')} Taille: Jeans oder Hose (optional leichte Strumpfhose)."
            f"\n{emoji.emojize(':hiking_boot:')} Beine: Socken, Turnschuhe.",

            f"{emoji.emojize(':scroll:')} 今天外面很酷，如果我是你的機器人媽媽，"
            "我會說穿上"
            f"\n\n{emoji.emojize(':coat:')} 軀幹：T 卹，可選輕便毛衣，夾克。"
            f"\n{emoji.emojize(':jeans:')} 腰圍：牛仔褲或長褲（可選淺色內褲）。"
            f"\n{emoji.emojize(':hiking_boot:')} 腿：襪子、運動鞋。",

            f"{emoji.emojize(':scroll:')} Hoy hace buen tiempo afuera, si yo fuera tu mamá robot, "
            "Yo diría que se ponga"
            f"\n\n{emoji.emojize(':coat:')} Torso: camiseta, suéter ligero opcional, chaqueta."
            f"\n{emoji.emojize(':jeans:')} Cintura: Jeans o pantalones (calzoncillos ligeros opcionales)."
            f"\n{emoji.emojize(':hiking_boot:')} Piernas: calcetines, tenis.",
            ]],


    "23": [[f"{emoji.emojize(':scroll:')} Замечательная температура, можно и в робобол сыграть, надевай на"
            f"\n\n{emoji.emojize(':coat:')} Торс: блузку, спортивную курточку."
            f"\n{emoji.emojize(':jeans:')} Талию: джинсы или юбку."
            f"\n{emoji.emojize(':hiking_boot:')} Ноги: носки, кеды (любую другую лёгкую обувь).",

            f"{emoji.emojize(':scroll:')} Great temperature, you can play roboball, put it on"
            f"\n\n{emoji.emojize(':coat:')} Torso: blouse, blazer."
            f"\n{emoji.emojize(':jeans:')} Waist: jeans or skirt."
            f"\n{emoji.emojize(':hiking_boot:')} Feet: socks, sneakers (any other light footwear).",

            f"{emoji.emojize(':scroll:')} Чудова температура, можна і в робобол зіграти, одягай на"
            f"\n\n{emoji.emojize(':coat:')} Торс: блузку, спортивну курточку."
            f"\n{emoji.emojize(':jeans:')} Талію: джинси або спідницю."
            f"\n{emoji.emojize(':hiking_boot:')} Ноги: шкарпетки, кеди (будь-яке інше легке взуття).",

            f"{emoji.emojize(':scroll:')} Tolle Temperatur, du kannst Roboball spielen, zieh es an"
            f"\n\n{emoji.emojize(':coat:')} Torso: Bluse, Blazer."
            f"\n{emoji.emojize(':jeans:')} Taille: Jeans oder Rock."
            f"\n{emoji.emojize(':hiking_boot:')} Füße: Socken, Turnschuhe (alle anderen leichten Schuhe).",

            f"{emoji.emojize(':scroll:')} 溫度很好，可以玩機器球，放上去吧"
            f"\n\n{emoji.emojize(':coat:')} 軀幹：襯衫、西裝外套。"
            f"\n{emoji.emojize(':jeans:')} 腰圍：牛仔褲或裙子。"
            f"\n{emoji.emojize(':hiking_boot:')} 腿：襪子、運動鞋（任何其他輕便的鞋類）。",

            f"{emoji.emojize(':scroll:')} Gran temperatura, puedes jugar roboball, póntelo"
            f"\n\n{emoji.emojize(':coat:')} Torso: blusa, blazer."
            f"\n{emoji.emojize(':jeans:')} Cintura: jeans o falda."
            f"\n{emoji.emojize(':hiking_boot:')} Piernas: calcetines, zapatillas (cualquier otro calzado ligero).",
            ],



           [f"{emoji.emojize(':scroll:')} Замечательная температура, можно и в робобол сыграть, надевай на"
            f"\n\n{emoji.emojize(':coat:')} Торс: майку, спортивную курточку."
            f"\n{emoji.emojize(':jeans:')} Талию: джинсы."
            f"\n{emoji.emojize(':hiking_boot:')} Ноги: носки, кеды (любую другую лёгкую обувь).",

            f"{emoji.emojize(':scroll:')} Great temperature, you can play roboball, put it on"
            f"\n\n{emoji.emojize(':coat:')} Torso: tank top, blazer."
            f"\n{emoji.emojize(':jeans:')} Waist: jeans."
            f"\n{emoji.emojize(':hiking_boot:')} Feet: socks, sneakers (any other light footwear).",

            f"{emoji.emojize(':scroll:')} Чудова температура, можна і в робобол зіграти, одягай на"
            f"\n\n{emoji.emojize(':coat:')} Торс: майку, спортивну курточку."
            f"\n{emoji.emojize(':jeans:')} Талію: джинси."
            f"\n{emoji.emojize(':hiking_boot:')} Ноги: шкарпетки, кеди (будь-яке інше легке взуття).",

            f"{emoji.emojize(':scroll:')} Tolle Temperatur, du kannst Roboball spielen, zieh es an"
            f"\n\n{emoji.emojize(':coat:')} Oberkörper: Tanktop, Blazer."
            f"\n{emoji.emojize(':jeans:')} Taille: Jeans."
            f"\n{emoji.emojize(':hiking_boot:')} Füße: Socken, Turnschuhe (alle anderen leichten Schuhe).",

            f"{emoji.emojize(':scroll:')} 溫度很好，可以玩機器球，放上去吧"
            f"\n\n{emoji.emojize(':coat:')} 軀幹：背心，西裝外套。"
            f"\n{emoji.emojize(':jeans:')} 腰圍：牛仔褲。"
            f"\n{emoji.emojize(':hiking_boot:')} 腿：襪子、運動鞋（任何其他輕便的鞋類）。",

            f"{emoji.emojize(':scroll:')} Gran temperatura, puedes jugar roboball, póntelo"
            f"\n\n{emoji.emojize(':coat:')} Torso: camiseta sin mangas, blazer."
            f"\n{emoji.emojize(':jeans:')} Cintura: jeans."
            f"\n{emoji.emojize(':hiking_boot:')} Piernas: calcetines, zapatillas (cualquier otro calzado ligero).",
            ]],


    "23+": [[f"{emoji.emojize(':scroll:')} Слушай такую жару даже мой радиатор не выдерживает, сказал бы идти "
             "в трусах, но где мои робоманеры, надевай на"
             f"\n\n{emoji.emojize(':crown:')} Голову: модные очки (по желанию)"
             f"\n{emoji.emojize(':coat:')} Торс: топик или тонкую футболку. "
             f"\n{emoji.emojize(':jeans:')} Талию: юбку."
             f"\n{emoji.emojize(':hiking_boot:')} Ноги: любую свободную для ног обувь.",

             f"{emoji.emojize(':scroll:')} Listen to this heat, even my radiator can't stand it, I'd say go"
             "in shorts, but where are my robomanners, put them on"
             f"\n\n{emoji.emojize(':crown:')} Head: fancy glasses (optional)"
             f"\n{emoji.emojize(':coat:')} Torso: Top or thin T-shirt. "
             f"\n{emoji.emojize(':jeans:')} Waist: skirt."
             f"\n{emoji.emojize(':hiking_boot:')} Legs: any loose footwear.",

             f"{emoji.emojize(':scroll:')} Слухай таку спеку навіть мій радіатор не витримує, сказав би йти"
             "в трусах, але де мої робоманери, одягай на"
             f"\n\n{emoji.emojize(':crown:')} Голову: модні окуляри (за бажанням)"
             f"\n{emoji.emojize(':coat:')} Торс: топік або тонку футболку."
             f"\n{emoji.emojize(':jeans:')} Талію: спідницю."
             f"\n{emoji.emojize(':hiking_boot:')} Ноги: будь-яке вільне для ніг взуття.",

             f"{emoji.emojize(':scroll:')} Hör dir diese Hitze an, selbst mein Heizkörper "
             "hält es nicht aus, ich würde sagen, geh "
             "in Shorts, aber wo sind meine Robomanners, zieh sie an"
             f"\n\n{emoji.emojize(':crown:')} Kopf: ausgefallene Brille (optional)"
             f"\n{emoji.emojize(':coat:')} Oberkörper: Top oder dünnes T-Shirt. "
             f"\n{emoji.emojize(':jeans:')} Taille: Rock."
             f"\n{emoji.emojize(':hiking_boot:')} Beine: jedes lockere Schuhwerk.",

             f"{emoji.emojize(':scroll:')} 聽這熱，連我的散熱器都受不了，我說去吧"
             "簡而言之，但是我的機器人在哪裡，穿上它們"
             f"\n\n{emoji.emojize(':crown:')} 頭：花式眼鏡（可選）"
             f"\n{emoji.emojize(':coat:')} 軀幹：上衣或薄T卹。"
             f"\n{emoji.emojize(':jeans:')} 腰圍：裙子。"
             f"\n{emoji.emojize(':hiking_boot:')} 腿：任何寬鬆的鞋子。",

             f"{emoji.emojize(':scroll:')} Escucha este calor, ni siquiera mi radiador lo soporta, yo diría que vayas"
             "en pantalones cortos, pero ¿dónde están mis robomodales, póntelos"
             f"\n\n{emoji.emojize(':crown:')} Cabeza: lentes elegantes (opcional)"
             f"\n{emoji.emojize(':coat:')} Torso: Top o camiseta fina. "
             f"\n{emoji.emojize(':jeans:')} Cintura: falda."
             f"\n{emoji.emojize(':hiking_boot:')} Piernas: cualquier calzado suelto.",
             ],



            [f"{emoji.emojize(':scroll:')} Слушай такую жару даже мой радиатор не выдерживает, сказал бы идти "
             "в трусах, но где мои робоманеры, надевай на"
             f"\n\n{emoji.emojize(':crown:')} Голову: модные очки (по желанию)"
             f"\n{emoji.emojize(':coat:')} Торс: майку. "
             f"\n{emoji.emojize(':jeans:')} Талию: шорты."
             f"\n{emoji.emojize(':hiking_boot:')} Ноги: любую свободную для ног обувь.",

             f"{emoji.emojize(':scroll:')} Listen to this heat, even my radiator can't stand it, I'd say go"
             "in shorts, but where are my robomanners, put them on"
             f"\n\n{emoji.emojize(':crown:')} Head: fancy glasses (optional)"
             f"\n{emoji.emojize(':coat:')} Torso: T-shirt. "
             f"\n{emoji.emojize(':jeans:')} Waist: shorts."
             f"\n{emoji.emojize(':hiking_boot:')} Feet: any loose shoes for feet.",

             f"{emoji.emojize(':scroll:')} Слухай таку спеку навіть мій радіатор не витримує, сказав би йти"
             "в трусах, але де мої робоманери, одягай на"
             f"\n\n{emoji.emojize(':crown:')} Голову: модні окуляри (за бажанням)"
             f"\n{emoji.emojize(':coat:')} Торс: майку."
             f"\n{emoji.emojize(':jeans:')} Талію: шорти."
             f"\n{emoji.emojize(':hiking_boot:')} Ноги: будь-яке вільне для ніг взуття.",

             f"{emoji.emojize(':scroll:')} Hör dir diese Hitze an, selbst mein "
             "Heizkörper hält es nicht aus, ich würde sagen, geh "
             "in Shorts, aber wo sind meine Robomanners, zieh sie an"
             f"\n\n{emoji.emojize(':crown:')} Kopf: ausgefallene Brille (optional)"
             f"\n{emoji.emojize(':coat:')} Oberkörper: T-Shirt. "
             f"\n{emoji.emojize(':jeans:')} Taille: Shorts."
             f"\n{emoji.emojize(':hiking_boot:')} Beine: jedes lockere Schuhwerk.",

             f"{emoji.emojize(':scroll:')} 聽這熱，連我的散熱器都受不了，我說去吧"
             "簡而言之，但是我的機器人在哪裡，穿上它們"
             f"\n\n{emoji.emojize(':crown:')} 頭：花式眼鏡（可選）"
             f"\n{emoji.emojize(':coat:')} 軀幹：T 卹。"
             f"\n{emoji.emojize(':jeans:')} 腰圍：短褲。"
             f"\n{emoji.emojize(':hiking_boot:')} 腿：任何寬鬆的鞋子。",

             f"{emoji.emojize(':scroll:')} Escucha este calor, ni siquiera mi radiador lo soporta, yo diría que vayas"
             "en pantalones cortos, pero ¿dónde están mis robomodales, póntelos"
             f"\n\n{emoji.emojize(':crown:')} Cabeza: lentes elegantes (opcional)"
             f"\n{emoji.emojize(':coat:')} Torso: Camiseta. "
             f"\n{emoji.emojize(':jeans:')} Cintura: shorts."
             f"\n{emoji.emojize(':hiking_boot:')} Piernas: cualquier calzado suelto.",
             ]],
}