from test2.calculator import is_positive


def test_is_positive():
    assert is_positive(10) is True

def test_is_negative():
    assert is_positive(-10) is False

def test_is_zero():
    assert is_positive(0) is False