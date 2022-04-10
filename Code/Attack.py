from Action import *


class Attack(Action):
    TYPE = "" # Melee, Ranged, Thrown, Finesse, Versatile
    WEAPON_TYPE = "" # Martial, Simple, etc.
    RANGE = 0 # Used for ranged weapons, default is 5ft
    DAMAGE = "" # Damage dice
    SAVE_DAMAGE = "" # Damage dice if requriing a save


    # Constructs an action with the given variables
    def __init__(self, name: str = "Unnamed", desc: str = "None", \
        atype: str = "Main Action", save: bool = False, type: str = "Melee", \
        wtype: str = "Simple", range: int = 5, dmg: str = "0d0", \
        sdmg: str = "0d0"):
        self.NAME = name
        self.DESCRIPTION = desc
        self.ACTION_TYPE = atype
        self.REQUIRES_SAVE = save
        self.TYPE = type
        self.WEAPON_TYPE = wtype
        self.RANGE = range
        self.DAMAGE = dmg
        self.SAVE_DAMAGE = sdmg

    
    # Represent function for disambiguation
    def __repr__(self) -> str:
        return "This is an 'Attack' object."

    # Print function for displaying object
    def __str__(self) -> str:
        print("Name: " + self.NAME)
        print("Desc: " + self.DESCRIPTION)
        print("Action Type: " + self.ACTION_TYPE)
        print("Requires Save?: " + self.REQUIRES_SAVE)
        print("Type: " + self.TYPE)
        print("Weapon Type: " + self.WEAPON_TYPE)
        print("Range: " + self.RANGE)
        print("Damage Dice: " + self.DAMAGE)
        print("Save Damage: " + self.SAVE_DAMAGE)