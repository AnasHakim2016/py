import pytest

def double(n):
    if not isinstance(n, (int, float)):
        raise TypeError("double erwartet eine Zahl")
    return n * 2


def test_double_verdoppelt_eine_zahl():
    assert double(5) == 10


def test_double_bei_null():
    assert double(0) == 0


def test_double_lehnt_text_ab():
    with pytest.raises(TypeError):
        double("a")

test_double_verdoppelt_eine_zahl()
test_double_bei_null()
test_double_lehnt_text_ab() 