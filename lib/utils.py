from binascii import hexlify, unhexlify
from base64 import b64decode, b64encode
from dataclasses import dataclass
from types import SimpleNamespace


@dataclass
class Encoder:
    """Collection of bytes-to-readable-format encoders."""

    Hex = SimpleNamespace(decode=unhexlify, encode=hexlify)
    Base64 = SimpleNamespace(decode=b64decode, encode=b64encode)


def strxor(a: bytes, b: bytes) -> bytes:
    """XOR two bytestrings together."""
    return bytes(x ^ y for x, y in zip(a, b))


def repxor(pt: bytes, key: bytes) -> bytes:
    """
    Repeating-key XOR.

    :param pt: plaintext to encrypt
    :param key: key to use
    """
    repkey = key * (len(pt) // len(key) + 1)
    return strxor(pt, repkey)


def bit_hamming(a: bytes, b: bytes) -> int:
    """Calculate bit Hamming distance between two bytestrings."""
    if len(a) != len(b):
        raise ValueError('bytestings should be of equal length')

    def bitcnt(i: int) -> int:
        """Count the set bits."""
        cnt = 0
        while i:
            cnt += 1
            i &= i - 1
        return cnt

    return sum(bitcnt(x ^ y) for x, y in zip(a, b))
