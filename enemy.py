import pygame
from object import Object
class Enemy(Object):
    def __init__(self, pos):
        super().__init__("cursor.png", pos)
        self.image = pygame.transform.scale(self.image, (70, 70))
        self.accel = pygame.math.Vector2(0, 0)
    def update(self):
        super().update()