# *******************
# CREANDO OPERACIONES
# *******************

def make_oper(oper: str):
    def operation(num1: int, num2: int):
        match oper:
            case "add":
                return num1 + num2
            case "sub":
                return num1 - num2
            case "mul":
                return num1 * num2
            case "div":
                return num1 / num2
            case _:
                return None
    return operation

def run(oper: str, num1: int, num2: int):
    operation = make_oper(oper)
    result = operation(num1, num2) 
    return result