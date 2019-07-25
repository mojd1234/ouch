import pygame
import random
from player import Player
from enemy import Enemy
pygame.init()
screeninfo = pygame.display.Info()
screenwidth = screeninfo.current_w
screenheight = screeninfo.current_h
w = pygame.display.set_mode([int(screenwidth), int(screenheight)])
cookie = Player((150,150))
enemies = pygame.sprite.Group()
enemies.empty()
for i in range(10):
    enemies.add(Enemy((random.randint(50, screenwidth - 50), random.randint(50, screenheight - 50))))
c = pygame.time.Clock()
def main():
    yes = True
    while yes:
        c.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                yes = False
            if event.type == pygame.KEYDOWN:
                # or event.key == pygame.K_UP
                # or event.key == pygame.K_DOWN
                # or event.key == pygame.K_LEFT
                # or event.key == pygame.K_RIGHT
                if event.key == pygame.K_w:
                    cookie.accel.y -= 0.2
                if event.key == pygame.K_s:
                    cookie.accel.y += 0.2
                if event.key == pygame.K_a:
                    cookie.accel.x -= 0.2
                if event.key == pygame.K_d:
                    cookie.accel.x += 0.2
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    cookie.accel.y += 0.2
                if event.key == pygame.K_s:
                    cookie.accel.y -= 0.2
                if event.key == pygame.K_a:
                    cookie.accel.x += 0.2
                if event.key == pygame.K_d:
                    cookie.accel.x -= 0.2

        cookie.update()
        enemies.update()
        w.fill((43,251,255))
        cookie.draw(w)
        enemies.draw(w)
        pygame.display.flip()
if __name__ == "__main__":
    main()
