"""
    Challenge 1-3: Single-byte XOR oracle
"""

import re
import sys
from pathlib import Path
from string import printable
from typing import AnyStr, Tuple

sys.path.insert(0, Path(__file__).parent.parent.as_posix())
from lib.utils import Encoder, strxor


def gen_long_key(ct: AnyStr, k: bytes) -> bytes:
    """
    Generate XOR encryption key from a single character.
    Return non-encoded key (i.e. raw bytes)

    :param ct: ciphertext
    :param k: character to use as a key
    :param encoder: encoder for the ciphertext
    """
    return bytes([k] * len(ct))


def stats_printable(bytestr: bytes) -> float:
    """Calculate the percentage of printable characters in bytestring."""
    no_of_printable = sum(b in bytes(printable, 'utf-8') for b in bytestr)

    return no_of_printable / len(bytestr)


def stats_etaion(bytestr: bytes) -> float:
    """Calculate cumulative percentage of the first 12 most common letters."""
    common = b'\x20etaoinshrdlu'
    data = b''.join(re.findall(rb'[\w\x20]', bytestr)).lower()
    return sum(data.count(c) for c in common) / len(bytestr)


def oracle(ct: bytes) -> Tuple[bytes, bytes, float]:
    """
    Guess the key to the single-byte XOR cipher.
    Return key, plaintext and message statistics.

    :param ct: ciphertext to crack
    """
    # Find keys which produce PT with all printable characters
    candidates_printable = []
    for i in bytes(range(256)):
        key = gen_long_key(ct, i)
        pt = strxor(ct, key)
        if stats_printable(pt) == 1.0:
            candidates_printable.append([i, pt])

    if not candidates_printable:
        return [None, None, 0]

    # Calculate letter statistics
    candidates_etaoin = []
    for i, pt in candidates_printable:
        freq_score = stats_etaion(pt)
        candidates_etaoin.append([i, pt, freq_score])

    candidates_etaoin.sort(key=lambda x: (x[-1]), reverse=True)
    return candidates_etaoin[0]


if __name__ == "__main__":
    ct = Encoder.Hex.decode(
        b'1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
    )
    best = oracle(ct)
    print(best[1])
