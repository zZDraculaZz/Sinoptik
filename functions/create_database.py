import os

import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

from config import my_db
from texts import CONSOLE_TEXT


# Поиск директории с базой данных
def search_directory_database():
    print()
    print(CONSOLE_TEXT["search_db_dir"])

    if os.path.exists("database"):
        print(CONSOLE_TEXT["db_dir_found"])

    else:
        print(CONSOLE_TEXT["db_dir_not_found"])
        os.mkdir("database")
        print(CONSOLE_TEXT["db_dir_created"])


# Поиск базы данных
def search_database():
    print()
    print(CONSOLE_TEXT["search_db"])

    try:
        conn = psycopg2.connect(dbname=my_db.db_name, user=my_db.db_user,
                                password=my_db.db_password, host=my_db.db_host)
        print(CONSOLE_TEXT["db_found"])

    except:
        print(CONSOLE_TEXT["db_not_found"])

        conn = psycopg2.connect(user=my_db.db_user, password=my_db.db_password, host=my_db.db_host)
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

        with conn.cursor() as cursor:
            cursor.execute(f"create database {my_db.db_name};")

        print(CONSOLE_TEXT["db_created"])

    conn.close()


# Поиск таблицы с пользователями
def search_tables():
    print()
    print(CONSOLE_TEXT["check_tables"])
    conn = psycopg2.connect(dbname=my_db.db_name, user=my_db.db_user,
                            password=my_db.db_password, host=my_db.db_host)
    cursor=conn.cursor()

    # проверка таблиц на наличие,если нету то создаст
    cursor.execute("create table if not exists bot_users(id serial primary key, chat_id varchar(255), "
                   "user_name varchar(255));")

    cursor.execute("create table if not exists coordinates(id serial primary key, chat_id varchar(255),"
                   "lat varchar(255), lon varchar(255));")

    cursor.execute("create table if not exists weathers(id serial primary key, chat_id varchar(255),"
                   "request_day varchar(255), temperatures varchar(255), precipitation varchar(255), "
                   "timezone integer, selected_day integer);")

    print(CONSOLE_TEXT["check_tables_completed"])

    conn.commit()
    cursor.close()
    conn.close()
