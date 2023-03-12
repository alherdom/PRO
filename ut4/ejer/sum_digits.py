def sum_digits(number):
    sume=0
    while number!=0:
        digit = number % 10
        sume += digit
        number = number // 10
    return sume

num=int(input("Número a procesar: "))
total_sumes = 0
while num!=0:
    print(f'Suma de dígitos: {sum_digits(num)}')
    total_sumes += sum_digits(num)
    print(f'Total sumas: {total_sumes}')
    print(f'Suma de dígitos de la suma total: {sum_digits(total_sumes)}')
    num=int(input("Número a procesar: "))
    