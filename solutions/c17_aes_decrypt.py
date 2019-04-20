"""
    Challenge 1-7: decrypt AES ciphertext
"""

import sys
from pathlib import Path

sys.path.insert(0, Path(__file__).parent.parent.as_posix())
from lib.aes import ECB
from lib.utils import Encoder

if __name__ == "__main__":
    ct_file = Path(__file__).parent / 'data' / 'c17_ciphertext.txt'
    with open(ct_file) as f:
        ct = Encoder.Base64.decode(f.read().replace('\n', ''))

    key = b'YELLOW SUBMARINE'
    print(ECB.decrypt(ct, key).decode())
