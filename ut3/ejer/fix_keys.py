# ********************
# LA CLAVE ES LA CLAVE
# ********************


def run(items: dict) -> dict:
    #fitems = {code.replace(' ',""):subj for code, subj in items.items()}
    fitems = {}
    for code, subjet in items.items():
        clean_code = code.replace(" ","")
        fitems[clean_code] = subjet
    
        
       
    
    return fitems


if __name__ == '__main__':
    run({'S  001': ['Math', 'Science'], 'S    002': ['Math', 'English']})
