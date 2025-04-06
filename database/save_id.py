import json
file_ids_path = "database/data/file_ids.json"


def save_id(recived_id):
    try:
        with open(file_ids_path, "r") as file:
            ids_list = json.load(file)
        ids_list.append(recived_id)

        with open(file_ids_path, "w") as file:
            json.dump(ids_list, file)
    except Exception as e:
        print(f"Ocurrió un error al intentar guardar el id: {
              recived_id} en la base de datos: {e}")
        return False
    return True
