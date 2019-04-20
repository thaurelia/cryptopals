from binascii import hexlify, unhexlify
from base64 import b64decode, b64encode
from dataclasses import dataclass
from types import SimpleNamespace
from typing import AnyStr


@dataclass
class Encoder:
    """Collection of bytes-to-readable-format encoders."""
    Hex = SimpleNamespace(decode=unhexlify, encode=hexlify)
    Base64 = SimpleNamespace(decode=b64decode, encode=b64encode)


def strxor(str_a: AnyStr, str_b: AnyStr, *, encoder: Encoder = None) -> bytes:
    """
    XOR two strings together.
    If `encoder` is not None, assume both inputs are encoded with the encoder.
    Decode data before XORing and encode result before returning.

    :param str_a: first string
    :param str_b: second string
    :param encoder: encoder to use
    """
    if isinstance(str_a, str):
        str_a = str_a.encode('utf-8')
    if isinstance(str_b, str):
        str_b = str_b.encode('utf-8')

    if encoder is not None:
        data_a = encoder.decode(str_a)
        data_b = encoder.decode(str_b)
    else:
        data_a, data_b = str_a, str_b

    xored = bytes(a ^ b for a, b in zip(data_a, data_b))

    return encoder.encode(xored) if encoder is not None else xored
