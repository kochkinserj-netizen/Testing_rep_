# Функции тестирующие
import pytest

from test1.calculator import add, subtract

def test_add_fall():
    result = add(1,1)
    assert result == 1, 'Намеренная ошибка для обучения'

def test_add_two_positive_numbers():
    result = add(16,3)
    assert result == 19

def test_add_three_negative_numbers():
    result = add(-16,-3)
    assert result == -19

def test_add_fore_zeros():
    result = add(0,0)
    assert result == 0

@pytest.mark.skip(reason="Not working")
def test_subtract_two_positive_numbers():
    result = subtract(6,5)
    assert result == 6

def test_subtract_two_negative_numbers():
    result = subtract(-6,-5)
    assert result == -1