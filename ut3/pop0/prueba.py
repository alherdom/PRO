fullname = 'Delgado Quintero, sergio'
initials = []
for char in fullname.title():
    if char.isupper():
        initials += char
        if len(initials) == 2:
            break    
print(initials)