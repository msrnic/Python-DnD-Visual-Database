import spell_reader as reader
import tag_conversion as tag
import file_list_loader as files
import spell_loader
import requests
import json

def spell_formatter(spell):
    for i in range(len(spell)):
        if ((i == 0) | (i == 6) | (i == 8)):
            spell[i] = spell[i].replace("_", " ")
        elif (i == 1):
            continue
        else:
            spell[i] = tag.measure_tag_converter(spell[i])
    return spell

def spell_headers(spellData):
    headers = [
        "Spell Name: ",
        "Spell Level: ",
        "Spell Type: ",
        "Casting Time: ",
        "Range: ",
        "Components: ",
        "Materials: ",
        "Duration: ",
        "Description: "
    ]
    for i in range(len(spellData)):
        spellData[i] = headers[i] + spellData[i]
    return spellData

def spell_printer(formedSpell):
    for i in formedSpell:
        if i == "Materials: N/A":
            continue
        else:
            print(i)
"""
def startup_text():
    fileList = []
    textLine = ""
    fileList = files.file_list_loader("Data Files.txt")
    print("Dungeons and Dragons Database V1\n-Spells Only-")
    print("Please choose a file to load:")
    for i in range(len(fileList)):
        if (i == len(fileList)-1):
            textLine += fileList[i]
        else:
            textLine += fileList[i] + ", "
    print(textLine)
    while True:
        choice = input()
        if choice in fileList:
            spells = reader.file_read(choice)
            for id in spells:
                currentSpell = spell_formatter(spells[id])
                spells[id] = currentSpell
                currentSpell = spell_headers(currentSpell)
                spell_printer(currentSpell)
                print(id)
        else:
            print("File not recognized, please type a file from the list.")
"""

def startup_text():
    spells = {}
    print("Dungeons and Dragons Database V1\n-Spells Only-")
    print("Now Loading...")
    spells = spell_loader.get_spells()
    spellCount = spells["count"]
    spellIndices = []
    spellNames = []
    spellIndex = 0
    spellURL = ""
    for i in range(0, spellCount):
        spellIndices.append(spells["results"][i]["index"])
        spellNames.append(spells["results"][i]["name"])
    print("Please choose a spell to load:")
    while True:
        choice = input()
        if (choice in spellIndices):
            spellIndex = spellIndices.index(choice)
            spellURL = spells["results"][spellIndex]["url"]
            spell_loader.load_spell(spellURL)
            
        else:
            print("Spell not recognized, please choose a spell from the list. Note that spells are case sensitive.")


startup_text()