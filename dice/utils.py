from dice.dice import * 

def parse(rolls: str) -> list:
    '''Parse a string into a stack of commands'''
    # Example: "1d20 + 7"
    stack = rolls.split(" ")
    return stack

def build_dice(dice: str) -> Dice:
    number, sides = dice.split('d')
    roll_list = [Die(sides) for i in number]
    roll = Dice(*roll_list)

    print(f'Roll: {str(roll)}')
    return roll 

def roll_dice():
    pass

def roll(dice: str):
    pass

def process_operation(left: int, operation: str, right: int) -> int:
    plus = '+'
    minus = '-'

    if operation is plus:
        return left + right
    if operation is minus:
        return left - right

    raise Exception("Unrecognized operation: %s", operation)