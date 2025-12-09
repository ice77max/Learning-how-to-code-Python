import pygame, sys
from pygame.locals import *

FPS = 30
WinWidth = 640
WinHeight = 480
RevealSpeed = 8
BoxSize = 40
GapSize = 10
BoardWidth = 10
BoardHeight = 7
assert (BoardWidth * BoardHeight) %2 == 0, "Board needs to have an even number of boxes for pairs of matches."
xMargin = int(WinWidth - (BoardWidth * (BoxSize + GapSize)) / 2)
yMargin = int(WinHeight - (BoardHeight * (BoxSize + GapSize)) / 2)

# Colors        r    g    b
GRAY        = (100, 100, 100)
NAVY_BLUE   = ( 60,  60, 100)
WHITE       = (255, 255, 255)
RED         = (255,   0,   0)
GREEN       = (  0, 255,   0)
BLUE        = (  0,   0, 255)
YELLOW      = (255, 255,   0)
ORANGE      = (255, 128,   0)
PURPLE      = (255,   0, 255)
CYAN        = (  0, 255, 255)

BgColor = NAVY_BLUE
LightBgColor = GRAY
BoxColor = WHITE
HighLightColor = BLUE

DONUT = "donut" 
SQUARE = "square"
DIAMOND = "diamond"
LINES = "lines"
OVAL = "oval"

AllColors = (RED, GREEN, BLUE, YELLOW, ORANGE, PURPLE, CYAN)
AllShapes = (DONUT, SQUARE, DIAMOND, LINES, OVAL)
assert len(AllColors) * len(AllShapes) * 2 >= BoardWidth * BoardHeight, "Board is too big for the number of shapes/colors defined."

def main():
    global fpsClock, screen
    pygame.init()
    fpsClock = pygame.time.Clock()
    screen = pygame.display.set_mode((WinWidth, WinHeight))

    mouseX = 0
    mouseY = 0
    
    pygame.display.set_caption("Memory Puzzle")

    mainBoard = getRandomizedBoard()
    revealedBoxes = generateRevealedBoxesData(False)
    
    firstSelection = None
    
    screen.fill(BgColor)
    startGameAnimation(mainBoard)

    while True:
        mouseClicked = False
        
        screen.fill(BgColor)
        drawBoard(mainBoard, revealedBoxes)
        
        for event in pygame.get():
            if event.type == pygame.QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONUP:
                mouseX, mouseY = event.pos
                mouseClicked = True
                
        boxX, boxY = getBoxAtPixel(mouseX, mouseY)
        if boxX != None and boxY != None:
            # the mouse is currently over a box.
            if not revealedBoxes[boxX][boxY]:
                drawHighlightBox(boxX, boxY)
            if not revealedBoxes[boxX][boxY] and mouseClicked:
                revealBoxesAnimation(mainBoard, [(boxX, boxY)])
                revealedBoxes[boxX][boxY] = True # set the box as "revealed"
                if firstSelection == None: # the current box was the first box clicked
                    firstSelection = (boxX, boxY)
                else: # the current box was the second one to be clicked
                    # check if there is a match between the two icons
                    icon1shape, icon1color = getShapeAndColor(mainBoard, firstSelection[0], firstSelection[1])
                    icon2shape, icon2color = getShapeAndColor(mainBoard, boxX, boxY)

                    if icon1shape != icon2shape or icon1color != icon2color:
                        # icons don't match. Re-cover both selections
                        pygame.time.wait(1000) # wait 1s in milliseconds
                        coverBoxesAnimation(mainBoard, [(firstSelection[0], firstSelection[1]), (boxX, boxY)])
                        revealedBoxes[boxX][boxY] = False
                    elif hasWon(revealedBoxes): # check if all pairs found
                        gameWonAnimation(mainBoard)
                        pygame.time.wait(2000)
                        
                        # Reset the board
                        mainBoard = getRandomizedBoard()
                        revealedBoxes = generateRevealedBoxesData(False)

                        # Show the fully unrevealed board for a second
                        drawBoard(mainBoard, revealedBoxes)
                        pygame.display.update()
                        pygame.time.wait(1000)

                        # Replay the start game animation
                        startGameAnimation(mainBoard)
                    firstSelection = None # reset firstSelection variable
                    
        # Redraw the screen and wait a clock tick.
        pygame.display.update()
        fpsClock.tick(FPS)

def generateRevealedBoxesData(val):
    revealedBoxes = []
    for i in range(BoardWidth):
        revealedBoxes.append([val] * BoardHeight)
    return revealedBoxes

def getRandomizedBoard():
    # Get a list of every possible shape in every possible color.
    icons = [] 
    for color in AllColors:
        for shape in AllShapes:
            icons.append((shape, color))

    random.shuffle(icons) # randomize the order of the icons list
    numIconsUsed = int(BoardWidth * BoardHeight / 2) # calculate how many icons are needed
    icons = icons[:numIconsUsed] * 2 # make two of each
    random.shuffle(icons)
    
    # create the board data structure, with randomly placed icons
    board = []
    for x in range(BoardWidth):
        column = []
        for y in range(BoardHeight):
            column.append(icons[0])
            del icons[0] # remove the icons as we assign them
        board.append(column)
    return board

