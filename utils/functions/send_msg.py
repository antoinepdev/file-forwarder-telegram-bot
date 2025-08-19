from bot_config import bot

def send_msg(to, msg):
    try:
        bot.send_message(to, msg)
    except Exception as e:
        print(e)
