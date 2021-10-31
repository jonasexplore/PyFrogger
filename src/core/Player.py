import pygame
import os


class Player(pygame.sprite.Sprite):

    def __init__(self, sprite_dir, player_speed=10):
        pygame.sprite.Sprite.__init__(self)

        self.sprites = []
        self.sprite_dir = sprite_dir
        self.player_speed = player_speed

        self.x = 100
        self.y = 100

        for file in os.listdir(self.sprite_dir):
            self.sprites.append(pygame.image.load(
                f"{self.sprite_dir}{file}"))

        self.current = 0
        self.image = self.sprites[self.current]
        self.rect = self.image.get_rect()
        self.rect.topleft = self.x, self.y

        self.animate = False

    def update(self):
        if self.animate == True:
            self.current += 0.7
            self.rect.topleft = self.x, self.y

            if self.current >= len(self.sprites):
                self.current = 0
                self.animate = False
            self.image = self.sprites[int(self.current)]

    def down(self):
        self.animate = True
        self.y += self.player_speed

    def up(self):
        self.animate = True
        self.y -= self.player_speed

    def left(self):
        self.animate = True
        self.x -= self.player_speed

    def right(self):
        self.animate = True
        self.x += self.player_speed

    def position(self):
        return (self.x, self.y)
