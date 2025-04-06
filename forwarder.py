from bot_config import bot, storage_id
from utils.functions.get_id import get_id
from database.find_id import find_id


@bot.message_handler(commands=["start"])
def start(msg):
    chat_id = msg.chat.id
    if msg.chat.type != "private":
        return
    recived_id = get_id(msg.text)
    if recived_id is None:
        bot.send_message(chat_id, "Enlace incorrecto")
        return
    id_on_database = find_id(recived_id)
    if not id_on_database:
        bot.send_message(
            chat_id, "Archivo no encontrado, informa al admin del grupo")
        return
    try:
        bot.copy_message(chat_id, storage_id, recived_id)
    except Exception as e:
        print(f"Ha ocurrido un error al intentar reenviar el archivo: {e}")
