# https://www.youtube.com/watch?v=IoQ6s80JM0s&index=2&list=PLE3D1A71BB598FEF6

import os
import sys
import math
import pygame
import pygame.mixer
import random
from pygame.locals import *

# define some basic colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# create an array of potential circle colors
colors = [BLACK, RED, GREEN, BLUE]

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
pygame.display.set_caption('Randomness and Order!')

# create an array to hold our set of circles
number_of_circles = 10
my_circles = []

# create instances of the MyCircle class to populate the array
for n in range(number_of_circles):
    size = random.randint(10, 20)
    x = random.randint(size, screen_width-size)
    y = random.randint(size, screen_height-size)
    color = random.choice(colors)
    my_circles.append(MyCircle((x, y), size, color))

# define variables for fps and continued running
fps_limit = 60
run_me = True

while run_me:
    # limit the frame rate
    clock.tick(fps_limit)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run_me = False
            
    # lock the screen
    screen.lock()
            
    # Clear the screen
    screen.fill(WHITE)
    
    # display the instances of the circles in the array
    for my_circle in my_circles:
        my_circle.display()
    
    # unlock the screen
    screen.unlock()
    
    # display everything in the screen
    pygame.display.flip()
    
# quit the game
pygame.quit()
sys.exit()
