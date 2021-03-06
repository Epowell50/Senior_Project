from sqlite3 import IntegrityError
from Character_Class import *
from Pdf_Rip import rip
from SQLite import *

# Creates character list for program during runtime
characters = []

print("Hello and welcome to the DND Utilities python tool!")
print("This program was created by Ethan Powell in fulfillment of " + \
      "the requirements of a BS in Cybersecurity and BS in Computer Science")
print("----------------------------------------------------------\n")
print("Loading saved characters...")

# Create the database file if it doesn't exist
initialize()
# Loads characters from database. Temporary fix until references to database can be made in program
characters = query_all()

print("To begin, please select from the options below by typing the number associated: ")

# Base program loop
while(True):
    print("----- DND Utilities -----")
    print("1: Create Character\n2: Edit Character\n3: Import Character from PDF\n4: View Characters\n5. Delete Character")
    print("Type 'stop' or press ENTER to quit.")
    temp = input("Selection: ")

    if(temp.lower() == "stop"):
        print("Goodbye!")
        break
    elif(temp.lower() == ""):
        print("Saving characters...")
        for i in characters:
            try:
                insert_char(i)
            except IntegrityError: # This is a temporary fix until a better update can be handled
                remove_char(i.NAME)
                insert_char(i)
                pass
        print("Goodbye!")
        break
    elif(temp == "1"): # Create character functionality
        print("\n\n\n\n\n\n\n\n\n\n")
        while(True):
            print("----- Create Character -----")
            print("\nSaved Characters: ")
            for i in characters:
                print(i.NAME)
            print("")
            name = input("Please type your new character's name or press ENTER to go back: ")
            if(name == ""):
                print("\n\n\n\n\n\n\n\n\n\n")
                break
            # Level input
            level = 'a'
            while(not(level.isdigit())):
                level = input("Please type " + name + "'s level: ")
                if(not(level.isdigit())):
                    print("\nPlease enter a positive number with no alphabetic characters.")
            # HP input
            flag = 1
            while(flag):
                currhp = input("Please type " + name + "'s current HP: ")
                try:
                    currhp = int(currhp)
                    flag = 0
                except ValueError:
                    print("\nPlease input an integer value.")
            flag = 1
            while(flag):
                maxhp = input("Please type " + name + "'s max HP: ")
                try:
                    maxhp = int(maxhp)
                    if(currhp > maxhp):
                        print("\nMaximum HP cannot be smaller than current hp.")
                    if(maxhp >= currhp and int(maxhp)):
                        flag = 0
                except ValueError:
                    print("\nPlease input an integer value.")
            # AC input
            ac = 'a'
            while(not(ac.isdigit())):
                ac = input("Please type " + name + "'s armor class: ")
                if(not(ac.isdigit())):
                    print("\nPlease enter a positive number with no alphabetic characters.")
            # Strength input
            stren = 'a'
            while(not(stren.isdigit())):
                stren = input("Please type " + name + "'s strength score: ")
                if(not(stren.isdigit())):
                    print("\nPlease enter a positive number with no alphabetic characters.")
            # Dexterity input
            dex = 'a'
            while(not(dex.isdigit())):
                dex = input("Please type " + name + "'s dexterity score: ")
                if(not(dex.isdigit())):
                    print("\nPlease enter a positive number with no alphabetic characters.")
            # Constitution input
            con = 'a'
            while(not(con.isdigit())):
                con = input("Please type " + name + "'s constitution score: ")
                if(not(con.isdigit())):
                    print("\nPlease enter a positive number with no alphabetic characters.")
            # Intelligence input
            intel = 'a'
            while(not(intel.isdigit())):
                intel = input("Please type " + name + "'s intelligence score: ")
                if(not(level.isdigit())):
                    print("\nPlease enter a positive number with no alphabetic characters.")
            # Wisdom input
            wis = 'a'
            while(not(wis.isdigit())):
                wis = input("Please type " + name + "'s wisdom score: ")
                if(not(wis.isdigit())):
                    print("\nPlease enter a positive number with no alphabetic characters.")
            # Charisma input
            cha = 'a'
            while(not(cha.isdigit())):
                cha = input("Please type " + name + "'s charisma score: ")
                if(not(cha.isdigit())):
                    print("\nPlease enter a positive number with no alphabetic characters.")
            newchar = Character(name, int(level), int(currhp), int(maxhp), \
                                int(ac), int(stren), int(dex), int(con), \
                                int(intel), int(wis), int(cha))
            print("----- " + name + "'s Statistics -----\n")
            print("Level: " + str(level))
            print("HP: " + str(currhp) + "/" + str(maxhp))
            print("Armor Class: " + str(ac))
            print("STR: " + str(stren) + " (" + newchar.format(newchar.getMod(stren)) + ")")
            print("DEX: " + str(dex) + " (" + newchar.format(newchar.getMod(dex)) + ")")
            print("CON: " + str(con) + " (" + newchar.format(newchar.getMod(con)) + ")")
            print("INT: " + str(intel) + " (" + newchar.format(newchar.getMod(intel)) + ")")
            print("WIS: " + str(wis) + " (" + newchar.format(newchar.getMod(wis)) + ")")
            print("CHA: " + str(cha) + " (" + newchar.format(newchar.getMod(cha)) + ")")
            userinput = input("\n Does this look right (y/n)? ")
            print("\n\n\n\n\n\n\n\n\n\n")
            if(userinput == "Y" or userinput == "y" or userinput == "Yes" or userinput == "yes"):
                characters.append(newchar)
                print("\n\n\n\n\n\n\n\n\n\n")
                break
    elif(temp == "2"): # Edit character functionality
        print("\n\n\n\n\n\n\n\n\n\n")
        while(True):
            print("----- Edit Character -----")
            print("\nSaved Characters: ")
            for i in characters:
                print(i.NAME)
            print("")
            name = input("Please type the character's name you wish to edit or press ENTER to go back: ")
            if(name == ""):
                print("\n\n\n\n\n\n\n\n\n\n")
                break
            else:
                flag = False
                for i in characters:
                    if(i.NAME.lower() == name.lower()):
                        flag = True
                        print("\n\n\n\n\n\n\n\n\n\n")
                        while(True):
                            print("----- Editing Character: " + name + " -----")
                            print("1. Base Stats\n2. Saves\n3. Skills\n4. Proficiencies & Expertises\n" + \
                                  "5. Resistances\n6. Vulnerabilities\n7. Enable/Disable Jack of All Trades")
                            option = input("Please choose the section you wish to edit or press ENTER to go back: ")
                            if(option == ""):
                                print("\n\n\n\n\n\n\n\n\n\n")
                                break
                            elif(option == "1"): # Edit base stats
                                print("\n\n\n\n\n\n\n\n\n\n")
                                while(True):
                                    print("----- Editing Character: " + name + "(Base Stats) -----")
                                    print("Level: " + str(i.LEVEL))
                                    print("Proficiency bonus: " + i.format(i.PROFICIENCY))
                                    print("Initiative: " + i.format(i.INITIATIVE))
                                    print("AC: " + str(i.AC))
                                    print("HP: " + str(i.CURRENT_HP) + "/" + str(i.MAX_HP))
                                    print("STRENGTH: " + str(i.STR) + \
                                        " (" + i.format(i.getMod(i.STR)) + ")")
                                    print("DEXTERITY: " + str(i.DEX) + \
                                        " (" + i.format(i.getMod(i.DEX)) + ")")
                                    print("CONSTITUTION: " + str(i.CON) + \
                                        " (" + i.format(i.getMod(i.CON)) + ")")
                                    print("INTELLIGENCE: " + str(i.INT) + \
                                        " (" + i.format(i.getMod(i.INT)) + ")")
                                    print("WISDOM: " + str(i.WIS) + \
                                        " (" + i.format(i.getMod(i.WIS)) + ")")
                                    print("CHARISMA: " + str(i.CHA) + \
                                        " (" + i.format(i.getMod(i.CHA)) + ")")
                                    selection = input("\nPlease enter the statistic you wish to edit or press ENTER to go back: ")
                                    if(selection == ""):
                                        print("\n\n\n\n\n\n\n\n\n\n")
                                        break
                                    elif(selection.lower() == "level"):
                                        level = 'a'
                                        while(not level.isdigit()):
                                            level = input(name + "'s new level: ")
                                            if(not level.isdigit()):
                                                print("Please enter a positive number with no alphabetic characters.")
                                        i.LEVEL = int(level)
                                    elif(selection.lower() == "proficiency bonus"):
                                        prof = 'a'
                                        while(not prof.isdigit()):
                                            prof = input(name + "'s new proficiency bonus: ")
                                            if(not prof.isdigit()):
                                                print("Please enter a positive number with no alphabetic characters.")
                                        i.PROFICIENCY = int(prof)
                                    elif(selection.lower() == "initiative"):
                                        initi = 'a'
                                        while(not initi.isdigit()):
                                            initi = input(name + "'s new initiative: ")
                                            if(not initi.isdigit()):
                                                print("Please enter a positive number with no alphabetic characters.")
                                        i.INITIATIVE = int(initi)
                                    elif(selection.lower() == "ac"):
                                        ac = 'a'
                                        while(not ac.isdigit()):
                                            ac = input(name + "'s new AC: ")
                                            if(not ac.isdigit()):
                                                print("Please enter a positive number with no alphabetic characters.")
                                        i.AC = int(ac)
                                    elif(selection.lower() == "hp"):
                                        while(True):
                                            print("HP: " + str(i.CURRENT_HP) + "/" + str(i.MAX_HP))
                                            hpedit = input("Edit 'current' or 'max' hp or press ENTER to return: ")
                                            if(hpedit == ""):
                                                print("\n\n\n\n\n\n\n\n\n\n")
                                                break
                                            elif(hpedit == "curr" or hpedit == "current"):
                                                t = int(input(name + "'s new current HP: "))
                                                while(t > i.MAX_HP):
                                                    print("\nCurrent HP cannot be greater than max HP")
                                                    t = int(input(name + "'s new current HP: "))
                                                i.CURRENT_HP = t
                                            elif(hpedit == "max" or hpedit == "maximum"):
                                                i.MAX_HP = int(input(name + "'s new max HP: "))
                                            else:
                                                print("\n\n\n\n\n\n\n\n\n\n")
                                                print("Please choose 'current' or 'maximum' HP")
                                    elif(selection.lower() == "strength" or selection.lower() == "str"):
                                        t = 'a'
                                        while(not t.isdigit()):
                                            t = input(name + "'s new strength score: ")
                                            if(not t.isdigit()):
                                                print("Please enter a positive number with no alphabetic characters.")
                                        i.STR = int(t)
                                    elif(selection.lower() == "dexterity" or selection.lower() == "dex"):
                                        t = 'a'
                                        while(not t.isdigit()):
                                            t = input(name + "'s new dexterity score: ")
                                            if(not t.isdigit()):
                                                print("Please enter a positive number with no alphabetic characters.")
                                        i.DEX = int(t)
                                    elif(selection.lower() == "constitution" or selection.lower() == "con"):
                                        t = 'a'
                                        while(not t.isdigit()):
                                            t = input(name + "'s new constitution score: ")
                                            if(not t.isdigit()):
                                                print("Please enter a positive number with no alphabetic characters.")
                                        i.CON = int(t)
                                    elif(selection.lower() == "intelligence" or selection.lower() == "int"):
                                        t = 'a'
                                        while(not t.isdigit()):
                                            t = input(name + "'s new intelligence score: ")
                                            if(not t.isdigit()):
                                                print("Please enter a positive number with no alphabetic characters.")
                                        i.INT = int(t)
                                    elif(selection.lower() == "wisdom" or selection.lower() == "wis"):
                                        t = 'a'
                                        while(not t.isdigit()):
                                            t = input(name + "'s new wisdom score: ")
                                            if(not t.isdigit()):
                                                print("Please enter a positive number with no alphabetic characters.")
                                        i.WIS = int(t)
                                    elif(selection.lower() == "charisma" or selection.lower() == "cha"):
                                        t = 'a'
                                        while(not t.isdigit()):
                                            t = input(name + "'s new dexterity score: ")
                                            if(not t.isdigit()):
                                                print("Please enter a positive number with no alphabetic characters.")
                                        i.CHA = int(t)
                                    else:
                                        print("\n\n\n\n\n\n\n\n\n\n")
                                        print("Please choose from the listed options below")
                            elif(option == "2"): # Edit Saves
                                while(True):
                                    print("----- Editing Character: " + name + "(Saves) -----")
                                    print("Strength Save: " + i.format(i.STR_SAVE))
                                    print("Dexterity Save: " + i.format(i.DEX_SAVE))
                                    print("Constitution Save: " + i.format(i.CON_SAVE))
                                    print("Intelligence Save: " + i.format(i.INT_SAVE))
                                    print("Wisdom Save: " + i.format(i.WIS_SAVE))
                                    print("Charisma Save: " + i.format(i.CHA_SAVE))
                                    selection = input("\nPlease enter the statistic you wish to edit or press ENTER to go back: ")
                                    if(selection == ""):
                                        print("\n\n\n\n\n\n\n\n\n\n")
                                        break
                                    elif(selection.lower() == "strength save" or selection.lower() == "str save" \
                                            or selection.lower() == "str"):
                                        t = 'a'
                                        while(not t.isdigit()):
                                            t = input(name + "'s new strength save: ")
                                            if(not t.isdigit()):
                                                print("Please enter a positive number with no alphabetic characters.")
                                        i.STR_SAVE = int(input(name + "'s new strength save: "))
                                    elif(selection.lower() == "dexterity save" or selection.lower() == "dex save" \
                                            or selection.lower() == "dex"):
                                        t = 'a'
                                        while(not t.isdigit()):
                                            t = input(name + "'s new dexterity save: ")
                                            if(not t.isdigit()):
                                                print("Please enter a positive number with no alphabetic characters.")
                                        i.DEX_SAVE = int(t)
                                    elif(selection.lower() == "constitution save" or selection.lower() == "con save" \
                                            or selection.lower() == "con"):
                                        t = 'a'
                                        while(not t.isdigit()):
                                            t = input(name + "'s new constitution save: ")
                                            if(not t.isdigit()):
                                                print("Please enter a positive number with no alphabetic characters.")
                                        i.CON_SAVE = int(t)
                                    elif(selection.lower() == "intelligence save" or selection.lower() == "int save" \
                                            or selection.lower() == "int"):
                                        t = 'a'
                                        while(not t.isdigit()):
                                            t = input(name + "'s new intelligence save: ")
                                            if(not t.isdigit()):
                                                print("Please enter a positive number with no alphabetic characters.")
                                        i.INT_SAVE = int(t)
                                    elif(selection.lower() == "wisdom save" or selection.lower() == "wis" \
                                            or selection.lower() == "wis"):
                                        t = 'a'
                                        while(not t.isdigit()):
                                            t = input(name + "'s new wisdom save: ")
                                            if(not t.isdigit()):
                                                print("Please enter a positive number with no alphabetic characters.")
                                        i.WIS_SAVE = int(t)
                                    elif(selection.lower() == "charisma save" or selection.lower() == "cha save" \
                                            or selection.lower() == "cha"):
                                        t = 'a'
                                        while(not t.isdigit()):
                                            t = input(name + "'s new charisma save: ")
                                            if(not t.isdigit()):
                                                print("Please enter a positive number with no alphabetic characters.")
                                        i.CHA_SAVE = int(t)
                                    else:
                                        print("\n\n\n\n\n\n\n\n\n\n")
                                        print("Please choose from the listed options below")
                            elif(option == "3"): # Edit Skills
                                while(True):
                                    print("----- Editing Character: " + name + "(Skills) -----")
                                    print("Acrobatics: " + i.format(i.ACROBATICS))
                                    print("Animal Handling: " + i.format(i.ANIMAL_HANDLING))
                                    print("Arcana: " + i.format(i.ARCANA))
                                    print("Athletics: " + i.format(i.ATHLETICS))
                                    print("Deception: " + i.format(i.DECEPTION))
                                    print("History: " + i.format(i.HISTORY))
                                    print("Insight: " + i.format(i.INSIGHT))
                                    print("Intimidation " + i.format(i.INTIMIDATION))
                                    print("Investigation: " + i.format(i.INVESTIGATION))
                                    print("Medicine: " + i.format(i.MEDICINE))
                                    print("Nature: " + i.format(i.NATURE))
                                    print("Perception: " + i.format(i.PERCEPTION))
                                    print("Performance: " + i.format(i.PERFORMANCE))
                                    print("Persuasion: " + i.format(i.PERSUASION))
                                    print("Religion: " + i.format(i.RELIGION))
                                    print("Sleight of Hand: " + i.format(i.SLEIGHT_OF_HAND))
                                    print("Stealth: " + i.format(i.STEALTH))
                                    print("Survival: " + i.format(i.SURVIVAL))
                                    print("Passive Perception: " + str(10 + i.PERCEPTION))
                                    selection = input("\nPlease enter the skill you wish to edit or press ENTER to go back: ")
                                    if(selection == ""):
                                            print("\n\n\n\n\n\n\n\n\n\n")
                                            break
                                    elif(selection.lower() == "acrobatics"):
                                        t = 'a'
                                        while(not t.isdigit()):
                                            t = input(name + "'s new acrobatics: ")
                                            if(not t.isdigit()):
                                                print("Please enter a positive number with no alphabetic characters.")
                                        i.ACROBATICS = int(t)
                                    elif(selection.lower() == "animal handling"):
                                        t = 'a'
                                        while(not t.isdigit()):
                                            t = input(name + "'s new animal handling: ")
                                            if(not t.isdigit()):
                                                print("Please enter a positive number with no alphabetic characters.")
                                        i.ANIMAL_HANDLING = int(t)
                                    elif(selection.lower() == "arcana"):
                                        t = 'a'
                                        while(not t.isdigit()):
                                            t = input(name + "'s new arcana: ")
                                            if(not t.isdigit()):
                                                print("Please enter a positive number with no alphabetic characters.")
                                        i.ARCANA = int(t)
                                    elif(selection.lower() == "athletics"):
                                        t = 'a'
                                        while(not t.isdigit()):
                                            t = input(name + "'s new athletics: ")
                                            if(not t.isdigit()):
                                                print("Please enter a positive number with no alphabetic characters.")
                                        i.ATHLETICS = int(t)
                                    elif(selection.lower() == "deception"):
                                        t = 'a'
                                        while(not t.isdigit()):
                                            t = input(name + "'s new deception: ")
                                            if(not t.isdigit()):
                                                print("Please enter a positive number with no alphabetic characters.")
                                        i.DECEPTION = int(t)
                                    elif(selection.lower() == "history"):
                                        t = 'a'
                                        while(not t.isdigit()):
                                            t = input(name + "'s new history: ")
                                            if(not t.isdigit()):
                                                print("Please enter a positive number with no alphabetic characters.")
                                        i.HISTORY = int(t)
                                    elif(selection.lower() == "insight"):
                                        t = 'a'
                                        while(not t.isdigit()):
                                            t = input(name + "'s new insight: ")
                                            if(not t.isdigit()):
                                                print("Please enter a positive number with no alphabetic characters.")
                                        i.INSIGHT = int(t)
                                    elif(selection.lower() == "intimidation"):
                                        t = 'a'
                                        while(not t.isdigit()):
                                            t = input(name + "'s new intimidation: ")
                                            if(not t.isdigit()):
                                                print("Please enter a positive number with no alphabetic characters.")
                                        i.INTIMIDATION = int(t)
                                    elif(selection.lower() == "investigation"):
                                        t = 'a'
                                        while(not t.isdigit()):
                                            t = input(name + "'s new investigation: ")
                                            if(not t.isdigit()):
                                                print("Please enter a positive number with no alphabetic characters.")
                                        i.INVESTIGATION = int(t)
                                    elif(selection.lower() == "medicine"):
                                        t = 'a'
                                        while(not t.isdigit()):
                                            t = input(name + "'s new medicine: ")
                                            if(not t.isdigit()):
                                                print("Please enter a positive number with no alphabetic characters.")
                                        i.MEDICINE = int(t)
                                    elif(selection.lower() == "nature"):
                                        t = 'a'
                                        while(not t.isdigit()):
                                            t = input(name + "'s new nature: ")
                                            if(not t.isdigit()):
                                                print("Please enter a positive number with no alphabetic characters.")
                                        i.NATURE = int(t)
                                    elif(selection.lower() == "perception"):
                                        t = 'a'
                                        while(not t.isdigit()):
                                            t = input(name + "'s new perception: ")
                                            if(not t.isdigit()):
                                                print("Please enter a positive number with no alphabetic characters.")
                                        i.PERCEPTION = int(t)
                                    elif(selection.lower() == "performance"):
                                        t = 'a'
                                        while(not t.isdigit()):
                                            t = input(name + "'s new performance: ")
                                            if(not t.isdigit()):
                                                print("Please enter a positive number with no alphabetic characters.")
                                        i.PERFORMANCE = int(t)
                                    elif(selection.lower() == "persuasion"):
                                        t = 'a'
                                        while(not t.isdigit()):
                                            t = input(name + "'s new persuasion: ")
                                            if(not t.isdigit()):
                                                print("Please enter a positive number with no alphabetic characters.")
                                        i.PERSUASION = int(t)
                                    elif(selection.lower() == "religion"):
                                        t = 'a'
                                        while(not t.isdigit()):
                                            t = input(name + "'s new religion: ")
                                            if(not t.isdigit()):
                                                print("Please enter a positive number with no alphabetic characters.")
                                        i.RELIGION = int(t)
                                    elif(selection.lower() == "sleight of hand"):
                                        t = 'a'
                                        while(not t.isdigit()):
                                            t = input(name + "'s new sleight of hand: ")
                                            if(not t.isdigit()):
                                                print("Please enter a positive number with no alphabetic characters.")
                                        i.SLEIGHT_OF_HAND = int(t)
                                    elif(selection.lower() == "stealth"):
                                        t = 'a'
                                        while(not t.isdigit()):
                                            t = input(name + "'s new stealth: ")
                                            if(not t.isdigit()):
                                                print("Please enter a positive number with no alphabetic characters.")
                                        i.STEALTH = int(t)
                                    elif(selection.lower() == "survival"):
                                        t = 'a'
                                        while(not t.isdigit()):
                                            t = input(name + "'s new survival: ")
                                            if(not t.isdigit()):
                                                print("Please enter a positive number with no alphabetic characters.")
                                        i.SURVIVAL = int(t)
                                    elif(selection.lower() == "passive perception"):
                                        t = 'a'
                                        while(not t.isdigit()):
                                            t = input(name + "'s new passive perception: ")
                                            if(not t.isdigit()):
                                                print("Please enter a positive number with no alphabetic characters.")
                                        i.PASSIVE_PERCEPTION = int(t)
                                    else:
                                        print("\n\n\n\n\n\n\n\n\n\n")
                                        print("Please choose from the listed options below")
                            elif(option == "4"): # Edit Proficiencies and Expertises
                                print("\n\n\n\n\n\n\n\n\n\n")
                                while(True):
                                    print("----- Editing Character: " + name + "(Proficiencies & Expertises) -----")
                                    print("\nProficiencies: ", end="")
                                    print(i.PROFICIENCIES, end="")
                                    print("\nExpertises: ", end="")
                                    print(i.EXPERTISES, end="")
                                    print("\n")
                                    print("1. Add Proficiency\n2. Add Expertise\n3. Remove Proficiency\n4. Remove Expertise")
                                    selection = input("Please choose from the menu options above or press ENTER to go back: ")
                                    if(selection == ""):
                                        print("\n\n\n\n\n\n\n\n\n\n")
                                        break
                                    elif(selection == "1"): # Add prof
                                        print("\n\n\n\n\n\n\n\n\n\n")
                                        while(True):
                                            print("----- Editing Character: " + name + "(Adding Proficiency) -----")
                                            print("1. Acrobatics\n2. Animal Handling\n3. Arcana\n4. Athletics\n" + \
                                                  "5. Deception\n6. History\n7. Insight\n8. Intimidation\n" + \
                                                  "9. Investigation\n10. Medicine\n11. Nature\n12. Perception\n" + \
                                                  "13. Performance\n14. Persuasion\n15. Religion\n16. Sleight of Hand\n" + \
                                                  "17. Stealth\n18. Surivial\n19. Strength Saves\n20. Dexterity Saves\n" + \
                                                  "21. Constitution Saves\n22. Intelligence Saves\n23. Wisdom Saves\n" + \
                                                  "24. Charisma Saves\n25. Custom")
                                            print("\nProficiencies: ", end="")
                                            print(i.PROFICIENCIES, end="")
                                            print("\n")
                                            selection = input("Please choose from the menu options above or press ENTER to go back: ")
                                            if(selection == ""):
                                                print("\n\n\n\n\n\n\n\n\n\n")
                                                break
                                            elif(selection == "1"):
                                                i.addStat("proficiency", "acrobatics")
                                            elif(selection == "2"):
                                                i.addStat("proficiency", "animal handling")
                                            elif(selection == "3"):
                                                i.addStat("proficiency", "arcana")
                                            elif(selection == "4"):
                                                i.addStat("proficiency", "athletics")
                                            elif(selection == "5"):
                                                i.addStat("proficiency", "deception")
                                            elif(selection == "6"):
                                                i.addStat("proficiency", "history")
                                            elif(selection == "7"):
                                                i.addStat("proficiency", "insight")
                                            elif(selection == "8"):
                                                i.addStat("proficiency", "intimidation")
                                            elif(selection == "9"):
                                                i.addStat("proficiency", "investigation")
                                            elif(selection == "10"):
                                                i.addStat("proficiency", "medicine")
                                            elif(selection == "11"):
                                                i.addStat("proficiency", "nature")
                                            elif(selection == "12"):
                                                i.addStat("proficiency", "perception")
                                            elif(selection == "13"):
                                                i.addStat("proficiency", "performance")
                                            elif(selection == "14"):
                                                i.addStat("proficiency", "persuasion")
                                            elif(selection == "15"):
                                                i.addStat("proficiency", "religion")
                                            elif(selection == "16"):
                                                i.addStat("proficiency", "sleight of hand")
                                            elif(selection == "17"):
                                                i.addStat("proficiency", "stealth")
                                            elif(selection == "18"):
                                                i.addStat("proficiency", "survival")
                                            elif(selection == "19"):
                                                i.addStat("proficiency", "stength saves")
                                            elif(selection == "20"):
                                                i.addStat("proficiency", "dexterity saves")
                                            elif(selection == "21"):
                                                i.addStat("proficiency", "constitution saves")
                                            elif(selection == "22"):
                                                i.addStat("proficiency", "intelligence saves")
                                            elif(selection == "23"):
                                                i.addStat("proficiency", "wisdom saves")
                                            elif(selection == "24"):
                                                i.addStat("proficiency", "charisma saves")
                                            elif(selection == "25"):
                                                prof = input("Please enter your custom proficiency: ")
                                                i.addStat("proficiency", prof)
                                            else:
                                                print("\n\n\n\n\n\n\n\n\n\n")
                                                print("Please choose a number from the listed options below")
                                    elif(selection == "2"): # Add expert
                                        print("\n\n\n\n\n\n\n\n\n\n")
                                        while(True):
                                            print("----- Editing Character: " + name + "(Adding Expertise) -----")
                                            print("1. Acrobatics\n2. Animal Handling\n3. Arcana\n4. Athletics\n" + \
                                                  "5. Deception\n6. History\n7. Insight\n8. Intimidation\n" + \
                                                  "9. Investigation\n10. Medicine\n11. Nature\n12. Perception\n" + \
                                                  "13. Performance\n14. Persuasion\n15. Religion\n16. Sleight of Hand\n" + \
                                                  "17. Stealth\n18. Surivial\n19. Custom")
                                            print("\nExpertises: ", end="")
                                            print(i.EXPERTISES, end="")
                                            print("\n")
                                            selection = input("Please choose from the menu options above or press ENTER to go back: ")
                                            if(selection == ""):
                                                print("\n\n\n\n\n\n\n\n\n\n")
                                                break
                                            elif(selection == "1"):
                                                i.addStat("expertise", "acrobatics")
                                            elif(selection == "2"):
                                                i.addStat("expertise", "animal handling")
                                            elif(selection == "3"):
                                                i.addStat("expertise", "arcana")
                                            elif(selection == "4"):
                                                i.addStat("expertise", "athletics")
                                            elif(selection == "5"):
                                                i.addStat("expertise", "deception")
                                            elif(selection == "6"):
                                                i.addStat("expertise", "history")
                                            elif(selection == "7"):
                                                i.addStat("expertise", "insight")
                                            elif(selection == "8"):
                                                i.addStat("expertise", "intimidation")
                                            elif(selection == "9"):
                                                i.addStat("expertise", "investigation")
                                            elif(selection == "10"):
                                                i.addStat("expertise", "medicine")
                                            elif(selection == "11"):
                                                i.addStat("expertise", "nature")
                                            elif(selection == "12"):
                                                i.addStat("expertise", "perception")
                                            elif(selection == "13"):
                                                i.addStat("expertise", "performance")
                                            elif(selection == "14"):
                                                i.addStat("expertise", "persuasion")
                                            elif(selection == "15"):
                                                i.addStat("expertise", "religion")
                                            elif(selection == "16"):
                                                i.addStat("expertise", "sleight of hand")
                                            elif(selection == "17"):
                                                i.addStat("expertise", "stealth")
                                            elif(selection == "18"):
                                                i.addStat("expertise", "survival")
                                            elif(selection == "19"):
                                                exp = input("Please enter your custom expertise: ")
                                                i.addStat("expertise", exp)
                                            else:
                                                print("\n\n\n\n\n\n\n\n\n\n")
                                                print("Please choose a number from the listed options below")
                                    elif(selection == "3"): # Remove prof
                                        print("\n\n\n\n\n\n\n\n\n\n")
                                        while(True):
                                            print("----- Editing Character: " + name + "(Remove Proficiency) -----")
                                            if(len(i.PROFICIENCIES) == 0 or i.PROFICIENCIES[0] == "None"):
                                                print(i.NAME + " has no proficiencies to remove. Exiting...")
                                                print("\n\n\n\n\n\n\n\n\n\n")
                                                break
                                            else:
                                                counter = 0
                                                for item in i.PROFICIENCIES:
                                                    counter = counter + 1
                                                    print(str(counter) + ". " + item)
                                                counter = 0
                                                selection = input("Please choose from the menu options above or press ENTER to go back: ")
                                                if(selection == ""):
                                                    print("\n\n\n\n\n\n\n\n\n\n")
                                                    break
                                                elif((not selection.isnumeric()) or int(selection) > len(i.PROFICIENCIES) \
                                                      or int(selection) < 0):
                                                    print("\n\n\n\n\n\n\n\n\n\n")
                                                    print("Please choose a number from the listed options below")
                                                else:
                                                    i.removeStat("proficiency", i.PROFICIENCIES[(int(selection) - 1)])
                                                    if(len(i.PROFICIENCIES) == 0):
                                                        i.PROFICIENCIES.append("None")
                                                    if(len(i.EXPERTISES) == 0):
                                                        i.EXPERTISES.append("None")
                                    elif(selection == "4"): # Remove expert
                                        print("\n\n\n\n\n\n\n\n\n\n")
                                        while(True):
                                            print("----- Editing Character: " + name + "(Remove Expertise) -----")
                                            if(len(i.EXPERTISES) == 0 or i.EXPERTISES[0] == "None"):
                                                print(i.NAME + " has no expertises to remove. Exiting...")
                                                print("\n\n\n\n\n\n\n\n\n\n")
                                                break
                                            else:
                                                counter = 0
                                                for item in i.EXPERTISES:
                                                    counter = counter + 1
                                                    print(str(counter) + ". " + item)
                                                counter = 0
                                                selection = input("Please choose from the menu options above or press ENTER to go back: ")
                                                if(selection == ""):
                                                    print("\n\n\n\n\n\n\n\n\n\n")
                                                    break
                                                elif((not selection.isnumeric()) or int(selection) > len(i.EXPERTISES) \
                                                      or int(selection) < 0):
                                                    print("\n\n\n\n\n\n\n\n\n\n")
                                                    print("Please choose a number from the listed options below")
                                                else:
                                                    i.removeStat("expertise", i.EXPERTISES[(int(selection) - 1)])
                                                    if(len(i.EXPERTISES) == 0):
                                                        i.EXPERTISES.append("None")
                                    else:
                                        print("\n\n\n\n\n\n\n\n\n\n")
                                        print("Please choose a number from the listed options below")
                            elif(option == "5"): # Edit Resistances
                                print("\n\n\n\n\n\n\n\n\n\n")
                                while(True):
                                    print("----- Editing Character: " + name + "(Resistances) -----")
                                    print("\nResistances: ", end="")
                                    print(i.RESISTANCES, end="")
                                    print("\n")
                                    print("1. Add Resistance\n2. Remove Resistance")
                                    selection = input("Please choose from the menu options above or press ENTER to go back: ")
                                    if(selection == ""):
                                        print("\n\n\n\n\n\n\n\n\n\n")
                                        break
                                    elif(selection == "1"):
                                        print("\n\n\n\n\n\n\n\n\n\n")
                                        while(True):
                                            print("----- Editing Character: " + name + "(Add Resistances) -----")
                                            print("1. Acid\n2. Bludgeoning\n3. Cold\n4. Fire\n5. Force\n" + \
                                                  "6. Lightning\n7. Necrotic\n8. Piercing\n9. Poison\n" + \
                                                  "10. Psychic\n11. Radiant\n12. Slashing\n13. Thunder\n14. Custom")
                                            print("\nResistances: ", end="")
                                            print(i.RESISTANCES, end="")
                                            print("\n")
                                            choice = input("Please choose from the menu options above or press ENTER to go back: ")
                                            if(choice == ""):
                                                print("\n\n\n\n\n\n\n\n\n\n")
                                                break
                                            elif(choice == "1"):
                                                i.addStat("resistance", "acid")
                                            elif(choice == "2"):
                                                i.addStat("resistance", "bludgeoning")
                                            elif(choice == "3"):
                                                i.addStat("resistance", "cold")
                                            elif(choice == "4"):
                                                i.addStat("resistance", "fire")
                                            elif(choice == "5"):
                                                i.addStat("resistance", "force")
                                            elif(choice == "6"):
                                                i.addStat("resistance", "lightning")
                                            elif(choice == "7"):
                                                i.addStat("resistance", "necrotic")
                                            elif(choice == "8"):
                                                i.addStat("resistance", "piercing")
                                            elif(choice == "9"):
                                                i.addStat("resistance", "poison")
                                            elif(choice == "10"):
                                                i.addStat("resistance", "psychic")
                                            elif(choice == "11"):
                                                i.addStat("resistance", "radiant")
                                            elif(choice == "12"):
                                                i.addStat("resistance", "slashing")
                                            elif(choice == "13"):
                                                i.addStat("resistance", "thunder")
                                            elif(choice == "14"):
                                                res = input("Please enter your custom resistance: ")
                                                i.addStat("resistance", res)
                                            else:
                                                print("\n\n\n\n\n\n\n\n\n\n")
                                                print("Please choose a number from the listed options below")
                                    elif(selection == "2"):
                                        print("\n\n\n\n\n\n\n\n\n\n")
                                        while(True):
                                            print("----- Editing Character: " + name + "(Remove Resistances) -----")
                                            if(len(i.RESISTANCES) == 0 or i.RESISTANCES[0] == "None"):
                                                print(i.NAME + " has no resistances to remove. Exiting...")
                                                print("\n\n\n\n\n\n\n\n\n\n")
                                                break
                                            else:
                                                counter = 0
                                                for item in i.RESISTANCES:
                                                    counter = counter + 1
                                                    print(str(counter) + ". " + item)
                                                counter = 0
                                                selection = input("Please choose from the menu options above or press ENTER to go back: ")
                                                if(selection == ""):
                                                    print("\n\n\n\n\n\n\n\n\n\n")
                                                    break
                                                elif((not selection.isnumeric()) or int(selection) > len(i.RESISTANCES) \
                                                      or int(selection) < 0):
                                                    print("\n\n\n\n\n\n\n\n\n\n")
                                                    print("Please choose a number from the listed options below")
                                                else:
                                                    i.removeStat("resistance", i.RESISTANCES[(int(selection) - 1)])
                                                    if(len(i.RESISTANCES) == 0):
                                                        i.RESISTANCES.append("None")
                                                    print("\n\n\n\n\n\n\n\n\n\n")
                                    else:
                                        print("\n\n\n\n\n\n\n\n\n\n")
                                        print("Please choose a number from the listed options below")
                            elif(option == "6"): # Edit Vulnerabilities
                                print("\n\n\n\n\n\n\n\n\n\n")
                                while(True):
                                    print("----- Editing Character: " + name + "(Vulnerabilities) -----")
                                    print("\nVulnerabilities: ", end="")
                                    print(i.VULNERABILITIES, end="")
                                    print("\n")
                                    print("1. Add Vulnerability\n2. Remove Vulnerability")
                                    selection = input("Please choose from the menu options above or press ENTER to go back: ")
                                    if(selection == ""):
                                        print("\n\n\n\n\n\n\n\n\n\n")
                                        break
                                    elif(selection == "1"):
                                        print("\n\n\n\n\n\n\n\n\n\n")
                                        while(True):
                                            print("----- Editing Character: " + name + "(Add Vulnerability) -----")
                                            print("1. Acid\n2. Bludgeoning\n3. Cold\n4. Fire\n5. Force\n" + \
                                                  "6. Lightning\n7. Necrotic\n8. Piercing\n9. Poison\n" + \
                                                  "10. Psychic\n11. Radiant\n12. Slashing\n13. Thunder\n14. Custom")
                                            print("\nVulnerabilities: ", end="")
                                            print(i.VULNERABILITIES, end="")
                                            print("\n")
                                            choice = input("Please choose from the menu options above or press ENTER to go back: ")
                                            if(choice == ""):
                                                print("\n\n\n\n\n\n\n\n\n\n")
                                                break
                                            elif(choice == "1"):
                                                i.addStat("vulnerability", "acid")
                                            elif(choice == "2"):
                                                i.addStat("vulnerability", "bludgeoning")
                                            elif(choice == "3"):
                                                i.addStat("vulnerability", "cold")
                                            elif(choice == "4"):
                                                i.addStat("vulnerability", "fire")
                                            elif(choice == "5"):
                                                i.addStat("vulnerability", "force")
                                            elif(choice == "6"):
                                                i.addStat("vulnerability", "lightning")
                                            elif(choice == "7"):
                                                i.addStat("vulnerability", "necrotic")
                                            elif(choice == "8"):
                                                i.addStat("vulnerability", "piercing")
                                            elif(choice == "9"):
                                                i.addStat("vulnerability", "poison")
                                            elif(choice == "10"):
                                                i.addStat("vulnerability", "psychic")
                                            elif(choice == "11"):
                                                i.addStat("vulnerability", "radiant")
                                            elif(choice == "12"):
                                                i.addStat("vulnerability", "slashing")
                                            elif(choice == "13"):
                                                i.addStat("vulnerability", "thunder")
                                            elif(choice == "14"):
                                                res = input("Please enter your custom vulnerability: ")
                                                i.addStat("vulnerability", res)
                                            else:
                                                print("\n\n\n\n\n\n\n\n\n\n")
                                                print("Please choose a number from the listed options below")
                                    elif(selection == "2"):
                                        print("\n\n\n\n\n\n\n\n\n\n")
                                        while(True):
                                            print("----- Editing Character: " + name + "(Remove Vulnerabilities) -----")
                                            if(len(i.VULNERABILITIES) == 0 or i.VULNERABILITIES[0] == "None"):
                                                print(i.NAME + " has no vulnerabilities to remove. Exiting...")
                                                print("\n\n\n\n\n\n\n\n\n\n")
                                                break
                                            else:
                                                counter = 0
                                                for item in i.VULNERABILITIES:
                                                    counter = counter + 1
                                                    print(str(counter) + ". " + item)
                                                counter = 0
                                                selection = input("Please choose from the menu options above or press ENTER to go back: ")
                                                if(selection == ""):
                                                    print("\n\n\n\n\n\n\n\n\n\n")
                                                    break
                                                elif((not selection.isnumeric()) or int(selection) > len(i.VULNERABILITIES) \
                                                      or int(selection) < 0):
                                                    print("\n\n\n\n\n\n\n\n\n\n")
                                                    print("Please choose a number from the listed options below")
                                                else:
                                                    i.removeStat("vulnerability", i.VULNERABILITIES[(int(selection) - 1)])
                                                    if(len(i.VULNERABILITIES) == 0):
                                                        i.VULNERABILITIES.append("None")
                                                    print("\n\n\n\n\n\n\n\n\n\n")
                                    else:
                                        print("\n\n\n\n\n\n\n\n\n\n")
                                        print("Please choose a number from the listed options below")
                            elif(option == "7"):
                                if(i.JACK_OF_ALL_TRADES == True):
                                    i.JACK_OF_ALL_TRADES = False
                                    print("\n\n\n\n\n\n\n\n\n\n")
                                    print("JOAT set to 'False'")
                                else:
                                    i.JACK_OF_ALL_TRADES = True
                                    print("\n\n\n\n\n\n\n\n\n\n")
                                    print("JOAT set to 'True'")
                            else:
                                print("\n\n\n\n\n\n\n\n\n\n")
                                print("Please choose from the listed options below by typing a number")
                if(not flag):
                    print("Character does not exist. Please check spelling.")
                    input("Please press ENTER to continue...")
                    print("\n\n\n\n\n\n\n\n\n\n")
    elif(temp == "3"): # Import character functionality
        print("\n\n\n\n\n\n\n\n\n\n")
        print("----- Import Character -----")
        fileName = input("Please enter the file path of your character PDF or press ENTER to go back: ")
        retVal = rip(fileName)
        if(fileName.lower() == ""):
            print("\n\n\n\n\n\n\n\n\n\n")
            pass
        elif(retVal == 0):
            print("File does not exist. Please check filepath.")
            input("Please press ENTER to continue...")
            print("\n\n\n\n\n\n\n\n\n\n")
        else:
            if(not(characters)):
                characters.append(retVal)
                print("Success! Please add proficiencies, expertises, resistances, and vulnerabilites manually" + \
                      " under the 'Edit Character' screen.")
                input("Please press ENTER to continue...")
                print("\n\n\n\n\n\n\n\n\n\n")
            else:
                isfound = False
                for i in characters:
                    if(retVal.NAME.lower() == i.NAME.lower()):
                        print("The character '" + retVal.NAME + "' already exists, so no action was taken.")
                        input("Press ENTER to continue...")
                        print("\n\n\n\n\n\n\n\n\n\n")
                        isfound = True
                        break
                if(not isfound):
                    characters.append(retVal)
                    print("Sucess! Please add proficiencies, expertises, resistances, and vulnerabilites manually.")
                    input("Please press ENTER to continue...")
                    print("\n\n\n\n\n\n\n\n\n\n")
    elif(temp == "4"): # View character funcitonality
        while(True):
            print("\n\n\n\n\n\n\n\n\n\n")
            print("----- View Characters -----")
            print("\nSaved Characters: ")
            for i in characters:
                print(i.NAME)
            print("")
            name = input("Please type which character you would like to view or press ENTER to go back: ")
            if(name == ""):
                print("\n\n\n\n\n\n\n\n\n\n")
                break
            else:
                flag = False
                for i in characters:
                    if(i.NAME.lower() == name.lower()):
                        flag = True
                        print("\n\n\n\n\n\n\n\n\n\n")
                        print(i)
                        input("Please press ENTER to continue...")
                if(not flag):
                    print("Character does not exist. Please check spelling.")
                    input("Please press ENTER to continue...")
    elif(temp == "5"):
        print("\n\n\n\n\n\n\n\n\n\n")
        while(True):
            print("----- Delete Character -----")
            print("\nSaved Characters: ")
            for i in characters:
                print(i.NAME)
            print("")
            name = input("Please type the character's name you wish to delete or press ENTER to go back: ")
            if(name == ""):
                print("\n\n\n\n\n\n\n\n\n\n")
                break
            else:
                flag = False
                for i in characters:
                    if(i.NAME.lower() == name.lower()):
                        flag = True
                        remove_char(name)
                        characters.remove(i)
                        input("Character deleted successfully. Please press ENTER to continue...")
                        print("\n\n\n\n\n\n\n\n\n\n")
                if(not flag):
                    print("Character does not exist. Please check spelling.")
                    input("Please press ENTER to continue...")
                    print("\n\n\n\n\n\n\n\n\n\n")
    else:
        print("\n\n\n\n\n\n\n\n\n\n")
        print("Please choose from the listed options below by typing a number")
