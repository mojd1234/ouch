import pygame
from object import Object
class Player(Object):
    def __init__(self, pos):
        super().__init__("cookie.png", pos)
        self.image = pygame.transform.scale(self.image, (70, 70))
        self.accel = pygame.math.Vector2(0,0)
    def update(self):
        screeninfo = pygame.display.Info()
        screenwidth = screeninfo.current_w
        screenheight = screeninfo.current_h
        self.speed += self.accel
        if (self.accel.length_squared() == 0):
            self.speed *= 0.85
        if (self.accel.length_squared() > 150):
            self.speed = 150
        if self.rect.right > screenwidth:
            self.speed.x *= -1
        if self.rect.left < 0:
            self.speed.x *= -1
        if self.rect.bottom > screenheight:
            self.speed.y *= -1
        if self.rect.top < 0:
            self.speed.y *= -1
        super().update()
    def reset(self, pos):
        self.rect.center = pos