from bot_config import bot, env_file
import id_asigner
import forwarder

if __name__ == "__main__":
    if env_file == ".env": print("prod mode actived")
    else: print("dev mode actived")
    print("works...")
    bot.infinity_polling()
