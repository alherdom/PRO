"""
Dado un nombre y apellidos en formato "apellidos, nombre", obtenga las iniciales de dicha
persona pasadas a mayúsculas y con punto al final.
"""


def run(fullname: str) -> str:
    initials = []
    fullname = fullname.title()
    fullname = fullname.split(', ')
    initial_name = fullname[1][0]
    fullname =' '.join(fullname)
    fullname = fullname.split(' ')
    first_lastname = fullname[0][0]
    second_lastname = fullname[1][0]
    initials = initial_name + first_lastname + second_lastname
    initials ='.'.join(initials)

    
    return initials


if __name__ == "__main__":
    run("Delgado Quintero, sergio")
