import sqlite3
from Character_Class import Character

# Creating database connection and name the file
conn = sqlite3.connect(':memory:')

# Create cursor to execute database commands
cursor = conn.cursor()

# Create table using doc-string
cursor.execute("""CREATE TABLE characters (
            name text,
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

# Insterts a character object into the database
def insert_char(char):
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
    cursor.execute("SELECT * FROM characters WHERE name = :name", {'name': name})
    return cursor.fetchall()

# Removes a character given the character object
def remove_char(name):
    with conn:
        cursor.execute("DELETE from characters WHERE name = :name", 
        {'name': name})

char1 = Character("Errant", 10, 20, 25, 16, 10, 18, 12, 4, 12, 20)

insert_char(char1)
print(search_char("Errant"))

conn.close()
