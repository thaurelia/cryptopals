from binascii import hexlify, unhexlify
from base64 import b64decode, b64encode
from dataclasses import dataclass
from types import SimpleNamespace


@dataclass
class Encoder:
    """Collection of bytes-to-readable-format encoders."""

    Hex = SimpleNamespace(decode=unhexlify, encode=hexlify)
    Base64 = SimpleNamespace(decode=b64decode, encode=b64encode)


def strxor(str_a: bytes, str_b: bytes) -> bytes:
    """
    XOR two strings together.

    :param str_a: first string
    :param str_b: second string
    """
    return bytes(a ^ b for a, b in zip(str_a, str_b))


def repxor(pt: bytes, key: bytes) -> bytes:
    """
    Repeating-key XOR.

    :param pt: plaintext to encrypt
    :param key: key to use
    """
    repkey = key * (len(pt) // len(key) + 1)
    return strxor(pt, repkey)
