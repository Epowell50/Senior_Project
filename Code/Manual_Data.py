# Character Dictionary Declaration - Need to shift to class structure
Character = {
    0: {"STR": 0, "DEX": 0, "CON": 0, "INT": 0, "WIS": 0, "CHA": 0},                                                # STATISTICS
    1: {"Armor": 0, "HP CURR": 0, "HP MAX": 0, "TEMP": 0, "INIT": 0, "FAILED SAVES": 0, "SUCCESSFUL SAVES": 0},     # DEFENSE STATISTICS
    2: {"STR SAVE": 0, "DEX SAVE": 0, "CON SAVE": 0, "INT SAVE": 0, "WIS SAVE": 0, "CHA SAVE": 0},                  # SAVING THROWS
    3: {"ACROBATICS": 0, "ANIMAL HANDLING": 0, "ARCANA": 0, "ATHLETICS": 0, "DECEPTION": 0, "HISTORY": 0,           # SKILLS
        "INSIGHT": 0, "INTIMIDATION": 0, "INVESTIGATION": 0, "MEDICINE": 0, "NATURE": 0, "PERCEPTION": 0,           # |
        "PERFORMANCE": 0, "PERSUASION": 0, "RELIGION": 0, "SLEIGHT OF HAND": 0, "STEALTH": 0, "SURVIVAL": 0,        # |
        "PASSIVE PERCEPTION": 0},                                                                                   # _
    4: {"VULNERABILITIES": [], "RESISTANCES": [], "IMMUNITIES": [], "EXHAUSTION": 0},                               # DAMAGE INFO
    # Likely going to split the below into an associated dictionary for ease of access
    5: {"ACTIONS": [], "REACTIONS": [], "BONUS ACTIONS": [], "PASSIVES": []}                                        # ACTIONS AND REACTIONS
}

# Info screen to help user
def info_screen(screen):
    for c_info in Character[int(screen)]:
        print(c_info + ":", Character[int(screen)][c_info])

# - Begins data prompt for character entry -
print("Beginning character data entry...")

# Iterate through each item
for c_stat, c_info in Character.items():
    # Iterate through each sub-item
    for item in c_info:
        # Print for user readability
        print("- Character Statistics -")
        info_screen(int(c_stat))
        print("")
        input_val = input(str(item) + ": ")
        Character[int(c_stat)][str(item)] = input_val
        print("")

# Final print for data verification
print(" --- FINAL CHARACTER --- ")
for c_stat, c_info in Character.items():
    print("----------------")
    info_screen(int(c_stat))