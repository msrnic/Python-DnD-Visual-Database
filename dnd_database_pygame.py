import pygame
import spell_loader as sl, print_render as pr, spell_display_online as onlineDisplay, drawBorder as border
import Button, Mouse, Searchbar

#spell dictionary is loaded by method from another viable via API
spellDict = {}
spellSearch = []
loadedSpell = {}

def startup():
    screen.fill((252, 245, 229))
    title = "DnD Database"
    bigTitleFont = pygame.font.Font("assets/RINGM___.TTF", 40)
    pr.print_render(screen, bigTitleFont, title, width/2, 80, True)
    subtitle = "Spells V1.0"
    pr.print_render(screen, bigSubtitleFont, subtitle, width/2, 120, True)
    startButton.draw_text(bigSubtitleFont, "Start", cursor.pos[0], cursor.pos[1], True)
    quitButton.draw_text(bigSubtitleFont, "quit", cursor.pos[0], cursor.pos[1], True)
    cursor.hover_check(quitButton.rect)
    cursor.hover_check(startButton.rect)

def state1():
    screen.fill((252, 245, 229))
    spellDict = sl.get_spells()
    statePath = 0
    if (spellDict == {}):
        statePath = 2.1
    else:
        spellSearch.clear()
        statePath = 2
        spellNames = spellDict["count"]*[""]
        spellIndices = spellDict["count"]*[""]
        for i in range(spellDict["count"]):
            spellNames[i] = spellDict["results"][i]["name"]
            spellIndices[i] = spellDict["results"][i]["index"]
        spellSearch.extend(spellNames)
        spellSearch.extend(spellIndices)
        spellSearch.sort()
    searchbar.reset()
    return statePath

def reconnect():
    screen.fill((252, 245, 229))
    title = "Connection Error"   
    pr.print_render(screen, bigSubtitleFont, title, width/2, 120, True)
    reconnectButton.draw_text(bigSubtitleFont, "Reconnect", cursor.pos[0], cursor.pos[1], True)
    cursor.hover_check(reconnectButton.rect)

def state2(state):
    screen.fill((252, 245, 229))
    searchbar.draw(cursor.pos[0], cursor.pos[1])
    backButton.draw_text(bigSubtitleFont, "back", cursor.pos[0], cursor.pos[1], True)
    if (searchbar.found == True):
        statePath = 2.9
    else:
        statePath = state
    cursor.hover_check(backButton.rect)
    return statePath

def loadSpell():
    loadedSpell.update(sl.load_spell(searchbar.savedText))
    if (loadedSpell == {}):
        statePath = 2.1
    else:
        statePath = 3
        searchbar.reset()
    return statePath

def state3():
    screen.fill((252, 245, 229))
    onlineDisplay.display_spell_page(screen, loadedSpell, 30, 40)
    backButton.draw_text(bigSubtitleFont, "back", cursor.pos[0], cursor.pos[1], True)
    cursor.hover_check(backButton.rect)

def loadScreen(text = "Loading..."):
    screen.fill((252, 245, 229))
    loadText = text
    pr.print_render(screen, bigSubtitleFont, loadText, width/2, height/2, True)
    border.drawBorder(screen)
    pygame.display.flip()

#start pygame
pygame.init()
bigSubtitleFont = pygame.font.Font("assets/RINGM___.TTF", 30)
bodyFont = pygame.font.Font("assets/MorrisRoman-Black.ttf", 18)
#resolution 
res = (540,720)
screen = pygame.display.set_mode(res)

#colours for drawing
color = (255,255,255)
colourLight = (170, 170, 170)
colourDark = (100, 100, 100)

#width and height variables
width = screen.get_width()
height = screen.get_height()

#fps clock
clock = pygame.time.Clock()

running = True
cursor = Mouse.Cursor(res[0], res[1])
state = 0
#new button
startButton = Button.Button(screen, colourDark[0], colourDark[1], colourDark[2], width/2-140, height/2-40, 280, 80)
reconnectButton = Button.Button(screen, colourDark[0], colourDark[1], colourDark[2], width/2-140, height/2-40, 280, 80)
quitButton = Button.Button(screen, colourDark[0], colourDark[1], colourDark[2], width/2-70, 600, 140, 40)
backButton = Button.Button(screen, colourDark[0], colourDark[1], colourDark[2], width/2-70, 600, 140, 40)
searchbar = Searchbar.Searchbar(screen, colourDark[0], colourDark[1], colourDark[2], width/2, 100, 240, 40)
#runtime loop
while running:
    border.drawBorder(screen)
    #clock ticks for fps
    clock.tick(60)
    fps = clock.get_fps()
    cursor.draw(screen)
    #print(state)
    pygame.display.flip()
    #print FPS in terminal
    #print("FPS: " + str(int(fps)))

    match state:
        case 0:
            startup()
        case 1:
            loadScreen()
            state = state1()
        case 2:
            state = state2(state)
        case 2.1:
            reconnect()
        case 2.9:
            loadScreen("Getting spell...")
            state = loadSpell()
        case 3:
            state3()
    #print("State: " + str(state))
    #event listener
    for event in pygame.event.get():
        cursor.handle_event(screen, event)
        match state:
            case 0:
                quitButton.handle_event(event)
                startButton.handle_event(event)
            case 2:
                backButton.handle_event(event)
                searchbar.handle_event(event, cursor.pos[0], cursor.pos[1], spellSearch)
                if len(searchbar.buttons) > 0:
                    for button in searchbar.buttons:
                        searchbar.buttons[button].handle_event(event)
            case 2.1:
                reconnectButton.handle_event(event)
            case 3:
                backButton.handle_event(event)
        
        if (quitButton.pressed):
            pygame.quit()
            running = False
        if (startButton.pressed):
            state = 1
            startButton.pressed = False
        if (reconnectButton.pressed):
            state = 1
            reconnectButton.pressed = False
        if (backButton.pressed):
            if (state == 3):
                state = 2
            else:
                state = 0
            backButton.pressed = False
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False
    