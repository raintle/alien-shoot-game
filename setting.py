import pygame

class Setting:

    def __init__(self):
        self.width = 800
        self.height = 600
        self.bg_color = (230, 230, 230)
        self.ship_speed = 2.5
        self.clock = 60

        self.bullet_speed = 5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.attack_speed = 10