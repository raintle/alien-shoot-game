import pygame
import sys

class Aliengame:

    def __init__(self):

        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))

    @staticmethod
    #静态装饰器
    def run_game():
        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            pygame.display.flip

if __name__ == '__main__':
    game = Aliengame()
    game.run_game()