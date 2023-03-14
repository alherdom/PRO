# Si utilizamos el operador ** delante del nombre de un parámetro nominal, estaremos indicando 
# que los argumentos pasados a la función se empaqueten en un diccionario.
# Supongamos un ejemplo en el que queremos encontrar la persona con mayor calificación de un examen.
# Haremos uso del ** para empaquetar los argumentos nominales:

def best_student(**marks):
    max_mark = -1
    for student, mark in marks.items():  # marks es un diccionario
        if mark > max_mark:
            max_mark = mark
            best_student = student
    return best_student

print(best_student(ana=8, antonio=6, inma=9, javier=7))