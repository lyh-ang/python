import pygame
class Ship():
    def __init__(self, screen):
        """初始化飞船并设置其初始位置"""
        self.screen = screen
        #加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('ship.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # 将每艘新飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        #允许飞船不断移动
        self.moving_r = False
        self.moving_l = False
        self.moving_u = False
        self.moving_d = False

    def update(self):
        if self.moving_r and self.rect.right < self.screen_rect.right:
            self.rect.centerx += 1
        elif self.moving_l and self.rect.left > 0:
            self.rect.centerx -= 1
        elif self.moving_u and self.rect.top > 0:
            self.rect.bottom -= 1
        elif self.moving_d and self.rect.bottom < self.screen_rect.bottom:
            self.rect.bottom += 1     

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)