# *******************
# CREANDO OPERACIONES
# *******************


def run(oper: str, num1: int, num2: int):
    match oper:
        case "add":
            operation = num1 + num2
        case "sub":
            operation = num1 - num2
        case "mul":
            operation = num1 * num2
        case "div":
            operation = num1 / num2
        case _:
            operation = None
    return operation
