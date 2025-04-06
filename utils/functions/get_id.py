def get_id(msg_text):
    try:
        movie_id_str = msg_text.split(" ")[1]
        movie_id = int(movie_id_str)
    except Exception:
        return None
    return movie_id
