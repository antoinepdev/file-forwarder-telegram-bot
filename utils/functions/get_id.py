def get_id(msg_text):
    try:
        file_id_str = msg_text.split(" ")[1]
        file_id = int(file_id_str)
    except Exception:
        return None
    return file_id
