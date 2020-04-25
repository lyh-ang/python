import pygame,sys

pygame.init()
Vinfo = pygame.display.Info()
# size = width,height =Vinfo.current_w,Vinfo.current_h
size = width,height = 600,400
speed = [1,1]
# color = 0,255,0
screen = pygame.display.set_mode(size)
pygame.display.set_caption('pygame壁球')
background = pygame.image.load('timg.jpg').convert()
icon = pygame.image.load('002.gif')
pygame.display.set_icon(icon)
ball = pygame.image.load('002.gif')
ballrect = ball.get_rect()
fps = 300
#刷新初始化
flock = pygame.time.Clock()
bgcolor = pygame.Color('BLACK')
still = False

def change(a):
  return 0 if a<0 else (255 if a>255 else int(a))
    
while True:
  #监听用户事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.QUIT
            sys.exit(0)
        elif event.type == pygame.KEYDOWN:
          if event.key == pygame.K_UP:
            speed[1] = speed[1]+1 if speed[0]>0 else speed[1] - 1
          if event.key == pygame.K_DOWN:
            speed[1] = speed[1] if speed[1] == 0 else (abs(speed[1]) - 1)*int(speed[1]/abs(speed[1]))
          if event.key == pygame.K_LEFT:
            speed[0] = speed[0] if speed[0] == 0 else (abs(speed[0]) - 1)*int(speed[0]/abs(speed[0]))
          if event.key == pygame.K_RIGHT:
            speed[0] = speed[0]+1 if speed[0]>0 else speed[0] - 1
          if event.key == pygame.K_ESCAPE:
            sys.exit()
        elif event.type == pygame.VIDEORESIZE:
          size = width,height = event.size[0],event.size[1]
          pygame.display.set_mode(size,pygame.RESIZABLE)
        elif event.type == pygame.MOUSEBUTTONDOWN:
          if event.button == 1:
            still = True
        elif event.type == pygame.MOUSEBUTTONUP:
          still = False
          if event.button == 1:
            ballrect = ballrect.move(event.pos[0]-ballrect.left,event.pos[1]-ballrect.top)
        elif event.type == pygame.MOUSEMOTION:
          if event.buttons[0] == 1:
            ballrect = ballrect.move(event.pos[0]-ballrect.left,event.pos[1]-ballrect.top)
        if pygame.display.get_active() and not still:
          ballrect = ballrect.move(speed[0],speed[1])
        if ballrect.right > width and ballrect.left < 0:
          speed[0] = - speed[0]
          if ballrect.right + speed[0] >width and ballrect.right >width:
            speed[0] = -speed[0]
        if ballrect.bottom > width and ballrect.top < 0:
          speed[0] = - speed[0]
          if ballrect.bottom + speed[0] >width and ballrect.top >width:
            speed[0] = -speed[0]

                            
#基本逻辑
    if pygame.display.get_active():
      ballrect = ballrect.move(speed[0],speed[1])
    if ballrect.left<0 or ballrect.right>width:
      speed[0] = - speed[0]
    if ballrect.top<0 or ballrect.bottom>height: 
      speed[1] = -speed[1]
    #设置背景随壁球的运动而改变
    bgcolor.r = change(ballrect.left*255/width)
    bgcolor.g = change(ballrect.top*255/height)
    bgcolor.b = change(min(speed[0],speed[1])*255/max(speed[0],speed[1],1))

    screen.fill(bgcolor)
    screen.blit(ball,ballrect)
    pygame.display.update()
    flock.tick(fps)