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

import pytest

import shop1


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
def empty_cart():
    return {
        "products": [],
    }


@pytest.fixture
def cart_with_product(empty_cart, product):
    return add_to_cart(empty_cart, product)


@pytest.fixture
def order(user, cart_with_product):
    return create_order(user, cart_with_product)


def test_new_cart_is_empty(empty_cart):
    assert empty_cart["products"] == []


def test_add_product(empty_cart, product):
    result = add_to_cart(empty_cart, product)

    assert result["products"] == [product]


def test_cart_total(cart_with_product):
    total = calculate_cart_total(cart_with_product)

    assert total == 500


def test_create_order(order, user, product):
    assert order["user_id"] == user["id"]
    assert order["products"] == [product]
    assert order["total"] == 500
