import pytest
from my_module.enigma import Enigma


@pytest.fixture
def enigma():
    return Enigma("jackson", "12345", "123456")

def test_shift_key(enigma):
    key_shift = {
        "a": "12",
        "b": "23",
        "c": "34",
        "d": "45"
    }
    assert enigma.shift_key() == key_shift

def test_shift_date(enigma):
    assert enigma.shift_date() == {'a': '6', 'b': '3', 'c': '9', 'd': '3'}
    
def test_final_key(enigma):
    assert enigma.final_key() == {'a': 18, 'b': 26, 'c': 43, 'd': 48}

def test_offset(enigma):
    assert enigma.offest() == {}

if __name__ == "__main__":
    pytest.main()
