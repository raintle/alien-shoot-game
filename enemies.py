import pygame
from pygame.sprite import Sprite

class Enemy(Sprite):

    def __init__(self, ai_game):

        super().__init__()
        self.screen = ai_game.screen

        self.image_load = pygame.image.load('源石虫.png')
        #图片导入
        self.image_surf = pygame.transform.scale_by(self.image_load, 0.1)
        #图片缩放
        self.image = self.image_surf
        #赋值
        self.rect = self.image.get_rect()
        #获取图片中央坐标

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

