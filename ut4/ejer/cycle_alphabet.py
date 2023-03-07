# *****************
# ALFABETO CIRCULAR
# *****************


def run(max_letters: int) -> str:
    ABC = "abcdefghijklmnopqrstuvwxyz"
    times = max_letters // len(ABC)
    limit = max_letters - (times * len(ABC))
    return ABC * times + ABC[:limit]


if __name__ == "__main__":
    run(43)
