from Crypto.Cipher import AES


class ECB:
    @staticmethod
    def encrypt(pt: bytes, key: bytes) -> bytes:
        """Encrypt with AES in ECB mode."""
        return AES.new(key).encrypt(pt)

    @staticmethod
    def decrypt(ct: bytes, key: bytes) -> bytes:
        """Decrypt with AES in ECB mode."""
        return AES.new(key).decrypt(ct)
