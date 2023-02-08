# ******************
# SUMA CRIPTOGRÁFICA
# ******************
from pathlib import Path


def run(crypto_path: Path) -> float:
    with open(crypto_path) as f:
        codes = {
            "sd": "-",
            "vo": ".",
            "ax": "0",
            "gh": "1",
            "hj": "2",
            "uv": "3",
            "ws": "4",
            "pk": "5",
            "et": "6",
            "mc": "7",
            "rh": "8",
            "wb": "9",
        }

        sum_cr = "output"

    return sum_cr


if __name__ == "__main__":
    run("data/sum_crypto/data1.crypto")
