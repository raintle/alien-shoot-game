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
        self._create_fleet()
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

    def _create_fleet(self):
        # 第一步：创建临时敌人对象，仅用于获取敌人的宽高尺寸（所有敌人尺寸一致）
        enemy = Enemy(self)
        # 第二步：一次性获取敌人的宽度和高度（rect.size返回元组：(宽度, 高度)）
        enemy_width, enemy_height = enemy.rect.size

        # 第三步：计算水平方向可放置敌人的空间
        # 逻辑：总窗口宽度 - 左右各留1个敌人宽度的边距 = 水平可用空间
        available_space_x = self.setting.width - (2 * enemy_width)
        # 第四步：计算一行能容纳的敌人数量
        # 逻辑：可用空间 // 每个敌人占用的水平空间（自身宽度 + 1个敌人宽度的间距）
        number_enemies_x = available_space_x // (2 * enemy_width)

        # 第五步：获取玩家飞船的高度（用于预留底部空间）
        ship_height = self.ship.rect.height

        # 第六步：计算垂直方向可放置敌人的空间
        # 逻辑：总窗口高度 - 顶部留1个敌人高度边距 - 底部留飞船高度+2个敌人高度的空间 - 其他边距
        # （3*enemy_height = 顶部1个 + 底部2个，避免敌人贴飞船）
        available_space_y = (self.setting.height - (3 * enemy_height) - ship_height)
        # 第七步：计算能容纳的敌人行数
        # 逻辑：垂直可用空间 // 每行敌人占用的垂直空间（自身高度 + 1个敌人高度的间距）
        number_rows = available_space_y // (2 * enemy_height)

        # 第八步：把计算好的“每行敌人数量”和“总行数”保存为实例变量
        # 供另一个函数_create_enemies调用
        self.number_rows = number_rows
        self.number_enemies_x = number_enemies_x

    def _create_enemies(self):
        # 第一步：外层循环——遍历每一行（控制敌人的垂直位置）
        for row in range(self.number_rows):
            # 第二步：内层循环——遍历当前行的每个敌人（控制敌人的水平位置）
            for enemy_number in range(self.number_enemies_x):
                # 第三步：为当前位置创建一个新的敌人对象（真正要显示的敌人）
                enemy = Enemy(self)
                # 第四步：重新获取敌人宽高（避免临时对象的尺寸失效，更健壮）
                enemy_width, enemy_height = enemy.rect.size

                # 第五步：计算当前敌人的水平坐标（x轴）
                # 公式：左边距(1*enemy_width) + 2*enemy_width * 敌人在本行的序号
                # 保证每个敌人水平间距为1个敌人宽度
                enemy.x = enemy_width + 2 * enemy_width * enemy_number
                # 第六步：将计算的x坐标同步到敌人的碰撞框（决定屏幕显示位置）
                enemy.rect.x = enemy.x

                # 第七步：计算当前敌人的垂直坐标（y轴）
                # 公式：顶部边距(1*enemy_height) + 2*enemy_height * 行号
                # 保证每行敌人垂直间距为1个敌人高度
                enemy.rect.y = enemy_height + 2 * enemy_height * row

                # 第八步：将当前敌人添加到敌人组（用于批量管理：绘制、碰撞检测、移动等）
                self.enemies.add(enemy)


if __name__ == '__main__':
    game = Aliengame()
    game.run_game()