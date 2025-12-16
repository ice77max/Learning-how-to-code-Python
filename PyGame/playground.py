import pygame, sys, random

pygame.init()

# setup

WIN_WIDTH, WIN_HEIGHT = 600, 500
SCREEN = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Playground")

# Colors

BLACK = pygame.Color("#0A0A0A")
WHITE = pygame.Color("#F3F3F3")
RED = pygame.Color("#D33E3E")
GREEN = pygame.Color("#71F147")
CYAN = pygame.Color("#3BEAF6")
PURPLE = pygame.Color("#922CFF")
BLUE = pygame.Color("#3F87FA")

allColors = [BLACK, WHITE, RED, GREEN, CYAN, PURPLE, BLUE]
# time 
FPS = 10
clock = pygame.time.Clock()

# game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            running = False

    SCREEN.fill(BLACK)

    randomPosition = (random.randint(10,590), random.randint(10, 490))

    pygame.draw.circle(SCREEN, random.choice(allColors), randomPosition, 10)
    
    pygame.display.update()
    
    clock.tick(FPS)


pygame.quit()
sys.exit()