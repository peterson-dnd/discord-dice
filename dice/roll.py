from dice.utils import *
from dice.dice import *

class Roll():

    def __init__(self, roll: list):
        
        self.raw_roll = roll # Example: ["1d10", "+", "8"]
        self.dice_roll = None
        self.rolled_dice = None

        self._build_roll() 
        self.sum = 0


    def _build_roll(self): 
        queue = []
        for i in self.raw_roll:
            if 'd' in i:
                queue.append(build_dice(i))
            else:
                queue.append(i)
        self.dice_roll = queue

    def _sum_roll(self):
        numbers = []
        for i in self.dice_roll:
            if type(i) == Dice:
                if not i.has_rolled:
                    raise Exception("Dice hasn't been rolled before sum.")
                numbers.append(i.total)
            else:
                if i is '-' or i is '+':
                    numbers.append(i)
                else:
                    numbers.append(int(i))
        self.rolled_dice = numbers
                

    def roll(self):
        for i in self.dice_roll:
            if type(i) is Dice:
                i.roll()
        self._sum_roll()
        self._calc_total()

    def _calc_total(self):
        total = self.rolled_dice[0] # Initialize as the first element of the list (should be an Integer)

        operation = None
        for i in self.rolled_dice[1:]:
            
            if isinstance(i, int):
                total = process_operation(total, operation, i)
            else:
                operation = i


        self.sum = total

    def dice_roll_to_str(self):
        answer = ""
        for i in self.dice_roll:
            answer += str(i)
        return answer

    def rolled_dice_to_str(self):
        answer = ""
        for i in self.dice_roll:
            answer += str(i) + ""
        return answer
    

    def __str__(self):
        return f'Original Roll: {self.raw_roll}\nParsed Numbers: {self.dice_roll_to_str()}\nSum Total: {self.sum}'