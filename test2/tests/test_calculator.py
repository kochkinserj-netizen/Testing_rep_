from test2.calculator import add, subtract


def test_add():
    assert add(2, 3) == 5

def test_subtract():
    assert subtract(10,4) == 6

class TestNegativeNumbers:
    def test_add_negative(self):
        assert add(-2,-7) == -9

    def test_subtract_negative(self):
        assert subtract(-2,-7) == 5
