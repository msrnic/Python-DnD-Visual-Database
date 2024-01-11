import pygame
import difflib as d
from collections import Counter
import Button as b
class Searchbar:

    def __init__(self, surface, r, g, b, x, y, w, h, text = ""):
        self.screen = surface
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)
        self.rect.center = (self.x, self.y)
        self.colourInactive = (r, g, b)
        self.colourActive = (r + 70, g + 70, b + 70)
        self.colour = self.colourInactive
        self.pressed = False
        self.hovering = False
        self.font = pygame.font.Font("assets/MorrisRoman-Black.ttf", (h - 5))
        self.fontRescale = pygame.font.Font("assets/MorrisRoman-Black.ttf", int(0.75*(h - 5)))
        self.text = text
        self.textPrint = self.font.render(self.text, True, "black")
        self.found = False
        self.savedText = ""
        self.suggested = []
        self.buttons = {}
        self.wideningList = [self.w, self.textPrint.get_width() + 5]
        self.xList = [self.x, self.textPrint.get_rect().x + 5]

    def collide(self, mX, mY):
        if (self.rect.collidepoint((mX, mY))):
            self.colour = self.colourActive
        else:
            self.colour = self.colourInactive

    def draw(self, mX, mY):
        resize = max(self.w, self.textPrint.get_width() + 5)
        self.rect.w = resize
        centerOffset = max(self.x, self.textPrint.get_rect().x + 5)
        self.rect.center = (centerOffset, self.y)
        pygame.draw.rect(self.screen, self.colour, self.rect, 2)
        self.screen.blit(self.textPrint, (self.rect.x + 5, self.rect.y + 5))
        if (len(self.suggested) > 0):
            for button in self.buttons:
                self.buttons[button].rect.w = resize
                self.buttons[button].rect.center = (centerOffset, self.buttons[button].y)
                self.buttons[button].draw_text(self.fontRescale, button, mX, mY, False)
    def handle_event(self, event, mX, mY, searchList):
        invalidKeys = [pygame.K_LSHIFT, pygame.K_RSHIFT]
        if (event.type == pygame.MOUSEBUTTONUP):
            if (self.rect.collidepoint((mX, mY))):
                self.pressed = True
            else:
                self.pressed = False
            buttonResult = ""
            buttonResult = self.buttonPresses(searchList)
            if buttonResult != "":
                self.found = True
                self.savedText = buttonResult
            else:
                self.found = False
        if (self.pressed):
            self.colour = self.colourActive
        else:
            self.collide(mX, mY)
        if (event.type == pygame.KEYDOWN):
            if (self.pressed):
                if (event.key == pygame.K_RETURN):
                    finder = ""
                    finder = self.search(self.text, searchList)
                    if (finder != ""):
                        self.found = True
                        self.savedText = finder
                        self.text = ""
                        self.buttons = {}
                    elif (len(self.suggested) == 1):
                        self.found = True
                        self.savedText = self.suggested[0]
                        self.text = ""
                        self.buttons = {}
                    else:
                        self.found = False
                elif (event.key == pygame.K_BACKSPACE):
                    self.text = self.text[:-1]
                    self.search3(self.text, searchList)
                    if self.text == "":
                        self.suggested.clear()
                        self.buttons.clear()
                        self.wideningList.clear()
                elif (event.key == pygame.K_ESCAPE):
                    self.pressed = False
                elif (event.key not in invalidKeys):
                    self.text += event.unicode
                    self.search3(self.text, searchList)
                self.textPrint = self.font.render(self.text, True, "black")

    def search(self, query, matchList):
        if (len(self.suggested) == 1):
            index = matchList.index(self.suggested[0])
            for c in query:
                    if (c.isupper()):
                        result = matchList[index + int(len(matchList)/2)]
                    else:    
                        result = matchList[index]
                    break
            return result
        result = ""
        for i in range(len(matchList)):
            if (query == matchList[i]):
                for c in query:
                    if (c.isupper()):
                        result = matchList[i + int(len(matchList)/2)]
                    else:    
                        result = matchList[i]
                    break
                break
        return result

    def reset(self):
        self.found = False
        self.suggested.clear()
        self.savedText = ""
        self.text = ""
        self.buttons.clear()
        self.xList.clear()
        self.wideningList.clear()
        self.textPrint = self.font.render(self.text, True, "black")
        
    def search3(self, query, matchList):
        nameList = matchList[:319]
        self.suggested = sorted(nameList, key=lambda x: d.SequenceMatcher(None, x, query).ratio(), reverse=True)
        self.suggested = self.suggested[:10]
        i = 1
        for name in self.suggested:
            self.buttons.update({name: b.Button(self.screen, self.colour[0], self.colour[1], self.colour[2], self.x, (self.y) + (i * self.h), self.rect.w, self.rect.h)})
            self.wideningList.append(self.buttons[name].textPrint.get_width() + 5)
            self.xList.append(self.buttons[name].textPrint.get_rect().x + 5)
            i += 1

    def buttonPresses(self, matchList):
        result = ""
        if len(self.buttons) > 0:
            for button in self.buttons:
                if self.buttons[button].pressed == True:
                    tempIndex = matchList.index(button)
                    index = tempIndex + int(len(matchList)/2)
                    result = matchList[index]
        return result