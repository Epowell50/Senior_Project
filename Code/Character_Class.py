import math
import re

class Character:
    # Base Stats
    NAME = ""
    LEVEL = 0
    PROFICIENCY = 0
    STR = 0
    DEX = 0
    CON = 0
    INT = 0
    WIS = 0
    CHA = 0

    # Saves
    STR_SAVE = 0
    DEX_SAVE = 0
    CON_SAVE = 0
    INT_SAVE = 0
    WIS_SAVE = 0
    CHA_SAVE = 0

    # Skills
    ACROBATICS = 0          # DEX
    ANIMAL_HANDLING = 0     # WIS
    ARCANA = 0              # INT
    ATHLETICS = 0           # STR
    DECEPTION = 0           # CHA
    HISTORY = 0             # INT
    INSIGHT = 0             # WIS
    INTIMIDATION = 0        # CHA
    INVESTIGATION = 0       # INT
    MEDICINE = 0            # WIS
    NATURE = 0              # INT
    PERCEPTION = 0          # WIS
    PERFORMANCE = 0         # CHA
    PERSUASION = 0          # CHA
    RELIGION = 0            # INT
    SLEIGHT_OF_HAND = 0     # DEX
    STEALTH = 0             # DEX
    SURVIVAL = 0            # WIS
    PASSIVE_PERCEPTION = 0  # Base
    JACK_OF_ALL_TRADES = False #JOAT

    # Lists
    PROFICIENCIES = []
    EXPERTISES = []
    RESISTANCES = []
    VULNERABILITIES = []

    # Constructs a character with the given stats
    def __init__(self, name = "Unnamed", level = 0, str = 0, dex = 0, \
        con = 0, int = 0, wis = 0, cha = 0, prof = ["None"], res = ["None"], \
        vuln = ["None"], expert = ["None"], joat = False):
        self.NAME = name
        self.LEVEL = level
        self.STR = str
        self.DEX = dex
        self.CON = con
        self.INT = int
        self.WIS = wis
        self.CHA = cha
        self.PROFICIENCIES = prof
        self.EXPERTISES = expert
        self.RESISTANCES = res
        self.VULNERABILITIES = vuln
        self.JACK_OF_ALL_TRADES = joat

    # Represent function for disambiguation
    def __repr__(self):
        return "This is a 'Character' object."
    
    # Print function for displaying object
    def __str__(self):
        print("----- CHARACTER: " + self.NAME + " -----")
        print("Level: " + str(self.LEVEL))
        print("Proficiency bonus: " + self.format(self.PROFICIENCY))
        print("STRENGTH: " + str(self.STR) + \
            " (" + self.format(self.getMod(self.STR)) + ")")
        print("DEXTERITY: " + str(self.DEX) + \
            " (" + self.format(self.getMod(self.DEX)) + ")")
        print("CONSTITUTION: " + str(self.CON) + \
            " (" + self.format(self.getMod(self.CON)) + ")")
        print("INTELLIGENCE: " + str(self.INT) + \
            " (" + self.format(self.getMod(self.INT)) + ")")
        print("WISDOM: " + str(self.WIS) + \
            " (" + self.format(self.getMod(self.WIS)) + ")")
        print("CHARISMA: " + str(self.CHA) + \
            " (" + self.format(self.getMod(self.CHA)) + ")")
        print("\n----- SAVES -----")
        print("Strength Save: " + self.format(self.STR_SAVE))
        print("Dexterity Save: " + self.format(self.DEX_SAVE))
        print("Constitution Save: " + self.format(self.CON_SAVE))
        print("Intelligence Save: " + self.format(self.INT_SAVE))
        print("Wisdom Save: " + self.format(self.WIS_SAVE))
        print("Charisma Save: " + self.format(self.CHA_SAVE))
        print("\n----- SKILLS -----")
        print("Acrobatics: " + self.format(self.ACROBATICS))
        print("Animal Handling: " + self.format(self.ANIMAL_HANDLING))
        print("Arcana: " + self.format(self.ARCANA))
        print("Athletics: " + self.format(self.ATHLETICS))
        print("Deception: " + self.format(self.DECEPTION))
        print("History: " + self.format(self.HISTORY))
        print("Insight: " + self.format(self.INSIGHT))
        print("Intimidation " + self.format(self.INTIMIDATION))
        print("Investigation: " + self.format(self.INVESTIGATION))
        print("Medicine: " + self.format(self.MEDICINE))
        print("Nature: " + self.format(self.NATURE))
        print("Perception: " + self.format(self.PERCEPTION))
        print("Performance: " + self.format(self.PERFORMANCE))
        print("Persuasion: " + self.format(self.PERSUASION))
        print("Religion: " + self.format(self.RELIGION))
        print("Sleight of Hand: " + self.format(self.SLEIGHT_OF_HAND))
        print("Stealth: " + self.format(self.STEALTH))
        print("Survival: " + self.format(self.SURVIVAL))
        print("Passive Perception: " + str(10 + self.PERCEPTION))
        print("\n----- PROFICIENCIES -----")
        temp = [i.title() for i in self.PROFICIENCIES]
        print(temp)
        print("\n----- EXPERTISES -----")
        temp = [i.title() for i in self.EXPERTISES]
        print(temp)
        print("\n----- RESISTANCES -----")
        temp = [i.title() for i in self.RESISTANCES]
        print(temp)
        print("\n----- VULNERABILITIES -----")
        temp = [i.title() for i in self.VULNERABILITIES]
        print(temp)
        return ""
    
    # Adds a '+' symbol to positive numbers
    def format(self, num):
        if(num >= 0):
            return "+" + str(num)
        else:
            return str(num)
    
    # Checks against proficiency & expertise list and returns modifier
    def isProf(self, item):
        for i in self.EXPERTISES:
            if (item == i):
                return (2 * self.PROFICIENCY)
        for i in self.PROFICIENCIES:
            if(item == i):
                return self.PROFICIENCY
        return 0

    def addStat(self, stat = "stop", value = ""):
        if (stat == "expertise"):
            if(self.EXPERTISES[0] == "None" and self.PROFICIENCIES[0] == "None"):
                self.EXPERTISES.remove("None")
                self.PROFICIENCIES.remove("None")
                if(value.lower() not in self.EXPERTISES):
                    self.EXPERTISES.append(value.lower())
                if(value.lower() not in self.PROFICIENCIES):
                    self.PROFICIENCIES.append(value.lower())
            elif(self.EXPERTISES[0] == "None" and self.PROFICIENCIES[0] != "None"):
                self.EXPERTISES.remove("None")
                if(value.lower() not in self.EXPERTISES):
                    self.EXPERTISES.append(value.lower())
                if(value.lower() not in self.PROFICIENCIES):
                    self.PROFICIENCIES.append(value.lower())
            elif(self.EXPERTISES[0] != "None" and self.PROFICIENCIES[0] == "None"):
                self.PROFICIENCIES.remove("None")
                if(value.lower() not in self.EXPERTISES):
                    self.EXPERTISES.append(value.lower())
                if(value.lower() not in self.PROFICIENCIES):
                    self.PROFICIENCIES.append(value.lower())
            else:
                if(value.lower() not in self.EXPERTISES):
                    self.EXPERTISES.append(value.lower())
                if(value.lower() not in self.PROFICIENCIES):
                    self.PROFICIENCIES.append(value.lower())
        elif (stat == "proficiency"):
            if(self.PROFICIENCIES[0] == "None"):
                self.PROFICIENCIES.remove("None")
            if(value.lower() not in self.PROFICIENCIES):
                self.PROFICIENCIES.append(value.lower())
        elif (stat == "resistance"):
            if(self.RESISTANCES[0] == "None"):
                self.RESISTANCES.remove("None")
            if(value.lower() not in self.RESISTANCES):
                self.RESISTANCES.append(value.lower())
        elif (stat == "vulnerability"):
            if(self.VULNERABILITIES[0] == "None"):
                self.VULNERABILITIES.remove("None")
            if(value.lower() not in self.VULNERABILITIES):
                self.VULNERABILITIES.append(value.lower())
        elif (stat == "stop"):
            return
    
    def removeStat(self, stat = "stop", value = ""):
        if (stat == "proficiency" and (value.lower() in self.PROFICIENCIES)):
            self.PROFICIENCIES.remove(value.lower())
        elif (stat == "resistance" and (value.lower() in self.RESISTANCES)):
            self.RESISTANCES.remove(value.lower())
        elif (stat == "vunerability" and (value.lower() in self.VULNERABILITIES)):
            self.VULNERABILITIES.remove(value.lower())
        elif (stat == "stop"):
            return

    
    # Gets the modifier for the given stat
    def getMod(self, stat = 0, item = ""):
        mod = (int(stat) - 10) / 2
        joat = 0
        if(mod < 0):
            mod = math.floor(mod)
        if(self.JACK_OF_ALL_TRADES == True and \
            item != "" and \
            not(bool(re.match("\w*\ssaves$", item.lower()))) and \
            item.lower() not in self.PROFICIENCIES):
                joat = math.floor(self.PROFICIENCY / 2)
        return int(mod + self.isProf(item) + joat)
    
    # Sets the skills of the character using base stats
    def set_specs(self):
        # Set proficiency bonus
        self.PROFICIENCY = math.ceil( 1 + (self.LEVEL / 4))

        # Set skills
        self.ACROBATICS = \
            self.getMod(self.DEX, "acrobatics")
        self.ANIMAL_HANDLING = \
            self.getMod(self.WIS, "animal handling")
        self.ARCANA = \
            self.getMod(self.INT, "arcana")
        self.ATHLETICS = \
            self.getMod(self.STR, "athletics")
        self.DECEPTION = \
            self.getMod(self.CHA, "deception")
        self.HISTORY = \
            self.getMod(self.INT, "history")
        self.INSIGHT = \
            self.getMod(self.WIS, "insight")
        self.INTIMIDATION = \
            self.getMod(self.CHA, "intimidation")
        self.INVESTIGATION = \
            self.getMod(self.INT, "investigation")
        self.MEDICINE = \
            self.getMod(self.WIS, "medicine")
        self.NATURE = \
            self.getMod(self.INT, "nature")
        self.PERCEPTION = \
            self.getMod(self.WIS, "perception")
        self.PERFORMANCE = \
            self.getMod(self.CHA, "performance")
        self.PERSUASION = \
            self.getMod(self.CHA, "persuasion")
        self.RELIGION = \
            self.getMod(self.INT, "religion")
        self.SLEIGHT_OF_HAND = \
            self.getMod(self.DEX, "sleight of hand")
        self.STEALTH = \
            self.getMod(self.DEX, "stealth")
        self.SURVIVAL = \
            self.getMod(self.WIS, "survival")
        self.PASSIVE_PERCEPTION = self.getMod(self.WIS, "perception") + 10

        # Set saves
        self.STR_SAVE = \
            self.getMod(self.STR, "strength saves")
        self.DEX_SAVE = \
            self.getMod(self.DEX, "dexterity saves")
        self.CON_SAVE = \
            self.getMod(self.CON, "constitution saves")
        self.INT_SAVE = \
            self.getMod(self.INT, "intelligence saves")
        self.WIS_SAVE = \
            self.getMod(self.WIS, "wisdom saves")
        self.CHA_SAVE = \
            self.getMod(self.CHA, "charisma saves")

# TESTING CODE HERE
char = Character("Errant", 9, 10, 18, 14, 12, 14, 20)
char.addStat("expertise", "acrobatics")
char.addStat("expertise", "performance")
char.addStat("proficiency", "perception")
char.addStat("proficiency", "stealth")
char.addStat("proficiency", "charisma saves")
char.addStat("proficiency", "dexterity saves")
char.addStat("resistance", "fire")
char.JACK_OF_ALL_TRADES = True

char.set_specs()
#print(bool(re.match("\w*\ssave$", "Acrobatics")))
print(char)