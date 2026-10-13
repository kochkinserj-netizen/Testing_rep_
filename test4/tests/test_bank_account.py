import pytest

from test4.bank_account import withdraw, get_account


def test_negative_amount():
    with pytest.raises(ValueError):
        withdraw(100,-10)

def test_more_amount():
    with pytest.raises(ValueError, match='Недостаточно средств'):
        withdraw(100,1000)

def test_account_not_found():
    accounts = {}

    with pytest.raises(KeyError) as exception_info:
        get_account(accounts, 15)

    assert exception_info.type is KeyError
    assert "id=15" in str(exception_info.value)

def test_low_balance():
    with pytest.warns(UserWarning,
                      match='Баланс становится меньше 100',):
        result = withdraw(110,20)
    assert result == 90

def test_positive_withdraw():
    result = withdraw(700,400)
    assert result == 300

