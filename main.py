import sys
import pygame

from bullet import Bullet
from setting import Setting
from ship import Ship
from enemies import Enemy

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
        self.enemies = pygame.sprite.Group()
        #创建敌人编组
        self._create_enemies()
        self.bullets = pygame.sprite.Group()
        #创建子弹编组
        self.attack_count = 0
        self.a_c = self.attack_count
        #攻击计时器
        self.attack_speed = self.setting.attack_speed
        self.a_s = self.attack_speed
        #攻击速度
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
            #消除子弹

        self.enemies.draw(self.screen)
        #绘制敌人

        self._fire_bullet()
        pygame.display.flip()
        # 事件刷新
        self.clock.tick(self.setting.clock)

    def _fire_bullet(self):
        """子弹函数"""
        if self.a_c != self.a_s:
            self.a_c += 1
        elif self.bullet_permit and self.a_c == self.a_s:
                new_bullet = Bullet(self)
                # 赋予类
                self.bullets.add(new_bullet)
                # 添加子弹
                self.a_c = 0
        print(self.a_c)

    def _create_enemies(self):

        # 创建一个临时敌人对象（用于获取敌人宽度）
        enemy = Enemy(self)
        # 获取单个敌人的宽度（从敌人的矩形碰撞框中获取）
        enemy_width = enemy.rect.width
        # 计算窗口中可用于放置敌人的水平空间
        # 逻辑：总窗口宽度 - 左右各留1个敌人宽度的边距 = 可用水平空间
        available_space_x = self.setting.width - (2 * enemy_width)
        # 计算一行能容纳的敌人数量
        # 逻辑：可用空间 // 每个敌人占用的宽度（自身宽度 + 间距宽度，这里间距也是1个敌人宽度）
        number_enemies_x = available_space_x // (2 * enemy_width)

        # 循环生成对应数量的敌人
        for enemy_number in range(number_enemies_x):
            # 为每个位置创建一个新的敌人对象
            enemy = Enemy(self)
            # 计算当前敌人的水平坐标（核心定位逻辑）
            # 公式：左边距(1个enemy_width) + 2*enemy_width * 敌人序号
            enemy.x = enemy_width + 2 * enemy_width * enemy_number
            # 将计算好的x坐标赋值给敌人的碰撞框x轴位置（决定敌人在屏幕上的显示位置）
            enemy.rect.x = enemy.x
            # 将生成的敌人添加到敌人组（用于统一管理，比如批量绘制、检测碰撞）
            self.enemies.add(enemy)

if __name__ == '__main__':
    game = Aliengame()
    game.run_game()