"""
Dado un nombre y apellidos en formato "apellidos, nombre", obtenga las iniciales de dicha
persona pasadas a mayúsculas y con punto al final.
"""


def run(fullname: str) -> str:
    initials = []
    fullname = fullname.title().split(", ")
    name_init = fullname[1][0]
    surname1_init = fullname[0][0]
    surname2_init = fullname[0][1]
    initials = print(f'{name_init}{surname1_init}.{surname2_init}')
    return initials


if __name__ == "__main__":
    run("Delgado Quintero, sergio")
