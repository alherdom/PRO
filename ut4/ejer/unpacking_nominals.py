# Al igual que veíamos previamente, existe la posibilidad de usar doble asterisco ** en la llamada 
# a la función para desempaquetar los argumentos nominales:

def best_student(**marks):
    max_mark = -1
    for student, mark in marks.items():  # marks es un diccionario
        if mark > max_mark:
            max_mark = mark
            best_student = student
    return best_student

marks = dict(ana=8, antonio=6, inma=9, javier=7)
print(best_student(**marks))