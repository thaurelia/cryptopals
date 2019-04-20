"""
    Challenge 1-4: Detect single-byte XOR in file and recover plaintext
"""
import sys
from pathlib import Path

sys.path.insert(0, Path(__file__).parent.parent.as_posix())
from c13_sbx_oracle import oracle
from lib.utils import Encoder


if __name__ == "__main__":
    ct_file = Path(__file__).parent / 'c14_ciphertexts.txt'
    with open(ct_file) as f:
        ciphertexts = f.read().splitlines()

    candidates = (oracle(ct, encoder=Encoder.Hex) for ct in ciphertexts)
    best = sorted(candidates, key=lambda x: x[-1], reverse=True)[0]

    print(best[1])
