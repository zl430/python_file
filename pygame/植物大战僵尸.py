# -*- conding:utf-8 -*-
import pygame
import sys
import time
import random
pygame.mixer.init()
width = 1200
height = 600
class Peas():
    def __init__(self):
        self.image = pygame.image.load("img/wandou.gif")
        self.image_rect = self.image.get_rect()
        self.image_rect.top = 280
        self.is_move_up = False
        self.is_move_down = False
        self.is_shout = False
    def display(self):
        screen.blit(self.image, self.image_rect)
    def move_up(self):
        if self.image_rect.top > 20:
            self.image_rect.move_ip(0, -10)
        for z in Zombie.zombie_list:
            if self.image_rect.colliderect(z.image_rect):
                exit()
    def move_down(self):
        if self.image_rect.bottom < 600:
            self.image_rect.move_ip(0, +10)
        for z in Zombie.zombie_list:
            if self.image_rect.colliderect(z.image_rect):
                exit()
    def shout_bullet(self):
        #创建炮弹对象
        bullet = Bullet(self)
        #保存创建好的对象
        Bullet.bullet_list.append(bullet)
class Bullet():
    bullet_list = []
    #炮弹创建间隔时间
    interval = 0
    def __init__(self, pea):
        self.image = pygame.image.load("img/zd.gif")
        self.image_rect = self.image.get_rect()
        self.image_rect.top = pea.image_rect.top
        self.image_rect.left = pea.image_rect.right
    def display(self):
        screen.blit(self.image, self.image_rect)
    def move(self):
        #移动X轴像素
        self.image_rect.move_ip(10, 0)
        #炮弹超出边界则清除
        if self.image_rect.left > width - 10:
            Bullet.bullet_list.remove(self)
        for z in Zombie.zombie_list:
            #colliderect  碰撞
            if self.image_rect.colliderect(z.image_rect):
                Bullet.bullet_list.remove(self)
                Zombie.zombie_list.remove(z)
                break
class Zombie():
    interval = 0
    zombie_list = []
    def __init__(self):
        self.image = pygame.image.load("img/js.gif")
        #改变图片大小
        self.image = pygame.transform.scale(self.image, (80, 80))
        self.image_rect = self.image.get_rect()
        self.image_rect.top = random.randint(10, height-80)
        self.image_rect.left = width
    def display(self):
        screen.blit(self.image, self.image_rect)
    def move(self):
        self.image_rect.move_ip(-5, 0)
        if self.image_rect.right <= 0:
            zombie.zombie_list.remove(self)
        for b in Bullet.bullet_list:
            if self.image_rect.colliderect(b.image_rect):
                Bullet.bullet_list.remove(b)
                Zombie.zombie_list.remove(self)
                break
        if self.image_rect.colliderect(peas.image_rect):
            exit()
def key_control():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                peas.is_move_down = True
            elif event.key == pygame.K_UP:
                peas.is_move_up = True
            elif event.key == pygame.K_SPACE:
                peas.is_shout = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                peas.is_move_down = False
            elif event.key == pygame.K_UP:
                peas.is_move_up = False
            elif event.key == pygame.K_SPACE:
                peas.is_shout = False
screen = pygame.display.set_mode((width, height), 0, 32)
pygame.mixer.music.load("mp3/bj.mp3")
#------------背景-----------------
background = pygame.image.load("img/beijing.png")
background = pygame.transform.scale(background, (width, height))
background_rect = background.get_rect()
#-----------优化运行速度--------------
clock = pygame.time.Clock()
peas = Peas()
while True:
    #------------------背景颜色--------------
    screen.fill((0, 0, 0))
    #-------------------背景音乐--------------
    if pygame.mixer.music.get_busy()==False:
        pygame.mixer.music.play()
    #-------------------显示图片-------------
    screen.blit(background, background_rect)
    peas.display()
    key_control()
    if peas.is_move_up:
        peas.move_up()
    if peas.is_move_down:
        peas.move_down()
    #发射炮弹
    Bullet.interval += 1
    if peas.is_shout and Bullet.interval >= 10:
        Bullet.interval = 0
        peas.shout_bullet()
    Zombie.interval += 1
    if Zombie.interval >= 50:
        Zombie.interval = 0
        #创建僵尸对象，并且保存起来
        zombie = Zombie()
        Zombie.zombie_list.append(zombie)
    #显示所有的炮弹
    for bullet in Bullet.bullet_list:
        #炮弹显示
        bullet.display()
        #炮弹移动
        bullet.move()
    for zombie in Zombie.zombie_list:
        zombie.display()
        #僵尸移动
        zombie.move()
    clock.tick(30)
    pygame.display.update()
    time.sleep(0.01)






# pygame.mixer.music.load("background.mp3")
# while True:
#     if pygame.mixer.music.get_busy()==False:
#         pygame.mixer.music.play()