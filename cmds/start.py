from bot_config import bot
from utils.validators.link_has_params import link_has_params
from utils.functions.welcome import welcome_msg
from utils.functions.file_forwarder import file_forwarder


@bot.message_handler(commands=["start"])
def start(msg):

    if msg.chat.type != "private":
        return



    if not link_has_params(msg.text): welcome_msg(msg)
    else: file_forwarder(msg)
