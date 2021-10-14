from dice.roll import *
import logging

test_roll = ["1d20", "+", "8"]

def test_roll_build():
    roll = Roll(test_roll)
    assert False