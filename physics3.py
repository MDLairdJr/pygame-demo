# https://www.youtube.com/watch?v=IoQ6s80JM0s&index=2&list=PLE3D1A71BB598FEF6

import os
import sys
import math
import pygame
import pygame.mixer
import random
import euclid  # from https://pypi.python.org/pypi/euclid
from pygame.locals import *

# define some basic colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# create an array of potential circle colors
colors = [BLACK, RED, GREEN, BLUE]

# define the initial velocity
initial_velocity = 20

# define the screen size
screen_size = screen_width, screen_height = 600, 400

# define a circle class
class MyCircle:
    
    def __init__(self, position, size, color = (255, 255, 255), velocity = euclid.Vector2(0,0), width = 1):
        # use a position vector instead of x and y coordinates
        self.position = position
        self.size = size 
        self.color = color 
        self.width = width
        self.velocity = velocity
        
    def display(self):
        rx, ry = int(self.position.x), int(self.position.y)
        pygame.draw.circle(screen, self.color, (rx, ry), self.size, self.width)
        
    def move(self):
        self.position += self.velocity * dtime
        
    def change_velocity(self, velocity):
        self.velocity = velocity
       
def get_random_velocity():
    new_angle = random.uniform(0, math.pi*2)
    new_x = math.sin(new_angle)
    new_y = math.cos(new_angle)
    new_vector = euclid.Vector2(new_x, new_y)
    new_vector.normalize()
    new_vector *= initial_velocity   # pixels per second
    return new_vector

# set the display and get the surface object
screen = pygame.display.set_mode(screen_size)

# get the clock object
clock = pygame.time.Clock()

# set the window title
pygame.display.set_caption('Vectors and Motion!')

# create an array to hold our set of circles
number_of_circles = 10
my_circles = []

# create instances of the MyCircle class to populate the array
for n in range(number_of_circles):
    size = random.randint(10, 20)
    x = random.randint(size, screen_width-size)
    y = random.randint(size, screen_height-size)
    color = random.choice(colors)
    velocity = get_random_velocity()
    my_circle = MyCircle(euclid.Vector2(x,y), size, color, velocity)
    my_circles.append(my_circle)
    
direction_tick = 0.0

# define variables for fps and continued running
fps_limit = 60
run_me = True

while run_me:
    # limit the frame rate and capture the time in 
    # milliseconds since the last tick (dtime_ms)
    dtime_ms = clock.tick(fps_limit)
    
    # divide by 1000 to get actual time in seconds
    dtime = dtime_ms/1000.0
    
    # increase direction_tick which keeps track of 
    # when we want to change direction
    direction_tick += dtime
    if(direction_tick > 1.0):
        direction_tick = 0.0
        random_circle = random.choice(my_circles)
        new_velocity = get_random_velocity()
        random_circle.change_velocity(new_velocity)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run_me = False
            
    # lock the screen
    screen.lock()
            
    # Clear the screen
    screen.fill(WHITE)
    
    # display the instances of the circles in the array
    for my_circle in my_circles:
        my_circle.move()
        my_circle.display()
    
    # unlock the screen
    screen.unlock()
    
    # display everything in the screen
    pygame.display.flip()
    
# quit the game
pygame.quit()
sys.exit()
