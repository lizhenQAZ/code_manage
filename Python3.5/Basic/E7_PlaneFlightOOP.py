import pygame
from pygame.locals import *
import time
import random


class HeroPlane(object):
    def __init__(self, screen):
        self.x = 150
        self.y = 400
        self.screen = screen
        self.image = pygame.image.load("./E7_Hero.jpg")
        self.bulletlist = list()

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))
        needdelitemlist = list()
        for i in self.bulletlist:
            if i.judge():
                needdelitemlist.append(i)
        for i in needdelitemlist:
            self.bulletlist.remove(i)
        for bullet in self.bulletlist:
            bullet.display()
            bullet.move()

    def move_left(self):
        self.x -= 10

    def move_right(self):
        self.x += 10

    def shebullet(self):
        newbullet = Bullet(self.x, self.y, self.screen)
        self.bulletlist.append(newbullet)


class Bullet(object):
    def __init__(self, x, y, screen):
        self.x = x + 20
        self.y = y - 20
        self.screen = screen
        self.image = pygame.image.load('./E7_Bullet.jpg')

    def move(self):
        self.y -= 5

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))

    def judge(self):
        if self.y < 0:
            return True
        else:
            return False


class EnemyPlane(object):
    def __init__(self, screen):
        self.x = 170
        self.y = 0
        self.screen = screen
        self.image = pygame.image.load("./E7_Enemy.jpg")
        self.direction = 'right'
        self.bulletlist = list()

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))
        needdelitemlist = list()
        for i in self.bulletlist:
            if i.judge():
                needdelitemlist.append(i)
        for i in needdelitemlist:
            self.bulletlist.remove(i)
        for bullet in self.bulletlist:
            bullet.display()
            bullet.move()

    def move(self):
        if self.direction == 'right':
            self.x += 4
        elif self.direction == 'left':
            self.x -= 4
        if self.x >= 440-100:
            self.direction = 'left'
        elif self.x <= 0:
            self.direction = 'right'

    def shebullet(self):
        num = random.randint(1,100)
        if num == 60:
            newbullet = EnemyBullet(self.x, self.y, self.screen)
            self.bulletlist.append(newbullet)


class EnemyBullet(object):
    def __init__(self, x, y, screen):
        self.x = x + 30
        self.y = y + 30
        self.screen = screen
        self.image = pygame.image.load('./E7_EnemyBullet.jpg')

    def move(self):
        self.y += 5

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))

    def judge(self):
        if self.y > 400-60:
            return True
        else:
            return False


def key_control(heroplane):
    for event in pygame.event.get():
        if event.type == QUIT:
            print('exit')
            exit()

        elif event.type == KEYDOWN:
            if event.key == K_a or event.key == K_LEFT:
                print('left shift')
                heroplane.move_left()

            elif event.key == K_d or event.key == K_RIGHT:
                print('right shift')
                heroplane.move_right()

            elif event.key == K_SPACE:
                print('space')
                heroplane.shebullet()


def main():
    # 创建一个画布
    screen = pygame.display.set_mode((440, 560), 0, 32)

    # 创建一张图片用作背景
    background = pygame.image.load('./E7_background.jpg')

    # 创建一个飞机对象
    heroplane = HeroPlane(screen)

    # 创建一个敌机对象
    enemyplane = EnemyPlane(screen)

    while True:
        # 设置背景图位置
        screen.blit(background, (0, 0))
        heroplane.display()
        enemyplane.move()
        enemyplane.display()
        enemyplane.shebullet()
        key_control(heroplane)
        pygame.display.update()
        time.sleep(0.01)


if __name__ == '__main__':
    main()