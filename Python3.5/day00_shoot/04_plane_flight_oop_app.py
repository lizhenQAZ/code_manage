import pygame
from pygame.locals import *
import time
import random


class Plane(object):
    def __init__(self, screen, image):
        self.screen = screen
        self.image = pygame.image.load(image)
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


class HeroPlane(Plane):
    def __init__(self, screen):
        super(HeroPlane, self).__init__(screen, "./hero.jpg")
        self.x = 150
        self.y = 400

    def move_left(self):
        self.x -= 10

    def move_right(self):
        self.x += 10

    def shebullet(self):
        newbullet = Bullet(self.x, self.y, self.screen, 'hero')
        self.bulletlist.append(newbullet)


class EnemyPlane(Plane):
    def __init__(self, screen):
        super(EnemyPlane, self).__init__(screen, "./enemy.jpg")
        self.x = 170
        self.y = 0
        self.direction = 'right'

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
            newbullet = Bullet(self.x, self.y, self.screen, 'enemy')
            self.bulletlist.append(newbullet)


class Bullet(object):
    def __init__(self, x, y, screen, planename):
        self.screen = screen
        self.planename = planename
        if self.planename == 'hero':
            self.x = x + 20
            self.y = y - 20
            self.image = pygame.image.load('./bullet.jpg')

        elif self.planename == 'enemy':
            self.x = x + 30
            self.y = y + 30
            self.image = pygame.image.load('./enemybullet.jpg')

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))

    def move(self):
        if self.planename == 'hero':
            self.y -= 5
        elif self.planename == 'enemy':
            self.y += 5

    def judge(self):
        if self.y < 0 or self.y > 400-60:
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
    background = pygame.image.load('./background.jpg')

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