"""
    Challenge 1-4: Detect single-byte XOR in file and recover plaintext
"""
from pathlib import Path

from c13_sbx_oracle import oracle
from utils import Encoder

if __name__ == "__main__":
    ct_file = Path(__file__).parent / 'data' / 'c14_ciphertexts.txt'
    with open(ct_file) as f:
        ciphertexts = f.read().splitlines()

    candidates = (oracle(Encoder.Hex.decode(ct)) for ct in ciphertexts)
    best = sorted(candidates, key=lambda x: x[-1], reverse=True)[0]

    print(best[1])
