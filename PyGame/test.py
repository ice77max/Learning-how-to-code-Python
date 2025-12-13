import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((600, 600))
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fade loop
    for start, end, step in ((0, 255, 1), (255, 0, -1)):
        for i in range(start, end, step):
            screen.fill((i, i, i))  # grayscale background
            pygame.display.flip()
            clock.tick(60)  # control speed

pygame.quit()
sys.exit()