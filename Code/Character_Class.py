import math

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

    # Lists
    PROFICIENCIES = []
    EXPERTISES = []
    RESISTANCES = []
    VULNERABILITIES = []

    # Constructs a character with the given stats
    def __init__(self, name = "Unnamed", level = 0, str = 0, dex = 0, \
        con = 0, int = 0, wis = 0, cha = 0, prof = ["None"], res = ["None"], vuln = ["None"], expert = ["None"]):
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

    # Represent function for disambiguation
    def __repr__(self):
        return "This is a 'Character' object."
    
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
        print("Strength Save: " + self.format(self.getMod(self.STR, "strength saves")))
        print("Dexterity Save: " + self.format(self.getMod(self.DEX, "dexterity saves")))
        print("Constitution Save: " + self.format(self.getMod(self.CON, "constitution saves")))
        print("Intelligence Save: " + self.format(self.getMod(self.INT, "intelligence saves")))
        print("Wisdom Save: " + self.format(self.getMod(self.WIS, "wisdom saves")))
        print("Charisma Save: " + self.format(self.getMod(self.CHA, "charisma saves")))
        print("\n----- SKILLS -----")
        print("Acrobatics: " + self.format(self.getMod(self.DEX, "acrobatics")))
        print("Animal Handling: " + self.format(self.getMod(self.WIS, "animal handling")))
        print("Arcana: " + self.format(self.getMod(self.INT, "arcana")))
        print("Athletics: " + self.format(self.getMod(self.STR, "athletics")))
        print("Deception: " + self.format(self.getMod(self.CHA, "deception")))
        print("History: " + self.format(self.getMod(self.INT, "history")))
        print("Insight: " + self.format(self.getMod(self.WIS, "insight")))
        print("Intimidation " + self.format(self.getMod(self.CHA, "intimidation")))
        print("Investigation: " + self.format(self.getMod(self.INT, "investigation")))
        print("Medicine: " + self.format(self.getMod(self.WIS, "medicine")))
        print("Nature: " + self.format(self.getMod(self.INT, "nature")))
        print("Perception: " + self.format(self.getMod(self.WIS, "perception")))
        print("Performance: " + self.format(self.getMod(self.CHA, "performance")))
        print("Persuasion: " + self.format(self.getMod(self.CHA, "persuasion")))
        print("Religion: " + self.format(self.getMod(self.INT, "religion")))
        print("Sleight of Hand: " + self.format(self.getMod(self.DEX, "sleight of hand")))
        print("Stealth: " + self.format(self.getMod(self.DEX, "stealth")))
        print("Survival: " + self.format(self.getMod(self.WIS, "survival")))
        print("Passive Perception: " + str(10 + self.getMod(self.WIS, "perception")))
        print("\n----- PROFICIENCIES -----")
        temp = [i.title() for i in self.PROFICIENCIES]
        print(temp)
        print("\n----- EXPERTISES -----")
        temp = [i.title() for i in self.EXPERTISES]
        print(temp)
        print("\n----- RESISTANCES -----")
        temp = [i.title() for i in self.RESISTANCES]
        print(self.RESISTANCES)
        print("\n----- VULNERABILITIES -----")
        temp = [i.title() for i in self.VULNERABILITIES]
        print(self.VULNERABILITIES)
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
            try:
                self.EXPERTISES.remove("None")
                self.EXPERTISES.append(value.lower())
                self.PROFICIENCIES.append(value.lower())
            except:
                self.EXPERTISES.append(value.lower())
                self.PROFICIENCIES.appen(value.lower())
        elif (stat == "proficiency"):
            try:
                self.PROFICIENCIES.remove("None")
                self.PROFICIENCIES.append(value.lower())
            except:
                self.PROFICIENCIES.append(value.lower())
        elif (stat == "resistance"):
            try:
                self.RESISTANCES.remove("None")
                self.RESISTANCES.append(value.lower())
            except:
                self.RESISTANCES.append(value.lower())
        elif (stat == "vunerability"):
            try:
                self.VULNERABILITIES.remove("None")
                self.VULNERABILITIES.append(value.lower())
            except:
                self.VULNERABILITIES.append(value.lower())
        elif (stat == "stop"):
            return
    
    def removeStat(self, stat = "stop", value = ""):
        if (stat == "proficiency"):
            self.PROFICIENCIES.remove(value.lower())
        elif (stat == "resistance"):
            self.RESISTANCES.remove(value.lower())
        elif (stat == "vunerability"):
            self.VULNERABILITIES.remove(value.lower())
        elif (stat == "stop"):
            return

    
    # Gets the modifier for the given stat
    def getMod(self, stat = 0, item = ""):
        mod = (int(stat) - 10) / 2
        if(mod < 0):
            mod = math.floor(mod)
        return int(mod + self.isProf(item))
    
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
char.set_specs()
print(char)