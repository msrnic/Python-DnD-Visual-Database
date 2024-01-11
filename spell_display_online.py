import pygame
import print_render as pr
import text_wrap as tw
def display_spell_page(screen, spell, marginWidth, marginHeight):
    screen.fill((252, 245, 229))
    #set fonts
    titleFont = pygame.font.Font("assets/RINGM___.TTF", 35)
    bodyFont = pygame.font.Font("assets/MorrisRoman-Black.ttf", 18)
    #text wrap the spell name in case it is too long
    spellName = tw.text_wrap(spell["name"], False, 30)
    #render and print line by line
    for line in spellName:
        pr.print_render(screen, titleFont, line, marginWidth, marginHeight, True)
    #move down 2 lines, leaving a space
    offset = 40
    #render and print the spell's level
    pr.print_render(screen, bodyFont, "Level: " + str(spell["level"]), marginWidth, marginHeight + offset, False)
    #move down 1 line
    offset += 20
    #if spell is ritual cast, include it alongside its school of magic
    if (spell["ritual"]):
        spellSchool = bodyFont.render("School: " + spell["school"]["name"] + " (Ritual)", True, "black")
    #otherwise only prepare school of magic
    else:
        spellSchool = bodyFont.render("School: " + spell["school"]["name"], True, "black")
    #print spell's school
    screen.blit(spellSchool, (marginWidth, marginHeight + offset))
    #move down 1 line
    offset += 20
    #render and print the spell's casting time
    pr.print_render(screen, bodyFont, "Casting Time: " + spell["casting_time"], marginWidth, marginHeight + offset, False)
    #move down 1 line
    offset += 20
    #print and render the spell's range
    pr.print_render(screen, bodyFont, "Range: " + spell["range"], marginWidth, marginHeight + offset, False)
    #move down 1 line
    offset += 20
    #loop to combine spell components into one string
    for tag in spell["components"]:
        #if multiple components, separate by comma
        if (tag != spell["components"][-1]):
            comps = ""
            comps += tag + ", "
        #Otherwise you must have either 1 or be at the final one, so do not include comma
        else:
            comps = ""
            comps += tag
    #print and render spell components
    pr.print_render(screen, bodyFont, "Components: " + comps, marginWidth, marginHeight + offset, False)
    #move down 1 line
    offset += 20
    #if there is a required material, text wrap it, and print line by line
    if "material" in spell:
        matWrap = tw.text_wrap("Materials: " + spell["material"], False, 30)
        for line in matWrap:
            pr.print_render(screen, bodyFont, line, marginWidth, marginHeight + offset, False)
            offset += 20
    #if the spell has concentration, print along side duration
    if (spell["concentration"]):
        spellDuration = bodyFont.render("Duration: " + spell["duration"] + " (Concentration)", True, "black")
    #otherwise print duration only
    else:
        spellDuration = bodyFont.render("Duration: " + spell["duration"], True, "black")
    #print spell duration
    screen.blit(spellDuration, (marginWidth, marginHeight + offset))
    #move down by 2 lines, leaving a space
    offset += 40
    #text wrap spell description and print it line by line
    spellDesc = tw.text_wrap(spell["desc"][0], True, 65)
    for line in spellDesc:
        pr.print_render(screen, bodyFont, line, marginWidth, marginHeight + offset, False)
        offset += 20
    #move down by one more, leaving a space
    offset += 20
    #if spell can be casted at higher levels, include that
    #include by text wrapping and printing line by line
    if spell["higher_level"] != []:
        spellDmgBoost = tw.text_wrap(spell["higher_level"][0], True, 65)
        for line in spellDmgBoost:
            pr.print_render(screen, bodyFont, line, marginWidth, marginHeight + offset, False)
            offset += 20
