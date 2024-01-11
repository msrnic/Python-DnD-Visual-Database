import pygame
pygame.font.init()
class Button:
    def __init__(self, surface, r,g,b, x, y, w, h, font = pygame.font.SysFont("Arial", 30, False, False), text = ""):
        self.screen = surface
        self.colour = (r, g, b)
        self.colourActive = (r+70, g+70, b+70)
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)
        self.hovering = False
        self.pressed = False
        self.font = font
        self.text = text
        self.textPrint = self.font.render(self.text, True, "black")

    def draw_blank(self, mX, mY, border):
        if (self.rect.collidepoint((mX, mY))):
            self.hovering = True
            pygame.draw.rect(self.screen, self.colourActive, self.rect)
        else:
            self.hovering = False
            pygame.draw.rect(self.screen, self.colour, self.rect)
        if (border == True):
            pygame.draw.rect(self.screen, (0, 0, 0), self.rect, width = 2)
        
    def draw_text(self, font, text, mX, mY, border):
        self.draw_blank(mX, mY, border)
        text = font.render(text, True, "Black")
        textRect = text.get_rect()
        self.textPrint = text
        textRect.center = self.rect.center
        self.screen.blit(text, textRect)
    
    def handle_event(self, event):
        if (event.type == pygame.MOUSEBUTTONDOWN and self.hovering):
            self.pressed = True
        else:
            self.pressed = False