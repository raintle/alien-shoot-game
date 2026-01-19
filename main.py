import sys
import pygame
from setting import Setting

class Aliengame:

    def __init__(self):

        pygame.init()
        self.setting = Setting()
        #初始化pygame
        self.screen = pygame.display.set_mode((self.setting.width, self.setting.height))
        #分辨率设置
        #屏幕颜色设置

    def run_game(self):
        while True:
            for event in pygame.event.get():
                #监视键盘事件
                if event.type == pygame.QUIT:
                    sys.exit()
            self.screen.fill(self.setting.bg_color)
            #屏幕颜色
            pygame.display.flip()
            #事件刷新

if __name__ == '__main__':
    game = Aliengame()
    game.run_game()