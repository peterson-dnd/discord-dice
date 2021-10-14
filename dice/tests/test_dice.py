from dice.dice import *

def test_die_sides():
    die = Die(6)
    assert die.sides == 6

def test_die_roll_action_negative():
    die = Die(6)
    
    assert die.has_rolled == False

def test_die_roll_action_positive():
    die = Die(6)
    die.roll()

    assert die.has_rolled == True

def test_die_result_range():
    die = Die(6)
    die.roll()
    assert die.result > 0 and die.result <= 6

def test_die_result_randomness():
    results = []
    for i in range(50):
        die = Die(50000)
        die.roll()
        assert die.result not in results
        results.append(die.result)

    

def test_die_result_min():
    die = Die(1)
    die.roll()

    assert die.result == 1

def test_die_result_max():
    results = []
    max = 2
    for i in range(50):
        die = Die(max)
        die.roll()
        results.append(die.result)
    
    assert max in results

def test_dice_action_positive():
    pass

def test_dice_action_negative():
    pass
