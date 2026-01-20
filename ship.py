import pygame

class Ship:

    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        self.image_load = pygame.image.load('早露.png')
        #图片导入
        self.image_surf = pygame.transform.scale_by(self.image_load, 0.2)
        #图片缩放
        self.image = self.image_surf
        #赋值
        self.rect = self.image.get_rect()
        #获取图片中央坐标

        self.rect.midbottom = self.screen_rect.midbottom
        #初始化飞船坐标

    def blitme(self):
        """绘制飞船"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """飞船坐标更新"""
        pass