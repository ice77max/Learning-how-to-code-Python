import pygame

# pygame setup
pygame.init()


screen = pygame.display.set_mode((1800, 900))
pygame.display.set_caption("Max's Plane")
clock = pygame.time.Clock()
delta_time = 0
moveSpeed = 100

# player setup

plane = pygame.image.load("PyGame/files/Max plain.png").convert() # load image
plane.set_colorkey((255, 255, 255)) # ignore white color of the background
scale_by = 2.2
plane = pygame.transform.scale(plane, (plane.get_width() / scale_by,
                                       plane.get_height() / scale_by)) # scale down
plane = pygame.transform.flip(plane, True, False)
plane_original = plane

plane_rec = plane.get_rect(center=screen.get_rect().center)
player_pos = pygame.Vector2(plane_rec.center)

tilt_angle = 0
target_tilt = 0
tilt_speed = 4


# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill("#94EAFF")
    
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] or keys[pygame.K_UP]:
        player_pos.y -= moveSpeed * delta_time
        target_tilt = 15
    elif keys[pygame.K_s] or keys[pygame.K_DOWN]:
        player_pos.y += moveSpeed * delta_time
        target_tilt = -15
    else:
        target_tilt = 0
    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        player_pos.x += moveSpeed * delta_time
    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        player_pos.x -= moveSpeed * delta_time 
    
    tilt_angle += (target_tilt - tilt_angle) * tilt_speed * delta_time
    plane = pygame.transform.rotate(plane_original, tilt_angle) # rotation up and down
    plane_rec = plane.get_rect(center=player_pos)
    
    screen.blit(plane, plane_rec)
    
    # tilt_angle = 0 # centers plane and by taking it out of key if statements, plane can be tilted while using other keys
    
    pygame.display.flip()
    delta_time = clock.tick(60) 
    delta_time = max(0.001, min(0.1, delta_time))
    
    
pygame.quit()