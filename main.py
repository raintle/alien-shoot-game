import sys
import pygame
from setting import Setting
from ship import Ship

class Aliengame:

    def __init__(self):

        pygame.init()
        self.setting = Setting()
        #初始化pygame
        self.screen = pygame.display.set_mode((self.setting.width, self.setting.height))
        #分辨率设置
        self.ship = Ship(self)



    def run_game(self):
        while True:
            self._check_events()
            self._update_screen()

    @staticmethod
    def _check_events():

        for event in pygame.event.get():
            # 监视键盘事件
            if event.type == pygame.QUIT:
                sys.exit()

    def _update_screen(self):
        self.screen.fill(self.setting.bg_color)
        # 屏幕颜色
        self.ship.blitme()
        # 绘制飞船
        pygame.display.flip()
        # 事件刷新

if __name__ == '__main__':
    game = Aliengame()
    game.run_game()