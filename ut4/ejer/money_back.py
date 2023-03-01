# ********************
# AQUÍ TIENE SU VUELTA
# ********************


def run(to_give_back: float, available_currencies: list) -> dict:
    money_back = {}
    available_currencies.sort(reverse=True)
    for currency in available_currencies:
        while currency <= to_give_back:
            quot, rem = divmod(to_give_back, currency)
            to_give_back -= quot * currency             
            money_back[currency] = quot
    if to_give_back != 0:
        money_back = None
    return money_back


if __name__ == '__main__':
    run(20, [5, 2, 1])