def leet_translate(text: str) -> str:
    leet_alphanet = {
        "a": "4",
        "b": "ß",
        "c": "¢",
        "d": "|)",
        "e": "3",
        "f": "|=",
        "g": "&",
        "h": "]-[",
        "i": "1",
        "j": ",_|",
        "k": ">|",
        "l": "1",
        "m": "^^",
        "n": "И",
        "o": "0",
        "p": "|º",
        "q": "(_,)",
        "r": "I2",
        "s": "5",
        "t": "7",
        "u": "(_)",
        "v": "|/",
        "w": "uu",
        "x": "><",
        "y": "j",
        "z": "2",
        " ": " ",
    }
    code = ""
    for char in text:
        code += leet_alphanet[char]
    return code

text = input('Introduza el texto a traducir a lenguaaje "leet": ')
print(leet_translate(text.lower()))
