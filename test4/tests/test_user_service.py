# test
from test4.users_service import register_user, clculate_discount
import pytest
import warnings


def test_empty_username():
    register_user('',25)

def test1_empty_username():
    with pytest.raises(ValueError):
        register_user('',25)

def test2_empty_username():
    with pytest.raises(TypeError):
        register_user('',25)


def test1_1_empty_username():
    with pytest.raises(
            ValueError,
    match='совершеннолетним') as exception_info:
        register_user('Alex',17)

def test1_2_empty_username():
    with pytest.raises(
            ValueError,
    match='Имя') as exception_info:
        register_user('',19)


def test2_1_empty_username():
    with pytest.raises(ValueError) as exception_info:
        register_user('',20)


def test2_2_empty_username():
    with pytest.raises(ValueError):
        pytest.fail('Учебное падение теста, за счет исключения',)
    register_user('',20)



def test_large_discount():
    with pytest.warns(UserWarning):
        clculate_discount(70)  