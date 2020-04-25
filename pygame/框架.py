import pygame,sys
class Setting:
    '''存储项目的设置'''
    def __init__(self):
        self.screen_w = 600
        self.screen_h = 400
        self.color = (230,230,230)
        self.title = 'pygame游戏之路—最美框架'
        self.fps = 300
        self.fclock = pygame.time.Clock()
        self.icon = pygame.image.load('游戏图标.ico')

#游戏初始化
pygame.init()
ai = Setting()
pygame.display.set_mode((int(ai.screen_w),int(ai.screen_h)))
pygame.display.set_caption(ai.title)
pygame.display.set_icon(ai.icon)
fps = ai.fps

#游戏主程序
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)



#屏幕刷新
pygame.fill(color) 
pygame.display.update()
fclock.tick(fps)
