import re
# Escriba un programa en Python que determine si un email dado tiene el formato correcto.
emails = (
    "ejemplo@gmail.com",
    "usuario_123@yahoo.co.uk",
    "nombre.apellido@empresa.com",
    "correo-electronico@dominio.net",
    "usuario1@subdominio.dominio.com",
    "ejemplogmail.com",
    "usuario@123@yahoo",
    "nombre.apellido@empresa",
    "correo@electrónico@dominio.com",
    "usuario@subdominio@dominio.com"
)
regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'
for email in emails:
    output = re.match(regex, email)
    print(output)