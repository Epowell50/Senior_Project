# This file is used to roll dice for the main program

import random

# Class that contains all dice actions
class Dice:

# Rolls x dice that have y sides
    def roll(sides = 0):
        if(sides != 0):
            num = random.randint(0, sides)
            return num
        else:
            return 0


