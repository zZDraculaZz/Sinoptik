# функции поиска базы с локациями, если нету базы - создаст
import os

import openpyxl
import xlrd3

from config import base_location


def search_directory_database():
    if os.path.exists("database"):
        print("Папка с базами данных обнаружена")

    else:
        print("Папка с базами данных не обнаружена...Создание")
        os.mkdir("database")
        print("Папка \"database\" успешно создана")


def search_database_location():
    try:
        wb = xlrd3.open_workbook(base_location)
        print("База данных с локациями пользователей обнаружена")

    except FileNotFoundError:
        print("База данных с локациями пользователей не обнаружена...Создание")
        filepath = base_location
        wb = openpyxl.Workbook()
        wb.save(filepath)
        print("База данных \"save_location.xlsx\" успешно создана ")