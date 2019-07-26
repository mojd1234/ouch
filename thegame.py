import pygame
import random
from player import Player
from enemy import Enemy
pygame.init()
screeninfo = pygame.display.Info()
screenwidth = screeninfo.current_w
screenheight = screeninfo.current_h
w = pygame.display.set_mode([int(screenwidth), int(screenheight)])
c = pygame.time.Clock()
cookie = Player((150,150))
enemies = pygame.sprite.Group()
font = pygame.font.SysFont(None, 40)
def init():
    cookie = Player((150, 150))
    cookie.speed = 0
    cookie.accel = 0
    enemies.empty()
    for i in range(10):
        enemies.add(Enemy((random.randint(50, screenwidth - 50), random.randint(50, screenheight - 50))))

def main():
    init()
    dead = False
    yes = True
    accelspeed = 0.3
    score = 0
    while yes:
        print(cookie.accel.x)
        print(cookie.accel.y)
        score += 1/60
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
                    cookie.accel.y -= accelspeed
                if event.key == pygame.K_s:
                    cookie.accel.y += accelspeed
                if event.key == pygame.K_a:
                    cookie.accel.x -= accelspeed
                if event.key == pygame.K_d:
                    cookie.accel.x += accelspeed

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    cookie.accel.y += accelspeed
                if event.key == pygame.K_s:
                    cookie.accel.y -= accelspeed
                if event.key == pygame.K_a:
                    cookie.accel.x += accelspeed
                if event.key == pygame.K_d:
                    cookie.accel.x -= accelspeed
        if not dead:
            cookie.update()
        enemies.update()
        player_hit = pygame.sprite.spritecollide(cookie, enemies, False)
        if player_hit:
            init()
            cookie.reset((150,150))
            dead = True
        w.fill((43,251,255))
        if not dead:
            cookie.draw(w)
        enemies.draw(w)
        text = font.render("Time not dead: " + str(int(score)) + " seconds", True, (255,255,255))
        text_rect = text.get_rect()
        text_rect.center = (200, 45)
        w.blit(text,text_rect)
        pygame.display.flip()
        if dead:
            dead = False
            pygame.time.delay(1000)
            score = 0
        cookie.draw(w)
        enemies.draw(w)
        pygame.display.flip()
if __name__ == "__main__":
    main()