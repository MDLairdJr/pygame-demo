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

# define a 2D vector for gravity
gravity = euclid.Vector2(0.0, 80.0)
drag = 0.1

# define the screen size
screen_size = screen_width, screen_height = 600, 400

# define a circle class
class MyCircle:
    # The position is the center point of the circle and the
    # size is the radius of the circle
    def __init__(self, position, size, color = (255, 255, 255), velocity = euclid.Vector2(0,0), accel = euclid.Vector2(0,0), width = 1):
        # use a position vector instead of x and y coordinates
        self.position = position
        self.size = size 
        self.color = color 
        self.width = width
        self.velocity = velocity
        self.accel = accel
        
    def display(self):
        rx, ry = int(self.position.x), int(self.position.y)
        pygame.draw.circle(screen, self.color, (rx, ry), self.size, self.width)
        
    def move(self):
        self.position += self.velocity * dtime + 0.5 * (self.accel * (dtime**2))
        self.velocity += self.accel * dtime
        self.velocity -= self.velocity * drag * dtime
        self.bounce()
        
    def change_velocity(self, velocity):
        self.velocity = velocity
        
    def bounce(self):
        if self.position.x <= self.size:
            self.position.x = 2 * self.size - self.position.x
            self.velocity = self.velocity.reflect(euclid.Vector2(1,0))
            
        elif self.position.x >= screen_width - self.size:
            self.position.x = 2 * (screen_width - self.size) - self.position.x
            self.velocity = self.velocity.reflect(euclid.Vector2(1,0))
            
        if self.position.y <= self.size:
            self.position.y = 2 * self.size - self.position.y 
            self.velocity = self.velocity.reflect(euclid.Vector2(0,1))
            
        elif self.position.y >= screen_height - self.size:
            self.position.y = 2 * (screen_height - self.size) - self.position.y 
            self.velocity = self.velocity.reflect(euclid.Vector2(0,1))
            
    # Equation for distance between surfaces is
    # d(t) = |A(t) - B(t)| - (Ra + Rb)
    # Absolute value of A's position minus B's position
    # minus the radius of the two circles
    def surface_distance(self, other, time):
        radiiAB = self.size + other.size
        posA = self.position + self.velocity * time + 0.5*(self.accel * (time**2))
        posB = other.position + other.velocity * time + 0.5*(other.accel * (time**2))
        posAB = abs(posA - posB)
        return posAB - radiiAB
        
    def collide(self, other):
        if self.surface_distance(other, dtime) <= 0:
            collision_vector = self.position - other.position
            collision_vector.normalize()
            self.velocity = self.velocity.reflect(collision_vector)
            other.velocity = other.velocity.reflect(collision_vector)
       
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
pygame.display.set_caption('Personal Bubbles!')

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
    my_circle = MyCircle(euclid.Vector2(x,y), size, color, velocity, gravity)
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
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run_me = False
            
    # lock the screen
    screen.lock()
            
    # Clear the screen
    screen.fill(WHITE)
    
    # display the instances of the circles in the array
    for i, my_circle in enumerate(my_circles):
        my_circle.move()
        for my_circle2 in my_circles[i+1:]:
            my_circle.collide(my_circle2)
        my_circle.display()
    
    # unlock the screen
    screen.unlock()
    
    # display everything in the screen
    pygame.display.flip()
    
# quit the game
pygame.quit()
sys.exit()
