def run(word: str) -> float:
    char_sum = 0
    for char in word:
        char_sum += ord(char)
    char_avg = char_sum / len(word)
    return char_avg