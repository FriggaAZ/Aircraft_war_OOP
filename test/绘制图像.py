import pygame
from plane_sprites import *

# 游戏的初始化
pygame.init()

screen = pygame.display.set_mode((480, 700))

# 绘制背景图像
# 1> 加载图像数据

bg = pygame.image.load("./images/background.png")
hero = pygame.image.load("./images/me1.png")
# 2> blit绘制图像
screen.blit(bg, (0, 0))
screen.blit(hero, (150, 300))
# 3> update 更新屏幕现实
# pygame.display.update()

pygame.time.Clock()

# 定义rect记录飞机的初始位置
hero_rect = pygame.Rect(200, 300, 102, 126)

# 创建敌人的精灵
enemy = GameSprite("./images/enemy1.png")
enemy1 = GameSprite("./images/enemy2.png", 2, 160, 50)
# 创建敌人的精灵组
enemy_group = pygame.sprite.Group(enemy, enemy1)



# 创建时钟对象
clock = pygame.time.Clock()

# 游戏循环 -> 意味着游戏正式开始
while True:
    clock.tick(60)

    # 捕获事件
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            print("退出游戏")
            pygame.quit()
            exit()

    hero_rect.y -= 5
    if hero_rect.y <= 0-hero_rect.height:
        hero_rect.y = 700

    # 调用blit方法绘制图像
    screen.blit(bg, (0, 0))
    screen.blit(hero, hero_rect)

    # 让精灵组调用两个方法

    # update
    enemy_group.update()
    # draw
    enemy_group.draw(screen)
    # update更新显示
    pygame.display.update()

pygame.quit()
