from db_connection import cursor_on, cursor_off


chat_id = "5011791486"
selected_day = 3

cursor = cursor_on()
cursor.execute("select * from bot_users")
language = cursor.fetchall()
print(language)
cursor_off(cursor)
1645534800
1645444800
1645873200
1645531200