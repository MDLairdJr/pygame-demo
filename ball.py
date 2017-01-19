import pygame, sys, time
from pygame.locals import *

pygame.init()

size = width, height = 320, 240
speed = [2, 2]
BLACK = (0, 0, 0)

screen = pygame.display.set_mode(size)

ball = pygame.image.load("ball.bmp")
ballrect = ball.get_rect()

while 1:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
    
    time.sleep(0.01)
    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]
        
    screen.fill(BLACK)
    screen.blit(ball, ballrect)
    pygame.display.flip()
    