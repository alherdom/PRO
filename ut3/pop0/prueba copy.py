fullname = 'Delgado Quintero, sergio'
fullname = fullname.title()
fullname = fullname.split(', ')
initial_name = fullname[1][0]
fullname ='.'.join(fullname)
fullname = fullname.split(' ')
first_lastname = fullname[0][0]
second_lastname = fullname[1][0]
initials = initial_name + first_lastname + second_lastname
initials ='.'.join(initials)
print(initials)

