import pygame
import random
from object import Object
class Enemy(Object):
    def __init__(self, pos):
        super().__init__("cursor.png", pos)
        self.image = pygame.transform.scale(self.image, (70, 90))
        self.accel = pygame.math.Vector2(0, 0)
        self.accelspeed = 0.1

    def update(self):
        screeninfo = pygame.display.Info()
        screenwidth = screeninfo.current_w
        screenheight = screeninfo.current_h
        if (self.accel.length_squared() > 10):
            self.speed = 10
        self.accel.y = self.accelspeed
        self.accel.x = self.accelspeed
        self.speed += self.accel
        if (self.accel.length_squared() == 0):
            self.speed *= 0.9
        if (self.accel.length_squared() > 150):
            self.speed = 150
        if self.rect.right > screenwidth:
            self.speed.x *= -1
            self.accelspeed *= -1
        if self.rect.left < 0:
            self.speed.x *= -1
            self.accelspeed *= -1
        if self.rect.bottom > screenheight:
            self.speed.y *= -1
            self.accelspeed *= -1
        if self.rect.top < 0:
            self.speed.y *= -1
            self.accelspeed *= -1
        super().update()
