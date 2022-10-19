#Escriba un programa que permita adivinar un personaje de Marvel en base a las tres preguntas siguientes:
#¿Puede volar?
#¿Es humano?
#¿Tiene máscara?
can_fly = input('Puede volar?[s/n]') == 's'
is_human = input('Es humano?[s/n]') == 's'
has_mask = input('Lleva máscara?[s/n]') == 's'
if can_fly:
    if is_human:
        if has_mask:
            print('Tu personaje es IRONMAN')
        else:
            print('Tu personaje es CAPTAIN MARVEL')
    else:
        if has_mask:
            print('Tu personaje es RONAN ACCUSER')
        else:
            print('Tu personaje es VISION')
else:
    if is_human:
        if has_mask:
            print('Tu personaje es SPIDERMAN')
        else:
            print('Tu personaje es HULK')
    else:
        if has_mask:
            print('Tu personaje es BLACK BOLT')
        else:
            print('Tu personaje es THANOS')