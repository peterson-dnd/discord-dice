from dice.dice import * 

def parse(rolls: str) -> list:
    '''Parse a string into a list of dice and number and operator values'''
    # Example: "1d20 + 7"
    rolls_list = rolls.split(" ")
    return rolls_list

def build_dice(dice: str) -> Dice:
    number, sides = dice.split('d')
    if number == "" or int(number) < 1:
        number = "1"
    roll_list = [Die(int(sides)) for i in range(int(number))]
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