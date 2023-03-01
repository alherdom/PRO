# **************************
# AQUÍ TIENE SU VUELTA (MAX)
# **************************


def run(to_give_back: float, available_currencies: dict) -> dict:
    money_back = {}
    available_currencies = dict(sorted(available_currencies.items(), key=lambda item:item[0],reverse=True)) 
    for currency, amount in available_currencies.items():
        while currency <= to_give_back:
            quot, rem = divmod(to_give_back, currency)        
            to_give_back -= quot * currency
            money_back[currency] = quot
    if to_give_back != 0:
        money_back = None
    return money_back


if __name__ == '__main__':
    run(20, {5: 3, 2: 7, 1: 3})