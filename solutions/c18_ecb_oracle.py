"""
    Challenge 1-8: ECB oracle
"""
from pathlib import Path

from utils import Encoder


def oracle(bytestr: bytes) -> bool:
    """Check if input is an ECB-encrypted data."""
    BLOCK_SIZE = 16  # bytes

    parts = (
        bytestr[i : i + BLOCK_SIZE] for i in range(0, len(bytestr), BLOCK_SIZE)
    )
    return len(set(parts)) * BLOCK_SIZE != len(bytestr)


if __name__ == "__main__":
    ct_file = Path(__file__).parent / 'data' / 'c18_ciphertexts.txt'
    with open(ct_file) as f:
        cts = f.read().splitlines()

    for entry in cts:
        ct = Encoder.Hex.decode(entry)
        if oracle(ct):
            print(entry)
