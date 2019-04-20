from Crypto.Cipher import AES

from padding import PKCS_7
from utils import strxor


class ECB:
    """AES ECB mode."""

    @staticmethod
    def encrypt(pt: bytes, key: bytes) -> bytes:
        """Encrypt with AES in ECB mode."""
        return AES.new(key).encrypt(pt)

    @staticmethod
    def decrypt(ct: bytes, key: bytes) -> bytes:
        """Decrypt with AES in ECB mode."""
        return AES.new(key).decrypt(ct)


class CBC:
    """AES CBC mode."""

    @staticmethod
    def encrypt(pt: bytes, key: bytes, iv: bytes) -> bytes:
        """Encrypt with AES in CBC mode."""
        ct = iv
        pad_pt = PKCS_7.pad(pt)
        for i in range(0, len(pad_pt), 16):
            block = pad_pt[i : i + 16]
            xored = strxor(block, ct[-16:])
            encrypted = ECB.encrypt(xored, key)
            ct += encrypted
        return ct[16:]

    @staticmethod
    def decrypt(ct: bytes, key: bytes, iv: bytes) -> bytes:
        """Decrypt with AES in CBC mode."""
        xor_key = iv
        pt = b''
        for i in range(0, len(ct), 16):
            block = ct[i : i + 16]
            xored = ECB.decrypt(block, key)
            pt += strxor(xored, xor_key)
            xor_key = block
        return pt
