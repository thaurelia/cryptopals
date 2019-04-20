import pytest

from solutions.padding import PKCS_7

@pytest.mark.parametrize('inp, bs, expected', [
    (b'YELLOW SUBMARINE', 20, b'YELLOW SUBMARINE\x04\x04\x04\x04'),
])
def test_pkcs_7_pad_with_bs(inp, bs, expected):
    assert PKCS_7.pad_with_bs(inp, bs) == expected


@pytest.mark.parametrize('inp, expected', [
    (b'YELLOW SUBMARINE', b'YELLOW SUBMARINE' + b'\x10'*16),
    (b'ICE ICE BABY', b'ICE ICE BABY\x04\x04\x04\x04')
])
def test_pkcs_7_pad(inp, expected):
    assert PKCS_7.pad(inp) == expected
