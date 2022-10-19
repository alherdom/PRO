#Escriba un programa en Python que acepte una ruta remota de recurso samba, y lo separe en nombre(IP) del equipo y ruta (solución).
#Entrada: //1.1.1.1/eoi/python
#Salida: equipo=1.1.1.1; ruta=/eoi/python
path = '//1.1.1.1/eoi/python'
slash_path = path.strip('/')
slash_position = slash_path.find('/')
host = slash_path[:slash_position]
path_out = slash_path[slash_position:]
print('equipo=',host)
print('ruta=',path_out)