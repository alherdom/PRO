# **************************
# AQUÍ TIENE SU VUELTA (MAX)
# **************************


def run(to_give_back: float, available_currencies: dict) -> dict:
    money_back = {}
    if to_give_back > 0:
        for currency, amount in sorted(available_currencies.items(), reverse=True):
            quot, rem = divmod(to_give_back, currency)
            if quot < amount:
                to_give_back -= quot * currency
                money_back[currency] = quot
                if rem == 0:
                    break
            else:
                to_give_back -= amount * currency
                money_back[currency] = amount
    if to_give_back > 0:
        money_back = None

    return money_back


if __name__ == "__main__":
    run(0, {0.5: 5, 0.2: 5, 0.1: 5})
