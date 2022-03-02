from db_connection import cursor_on, cursor_off


def amount_users():
    cursor = cursor_on()
    cursor.execute("select id from bot_users")
    count_users = str(len(cursor.fetchall()))
    cursor_off(cursor)
    return count_users


def amount_registered_users():
    cursor = cursor_on()
    cursor.execute("select id from coordinates")
    count_users = str(len(cursor.fetchall()))
    cursor_off(cursor)
    return count_users