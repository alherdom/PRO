# Escriba un programa en Python que acepte la opción de dos jugadoras en Piedra-Papel-Tijera y decida el resultado (solución).
# Entrada: persona1=piedra; persona2=papel
# Salida: Gana persona2: El papel envuelve a la piedra
piedra = input('Escoge piedra?[s/n]') == 's'
papel = input('Escoge papel?[s/n]') == 's'
tijera = input('Escoge tijera?[s/n]') == 's'
if piedra and papel:
    print('Gana papel')
elif tijera and not piedra:
    print('Gana tijera')
if not papel and piedra:
    print('Gana piedra')