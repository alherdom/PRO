vending_path = 'ut4/te1/data/vending.dat'
operations_path = 'ut4/te1/data/operations.dat'
status_path = 'ut4/te1/data/status.dat'

def order(choice,money):
    ARTICLES = {1:'Coca-Cola',2:'Clipper',3:'Tirma',4:'Fanta',5:'Eidetesa'}
    PRICES = {1:1.5,2:1.8,3:1.1,4:1.5,5:2.8}
    STOCK = [20,30,20,20,10]
    if PRICES[choice] == money:          
        return(f'Dinero justo, aquí tiene su {ARTICLES[choice]} quedan') 
    elif PRICES[choice] > money:
        return(f'Dinero insuficiente, introduzca más dinero')
    
input_path = 'ut4/data/choices.dat'
with open(input_path) as f:
    for line in f:
        elements = line.strip().split(",")
        print(order(elements[0], elements[1]))
        



    