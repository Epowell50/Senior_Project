import math

class Character:
    # Base Stats
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

    # Lists
    PROFICIENCIES = []
    VULNERABILITIES = []
    RESISTANCES = []

    # Constructs a character with the given stats
    def __init__(self, str = 0, dex = 0, \
        con = 0, int = 0, wis = 0, cha = 0):
        STR = str
        DEX = dex
        CON = con
        INT = int
        WIS = wis
        CHA = cha
    
    # Gets the modifier for the given stat
    def getMod(self, stat):
        mod = (int(stat) - 10) / 2
        if(mod < 0):
            mod = math.floor(mod)
        return int(mod)

    # Checks against proficiency list and returns modifier
    def isProf(self, item):
        pass
    
    # Sets the skills of the character using base stats
    def set_specs(self):
        # Get base modifications
        strMod = self.getMod(self.STR)
        dexMod = self.getMod(self.DEX)
        conMod = self.getMod(self.CON)
        intMod = self.getMod(self.STR)
        wisMod = self.getMod(self.STR)
        chaMod = self.getMod(self.STR)

        # Set skills
        self.ACROBATICS = \
            dexMod + self.isProf("Acrobatics")
        self.ANIMAL_HANDLING = \
            wisMod + self.isProf("Animal Handling")
        self.ARCANA = \
            intMod + self.isProf("Arcana")
        self.ATHLETICS = \
            strMod + self.isProf("Athletics")
        self.DECEPTION = \
            chaMod + self.isProf("Deception")
        self.HISTORY = \
            intMod + self.isProf("History")
        self.INSIGHT = \
            wisMod + self.isProf("Insight")
        self.INTIMIDATION = \
            chaMod + self.isProf("Intimidation")
        self.INVESTIGATION = \
            intMod + self.isProf("Investigation")
        self.MEDICINE = \
            wisMod + self.isProf("Medicine")
        self.NATURE = \
            intMod + self.isProf("Nature")
        self.PERCEPTION = \
            wisMod + self.isProf("Perception")
        self.PERFORMANCE = \
            chaMod + self.isProf("Performance")
        self.PERSUASION = \
            chaMod + self.isProf("Persuasion")
        self.RELIGION = \
            intMod + self.isProf("Religion")
        self.SLEIGHT_OF_HAND = \
            dexMod + self.isProf("Sleight of Hand")
        self.STEALTH = \
            dexMod + self.isProf("Stealth")
        self.SURVIVAL = \
            wisMod + self.isProf("Survival")
        self.PASSIVE_PERCEPTION = self.PERCEPTION + 10

        # Set saves
        self.STR_SAVE = \
            strMod + self.isProf("Strength Saves")
        self.DEX_SAVE = \
            dexMod + self.isProf("Dexterity Saves")
        self.CON_SAVE = \
            conMod + self.isProf("Constitution Saves")
        self.INT_SAVE = \
            intMod + self.isProf("Intelligence Saves")
        self.WIS_SAVE = \
            wisMod + self.isProf("Wisdom Saves")
        self.CHA_SAVE = \
            chaMod + self.isProf("Charisma Saves")

# TESTING CODE HERE
char = Character()
user_input = input("Please input a stat: ")
out = char.getMod(user_input)
print(out)