import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """子弹的相关设置"""
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        #继承实例信息
        self.setting = ai_game.setting
        #继承实例信息
        self.color =self.setting.bullet_color
        #获得子弹颜色

        self.rect = pygame.Rect(0, 0, self.setting.bullet_width, self.setting.bullet_height)
        #初始子弹位置及生成子弹大小
        self.rect.midtop = ai_game.ship.rect.midtop
        #位移子弹至飞船顶部

        self.y = float(self.rect.y)
        #浮点数化rect.y

    def update(self):
        """更新子弹位置"""
        self.y -= self.setting.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self):
        """绘制子弹"""
        pygame.draw.rect(self.screen, self.color, self.rect)
