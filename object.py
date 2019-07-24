import pygame
class object(pygame.sprite.Sprite):
    def __init__(self, image, pos):
        super().__init__()
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (70, 70))
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.speed = pygame.math.Vector2(0, 0)
    def update(self):
        self.rect.move_ip(self.speed)
    def draw(self,w):
        w.blit(self.image, self.rect)