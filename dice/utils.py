from dice.dice import * 

def parse(rolls: str) -> list:
    '''Parse a string into a list of dice and number and operator values'''
    # Example: "1d20 + 7"
    rolls_list = rolls.split(" ")
    return rolls_list

def _build_dice(dice: str) -> Die:
    number, sides = dice.split('d')
    if number == "" or int(number) < 1:
        number = "1"
    return (int(number), int(sides))


def build_dice(dice: str) -> Dice:
    number, sides = _build_dice(dice)
    roll_list = [Die(sides) for i in range(number)]
    roll = Dice(*roll_list)

    return roll 

def process_operation(left: int, operation: str, right: int) -> int:
    plus = '+'
    minus = '-'

    if operation is plus:
        return left + right
    if operation is minus:
        return left - right

    raise Exception("Unrecognized operation: %s", operation)
