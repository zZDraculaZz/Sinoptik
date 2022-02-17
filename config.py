# Получаем данные из .env, что бы взаимодействовать с ними в дальнейшем
import os


from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, ".env"))

BOT_TOKEN = os.environ.get("BOT_TOKEN")
WEATHER_TOKEN = os.environ.get("WEATHER_TOKEN")

base_location = os.environ.get("base_location")


ADMINS_ID = os.environ.get("ADMINS_ID").split(", ")

server_timezone = int(os.environ.get("server_timezone"))


class my_db:
    db_name = os.environ.get("db_name")
    db_user = os.environ.get("db_user")
    db_password = os.environ.get("db_password")
    db_host = os.environ.get("db_host")