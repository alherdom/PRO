# ********************
# AQUÍ TIENE SU VUELTA
# ********************


def run(to_give_back: float, available_currencies: list) -> dict:
    money_back = {}
    available_currencies.sort(reverse=True)  
    for currency in available_currencies:
        if currency <= to_give_back:
            money_back[currency] = (to_give_back // currency)
            to_give_back -= (to_give_back // currency) * currency
    if to_give_back:
        money_back = None
    return money_back


if __name__ == "__main__":
    run(20, [5, 2, 1])
