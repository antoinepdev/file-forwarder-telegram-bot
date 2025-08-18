from telebot import TeleBot
from dotenv import load_dotenv
from os import getenv

env_file = ".env"
load_dotenv(env_file)
bot_token = getenv("BOT_TOKEN")
storage_id_str = getenv("STORAGE_ID")
bot_link = getenv("BOT_LINK")



def env_error(varname):
    raise Exception(f"{varname} not provaided. Please add {varname} variable into your {env_file} file")

if bot_token == None:
    env_error("BOT_TOKEN")
if storage_id_str == None:
    env_error("STORAGE_ID")
if bot_link == None:
    env_error("BOT_LINK")



storage_id = int(storage_id_str) #type: ignore
bot = TeleBot(bot_token) #type: ignore
