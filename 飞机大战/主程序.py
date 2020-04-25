import pygame,sys
from setting import Setting
from ship import Ship
import game_functions as gf

def run_game():
    pygame.init()
    pygame.mixer.init()
    ai = Setting()
    screen = pygame.display.set_mode((int(ai.screen_w),int(ai.screen_h)))
    pygame.display.set_caption(ai.title)
    pygame.display.set_icon(ai.icon)
    background = ai.background
    backmusic = ai.backmusic
    pygame.mixer.music.play()
    ship = Ship(screen)
 
    while True:
        gf.check_down()        
        gf.check_keydown()
        gf.check_keyup()
        # ship.update()        
        gf.update_screen(ai,screen,background,ship)
       
run_game()
