import pygame

class Ship:

    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.setting = ai_game.setting
        #引用其他实例上的Setting类

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
        self.move_right = False
        self.move_left = False
        #飞船移动标志
        self.x = float(self.rect.x)
        #将int类型rect.x转换为浮点数


    def blitme(self):
        """绘制飞船"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """飞船坐标更新"""
        if self.move_right:
            if self.rect.right < self.screen_rect.right:
                self.x += self.setting.ship_speed
        if self.move_left:
            if self.rect.left > self.screen_rect.left:
                self.x -= self.setting.ship_speed
        self.rect.x = self.x