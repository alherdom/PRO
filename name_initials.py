"""
Dado un nombre y apellidos en formato "apellidos, nombre", obtenga las iniciales de dicha
persona pasadas a mayúsculas y con punto al final.
"""


def run(fullname: str) -> str:
    initials =[]
    name = fullname.split(",")
    lastname = fullname.split(" ")
    
    return initials


if __name__ == "__main__":
    run("Delgado Quintero, sergio")
