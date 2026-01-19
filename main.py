import sys
import pygame

class Aliengame:

    def __init__(self):

        pygame.init()
        #初始化pygame
        self.screen = pygame.display.set_mode((800, 600))
        #分辨率设置
        self.bg_color = (230, 230, 230)
        #屏幕颜色设置

    def run_game(self):
        while True:
            for event in pygame.event.get():
                #监视键盘事件
                if event.type == pygame.QUIT:
                    sys.exit()
            self.screen.fill(self.bg_color)
            #屏幕颜色
            pygame.display.flip()
            #事件刷新

if __name__ == '__main__':
    game = Aliengame()
    game.run_game()