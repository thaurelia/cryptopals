"""
    Challenge 1-6: Break repeating-key XOR cipher
"""

import sys
from itertools import zip_longest as zipl
from pathlib import Path
from typing import List

sys.path.insert(0, Path(__file__).parent.parent.as_posix())
from c13_sbx_oracle import oracle as sbx_oracle
from lib.utils import Encoder, bit_hamming, repxor


def guess_key_length(ct: bytes) -> int:
    """Guess key length for a repeating-key XOR cipher."""
    hamming_dists = []

    for i in range(2, 41):
        first_block = ct[:i]
        second_block = ct[i : 2 * i]
        h_normalized = bit_hamming(first_block, second_block) / i
        hamming_dists.append((h_normalized, i))

    return sorted(hamming_dists)


def transpose_ct(ct: bytes, keysize: int) -> List[bytes]:
    """Break repkey-XOR ciphertext into single-byte XOR parts."""
    keysize_parts = (ct[i : i + keysize] for i in range(0, len(ct), keysize))
    return [bytes(filter(None.__ne__, part)) for part in zipl(*keysize_parts)]


def oracle(ct: bytes):
    for h_normalized, keysize in guess_key_length(ct):
        sbx_oracle_results = (
            sbx_oracle(part) for part in transpose_ct(ct, keysize)
        )
        key = [r[0] for r in sbx_oracle_results]
        if all(key):
            return repxor(ct, bytes(key))


if __name__ == "__main__":
    ct_file = Path(__file__).parent / 'data' / 'c16_ciphertext.txt'
    with open(ct_file) as f:
        ct = Encoder.Base64.decode(f.read().replace('\n', ''))

    print(oracle(ct).decode())
