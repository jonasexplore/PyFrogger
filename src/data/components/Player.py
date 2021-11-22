import pygame
import os

from src.config.constants import *


class Player(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.sprites = []
        self.sprite_dir = FROG_SPRITES_DIR
        self.player_speed = PLAYER_SPEED
        self.life = 3

        self.x = 220
        self.y = 465

        for file in os.listdir(self.sprite_dir):
            self.sprites.append(pygame.image.load(
                f"{self.sprite_dir}{file}"))

        self.current = 0
        self.image = self.sprites[self.current]
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x, self.y)

        self.mask = pygame.mask.from_surface(self.image)

        self.animate = False

    def update(self):
        if self.animate == True:
            self.current += 0.7
            if self.current >= len(self.sprites):
                self.current = 0
                self.animate = False
            self.image = self.sprites[int(self.current)]

    def move(self, direction):
        self.animate = True

        if direction[pygame.K_s]:
            self.rect.y += self.player_speed
        elif direction[pygame.K_a]:
            self.rect.x -= self.player_speed
        elif direction[pygame.K_d]:
            self.rect.x += self.player_speed
        elif direction[pygame.K_w]:
            self.rect.y -= self.player_speed

    def initialPosition(self):
        self.rect.x = self.x
        self.rect.y = self.y

    def loseLife(self):
        self.initialPosition()

        self.life -= 1

        return self.life
