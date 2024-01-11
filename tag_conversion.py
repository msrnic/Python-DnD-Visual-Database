import string
def measure_tag_converter(word):
    tag = word[-1]
    word = word.rstrip(tag)
    match(tag):
        case "A":
            word = word + " Action"
        case "B":
            word = word + " Bonus Action"
        case "F":
            word = word + " feet"
        case "H":
            if (word[0] == '1'):
                word = word + " hour"
            else:
                word = word + " hours"
        case "M":
            if (word == "VS"):
                word = "Verbal, Somatic, Material"
            elif (word == "S"):
                word = "Somatic, Material"
            elif (word == "V"):
                word = "Verbal, Material"
            else:
                word = "Material"
        case "m":
            if (word[0] == '1'):
                word = word + " minute"
            else:
                word = word + " minutes"
        case "R":
            splitter = word.find('F')
            dist = word[:splitter]
            radius = word[(splitter + 1):]
            word = (dist + " feet (" + radius + " feet radius)")
        case "S":
            if (word == "V"):
                word = "Verbal, Somatic"
            else:
                word = "Somatic"
        case "V":
            word = "Verbal"
        case "0":
            word = "Instantaneous"
        case default:
            word = "Unknown"
    return word

def spell_type_converter(word):
    match word:
        case "ABJ":
            word = "Abjuration"
        case "ABJR":
            word = "Abjuration (Ritual)"
        case "CON":
            word = "Conjuration"
        case "CONR":
            word = "Conjuration (Ritual)"
        case "ENC":
            word = "Enchantment"
        case "ENC":
            word = "Enchantment"
        case "ENCR":
            word = "Enchantment (Ritual)"
        case "NEC":
            word = "Necromancy"
        case "NECR":
            word = "Necromancy (Ritual)"
        case "TRA":
            word = "Transfiguration"
        case "TRAR":
            word = "Transfiguration (Ritual)"
        case default:
            return word
    return word