import pygame
from pygame.locals import *

from sys import exit

from src.config.default import *
from src.config.constants import *

from src.data.components.Enemy import Enemy
from src.data.components.Player import Player

allSprites = pygame.sprite.Group()
enemyGroup = pygame.sprite.Group()

player = Player()


enemiesSprites = [CAR_SPRITE_DIR, CAR_SPRITE_DIR,
                  CAR_SPRITE_DIR, CAR_SPRITE_DIR,
                  CAR_SPRITE_DIR, CAR_SPRITE_DIR,
                  CAR_SPRITE_DIR, CAR_SPRITE_DIR,
                  FLY_SPRITE_DIR, FLY_SPRITE_DIR,
                  FLY_SPRITE_DIR, FLY_SPRITE_DIR]
enemiesPositionsStartX = [-330, -160, 50, -100, -
                          100, -10, -150, -10, -10, -100, -150, -10]
enemiesPositionsStartY = [427, 427, 427, 389,
                          351, 313, 285, 285, 199, 161, 123, 85]
enemiesSpeed = [5, 5, 5, 4, 3, 3, 2, 2, 3, 4, 5, 4]

for i in range(0, len(enemiesPositionsStartX)):
    enemy = Enemy(
        x=enemiesPositionsStartX[i],
        y=enemiesPositionsStartY[i],
        player_speed=enemiesSpeed[i],
        sprite_dir=enemiesSprites[i]
    )

    allSprites.add(enemy)
    enemyGroup.add(enemy)

allSprites.add(player)


class Game:
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.background = pygame.image.load(BACKGROUND_PATH)
        self.saveFrogs = 0

        self.savePosX = [10, 120, 230, 340, 450]
        self.savePosY = 25

        pygame.display.set_caption('PyFrogger')

    def update(self):
        self.clock.tick(MAX_TICK)

        self.screen.fill(BLACK_COLOR)
        self.screen.blit(self.background, (0, 0))

        self.keys = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if player.animate == False and player.life > 0:
                if self.keys[pygame.K_s] or self.keys[pygame.K_w] or self.keys[pygame.K_a] or self.keys[pygame.K_d]:
                    player.move(self.keys)

        if player.rect.y < 85:
            enemy = Enemy(x=self.savePosX[self.saveFrogs], y=self.savePosY,
                          player_speed=0, sprite_dir=FROG_SPRITE_DIR)
            allSprites.add(enemy)
            self.saveFrogs += 1
            player.initialPosition()

        collision = pygame.sprite.spritecollide(
            player, enemyGroup, False, pygame.sprite.collide_mask)

        allSprites.draw(self.screen)

        if collision:
            player.loseLife()
            pass
        else:
            if player.life > 0:
                allSprites.update()

        pygame.display.flip()
