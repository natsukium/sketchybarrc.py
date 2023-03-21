import pytest

from sketchybarrc._types import Nat, nat


def test_nat():
    value = 5
    actual = nat(value)
    expected = Nat(value)
    assert actual == expected
    assert actual == value


def test_nat_with_negative_integer():
    value = -10
    with pytest.raises(ValueError):
        nat(value)
