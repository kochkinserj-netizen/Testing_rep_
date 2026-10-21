import pytest


@pytest.fixture
def user():
    return {
        "id": 1,
        "name": "Alex",
    }


@pytest.fixture
def product():
    return {
        "id": 10,
        "name": "Book",
        "price": 500,
    }


@pytest.fixture
def order(user, product):
    return {
        "user": user,
        "products": [product],
        "total": product["price"],
    }


def test_order_total(order):
    assert order["total"] == 500