# **********************************
# ORDENANDO IDS EN UNA BASE DE DATOS
# **********************************


def sort_id(db: list) -> list:
    # sorted_db = db.copy()
    # i = 1
    # for item in sorted_db:
    #     item['id'] = i
    #     i += 1
    # return sorted_db
    sorted_db = db.copy()
    for i, item in enumerate(sorted_db, start=1):
        item['id'] = i
    return sorted_db