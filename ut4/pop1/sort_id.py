# **********************************
# ORDENANDO IDS EN UNA BASE DE DATOS
# **********************************


def sort_id(db: list) -> list:
    sorted_db = db.copy()
    i = 1
    for item in sorted_db:
        item['id'] = i
        i += 1
    return sorted_db