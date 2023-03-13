def num_frec(number: str, digit: str) -> int:
    digit_list = list(digit)
    frecs = digit_list.count(number)
    return frecs

number = input('Introduzca un número a contar: ')
digit = input('Introduzca un dígito para buscar en el: ')

print(num_frec(number,digit))