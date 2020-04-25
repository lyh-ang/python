import sys
import pygame
from ship import Ship as ship
def check_events():
    '''响应鼠标和键盘事件'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ship.moving_r = True            
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.moving_r = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                ship.moving_l = True            
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                ship.moving_l = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                ship.moving_u = True            
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                ship.moving_u = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                ship.moving_d = True            
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                ship.moving_d = False





def update_screen(ai,screen,background,ship):
    '''刷新屏幕'''
    screen.blit(background,(0,0))
    ship.blitme()    
    pygame.display.update()

