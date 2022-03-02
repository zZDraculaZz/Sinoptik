import os

import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

from config import my_db
from texts import CONSOLE_TEXT


# Функция которая будет проверять наличие базы данных, её таблиц. На выход дает конекшен к базе данных.
def create_db():
    # print()
    # print(CONSOLE_TEXT["search_db_dir"])
    #
    # if os.path.exists("database"):
    #     print(CONSOLE_TEXT["db_dir_found"])
    #
    # else:
    #     print(CONSOLE_TEXT["db_dir_not_found"])
    #     os.mkdir("database")
    #     print(CONSOLE_TEXT["db_dir_created"])

    # Поиск базы данных
    print()
    print(CONSOLE_TEXT["search_db"])

    try:
        connection = psycopg2.connect(dbname=my_db.db_name, user=my_db.db_user,
                                      password=my_db.db_password, host=my_db.db_host)
        print(CONSOLE_TEXT["db_found"])

    except:
        print(CONSOLE_TEXT["db_not_found"])

        connection = psycopg2.connect(user=my_db.db_user, password=my_db.db_password, host=my_db.db_host)
        connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cursor = connection.cursor()
        cursor.execute(f"create database {my_db.db_name};")
        cursor.close()

        print(CONSOLE_TEXT["db_created"])
    connection.close()

    # Поиск таблицы с пользователями
    print()
    print(CONSOLE_TEXT["check_tables"])
    connection = psycopg2.connect(dbname=my_db.db_name, user=my_db.db_user,
                                  password=my_db.db_password, host=my_db.db_host)
    cursor = connection.cursor()

    # проверка таблиц на наличие,если нету то создаст
    cursor.execute("create table if not exists bot_users(id serial primary key, chat_id varchar(255), "
                   "user_name varchar(255), gender varchar(255), language varchar(255));")

    cursor.execute("create table if not exists coordinates(id serial primary key, chat_id varchar(255),"
                   "lat varchar(255), lon varchar(255));")

    cursor.execute("create table if not exists weathers(id serial primary key, chat_id varchar(255),"
                   "request_day varchar(255), temperatures varchar(255), precipitation varchar(255),"
                   "humidity varchar(255), wind_speed varchar(255), timezone integer, selected_day integer);")

    print(CONSOLE_TEXT["check_tables_completed"])

    connection.commit()
    cursor.close()
    connection.close()

    conn = psycopg2.connect(dbname=my_db.db_name, user=my_db.db_user,
                            password=my_db.db_password, host=my_db.db_host)

    return conn


conn = create_db()


def cursor_on():
    cursor = conn.cursor()
    return cursor


def cursor_off(cursor):
    conn.commit()
    cursor.close()
