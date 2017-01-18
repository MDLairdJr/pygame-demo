import pygame, sys, time
from pygame.locals import *

RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)

def main():
    pygame.init()
    screen = pygame.display.set_mode((400,300))
    
    x = 20
    y = 20
    
    while True:
        screen.fill(BLACK)
        pygame.draw.circle(screen, YELLOW, (x,y), 10)
        pygame.display.update()
        x+=1
        time.sleep(0.01)
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
                
# Before executing the code, the python interpreter will define 
# a few special variables. For example, if the python interpreter 
# is running this module (shape.py) as the main program, it sets
# the special __name__ variable to have a value "__main__".  If
# this file is being imported from another module, __name__ will 
# be set to the module's name instead.  Since we're running this as
# the main program, we want the main() method to be called.
if __name__ == '__main__':
    main()