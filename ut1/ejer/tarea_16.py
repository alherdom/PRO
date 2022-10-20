# Escriba un programa en Python que acepte un país (como «string») y muestre por pantalla su bandera (como «emoji»). Puede restringirlo a un conjunto limitado de países.
# Entrada: Italia
# Salida: 🇮🇹
country = input('Teclee el nombre del país: ')
country_in_lowercase = country.lower()
if country_in_lowercase == 'italia':
    emoji = '🇮🇹'
elif country_in_lowercase == 'españa':
    emoji = '🇪🇸'
elif country_in_lowercase == 'taliandia':
    emoji = '🇹🇭'
elif country_in_lowercase == 'suecia':
    emoji = '🇸🇪'
print(emoji)
