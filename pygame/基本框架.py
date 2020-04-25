import pygame,sys

pygame.init()
screen = pygame.display.set_mode((600,400))
pygame.display.set_caption('超级马里奥-by 你亲爱的航航')

color = (0,45,0)
while True:
    for event in pygame.event.get():
        screen.fill(color)
        if event == pygame.QUIT:
            pygame.QUIT()
            sys.exit(0)
        
        

#刷新屏幕
pygame.display.update()
