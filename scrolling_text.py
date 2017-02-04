import pygame
from pygame.locals import *
from sys import exit

background_image_filename = 'background.jpg'
SCREEN_SIZE = (640, 427)
FONT_COLOR = (255,255,255)
message = "   The Phillies are great!   "

# define variables for fps_limit
fps_limit = 60

pygame.init()

# get the clock object
clock = pygame.time.Clock()

screen = pygame.display.set_mode(SCREEN_SIZE, 0, 32)

my_font = pygame.font.SysFont("arial", 32)
text_surface = my_font.render(message, True, FONT_COLOR)

x = 0
y = (SCREEN_SIZE[1] - text_surface.get_height()) - (SCREEN_SIZE[1] * .05)

background = pygame.image.load(background_image_filename).convert()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
            
    # limit the frame rate
    clock.tick(fps_limit)
    
    screen.blit(background, (0,0))
    
    x-=2
    if x < -text_surface.get_width():
        x = SCREEN_SIZE[0] 
        
    screen.blit(text_surface, (x,y))
    #screen.blit(text_surface, (x+text_surface.get_width(),y))
    pygame.display.update()
    
    