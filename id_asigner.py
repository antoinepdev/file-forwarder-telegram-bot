from bot_config import bot, storage_id, bot_link
from database.save_id import save_id


@bot.message_handler(content_types=["video"])
def id_asigner(msg):
    chat_id = msg.chat.id
    if chat_id != storage_id:
        return
    if save_id(msg.message_id):
        message = f"{bot_link}?start={msg.message_id}"
        bot.send_message(
            storage_id,
            f"```{message}```",
            parse_mode="MarkdownV2"
        )
