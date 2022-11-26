"""
Dado un nombre y apellidos en formato "apellidos, nombre", obtenga las iniciales de dicha
persona pasadas a mayúsculas y con punto al final.
"""


def run(fullname: str) -> str:
    initials = []
    fullname = fullname.title()
    fullname = fullname.split(", ")
    surname = fullname[0].split()
    name = fullname[1]
    if len(surname) > 1:
        ini_surname1 = surname[0][0]
        ini_surname2 = surname[1][0]
        ini_name = name[0][0]
        initials = f'{ini_name}.{ini_surname1}.{ini_surname2}.'
    else:
        ini_surname1 = surname[0][0]
        ini_name = name[0][0]
        initials = f'{ini_name}.{ini_surname1}.'

    return initials


if __name__ == "__main__":
    run("Delgado Quintero, sergio")
