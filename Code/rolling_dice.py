# This file is used to roll dice for the main program

import random

# Rolls x dice that have y sides
def roll(sides = 1):
    num = random.randint(1, sides)
    return num

info = input("How many sides: ")
print(roll(int(info)))