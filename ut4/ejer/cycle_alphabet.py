# *****************
# ALFABETO CIRCULAR
# *****************


def cycle_text(text: str,max_letters:int):
    for i in range(max_letters):
        current_pos = i % len(text)
        yield text[current_pos]

def run(max_letters: int) -> str:
    ABC = "abcdefghijklmnopqrstuvwxyz"
    return ''.join(cycle_text(ABC, max_letters))

if __name__ == "__main__":
    run(0)



# def run(max_letters: int) -> str:  
#     ABC = "abcdefghijklmnopqrstuvwxyz"
#     times = max_letters // len(ABC)
#     limit = max_letters - (times * len(ABC))
#     return ABC * times + ABC[:limit]


# if __name__ == "__main__":
#     run(0)
