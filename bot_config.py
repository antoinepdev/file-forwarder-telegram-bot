from telebot import TeleBot
from dotenv import load_dotenv
from os import getenv

load_dotenv(".env.dev")
bot_token = getenv("BOT_TOKEN")
storage_id = int(getenv("STORAGE_ID"))
bot_link = getenv("BOT_LINK")

bot = TeleBot(bot_token)
