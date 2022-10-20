# Escriba un programa en Python que acepte la opción de dos jugadoras en Piedra-Papel-Tijera y decida el resultado (solución).
# Entrada: persona1=piedra; persona2=papel
# Salida: Gana persona2: El papel envuelve a la piedra
persona1 = input('Piedra, papel o tijera, saca lo que quieras ya! ')
persona2 = input('Piedra, papel o tijera, saca lo que quieras ya! ')
eleccion1 = persona1.lower()
eleccion2 = persona2.lower()
print('La persona1 ha elegido: ',eleccion1)
print('La persona2 ha elegido: ',eleccion2)
if eleccion1 == 'piedra' and eleccion2 == 'papel':
    ganador = 2
    mensaje ='EL PAPEL ENVUELVE A LA PIEDRA'
if eleccion1 == 'papel' and eleccion2 == 'piedra':
    ganador = 1
    mensaje ='EL PAPEL ENVUELVE A LA PIEDRA'
if eleccion1 == 'piedra' and persona2 == 'tijera':
    ganador = 1
    mensaje ='LA PIEDRA ROMPE LA LA TIJERA'
if eleccion1 == 'tijera' and eleccion2 == 'piedra':
    ganador = 2
    mensaje ='LA PIEDRA ROMPE LA LA TIJERA'
if eleccion1 == 'tijera' and eleccion2 == 'papel':
    ganador = 1
    mensaje ='LA TIJERA CORTA EL PAPEL'
if eleccion1 == 'papel' and eleccion2 == 'tijera':
    ganador = 2
    mensaje ='LA TIJERA CORTA EL PAPEL'
if eleccion1 == eleccion2:
    mensaje = 'EMPATE'
    ganador = 0
    print("EMPATE")
else:
    print(f'Gana persona{ganador}: {mensaje}')