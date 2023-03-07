# *****************
# ALFABETO CIRCULAR
# *****************


def run(max_letters: int) -> str:
    ABC = 'abcdefghijklmnopqrstuvwxyz'
    if max_letters > 0:
        times = max_letters // len(ABC)
        limit = max_letters - (times * len(ABC))
        return ABC * times + ABC[:limit]
    return ''

if __name__ == '__main__':
    run(43)