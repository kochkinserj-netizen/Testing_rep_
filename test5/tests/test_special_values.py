import pytest

@pytest.mark.skip(reason = 'Падающий тест, скипнут осозннано')
def test_sum():  # тест не пройдет из-за:  assert 0.30000000000000004 == 0.3
    result = 0.1+0.2
    assert result == 0.3


def test_sum2():
    result = 0.1+0.2
    assert result == pytest.approx(0.3)


def test_sum3():  # относительная погрешность задается через rel = 0.05 это 5%
    result = 0.1 + 0.2
    assert result == pytest.approx(0.3 , rel=.05)

@pytest.mark.xfail(reason="если разница в approx abs> фактического то будет падение теста")
def test_sum4():  # Абсолютная погрешность задается через abc = 0.05 это конкретная разница в разных показаниях
    result = 0.1 + 0.2
    assert result == pytest.approx(0.3 , abs=.000000000000000000000000000004)

