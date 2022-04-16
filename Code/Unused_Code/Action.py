class Action:
    NAME = ""
    DESCRIPTION = "" # Explain the ability
    ACTION_TYPE = "" # Bonus, reaction, spell, main action
    REQUIRES_SAVE = False

    # Constructs an action with the given variables
    def __init__(self, name: str = "Unnamed", desc: str = "None", \
        type: str = "Main Action", save: bool = False):
        self.NAME = name
        self.DESCRIPTION = desc
        self.ACTION_TYPE = type
        self.REQUIRES_SAVE = save
    
    # Represent function for disambiguation
    def __repr__(self) -> str:
        return "This is an 'Action' object."

    # Print function for displaying object
    def __str__(self) -> str:
        print("Name: " + self.NAME)
        print("Desc: " + self.DESCRIPTION)
        print("Action Type: " + self.ACTION_TYPE)
        print("Requires Save?: " + self.REQUIRES_SAVE)