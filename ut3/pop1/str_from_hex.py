# *******************
# HEXADECIMAL A TEXTO
# *******************


def run(hex_codes: list) -> str:
    text = ""
    for codes in hex_codes:
        decimal = int(codes,16)
        text += chr(decimal)
    return text


if __name__ == '__main__':
    run(['1f49a', '2728', '1f389', '1f3c6'])
