import pygame
from pygame.locals import *
from sys import exit

from src.core.Enemy import Enemy
from src.core.Player import Player

from src.config.constants import *

pygame.init()

screen_width = 512
screen_length = 500

screen = pygame.display.set_mode((screen_width, screen_length))
pygame.display.set_caption('PyFrogger')

sprites = pygame.sprite.Group()

player = Player(sprite_dir=FROG_SPRITES_DIR, player_speed=PLAYER_SPEED)
sprites.add(player)

enemy = Enemy(sprite_dir=CAR_SPRITE_DIR, x_p=220, y_p=425, player_speed=5)
enemy2 = Enemy(sprite_dir=CAR_SPRITE_DIR, x_p=220, y_p=395, player_speed=3)
enemy3 = Enemy(sprite_dir=CAR_SPRITE_DIR, x_p=220, y_p=345, player_speed=4)
enemy4 = Enemy(sprite_dir=CAR_SPRITE_DIR, x_p=220, y_p=295, player_speed=2)

clock = pygame.time.Clock()

background = pygame.image.load("./src/data/textures/background.jpg")

while True:
    clock.tick(30)

    screen.fill(BLACK_COLOR)
    screen.blit(background, (0, 0))

    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if player.animate == False:
            if keys[pygame.K_s]:
                player.down()
            if keys[pygame.K_w]:
                player.up()
            if keys[pygame.K_a]:
                player.left()
            if keys[pygame.K_d]:
                player.right()

    print(player.is_collide(enemy))
    print(player.is_collide(enemy2))
    print(player.is_collide(enemy3))
    print(player.is_collide(enemy4))

    screen.blit(player.image, player.position())
    screen.blit(enemy.image, enemy.position())
    screen.blit(enemy2.image, enemy2.position())
    screen.blit(enemy3.image, enemy3.position())
    screen.blit(enemy4.image, enemy4.position())

    sprites.draw(screen)
    sprites.update()

    enemy.update()
    enemy2.update()
    enemy3.update()
    enemy4.update()

    pygame.display.flip()
