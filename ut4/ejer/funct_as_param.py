# Las funciones se pueden utilizar en cualquier contexto de nuestro programa.
# Son objetos que pueden ser asignados a variables, usados en expresiones, devueltos
# como valores de retorno o pasados como argumentos a otras funciones. Ejemplo:

def repeat_please(text, times=1):
    return text * times

# type(repeat_please)
# function

def doit(f, arg1, arg2):
    return f(arg1, arg2)

print(doit(repeat_please, 'Functions as params', 2))