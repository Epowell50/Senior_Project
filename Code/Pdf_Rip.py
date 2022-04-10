from PyPDF2 import PdfFileReader
from Character_Class import *
import os.path

# The main function that pulls all information from the PDF
def rip(filename):
    # Checks if the file exists, errors if not
    if(os.path.exists(filename)):
        # Pulls the information and puts it in a list called "text"
        with open(filename, 'rb') as f:
            pdf = PdfFileReader(f)
            text = pdf.getFormTextFields()
        
        # Rips level
        templist = text["ClassLevel"].split()
        level = int(templist[1])
        
        newchar = Character(text["CharacterName"], level, int(text["HPCurrent"]), \
            int(text["HPMax"]), int(text["AC"]), int(text["STR"]), int(text["DEX"]), \
            int(text["CON"]), int(text["INT"]), int(text["WIS"]), int(text["CHA"]))
        return newchar
    else:
        return 0