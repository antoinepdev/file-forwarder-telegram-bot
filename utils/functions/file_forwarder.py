from bot_config import bot, storage_id
from utils.functions.get_file_id import get_file_id
from utils.functions.send_msg import send_msg

def file_forwarder(msg):
    chat_id = msg.chat.id

    recived_file_id = get_file_id(msg.text)
    if recived_file_id is None:
        send_msg(chat_id, "Enlace incorrecto") 
        return

    try:
        bot.copy_message(chat_id, storage_id, recived_file_id)
    except Exception as e:
        if "A request to the Telegram API was unsuccessful. Error code: 400. Description: Bad Request: message to copy not found" in str(e):
            send_msg(chat_id, "Lo siento, no existe el archivo al que el enlace apunta. Avisale al que te envió el enlace.")
            return
        print(f"Ha ocurrido un error al intentar reenviar el archivo: {e}")
