import pygame
def drawBorder(screen):
    colourDark = (100, 100, 100)
    diamond1 = [(25, 15), (35, 25), (25, 35), (15, 25)]
    diamond2 = [(screen.get_width() - 25, 15), (screen.get_width() - 35, 25), (screen.get_width() - 25, 35), (screen.get_width() - 15, 25)]
    diamond3 = [(25, screen.get_height() - 15), (35, screen.get_height() - 25), (25, screen.get_height() - 35), (15, screen.get_height() - 25)]
    diamond4 = [(screen.get_width() - 25, screen.get_height() - 15), (screen.get_width() - 35, screen.get_height() - 25), (screen.get_width() - 25, screen.get_height() - 35), (screen.get_width() - 15, screen.get_height() - 25)]
    pygame.draw.rect(screen, colourDark, [0, 65, 15, screen.get_height() - 130])
    pygame.draw.rect(screen, colourDark, [screen.get_width() - 15, 65, 15, screen.get_height() - 130])
    pygame.draw.rect(screen, colourDark, [65, 0, screen.get_width() - 130, 15])
    pygame.draw.rect(screen, colourDark, [65, screen.get_height() - 15, screen.get_width() - 130, 15])
    
    pygame.draw.rect(screen, (0, 0, 0), [-15, 60, 30, screen.get_height() - 120], 5)
    pygame.draw.rect(screen, (0, 0, 0), [screen.get_width() - 15, 60, 30, screen.get_height() - 120], 5)
    pygame.draw.rect(screen, (0, 0, 0), [60, -15, screen.get_width() - 120, 30], 5)
    pygame.draw.rect(screen, (0, 0, 0), [60, screen.get_height() - 15, screen.get_width() - 120, 30], 5)
    
    pygame.draw.rect(screen, colourDark, [0, 0, 60, 15])
    pygame.draw.rect(screen, colourDark, [screen.get_width() - 60, 0, 60, 15])
    pygame.draw.rect(screen, colourDark, [0, screen.get_height() - 15, 60, 15])
    pygame.draw.rect(screen, colourDark, [screen.get_width() - 60, screen.get_height() - 15, 60, 15])
    
    pygame.draw.rect(screen, colourDark, [0, 15, 15, 45])
    pygame.draw.rect(screen, colourDark, [screen.get_width() - 15, 15, 15, 45])
    pygame.draw.rect(screen, colourDark, [0, screen.get_height() - 60, 15, 45])
    pygame.draw.rect(screen, colourDark, [screen.get_width() - 15, screen.get_height() - 60, 15, 45])
    
    pygame.draw.circle(screen, colourDark, (15, 15), 50, draw_bottom_right = True)
    pygame.draw.circle(screen, colourDark, (15, screen.get_height() - 15), 50, draw_top_right = True)
    pygame.draw.circle(screen, colourDark, (screen.get_width() - 15, 15), 50, draw_bottom_left = True)
    pygame.draw.circle(screen, colourDark, (screen.get_width() - 15, screen.get_height() - 15), 50, draw_top_left = True)
    
    pygame.draw.circle(screen, (0, 0, 0), (15, 15), 50, width = 5, draw_bottom_right = True)
    pygame.draw.circle(screen, (0, 0, 0), (15, screen.get_height() - 15), 50, width = 5, draw_top_right = True)
    pygame.draw.circle(screen, (0, 0, 0), (screen.get_width() - 15, 15), 50, width = 5, draw_bottom_left = True)
    pygame.draw.circle(screen, (0, 0, 0), (screen.get_width() - 15, screen.get_height() - 15), 50, width = 5, draw_top_left = True)
    
    pygame.draw.circle(screen, (255, 255, 0), (25, 25), 20)
    pygame.draw.circle(screen, (255, 255, 0), (screen.get_width() - 25, 25), 20)
    pygame.draw.circle(screen, (255, 255, 0), (25, screen.get_height() - 25), 20)
    pygame.draw.circle(screen, (255, 255, 0), (screen.get_width() - 25, screen.get_height() - 25), 20)

    pygame.draw.circle(screen, (0, 0, 0), (25, 25), 20, width = 2)
    pygame.draw.circle(screen, (0, 0, 0), (screen.get_width() - 25, 25), 20, width = 2)
    pygame.draw.circle(screen, (0, 0, 0), (25, screen.get_height() - 25), 20, width = 2)
    pygame.draw.circle(screen, (0, 0, 0), (screen.get_width() - 25, screen.get_height() - 25), 20, width = 2)

    pygame.draw.polygon(screen, (255, 0, 0), diamond1)
    pygame.draw.polygon(screen, (255, 0, 0), diamond2)
    pygame.draw.polygon(screen, (255, 0, 0), diamond3)
    pygame.draw.polygon(screen, (255, 0, 0), diamond4)
    
    pygame.draw.polygon(screen, (0, 0, 0), diamond1, width = 1)
    pygame.draw.polygon(screen, (0, 0, 0), diamond2, width = 1)
    pygame.draw.polygon(screen, (0, 0, 0), diamond3, width = 1)
    pygame.draw.polygon(screen, (0, 0, 0), diamond4, width = 1)