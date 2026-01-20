import sys
import pygame

from bullet import Bullet
from setting import Setting
from ship import Ship

class Aliengame:

    def __init__(self):

        pygame.init()
        self.setting = Setting()
        #初始化pygame
        if self.setting.width != 0 or self.setting.height != 0:
            self.screen = pygame.display.set_mode((self.setting.width, self.setting.height))
        else:
            self.screen = pygame.display.set_mode((self.setting.width, self.setting.height), pygame.FULLSCREEN)
        self.setting.screen_width = self.screen.get_rect().width
        self.setting.screen_height = self.screen.get_rect().height
        #分辨率设置
        self.ship = Ship(self)
        #存储Ship（）类
        self.bullets = pygame.sprite.Group()
        #创建子弹编组
        self.aaa = 0
        self.bullet_permit = False
        self.clock = pygame.time.Clock()
        #帧率限制，机子不稳定造成的游戏不稳定




    def run_game(self):
        """游戏主程序运行"""
        while True:
            self._check_events()
            self._update_screen()

    def _check_events(self):
        """事件响应"""
        for event in pygame.event.get():
            # 监视键盘事件
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                #响应按下事件
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                #响应抬起事件
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """按下事件判断"""
        if event.key == pygame.K_LEFT:
            self.ship.move_left = True
        if event.key == pygame.K_RIGHT:
            self.ship.move_right = True
        if event.key == pygame.K_SPACE:
            self.bullet_permit = True
            #绘制子弹
        if event.key == pygame.K_q:
            #按q时推出系统
            sys.exit()

    def _check_keyup_events(self, event):
        """抬起事件判断"""
        if event.key == pygame.K_LEFT:
            self.ship.move_left = False
        if event.key == pygame.K_RIGHT:
            self.ship.move_right = False
        if event.key == pygame.K_SPACE:
            self.bullet_permit = False
                # 绘制子弹


    def _update_screen(self):
        """屏幕绘制"""
        self.screen.fill(self.setting.bg_color)
        # 屏幕颜色
        self.ship.blitme()
        self.ship.update()
        # 绘制飞船
        self.bullets.update()
        #绘制子弹
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        self._fire_bullet()
        pygame.display.flip()
        # 事件刷新
        self.clock.tick(self.setting.clock)

    def _fire_bullet(self):
        """子弹函数"""
        if  self.bullet_permit:
            self.aaa += 1
            if self.aaa % 10 == 0:
                new_bullet = Bullet(self)
                # 赋予类
                self.bullets.add(new_bullet)
                # 添加子弹
                self.aaa = 0
        else:
            if self.aaa != -1:
                self.aaa -= 1
        print(self.aaa)


if __name__ == '__main__':
    game = Aliengame()
    game.run_game()