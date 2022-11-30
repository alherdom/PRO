# *******************
# HEXADECIMAL A TEXTO
# *******************


def run(hex_codes: list) -> str:
    text = ""
    for codes in hex_codes:
        decimal = int(codes,16)
        emoji = chr(decimal)
        text += emoji
    return text


if __name__ == '__main__':
    run(['1f49a', '2728', '1f389', '1f3c6'])
