import pygame
from pygame.locals import *
from sys import exit

from src.core.Enemy import Enemy
from src.core.Player import Player

from src.config.constants import *
from src.config.default import *

pygame.init()


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('PyFrogger')


player = Player(sprite_dir=FROG_SPRITES_DIR, player_speed=PLAYER_SPEED)
enemy = Enemy(sprite_dir=CAR_SPRITE_DIR, x_p=10, y_p=325, player_speed=5)

allSprites = pygame.sprite.Group()
allSprites.add(player)
allSprites.add(enemy)

enemyGroup = pygame.sprite.Group()
enemyGroup.add(enemy)

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

    collision = pygame.sprite.spritecollide(
        player, enemyGroup, True, pygame.sprite.collide_mask)

    allSprites.draw(screen)
    allSprites.update()

    pygame.display.flip()
