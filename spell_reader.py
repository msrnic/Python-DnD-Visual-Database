def file_read(filename):
    spells = {}
    try:
        f = open(filename, "rt", encoding = "UTF-8")
        parameters = f.readline().strip("\n")
        parameters.split(" ")
        for line in f:
            parameters = line.strip('\n')
            spellDetails = parameters.split(' ')
            spells[spellDetails[0]] = [spellDetails[1], spellDetails[2], spellDetails[3], spellDetails[4], spellDetails[5], spellDetails[6], spellDetails[7], spellDetails[8], spellDetails[9]]
    except FileNotFoundError:
        print("File not found.")
    except EOFError:
        f.close()
    return spells