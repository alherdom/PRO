initials_1 = []
initials = []
fullname = 'Delgado Quintero, sergio'
fullname = fullname.title()
for i in fullname:
    if i.isupper():
        initials_1 += i
initials = initials_1[2] + initials_1[0] + initials_1[1] + " "
initials ='.'.join(initials)
print(initials)