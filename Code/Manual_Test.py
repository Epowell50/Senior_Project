from Character_Class import *
from Pdf_Rip import *

characters = {ID: }
# TESTING CODE HERE
char1 = Character("Errant", 9, 66, 66, 16, 10, 18, 14, 12, 14, 20)
characters[str(char1.NAME)].append(char1)
char1.addStat("expertise", "acrobatics")
char1.addStat("expertise", "performance")
char1.addStat("proficiency", "perception")
char1.addStat("proficiency", "stealth")
char1.addStat("proficiency", "charisma saves")
char1.addStat("proficiency", "dexterity saves")
char1.addStat("resistance", "fire")
char1.JACK_OF_ALL_TRADES = True
newchar = rip("Test.pdf")
newchar.NAME = "Test1"
characters[newchar.NAME].append[newchar]

print(characters)