import pytest
from my_module.enigma import Enigma


@pytest.fixture
def enigma():
    return Enigma("jackson", "12345", "123456")

def test_shift(enigma):
    assert enigma.encrypt() == "12"

if __name__ == "__main__":
    pytest.main()
