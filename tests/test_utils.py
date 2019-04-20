import pytest

from lib.utils import Encoder, strxor


@pytest.mark.parametrize(
    'str_a, str_b, encoder, expected',
    [
        ('ABCD', '\x20' * 4, None, b'abcd'),
        (
            '1c0111001f010100061a024b53535009181c',
            '686974207468652062756c6c277320657965',
            Encoder.Hex,
            b'746865206b696420646f6e277420706c6179',
        ),
        (b'YWJjZA==', b'ICAgIA==', Encoder.Base64, b'QUJDRA=='),
    ],
)
def test_strxor(str_a, str_b, encoder, expected):
    assert strxor(str_a, str_b, encoder=encoder) == expected
