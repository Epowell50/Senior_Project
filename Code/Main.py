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
    temp = input()

    if(temp.lower() == "stop"):
        print("Goodbye!")
        break
    elif(temp.lower() == ""):
        print("Goodbye!")
        break
    elif(temp == "1"):
        # Create character stuff here
        pass
    elif(temp == "2"):
        # Edit character stuff here
        pass
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
                print("Sucess! Please add proficiencies, expertises, resistances, and vulnerabilites manually.")
                input("Please press ENTER to continue...")
                print("\n\n\n\n\n\n\n\n\n\n")
            else:
                for i in characters:
                    if(retVal.NAME.lower() == i.NAME.lower()):
                        input("The character '" + retVal.NAME + "' already exists, so no action was taken. " +
                              "Press ENTER to continue.")
                        print("\n\n\n\n\n\n\n\n\n\n")
                        break
                    else:
                        characters.append(retVal)
                        print("Sucess! Please add proficiencies, expertises, resistances, and vulnerabilites manually.")
                        input("Please press ENTER to continue...")
                        print("\n\n\n\n\n\n\n\n\n\n")
    elif(temp == "4"):
        while(True):
            print("\n\n\n\n\n\n\n\n\n\n")
            print("----- View Characters -----")
            print("\nSaved Characters: ")
            for i in characters:
                print(i.NAME)
            print("")
            name = input("Please type which character you would like to view or press ENTER to go back: ")
            if(name == ""):
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