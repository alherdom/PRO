# **************************
# AQUÍ TIENE SU VUELTA (MAX)
# **************************


def run(to_give_back: float, available_currencies: dict) -> dict:
    money_back = {}
    available_currencies = dict(
        sorted(available_currencies.items(), key=lambda item: item[0], reverse=True)
    )
    if to_give_back != 0:
        for currency, amount in available_currencies.items():
            quot, rem = divmod(to_give_back, currency)
            if quot <= amount:
                to_give_back -= quot * currency
                money_back[currency] = quot
                if rem == 0:
                    break            
            else:
                to_give_back -= amount * currency
                money_back[currency] = amount
    if to_give_back:
        money_back = None
 
    return money_back


if __name__ == "__main__":
    run(20, {5: 3, 2: 7, 1: 3})
