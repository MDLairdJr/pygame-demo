# https://www.youtube.com/watch?v=7AKatTpNSNQ&index=1&list=PLE3D1A71BB598FEF6

import os
import sys
import math
import pygame
import pygame.mixer
from pygame.locals import *

# define some basic colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# define the screen size
screen_size = screen_width, screen_height = 600, 400

# define a circle class
class MyCircle:
    
    def __init__(self, (x, y), size, color = (255, 255, 255), width = 1):
        self.x = x
        self.y = y 
        self.size = size 
        self.color = color 
        self.width = width
        
    def display(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.size, self.width)
        

# set the display and get the surface object
screen = pygame.display.set_mode(screen_size)

# get the clock object
clock = pygame.time.Clock()

# set the window title
pygame.display.set_caption('Physics practice!')

# create instances of the MyCircle class
my_circle = MyCircle((100, 100), 10, RED)
my_circle_2 = MyCircle((200, 200), 30, BLUE)
my_circle_3 = MyCircle((300, 150), 40, GREEN, 4)
my_circle_4 = MyCircle((450, 250), 120, BLACK, 0)

# define variables for fps and continued running
fps_limit = 60
run_me = True

while run_me:
    # limit the frame rate
    clock.tick(fps_limit)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run_me = False
            
    # Clear the screen
    screen.fill(WHITE)
    
    # display the instance of my_circle
    my_circle.display()
    my_circle_2.display()
    my_circle_3.display()
    my_circle_4.display()
    
    # display everything in the screen
    pygame.display.flip()
    
# quit the game
pygame.quit()
sys.exit()

    