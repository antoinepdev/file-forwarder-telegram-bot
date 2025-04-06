import json

file_ids_path = "database/data/file_ids.json"


def find_id(recived_id):
    try:
        with open(file_ids_path, "r") as data:
            ids_list = json.load(data)
        if recived_id in ids_list:
            return True
    except Exception as e:
        print(f"Error al intentar buscar el id({recived_id} en la BD: {e})")
    return False
