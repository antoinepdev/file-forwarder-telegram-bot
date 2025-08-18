from bot_config import bot, env_file



import storage_group.file_listener
import forwarder



if __name__ == "__main__":
    if env_file == ".env": print("prod mode actived")
    else: print("dev mode actived")
    print("works...")
    bot.infinity_polling()
