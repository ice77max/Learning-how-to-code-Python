import pygame, sys, random
from pygame.locals import *

FPS = 30
WinWidth = 640
WinHeight = 480
RevealSpeed = 8
BoxSize = 40
GapSize = 10
BoardWidth = 10
BoardHeight = 7
assert (BoardWidth * BoardHeight) % 2 == 0, "Board must have an even number of boxes."

xMargin = int((WinWidth - (BoardWidth * (BoxSize + GapSize))) / 2)
yMargin = int((WinHeight - (BoardHeight * (BoxSize + GapSize))) / 2)

# Colors
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

assert len(AllColors) * len(AllShapes) * 2 >= BoardWidth * BoardHeight, \
    "Board is too big for available shapes/colors."

def main():
    global fpsClock, screen
    pygame.init()
    fpsClock = pygame.time.Clock()
    screen = pygame.display.set_mode((WinWidth, WinHeight))

    pygame.display.set_caption("Memory Puzzle")

    mouseX = 0
    mouseY = 0

    mainBoard = getRandomizedBoard()
    revealedBoxes = generateRevealedBoxesData(False)
    firstSelection = None

    screen.fill(BgColor)
    startGameAnimation(mainBoard)

    while True:
        mouseClicked = False
        screen.fill(BgColor)
        drawBoard(mainBoard, revealedBoxes)

        # FIX HERE — changed pygame.get() → pygame.event.get()
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONUP:
                mouseX, mouseY = event.pos
                mouseClicked = True

        boxX, boxY = getBoxAtPixel(mouseX, mouseY)

        if boxX is not None and boxY is not None:
            if not revealedBoxes[boxX][boxY]:
                drawHighlightBox(boxX, boxY)

            if not revealedBoxes[boxX][boxY] and mouseClicked:
                revealBoxesAnimation(mainBoard, [(boxX, boxY)])
                revealedBoxes[boxX][boxY] = True

                if firstSelection is None:
                    firstSelection = (boxX, boxY)
                else:
                    icon1shape, icon1color = getShapeAndColor(mainBoard, firstSelection[0], firstSelection[1])
                    icon2shape, icon2color = getShapeAndColor(mainBoard, boxX, boxY)

                    if icon1shape != icon2shape or icon1color != icon2color:
                        pygame.time.wait(1000)
                        coverBoxesAnimation(mainBoard, [firstSelection, (boxX, boxY)])
                        revealedBoxes[firstSelection[0]][firstSelection[1]] = False
                        revealedBoxes[boxX][boxY] = False
                    else:
                        if hasWon(revealedBoxes):
                            gameWonAnimation(mainBoard)
                            pygame.time.wait(2000)
                            mainBoard = getRandomizedBoard()
                            revealedBoxes = generateRevealedBoxesData(False)
                            drawBoard(mainBoard, revealedBoxes)
                            pygame.display.update()
                            pygame.time.wait(1000)
                            startGameAnimation(mainBoard)

                    firstSelection = None

        pygame.display.update()
        fpsClock.tick(FPS)


def generateRevealedBoxesData(val):
    return [[val] * BoardHeight for _ in range(BoardWidth)]


def getRandomizedBoard():
    icons = [(shape, color) for color in AllColors for shape in AllShapes]
    random.shuffle(icons)

    numIconsUsed = (BoardWidth * BoardHeight) // 2
    icons = icons[:numIconsUsed] * 2
    random.shuffle(icons)

    board = []
    for x in range(BoardWidth):
        column = []
        for y in range(BoardHeight):
            column.append(icons.pop())
        board.append(column)
    return board


def splitIntoGroupsOf(groupSize, theList):
    return [theList[i:i + groupSize] for i in range(0, len(theList), groupSize)]


def leftTopCoordsOfBox(boxX, boxY):
    left = boxX * (BoxSize + GapSize) + xMargin
    top = boxY * (BoxSize + GapSize) + yMargin
    return (left, top)


