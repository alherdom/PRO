# ****************************
# DECORANDO LA SUMA DE VALORES
# ****************************


def result_as_status(func):
    def wrapper(*args, **kwargs):
        result_w = func(*args, **kwargs)
        status, result = result_w
        rstatus = {"status": status, "result": result}
        return rstatus
    return wrapper


@result_as_status
def run(values: list) -> tuple:
    status = True
    result = 0
    for value in values:
        if isinstance(value, int):
            status = True
            result += value
        else:
            status = False
            result = "Not int value found"
            break
    return (status, result)
