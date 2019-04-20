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
    common = b'\x20ETAOINSHRDLU'
    data = b''.join(re.findall(rb'[\w\x20]', bytestr)).upper()
    return sum(data.count(c) for c in common) / len(data)


def stats_bigrams(bytestr: bytes) -> int:
    """Calculate cumulative number of the first 10 most common bigrams."""
    bigrams = (
        b'TH',
        b'HE',
        b'IN',
        b'ER',
        b'AN',
        b'RE',
        b'ND',
        b'AT',
        b'ON',
        b'NT',
    )
    data = bytestr.upper()
    return sum(data.count(b) for b in bigrams)


def oracle(
    ct: AnyStr, *, encoder: Encoder = None
) -> Tuple[bytes, bytes, float, int]:
    """
    Guess the key to the single-byte XOR cipher.
    Return key (hex-encoded), plaintext and message statistics.

    :param ct: ciphertext to crack
    :param encoder: encoder to decode the ciphertext
    """
    if encoder is not None:
        ct = encoder.decode(ct)

    # Find keys which produce PT with all printable characters
    candidates_printable = []
    for i in bytes(range(256)):
        key = gen_long_key(ct, i)
        pt = strxor(ct, key)
        if stats_printable(pt) == 1.0:
            candidates_printable.append([i, pt])

    # Calculate letter statistics
    candidates_etaoin = []
    for i, pt in candidates_printable:
        freq_score = stats_etaion(pt)
        bigrams = stats_bigrams(pt)
        candidates_etaoin.append([i, pt, freq_score, bigrams])

    candidates_etaoin.sort(key=lambda x: (x[-1], x[-2]), reverse=True)
    return candidates_etaoin[0]


if __name__ == "__main__":
    ct = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
    best = oracle(ct, encoder=Encoder.Hex)
    print(best[1])