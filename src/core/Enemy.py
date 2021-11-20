import pygame
from src.config.default import *


class Enemy(pygame.sprite.Sprite):
    def __init__(self, sprite_dir, x_p, y_p, player_speed=4):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprite_dir = sprite_dir
        self.player_speed = player_speed

        self.x = x_p
        self.y = y_p

        self.sprites.append(pygame.image.load(f"{self.sprite_dir}"))

        self.current = 0
        self.image = self.sprites[self.current]

        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x, self.y)

        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        self.rect.x += self.player_speed
        if self.rect.topleft[0] > WIDTH:
            self.rect.x = -200

    def position(self):
        return (self.x, self.y)
