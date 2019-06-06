import pygame

# 定义一个屏幕大小的常量
SCREEN_RECT = pygame.Rect(0, 0, 480, 700)
# 定义刷新帧率
FRAME_PER_SEC = 60


class GameSprite(pygame.sprite.Sprite):
    def __init__(self, image_name, speed=5, x=0, y=0):

        # 一定要调用父类的初始化方法
        super().__init__()

        # 定义对象属性
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = speed
        self.rect.x = x
        self.rect.y = y

    def update(self):

        # 在屏幕垂直方向移动
        self.rect.y += self.speed


# 派生了一个字类，继承GameSprites
class Background(GameSprite):

    def __init__(self, is_alt=False):

        # 1. 调用父类方法实现
        super().__init__("./images/background.png")

        # 2. 判断是否是交替图像，如果是，就要设置初始位置
        if is_alt is True:
            # 交替图像
            self.rect.y = -self.rect.height
    # 游戏背景精灵
    # 重写了update方法
    def update(self):

        # 1.调用父类方法实现
        super().update()
        # 2.判断图像是否益处屏幕，如果是，将图片设置到屏幕上方
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -self.rect.height
