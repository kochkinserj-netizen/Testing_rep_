import pytest


@pytest.fixture
def user():
    return {
        "id": 1,
        "name": "Alex",
        "active": True,
    }


def test_user_name(user):
    assert user["name"] == "Alex"


def test_user_is_active(user):
    assert user["active"] is True


def test_user_has_id(user):
    assert user["id"] == 1

@pytest.fixture
def product():
    return {
        "id": 10,
        "name": "Book",
        "price": 500,
    }


def test_add_product_to_user_cart(user, product):
    cart = {
        "user_id": user["id"],
        "products": [product],
    }

    assert cart["user_id"] == 1
    assert cart["products"][0]["name"] == "Book"

