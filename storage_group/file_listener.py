from bot_config import bot, storage_id, bot_link

@bot.message_handler(content_types=["video", "document"])
def link_creator(msg):
    chat_id = msg.chat.id
    if chat_id != storage_id:
        return
    message = f"{bot_link}?start={msg.message_id}"
    bot.send_message(
        storage_id,
        f"```{message}```",
        parse_mode="MarkdownV2"
    )
