from utils.functions.send_msg import send_msg

def welcome_msg(msg):
    chat_id = msg.chat.id
    send_msg(chat_id, f"Welcome {msg.from_user.first_name}")
