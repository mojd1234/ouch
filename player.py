import pygame
class player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__("cursor.png", pos)
    def update(self):
        super().update(self)