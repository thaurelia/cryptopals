class PKCS_7:
    @staticmethod
    def pad_with_bs(inp: bytes, bs: int) -> bytes:
        """
        Pad input according to blocksize.

        :param inp: input to pad (bytes)
        :param bs: block size to pad to
        """
        padding_len = bs - (len(inp) % bs)
        return inp + bytes([padding_len] * padding_len)

    def pad(inp: bytes) -> bytes:
        """Pad input for AES encryption."""
        return PKCS_7.pad_with_bs(inp, 16)
