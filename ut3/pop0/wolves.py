# **************
# EL LOBO ACECHA
# **************


def run(farm: list) -> str:
    if farm[-1] == "lobo":
        msg = "No te quiero ver más por aquí, lobo"
    else:
        for i, animal in enumerate(farm[::-1]):
            if animal == "lobo":
                break
        msg = f"Cuidado oveja {i}, el lobo te va a comer"
    

    
    
    return msg


if __name__ == '__main__':
    run(['oveja', 'oveja', 'lobo', 'oveja'])
