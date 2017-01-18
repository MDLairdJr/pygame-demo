import pygame, sys
from pygame.locals import *

RED = (255, 0, 0)
YELLOW = (255, 255, 0)

def main():
    pygame.init()
    screen = pygame.display.set_mode((400,300))
    
    pygame.draw.circle(screen, RED, (40,40), 20)
    pygame.display.update()
    
    while True:
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