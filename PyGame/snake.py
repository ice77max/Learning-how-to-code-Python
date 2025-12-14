import pygame, random, sys
from pygame.locals import *

FPS = 15
WINDOWWIDTH = 640
WINDOWHEIGHT = 480
CELLSIZE = 20
assert WINDOWHEIGHT % CELLSIZE == 0, "WINDOW WIDTH MUST BE A MULTIPLE OF CELL SIZE."
assert WINDOWHEIGHT % CELLSIZE == 0, "Window height must be a multiple of cell size."
CELLWIDTH = int(WINDOWWIDTH / CELLSIZE)
CELLHEIGHT = int(WINDOWHEIGHT / CELLSIZE)

WHITE = (255, 255, 255)
BLACK = (0,0,0)
RED = (250,0,0)
GREEN = (0, 255, 0)
DARKGREEN = (0, 155, 0)
DARKGRAY = (40, 40, 40)
BGCOLOR = BLACK

UP = "up"
DOWN = "down"
LEFT = "left"
RIGHT = "right"

HEAD = 0

def main ():
    global FPSCLOCK, DISPLAYSURF, BASICFONT
    
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    BASICFONT = pygame.font.Font("freesansbold.ttf", 18)
    pygame.display.set_caption("Snake")

    showStartScreen()
    while True:
        runGame()
        showGameOverScreen()
        
        
def runGame():
    # set a random start point
    startx = random.randint(5, CELLWIDTH - 6)
    starty = random.randint(5, CELLHEIGHT - 6)
    wornCoords = [{"x": startx,     "y": starty},
                  {"x": startx - 1,     "y": starty},
                  {"x": startx - 2,     "y": starty}]
    direction = RIGHT

    # start the apple in a random place
    apple = getRandomLocation()
    
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            elif event.type == KEYDOWN:
                if (event.key == K_LEFT or event.key == K_a) and direction != RIGHT:
                    direction = LEFT
                elif (event.key == K_RIGHT or event.key == K_d) and direction != LEFT:
                    direction == RIGHT
                elif (event.key == K_UP or event.key == K_w) and direction != DOWN:
                    direction == UP
                elif (event.key == K_DOWN or event.key == K_s) and direction != UP:
                    direction == DOWN
                # using 2 buttons only
                elif (event.key == K_z) and direction == LEFT:
                    direction == UP
                elif (event.key == K_z) and direction == UP:
                    direction == LEFT
                elif (event.key == K_x) and direction == RIGHT:
                    direction == DOWN
                elif (event.key == K_x) and direction == DOWN:
                    direction == RIGHT
                elif event.key == K_ESCAPE:
                    terminate()
                    
    if wormCoords[HEAD]["x"]
                