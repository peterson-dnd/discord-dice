from dice.roll import *

test_roll = ["20d1", "+", "8"]

def test_roll_build():
    r = Roll(test_roll)
    r.roll()

    assert r.sum == 28
