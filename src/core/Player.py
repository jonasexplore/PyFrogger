import pygame
import os


class Player(pygame.sprite.Sprite):

    def __init__(self, sprite_dir, player_speed=10):
        pygame.sprite.Sprite.__init__(self)

        self.sprites = []
        self.sprite_dir = sprite_dir
        self.player_speed = player_speed

        self.x = 220
        self.y = 435

        for file in os.listdir(self.sprite_dir):
            self.sprites.append(pygame.image.load(
                f"{self.sprite_dir}{file}"))

        self.current = 0
        self.image = self.sprites[self.current]
        self.rect = self.image.get_rect()
        self.rect.topleft = self.x, self.y

        # self.direction = {'up': 180, 'down': 0, 'left': 270, 'right': 90}
        # self.side = 'up'

        self.animate = False

    def update(self):
        if self.animate == True:
            # print(self.position())
            self.current += 0.7
            self.rect.topleft = self.x, self.y

            if self.current >= len(self.sprites):
                self.current = 0
                self.animate = False
            self.image = self.sprites[int(self.current)]
            # self.image = pygame.transform.rotate(
            # self.image, self.direction[self.side])

    def down(self):
        self.animate = True
        self.y += self.player_speed
        # self.side = 'down'

    def up(self):
        self.animate = True
        self.y -= self.player_speed
        # self.side = 'up'

    def left(self):
        self.animate = True
        self.x -= self.player_speed
        # self.side = 'left'

    def right(self):
        self.animate = True
        self.x += self.player_speed
        # self.side = 'right'

    def position(self):
        return (self.x, self.y)
