import pygame

class Cursor:

    def __init__(self, width, height):
        self.pos = pygame.mouse.get_pos()
        pygame.mouse.set_visible(False)
        self.sprite = pygame.image.load("assets/cursor/cursor.gif")
        self.isOver = False
        self.isPressed = False
        self.screenX = width
        self.screenY = height

    def draw(self, screen):
        self.update()
        #if in bounds, draw sprite
        if (not self.offScreen):
            pygame.Surface.convert(self.sprite)
            screen.blit(self.sprite, (self.pos[0], self.pos[1]))

    def hover_check(self, rect):
        self.update()
        #check if mouse is over chosen rectangle
        if (rect.collidepoint(self.pos)):
            self.isOver = True
        else:
            self.isOver = False
        
    def handle_event(self, screen, event):
        #change cursor texture on click
        if (event.type == pygame.MOUSEBUTTONDOWN):
            self.isPressed = True
        if (event.type == pygame.MOUSEBUTTONUP):
            self.isPressed = False
        self.update()
        
    def update(self):
        self.pos = pygame.mouse.get_pos()
        #load sprite only if in bounds of window
        if (pygame.mouse.get_focused() == 0):
            self.offScreen = True
        else:
            self.offScreen = False
        #change sprite based on interaction
        if (self.isPressed):
            self.sprite = pygame.image.load("assets/cursor/cursor_down.gif")
        elif (self.isOver):
            self.sprite = pygame.image.load("assets/cursor/cursor_open.gif")
        else:
            self.sprite = pygame.image.load("assets/cursor/cursor.gif")