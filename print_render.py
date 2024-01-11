"""dunction that renders a string in the desired font and displays it on the surface.
Inputs are the surface, font, string to display, and 2 numbers for coordinates."""
def print_render(screen, font, line, locX, locY, centerMode):
    if (centerMode):
        line = font.render(line, True, "black")
        lineRect = line.get_rect(center = (screen.get_width()/2, locY))
        screen.blit(line, lineRect)
    else:
        line = font.render(line, True, "black")
        screen.blit(line, (locX, locY))