import pygame
from pygame import Surface, Rect
from pygame.sprite import Sprite, Group
import random
import math
class Background(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.back_purple_phon = pygame.image.load("Background/purple.png")
        self.star1 = pygame.image.load("Background/star1.png")
        self.star2 = pygame.image.load("Background/star2.png")
        self.star3 = pygame.image.load("Background/star3.png")

        self.planet_red = pygame.image.load("Background/planet_red.png")
        self.planet_green = pygame.image.load("Background/planet_green.png")
        self.planet_purple_light = pygame.image.load("Background/planet_purple_light.png")
        self.planet_purple_dark = pygame.image.load("Background/planet_purple_dark.png")
        self.planet_orange = pygame.image.load("Background/palnet_orange.png")

        self.sb = pygame.image.load("Background/хзхзхзхзхзхзхзхзхзхз.png")

        self.planet_green_dark = pygame.image.load("Background/planet_green_dark.png")
        self.planet_top = pygame.image.load("Background/planet_top.png")
        self.baza = pygame.image.load("images/baza.png")
        self.cannon_green = pygame.image.load("images/new_green.png")
        self.cannon_blue = pygame.image.load("images/new_blue.png")
        self.cannon_red = pygame.image.load("images/new_red.png")

    def draw(self, screen):
        screen.blit(self.back_purple_phon, (0, 0))
        screen.blit(self.star1, (0, 0))
        screen.blit(self.star2, (0, 0))
        screen.blit(self.star3, (0, 0))
        screen.blit(self.planet_red, (50, 80))
        screen.blit(self.planet_green, (680, 100))
        screen.blit(self.planet_purple_light, (1040, 50))
        screen.blit(self.planet_purple_dark, (400, 200))
        screen.blit(self.planet_orange, (500, 760))
        screen.blit(self.sb, (0, 0))
        screen.blit(self.planet_green_dark, (30, 550))
        screen.blit(self.planet_top, (740, 520))
        screen.blit(self.baza, (0, 956))
        screen.blit(self.cannon_green, (50, 810))
        screen.blit(self.cannon_blue, (490, 810))
        screen.blit(self.cannon_red, (1074, 815))

class Block(pygame.sprite.Sprite):

    RED = pygame.image.load("images/cannon_red_new.png")
    BLUE = pygame.image.load("images/blue_new.png")
    GREEN = pygame.image.load("images/green_new.png")

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.colors = {"red": self.RED,
                      "blue": self.BLUE,
                      "green": self.GREEN}

        self.rect = Rect(x, y, 136, 136)
        self.color = 0
        self.cc = 0
        self.yvel = 136
        self.frame = 0
    def draw(self, screen):
        screen.blit(self.colors[self.cc], (self.rect.x, self.rect.y))

    def update(self):
        if self.frame % 60 == 0:
            self.rect.y += self.yvel
        self.frame += 1


# class Bullet(pygame.sprite.Sprite):
#     def __init__(self):
#         pygame.sprite.Sprite.__init__(self)
#         self.coordinates_for_color = {
#             "red": (1120, 840),
#             "green": (75, 800),
#             "blue": (630, 770),
#         }
#         self.image = {
#             "bullet_create_green": pygame.image.load("images/bullet.png"),
#             "bullet_create_blue": pygame.image.load("images/bullet_blue.png"),
#             "bullet_create_red": pygame.image.load("images/red_bullet.png")
#         }
#         self.color = "green"
#         self.state = "green"
#         self.rect = Rect(self.coordinates_for_color[self.state][0], self.coordinates_for_color[self.state][1], 136, 136)
#         self.frame = 0
#     def draw(self, screen):
#         screen.blit(self.image["bullet_create_green"], (500, 500)) #self.coordinates_for_color[self.state])
#
#     def update(self):
#         self.rect.y -= 5

class Bullet(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.coordinates_for_color = {"red": (1120, 840),
                                      "green": (75, 800),
                                      "blue": (630, 770)}
        self.images = {
            "bullet_create_green": pygame.image.load("images/bullet.png"),
            "bullet_create_blue": pygame.image.load("images/bullet_blue.png"),
            "bullet_create_red": pygame.image.load("images/red_bullet.png")
            }
        self.color = 0
        self.image = 0
        self.rect = 0
        self.yvel = 100
        self.ty = 0
        self.tx = 0

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def update(self):
        s = (self.tx - self.rect.x) ** 2 + (self.rect.y - self.ty) ** 2
        s2 = math.sqrt(s)
        coef = 800 / (s2 + 0.000000000000000000000000001)
        dy = -int((self.rect.y - self.ty)) * coef
        self.rect.x += int(self.tx - self.rect.x) * coef
        self.rect.y += dy
        if s2 < 800:
            self.rect.x = self.tx
            self.rect.y = self.ty

    def is_finished(self):
         return int(self.tx) <= int(self.rect.x) and int(self.tx) + 136 > int(self.rect.x) and int(self.ty) >= \
                int(self.rect.y) and int(self.ty) + 136 >= int(self.rect.y)


class Aim(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images/aim2.png")
        self.rect = Rect(x, y, 136, 136)
        self.frame = 0
    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def update(self):
        if self.frame % 60 == 0:
            self.rect.y += 136
        self.frame += 1

    def move_right(self):
        self.rect.x += 136

    def move_left(self):
        self.rect.x -= 136

    def move_up(self):
        self.rect.y -= 136

    def move_down(self):
        self.rect.y += 136




class Intersection():
    def __init__(self):
        self.current_bullet = 0
        self.current_block = 0

    def bullet_intersects_block(self, bullet, block):
        return block.rect.x < bullet.rect.x + 40 < block.rect.x + 136 and block.rect.y < bullet.rect.y + 20 < bullet.rect.y + 136

    def should_hit(self, bullet, block):
        if block.rect.x <= bullet.rect.x < block.rect.x + 136 and block.rect.y <= bullet.rect.y < block.rect.y + 136:
            return True

    def same_color(self, bullet, block):
        if block.color == bullet.color:
            return True

    def is_neightboor(self, block, neightboor):
        if abs(neightboor.rect.x - block.rect.x) == 136 and neightboor.rect.y == block.rect.y:
            return True
        if neightboor.rect.x == block.rect.x and abs(neightboor.rect.y - block.rect.y) == 136:
            return True

    def delete_block(self, block):
        block.kill()

    def delete_bullet(self, bullet):
        bullet.kill()

pygame.init()

screen = pygame.display.set_mode((1024, 768))
pygame.display.set_caption("GAME")

bg = Background()

players = pygame.sprite.Group()
bullets = pygame.sprite.Group()
clock = pygame.time.Clock()
frame = 0
intersection = Intersection()
aim = Aim(30, -136)
color = "green"
while True:
    bg.draw(screen)
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            raise SystemExit("QUIT")
        if e.type == pygame.KEYDOWN and e.key == pygame.K_LEFT:
            color = "green"
        if e.type == pygame.KEYDOWN and e.key == pygame.K_UP:
            color = "blue"
        if e.type == pygame.KEYDOWN and e.key == pygame.K_RIGHT:
            color = "red"
        if e.type == pygame.KEYDOWN and e.key == pygame.K_SPACE:
            y = aim.rect.y + 68
            x = aim.rect.x + 68
            for block in players:
                if block.rect.x < aim.rect.x + 68 <= block.rect.x + 136 and block.rect.y <= aim.rect.y+68 <= block.rect.y + 136:
                    bullet = Bullet()
                    bullet.ty = y
                    bullet.tx = x
                    bullet.color = color
                    bullet.image = bullet.images[f"bullet_create_{bullet.color}"]
                    bullet.rect = pygame.Rect(bullet.coordinates_for_color[bullet.color][0],
                                            bullet.coordinates_for_color[bullet.color][1],
                                            80, 20)
                    bullets.add(bullet)
        if e.type == pygame.KEYDOWN and e.key == pygame.K_d:
            aim.move_right()
        if e.type == pygame.KEYDOWN and e.key == pygame.K_a:
            aim.move_left()
        if e.type == pygame.KEYDOWN and e.key == pygame.K_w:
            aim.move_up()
        if e.type == pygame.KEYDOWN and e.key == pygame.K_s:
            aim.move_down()


    if frame % 60 == 0:
        x = 30
        for _ in range(9):
            player = Block(x, -136)
            player.cc = random.choice(list(player.colors))
            player.color = player.cc
            x += 136
            intersection.current_block = player.color
            players.add(player)
    frame += 1

    for player in players:
        player.update()
        player.draw(screen)

    aim.draw(screen)
    aim.update()

    for bullet in bullets:
        bullet.draw(screen)
        intersection.current_bullet = bullet.color
        bullet.update()

    # should_delete = []
    # neightboor2 = []
    # for bullet in bullets:
    #     if not bullet.is_finished():
    #         continue
    #     for block in players:
    #         if intersection.bullet_intersects_block(bullet, block):
    #             if not intersection.same_color(bullet, block):
    #                 intersection.delete_bullet(bullet)
    #                 break
    #             else:
    #                 if block not in should_delete:
    #                     should_delete.append(block)
    #                 intersection.delete_bullet(bullet)
    #                 break
    #
    # while len(should_delete) != 0:
    #     for block in should_delete[:]:
    #         for neightboor in players:
    #             if intersection.is_neightboor(block, neightboor) and intersection.same_color(block, neightboor):
    #                 if neightboor not in should_delete and neightboor not in neightboor2:
    #                     neightboor2.append(neightboor)
    #         intersection.delete_block(block)
    #         should_delete = neightboor2
    #         neightboor2 = []

    pygame.display.update()
    clock.tick(60)