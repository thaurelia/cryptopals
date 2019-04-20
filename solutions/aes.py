from Crypto.Cipher import AES


class ECB:
    @staticmethod
    def encrypt(pt, key):
        return AES.new(key).encrypt(pt)

    @staticmethod
    def decrypt(ct, key):
        return AES.new(key).decrypt(ct)
