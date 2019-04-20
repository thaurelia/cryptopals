import solutions.utils as utils

Encoder = utils.Encoder


def test_strxor():
    data_a = Encoder.Hex.decode(b'1c0111001f010100061a024b53535009181c')
    data_b = Encoder.Hex.decode(b'686974207468652062756c6c277320657965')
    expected = Encoder.Hex.decode(b'746865206b696420646f6e277420706c6179')
    assert utils.strxor(data_a, data_b) == expected


def test_repxor():
    pt = (
        b'Burning \'em, if you ain\'t quick and nimble\n'
        b'I go crazy when I hear a cymbal'
    )
    key = b'ICE'

    expected = Encoder.Hex.decode(
        b'0b3637272a2b2e63622c2e69692a2369'
        b'3a2a3c6324202d623d63343c2a262263'
        b'24272765272a282b2f20430a652e2c65'
        b'2a3124333a653e2b2027630c692b2028'
        b'3165286326302e27282f'
    )

    assert utils.repxor(pt, key) == expected


def test_bit_hamming():
    a = b'this is a test'
    b = b'wokka wokka!!!'

    assert utils.bit_hamming(a, b) == 37