def getBoxAtPixel(x, y):
    for boxX in range(BoardWidth):
        for boxY in range(BoardHeight):
            left, top = leftTopCoordsOfBox(boxX, boxY)
            boxRect = pygame.Rect(left, top, BoxSize, BoxSize)
            if boxRect.collidepoint(x, y):
                return (boxX, boxY)
    return (None, None)


def drawIcon(shape, color, boxX, boxY):
    quarter = int(BoxSize * 0.25)
    half = int(BoxSize * 0.5)

    left, top = leftTopCoordsOfBox(boxX, boxY)

    if shape == DONUT:
        pygame.draw.circle(screen, color, (left + half, top + half), half - 5)
        pygame.draw.circle(screen, BgColor, (left + half, top + half), quarter - 5)

    elif shape == SQUARE:
        pygame.draw.rect(screen, color, (left + quarter, top + quarter, BoxSize - half, BoxSize - half))

    elif shape == DIAMOND:
        pygame.draw.polygon(screen, color,
            [(left + half, top), (left + BoxSize - 1, top + half),
             (left + half, top + BoxSize - 1), (left, top + half)])

    elif shape == LINES:
        for i in range(0, BoxSize, 4):
            pygame.draw.line(screen, color, (left, top + i), (left + i, top))
            pygame.draw.line(screen, color, (left + i, top + BoxSize - 1),
                                          (left + BoxSize - 1, top + 1))

    elif shape == OVAL:
        pygame.draw.ellipse(screen, color, (left, top + quarter, BoxSize, quarter * 2))


def getShapeAndColor(board, boxX, boxY):
    return board[boxX][boxY]


def drawBoxCovers(board, boxes, coverage):
    for boxX, boxY in boxes:
        left, top = leftTopCoordsOfBox(boxX, boxY)
        pygame.draw.rect(screen, BgColor, (left, top, BoxSize, BoxSize))

        shape, color = getShapeAndColor(board, boxX, boxY)
        drawIcon(shape, color, boxX, boxY)

        if coverage > 0:
            pygame.draw.rect(screen, BoxColor, (left, top, coverage, BoxSize))

    pygame.display.update()
    fpsClock.tick(FPS)


def revealBoxesAnimation(board, boxes):
    for coverage in range(BoxSize, -RevealSpeed - 1, -RevealSpeed):
        drawBoxCovers(board, boxes, coverage)


def coverBoxesAnimation(board, boxes):
    for coverage in range(0, BoxSize + RevealSpeed, RevealSpeed):
        drawBoxCovers(board, boxes, coverage)


def drawBoard(board, revealed):
    for boxX in range(BoardWidth):
        for boxY in range(BoardHeight):
            left, top = leftTopCoordsOfBox(boxX, boxY)
            if not revealed[boxX][boxY]:
                pygame.draw.rect(screen, BoxColor, (left, top, BoxSize, BoxSize))
            else:
                shape, color = getShapeAndColor(board, boxX, boxY)
                drawIcon(shape, color, boxX, boxY)


def drawHighlightBox(boxX, boxY):
    left, top = leftTopCoordsOfBox(boxX, boxY)
    pygame.draw.rect(screen, HighLightColor, (left - 5, top - 5, BoxSize + 10, BoxSize + 10), 4)


def startGameAnimation(board):
    coveredBoxes = generateRevealedBoxesData(False)
    boxes = [(x, y) for x in range(BoardWidth) for y in range(BoardHeight)]
    random.shuffle(boxes)
    boxGroups = splitIntoGroupsOf(8, boxes)

    drawBoard(board, coveredBoxes)
    for group in boxGroups:
        revealBoxesAnimation(board, group)
        coverBoxesAnimation(board, group)


def gameWonAnimation(board):
    coveredBoxes = generateRevealedBoxesData(True)
    color1 = LightBgColor
    color2 = BgColor

    for _ in range(13):
        color1, color2 = color2, color1
        screen.fill(color1)
        drawBoard(board, coveredBoxes)
        pygame.display.update()
        pygame.time.wait(300)


def hasWon(revealedBoxes):
    return all(all(row) for row in revealedBoxes)


if __name__ == "__main__":
    main()
