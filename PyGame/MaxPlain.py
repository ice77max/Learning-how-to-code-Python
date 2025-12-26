import pygame

# pygame setup
pygame.init()

screen = pygame.display.set_mode((1800, 1000))
pygame.display.set_caption("Max's Plane")
clock = pygame.time.Clock()
delta_time = 0
moveSpeed = 500

# player setup
player_pos = pygame.Vector2(screen.get_width() / 2,
                            screen.get_width() / 2)

plane = pygame.image.load("PyGame/files/Max plain.png").convert()
plane.set_colorkey((255, 255, 255))

plane_rec = plane.get_rect()


# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill("#94EAFF")
    screen.blit(plane, player_pos)
    
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] or keys[pygame.K_UP]:
        player_pos.y -= moveSpeed * delta_time
    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        player_pos.x += moveSpeed * delta_time
    if keys[pygame.K_s] or keys[pygame.K_DOWN]:
        player_pos.y += moveSpeed * delta_time
    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        player_pos.x -= moveSpeed * delta_time 
    
    
    pygame.display.flip()
    delta_time = clock.tick(60) 
    delta_time = max(0.001, min(0.1, delta_time))
    
    
pygame.quit()