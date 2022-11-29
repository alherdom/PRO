# *************************
# PALABRAS EN ORDEN INVERSO
# *************************


def run(text: str) -> str:
    text = text.lower()
    text = text.split()
    reversing = text[::-1]
    reversing = " ".join(reversing)
    
    return reversing


if __name__ == '__main__':
    run('Hello World')
