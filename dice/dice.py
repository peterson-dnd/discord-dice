import random
import logging

class Die:

    def __init__(self, sides: int):
        self.sides = int(sides)
        self.has_rolled = False
        self.result = None

    def __str__(self):
        return f'Sides: {self.sides}\nHas been rolled: {self.has_rolled}\nResult: {self.result}'

    def roll(self):
        self.result = random.randint(1, self.sides)
        logging.debug(f'{self}')
        self.has_rolled = True



class Dice:

    def __init__(self, *dice: Die):
        self.dice = list(dice)
        self.total = None
        self.has_rolled = False

    def roll(self):
        for die in self.dice:
            if not die.has_rolled:
                die.roll()
        self.has_rolled = True
        self._total()
    
    def _total(self):
        dice_total = 0
        for die in self.dice:
            dice_total += die.result
        self.total = dice_total        

    def __str__(self):
        result = ""
        for die in self.dice:
            result += str(die) + "\n"
        return result