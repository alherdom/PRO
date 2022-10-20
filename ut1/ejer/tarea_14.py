# Escriba un programa en Python que acepte la opción de dos jugadoras en Piedra-Papel-Tijera y decida el resultado (solución).
# Entrada: persona1=piedra; persona2=papel
# Salida: Gana persona2: El papel envuelve a la piedra
persona1 = input('Piedra, papel o tijera, saca lo que quieras ya!') 
persona2 = input('Piedra, papel o tijera, saca lo que quieras ya!')

if persona1 == 'piedra' and persona2 == 'papel':
    print('Gana persona2: El papel envuelve a la piedra')
elif persona1 == 'tijera' and not persona2 == 'piedra':
    print('Gana persona1: La tijera corta el papel')
if not persona1 == 'papel' and persona2 == 'piedra':
    print('Gana persona2: La piedra rompe las tijeras')