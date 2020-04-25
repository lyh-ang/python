import pygame,sys
from pygame.sprite import Group
from pygame.sprite import Sprite
class Setting:
    '''存储项目的设置'''
    def __init__(self):
        self.screen_w = 600
        self.screen_h = 400
        self.color = (230,230,230)
        self.title = '飞机大战--by 航航'
        self.fps = 300
        self.fclock = pygame.time.Clock()
        self.icon = pygame.image.load('游戏图标.ico')
        self.background = pygame.image.load('background.jpg')
        self.backmusic = pygame.mixer.music.load('backmusic.mp3')
        self.bullet_speed = 0.8
        self.bullet_color = 60,60,60
        self.bullet_width = 3
        self.bullet_height = 15


class Ship():
    '''创造飞船的类'''
    def __init__(self,screen):
        self.screen = screen
        self.image = pygame.image.load('ship.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        #初始化方向控制模块
        self.moving_r = False
        self.moving_l = False
        self.moving_u = False
        self.moving_d = False  
   
    def update(self):
        if self.moving_r and self.rect.right < self.screen_rect.right:
            self.rect.centerx += 1
        if self.moving_l and self.rect.left > 0:
            self.rect.centerx -= 1
        if self.moving_u and self.rect.top > 0:
            self.rect.bottom -= 1
        if self.moving_d and self.rect.bottom < self.screen_rect.bottom:
            self.rect.bottom += 1    
  
    def biltf(self):
        self.screen.blit(self.image,self.rect)    
        
class Bullet():
    '''子弹的设置'''
    def __init__(self,ai,screen,ship):
        super().__init__
        self.screen = screen    
        self.rect = pygame.Rect(0,0,ai.screen_w,ai.screen_h)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        self.y = float(self.rect.y)
        self.color = ai.bullet_color
        self.speed = ai.bullet_speed
    def update(self):
        self.y -= self.speed
        self.rect.y = self.y
    def draw_bullet(self):
        pygame.draw.rect(self.screen,self.rect,self.color)
    def check_keydown_bullet(event,ai,screen,ship,bullet):
        '''相应子弹并加入编组'''
        new_bullet = Bullet(ai, screen, ship)
        bullets.add(new_bullet)    
        
    def check_events(ai,screen,ship,bullet):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                check_keydown_bullet(event,ai,screen,ship,bullets)
    def update_bullet(self):     
        for bullet in bullets.sprites():
            bullet.draw_bullet

#游戏初始化            
pygame.init()
pygame.mixer.init()
ai = Setting()
screen = pygame.display.set_mode((int(ai.screen_w),int(ai.screen_h)))
pygame.display.set_caption(ai.title)
pygame.display.set_icon(ai.icon)
fps = ai.fps
ship = Ship(screen)
background = ai.background
backmusic = ai.backmusic
pygame.mixer.music.play()
bullets = Group()
zd  = Bullet(ai,screen,ship)
#游戏主程序
while True:
    screen.blit(background,(0,0))
    ship.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        #方向控制模块
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
        
        

        

    
    #将飞船放在屏幕底部中间
    ship.biltf()      
    #屏幕刷新
    # pygame.fill(ai.color)
    pygame.display.update()
    # fclock.tick(fps)

