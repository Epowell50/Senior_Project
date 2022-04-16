import sqlite3
from Character_Class import Character

def initialize():
    conn = sqlite3.connect('characters.db')

    # Create cursor to execute database commands
    cursor = conn.cursor()
    
    try:
        # Create table using doc-string
        cursor.execute("""CREATE TABLE characters (
                name text NOT NULL PRIMARY KEY,
                level integer,
                proficiency integer,
                ac integer,
                initiative integer,
                current_hp integer,
                max_hp integer,
                str integer,
                dex integer,
                con integer,
                int integer,
                wis integer,
                cha integer,
                str_save integer,
                dex_save integer,
                con_save integer,
                int_save integer,
                wis_save integer,
                cha_save integer,
                death_success integer,
                death_failure integer,
                acrobatics integer,
                animal_handling integer,
                arcana integer,
                athletics integer,
                deception integer,
                history integer,
                insight integer,
                intimidation integer,
                invesitgation integer,
                medicine integer,
                nature integer,
                perception integer,
                performance integer,
                persuasion integer,
                religion integer,
                sleight_of_hand integer,
                stealth integer,
                survival integer,
                prof text,
                expert text,
                resist text,
                vuln text,
                joat integer)""")
    except sqlite3.OperationalError:
         pass
    conn.close()

# Insterts a character object into the database
def insert_char(char):
    # Creating database connection and name the file
    conn = sqlite3.connect('characters.db')

    # Create cursor to execute database commands
    cursor = conn.cursor()
    # Convert lists to strings for storage
    proficiencies = ','.join(char.PROFICIENCIES)
    expertises = ','.join(char.EXPERTISES)
    resistantces = ','.join(char.RESISTANCES)
    vulnerabilities = ','.join(char.VULNERABILITIES)
    # Store the character
    with conn:
        cursor.execute("""INSERT INTO characters VALUES
        (:name, :level, :proficiency, :ac, :initiative,
         :current_hp, :max_hp, :str, :dex, :con,
         :int, :wis, :cha, :str_save, :dex_save,
         :con_save, :int_save, :wis_save, :cha_save,
         :death_success, :death_failure, :acrobatics,
         :animal_handling, :arcana, :athletics, :deception,
         :history, :insight, :intimidation, :investigation,
         :medicine, :nature, :perception, :performance,
         :persuasion, :religion, :sleight_of_hand,
         :stealth, :survival, :prof, :expert, :resist,
         :vuln, :JOAT)""", \
         {'name': str(char.NAME), 'level': int(char.LEVEL), \
          'proficiency': int(char.PROFICIENCY), 'ac': int(char.AC), \
          'initiative': int(char.INITIATIVE), 'current_hp': int(char.CURRENT_HP), \
          'max_hp': int(char.MAX_HP), 'str': int(char.STR), 'dex': int(char.DEX), \
          'con': int(char.CON), 'int': int(char.INT), 'wis': int(char.WIS), \
          'cha': int(char.CHA), 'str_save': int(char.STR_SAVE), 'dex_save': int(char.DEX_SAVE), \
          'con_save': int(char.CON_SAVE), 'int_save': int(char.INT_SAVE), \
          'wis_save': int(char.WIS_SAVE), 'cha_save': int(char.CHA_SAVE), \
          'death_success': int(char.DEATH_SUCCESS), 'death_failure': int(char.DEATH_FAILURE), \
          'acrobatics': char.ACROBATICS, 'animal_handling': char.ANIMAL_HANDLING, \
          'arcana': int(char.ARCANA), 'athletics': int(char.ATHLETICS), \
          'deception': int(char.DECEPTION), 'history': int(char.HISTORY), 'insight': int(char.INSIGHT), \
          'intimidation': int(char.INTIMIDATION), 'investigation': int(char.INVESTIGATION), \
          'medicine': int(char.MEDICINE), 'nature': int(char.NATURE), 'perception': int(char.PERCEPTION), \
          'performance': int(char.PERFORMANCE), 'persuasion': int(char.PERSUASION), \
          'religion': int(char.RELIGION), 'sleight_of_hand': int(char.SLEIGHT_OF_HAND), \
          'stealth': int(char.STEALTH), 'survival': int(char.SURVIVAL), 'prof': str(proficiencies), \
          'expert': str(expertises), 'resist': str(resistantces), 'vuln': str(vulnerabilities), \
          'JOAT': bool(char.JACK_OF_ALL_TRADES)}) 

# Searches a character by their last name
def search_char(name):
    # Creating database connection and name the file
    conn = sqlite3.connect('characters.db')

    # Create cursor to execute database commands
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM characters WHERE name = :name", {'name': name})
    conn.close()
    return cursor.fetchone()

# Removes a character given the character object
def remove_char(name):
    # Creating database connection and name the file
    conn = sqlite3.connect('characters.db')

    # Create cursor to execute database commands
    cursor = conn.cursor()
    with conn:
        cursor.execute("DELETE from characters WHERE name = :name", 
        {'name': name})

# Returns a list with all characters in the database
def query_all():
    character_list = []

    # Creating databse connection and namem the file
    conn = sqlite3.connect('characters.db')
    cursor = conn.cursor()
    with conn:
        cursor.execute("SELECT * from characters")
        for character in cursor.fetchall():
            # Fix strings into lists
            prof = character[39].split(",")
            expert = character[40].split(",")
            res = character[41].split(",")
            vuln = character[42].split(",")

            # Create character object with database stats
            # This is not as scalable as a select statement, but is more compact
            #   for my purposes. In the future, it should be modified for scalability
            newchar = Character(character[0], character[1], character[5], \
                character[6], character[3], character[7], character[8], \
                character[9], character[10], character[11], character[12], \
                prof, res, vuln, expert, character[43], character[19], \
                character[20], character[4])
            
            # Fill in skills and saves as they are not in the constructor
            newchar.STR_SAVE = character[13]
            newchar.DEX_SAVE = character[14]
            newchar.CON_SAVE = character[15]
            newchar.INT_SAVE = character[16]
            newchar.WIS_SAVE = character[17]
            newchar.CHA_SAVE = character[18]
            newchar.ACROBATICS = character[19]
            newchar.ANIMAL_HANDLING = character[20]
            newchar.ARCANA = character[21]
            newchar.ATHLETICS = character[22]
            newchar.DECEPTION = character[23]
            newchar.HISTORY = character[24]
            newchar.INSIGHT = character[25]
            newchar.INTIMIDATION = character[26]
            newchar.INVESTIGATION = character[27]
            newchar.MEDICINE = character[28]
            newchar.NATURE = character[29]
            newchar.PERCEPTION = character[30]
            newchar.PERFORMANCE = character[31]
            newchar.PERSUASION = character[32]
            newchar.RELIGION = character[33]
            newchar.SLEIGHT_OF_HAND = character[34]
            newchar.STEALTH = character[35]
            newchar.SURVIVAL = character[36]
            character_list.append(newchar)

    return character_list