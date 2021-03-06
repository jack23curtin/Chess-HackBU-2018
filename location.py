import pygame

def location(num): #num is a list of two values, x and y
    x,y = pygame.display.get_surface().get_size()
    xunit=x/8
    yunit=y/8
    realx = (num[0] - 1) * xunit + (xunit / 2)  # x pixels
    realy = (8-num[1])*yunit+ (yunit/2) #y pixels
    return [realx, realy]