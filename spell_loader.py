import requests
import json
def get_spells():
    try:
        spellsAPI = requests.get("https://www.dnd5eapi.co/api/spells")
        spellData = spellsAPI.text
        spellDict = json.loads(spellData)
        return spellDict
    except requests.exceptions.ConnectionError:
        return {}
        
def load_spell(URL):
    spellURL = "https://www.dnd5eapi.co/api/spells/" + URL
    try:    
        getSpellAPI = requests.get(spellURL)
        currentSpellData = getSpellAPI.text
        currentSpell = json.loads(currentSpellData)
        return currentSpell
    except requests.exceptions.ConnectionError:
        return {}