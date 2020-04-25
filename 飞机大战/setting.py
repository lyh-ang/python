import pygame,sys
from pygame.sprite import*
class Setting:
    '''存储项目基本设置'''
    def __init__(self):
        self.screen_w = 600
        self.screen_h = 400
        self.color = (230,230,230)
        self.title = '飞机大战  --by 航航'
        self.fps = 300
        self.fclock = pygame.time.Clock()
        self.icon = pygame.image.load('游戏图标.ico')
        self.background = pygame.image.load('background.jpg')
        self.backmusic = pygame.mixer.music.load('backmusic.mp3')
        self.bullet_speed = 0.8
        self.bullet_color = 60,60,60
        self.bullet_width = 3
        self.bullet_height = 15
        
        

