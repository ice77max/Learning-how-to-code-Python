import pygame as pg

pg.init()
screen = pg.display.set_mode((500, 500))
pg.display.set_caption("Hello World!")

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    
    screen.fill("#F4FF61")
    
    
        
    pg.display.flip()
    
pg.quit()
