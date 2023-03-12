
def email_check(email:str) -> bool:
    request_char = '@'
    for char in email:
        if char == request_char:
            return True
    else:
        return False
    
email = input('Introduzca un correo electrónico: ')
print(email_check(email))