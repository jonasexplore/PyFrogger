import pygame
import random

from src.config.default import *
from src.config.constants import *


class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, player_speed=4, sprite_dir=CAR_SPRITE_DIR):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprite_dir = sprite_dir
        self.player_speed = player_speed

        self.x = x
        self.y = y

        self.sprites.append(pygame.image.load(f"{self.sprite_dir}"))

        self.current = 0
        self.image = self.sprites[self.current]

        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x, self.y)

        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        self.rect.x += self.player_speed
        if self.rect.topleft[0] > WIDTH:
            self.rect.x = (random.randint(20, SPRITE_POS_RESTART) + 50) * -1
