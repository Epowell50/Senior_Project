from select import select
from Character_Class import *
from Attack import *
from Pdf_Rip import rip

# Character list
characters = []

print("Hello and welcome to the DND Utilities python tool!")
print("This program was created by Ethan Powell in fulfillment of " + \
      "the requirements of a BS in Cybersecurity and BS in Computer Science")
print("----------------------------------------------------------\n")
print("To begin, please select from the options below by typing the number associated: ")

# Base program loop
while(True):
    print("----- DND Utilities -----")
    print("1: Create Character\n2: Edit Character\n3: Import Character from PDF\n4: View Characters")
    print("Type 'stop' or press ENTER to quit.")
    temp = input("Selection: ")

    if(temp.lower() == "stop"):
        print("Goodbye!")
        break
    elif(temp.lower() == ""):
        print("Goodbye!")
        break
    elif(temp == "1"): # Create character functionality
        # Create character stuff here
        pass
    elif(temp == "2"): # Edit character functionality
        while(True):
            print("\n\n\n\n\n\n\n\n\n\n")
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
                        print("\n\n\n\n\n\n\n\n\n\n")
                        while(True):
                            print("----- Editing Character: " + name + " -----")
                            print("1. Base Stats\n2. Saves\n3. Skills\n4. Proficiencies & Expertises\n" + \
                                  "5. Resistances\n6. Vulnerabilities")
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
                                        i.LEVEL = int(input(name + "'s new level: "))
                                    elif(selection.lower() == "proficiency bonus"):
                                        i.PROFICIENCY = int(input(name + "'s new proficiency bonus: "))
                                    elif(selection.lower() == "initiative"):
                                        i.INITIATIVE = int(input(name + "'s new initiative: "))
                                    elif(selection.lower() == "ac"):
                                        i.AC = int(input(name + "'s new AC: "))
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
                                        i.STR = int(input(name + "'s new strength: "))
                                    elif(selection.lower() == "dexterity" or selection.lower() == "dex"):
                                        i.DEX = int(input(name + "'s new dexterity: "))
                                    elif(selection.lower() == "constitution" or selection.lower() == "con"):
                                        i.CON = int(input(name + "'s new constitution: "))
                                    elif(selection.lower() == "intelligence" or selection.lower() == "int"):
                                        i.INT = int(input(name + "'s new intelligence: "))
                                    elif(selection.lower() == "wisdom" or selection.lower() == "wis"):
                                        i.WIS = int(input(name + "'s new wisdom: "))
                                    elif(selection.lower() == "charisma" or selection.lower() == "cha"):
                                        i.CHA = int(input(name + "'s new charisma: "))
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
                                        i.STR_SAVE = int(input(name + "'s new strength save: "))
                                    elif(selection.lower() == "dexterity save" or selection.lower() == "dex save" \
                                            or selection.lower() == "dex"):
                                        i.DEX_SAVE = int(input(name + "'s new dexterity save: "))
                                    elif(selection.lower() == "constitution save" or selection.lower() == "con save" \
                                            or selection.lower() == "con"):
                                        i.CON_SAVE = int(input(name + "'s new constitution save: "))
                                    elif(selection.lower() == "intelligence save" or selection.lower() == "int save" \
                                            or selection.lower() == "int"):
                                        i.INT_SAVE = int(input(name + "'s new intelligence save: "))
                                    elif(selection.lower() == "wisdom save" or selection.lower() == "wis" \
                                            or selection.lower() == "wis"):
                                        i.WIS_SAVE = int(input(name + "'s new wisdom save: "))
                                    elif(selection.lower() == "charisma save" or selection.lower() == "cha save" \
                                            or selection.lower() == "cha"):
                                        i.CHA_SAVE = int(input(name + "'s new charisma save: "))
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
                                        i.ACROBATICS = int(input(name + "'s new acrobatics: "))
                                    elif(selection.lower() == "animal handling"):
                                        i.ANIMAL_HANDLING = int(input(name + "'s new animal handling: "))
                                    elif(selection.lower() == "arcana"):
                                        i.ARCANA = int(input(name + "'s new arcana: "))
                                    elif(selection.lower() == "athletics"):
                                        i.ATHLETICS = int(input(name + "'s new athletics: "))
                                    elif(selection.lower() == "deception"):
                                        i.DECEPTION = int(input(name + "'s new deception: "))
                                    elif(selection.lower() == "history"):
                                        i.HISTORY = int(input(name + "'s new history: "))
                                    elif(selection.lower() == "insight"):
                                        i.INSIGHT = int(input(name + "'s new insight: "))
                                    elif(selection.lower() == "intimidation"):
                                        i.INTIMIDATION = int(input(name + "'s new intimidation: "))
                                    elif(selection.lower() == "investigation"):
                                        i.INVESTIGATION = int(input(name + "'s new investigation: "))
                                    elif(selection.lower() == "medicine"):
                                        i.MEDICINE = int(input(name + "'s new medicine: "))
                                    elif(selection.lower() == "nature"):
                                        i.NATURE = int(input(name + "'s new nature: "))
                                    elif(selection.lower() == "perception"):
                                        i.PERCEPTION = int(input(name + "'s new perception: "))
                                    elif(selection.lower() == "performance"):
                                        i.PERFORMANCE = int(input(name + "'s new performance: "))
                                    elif(selection.lower() == "persuasion"):
                                        i.PERSUASION = int(input(name + "'s new persuasion: "))
                                    elif(selection.lower() == "religion"):
                                        i.RELIGION = int(input(name + "'s new religion: "))
                                    elif(selection.lower() == "sleight of hand"):
                                        i.SLEIGHT_OF_HAND = int(input(name + "'s new sleight of hand: "))
                                    elif(selection.lower() == "stealth"):
                                        i.STEALTH = int(input(name + "'s new stealth: "))
                                    elif(selection.lower() == "survival"):
                                        i.SURVIVAL = int(input(name + "'s new survival: "))
                                    elif(selection.lower() == "passive perception"):
                                        i.PASSIVE_PERCEPTION = int(input(name + "'s new passive perception: "))
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
                                                  "17. Stealth\n18. Surivial\n19. Custom")
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
                            else:
                                print("\n\n\n\n\n\n\n\n\n\n")
                                print("Please choose from the listed options below by typing a number")
                            flag = True
                if(not flag):
                    print("Character does not exist. Please check spelling.")
                    input("Please press ENTER to continue...")
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
                for i in characters:
                    if(retVal.NAME.lower() == i.NAME.lower()):
                        print("The character '" + retVal.NAME + "' already exists, so no action was taken.")
                        input("Press ENTER to continue...")
                        print("\n\n\n\n\n\n\n\n\n\n")
                        break
                    else:
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
        print("1: Create Character\n2: Edit Character\n3: Import Character from PDF\n4: Display Character")
    else:
        print("\n\n\n\n\n\n\n\n\n\n")
        print("Please choose from the listed options below by typing a number")