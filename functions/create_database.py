# функции поиска базы с локациями, если нету базы - создаст
import os

import openpyxl
import xlrd3

from config import base_location
from texts import CONSOLE_TEXT


def search_directory_database():
    print()
    print(CONSOLE_TEXT["search_db_dir"])

    if os.path.exists("database"):
        print(CONSOLE_TEXT["db_dir_found"])

    else:
        print(CONSOLE_TEXT["db_dir_not_found"])
        os.mkdir("database")
        print(CONSOLE_TEXT["db_dir_created"])


def search_database_location():
    print()
    print(CONSOLE_TEXT["search_db_with_loc"])

    try:
        wb = xlrd3.open_workbook(base_location)
        print(CONSOLE_TEXT["db_with_loc_found"])

    except FileNotFoundError:
        print(CONSOLE_TEXT["db_with_loc_not_found"])
        filepath = base_location
        wb = openpyxl.Workbook()
        wb.save(filepath)
        print(CONSOLE_TEXT["db_with_loc_created"])