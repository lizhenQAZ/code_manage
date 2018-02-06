import pygame
from pygame.locals import *


def main():
    # 创建一个画布
    screen = pygame.display.set_mode((440, 560), 0, 32)

    # 创建一张图片用作背景
    background = pygame.image.load('./E7_Background.jpg')

    # 测试,用来创建一个玩家飞机的图片
    hero = pygame.image.load("./E7_Hero.jpg")

    # 用来保存飞机的x，y坐标
    x = 0
    y = 0

    while True:
        # 设置背景图位置
        screen.blit(background, (0, 0))

        # 设定需要显示的飞机图片
        screen.blit(hero, (x, y))

        for event in pygame.event.get():
            if event.type == QUIT:
                print('exit')
                exit()

            elif event.type == KEYDOWN:
                if event.key == K_a or event.key == K_LEFT:
                    print('left shift')
                    x -= 5

                elif event.key == K_d or event.key == K_RIGHT:
                    print('right shift')
                    x += 5

                elif event.key == K_SPACE:
                    print('space')

        pygame.display.update()


if __name__ == '__main__':
    main()