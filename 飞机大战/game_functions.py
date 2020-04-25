import pygame,sys
from ship import Ship as ship

def check_keydown():
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                ship.moving_u = True
            elif event.key == pygame.K_DOWN:
                ship.moving_d = True
        
def check_keyup():
    for event in pygame.event.get():
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                ship.moving_u = False
            elif event.key == pygame.K_DOWN:
                ship.moving_d = False

def check_down():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)

def update_screen(ai,screen,background,ship):
    '''刷新屏幕'''
    screen.blit(background,(0,0))
    ship.update()
    ship.blitme()    
    pygame.display.update()