# Ну тут даже мне понятно
import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, ".env"))

BOT_TOKEN = os.environ.get("BOT_TOKEN")
WEATHER_TOKEN = os.environ.get("WEATHER_TOKEN")

base_location = os.environ.get("base_location")
ADMINS_ID = os.environ.get("ADMINS_ID").split(", ")