import pygame
from pygame.locals import *
from sys import exit

from src.config.default import *
from src.config.constants import *

from src.data.utils import showText
from src.data.utils import showButton

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
        self.isRunning = True
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.background = pygame.image.load(BACKGROUND_PATH)
        self.saveFrogs = 0
        self.selectedScreen = screens.MAIN_MENU
        self.start_ticks = 0
        self.finishTime = 0

        self.savePosX = [10, 120, 230, 340, 450]
        self.savePosY = 25

        self.font = pygame.font.match_font(FONT)

        pygame.display.set_caption('PyFrogger')

    def exit():
        pygame.quit()
        exit()

    def initialize(self):
        self.start_ticks = 0
        self.saveFrogs = 0
        player.life = 3

    def main_menu(self):
        self.initialize()
        self.clock.tick(MAX_TICK)
        self.screen.fill(MEDIUMSEAGREEN)

        logo = pygame.image.load(LOGO)
        logo_rect = logo.get_rect()
        logo = pygame.transform.scale(
            logo, (logo_rect.width/2, logo_rect.height/2))
        logo_rect = logo_rect.move((WIDTH / 4, 30))

        self.screen.blit(logo, logo_rect)

        mx, my = pygame.mouse.get_pos()
        btn_start = showButton(self, DARKGREEN, WIDTH / 2.5, HEIGHT / 2 - 30)
        btn_exit = showButton(self, DARKGREEN, WIDTH / 2.5, HEIGHT / 2 + 30)
        showText(
            self, f"Tempo da última partida: {self.finishTime} segundos!", 16, BLACK, WIDTH / 2 + 8, 120)
        showText(self, 'START', 24, WHITE, WIDTH / 2 + 8, HEIGHT / 2 - 25)
        showText(self, 'EXIT', 24, WHITE, WIDTH / 2 + 8, HEIGHT / 2 + 35)
        showText(self, f"Esse jogo foi desenvolvido por",
                 14, BLACK, WIDTH / 2, HEIGHT - 60)
        showText(self, f"Jonas Brito, Estefanny David e Laryssa Bezerra",
                 14, BLACK, WIDTH / 2, HEIGHT - 40)

        self.keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == pygame.BUTTON_LEFT:
                    if btn_start.collidepoint(mx, my):
                        self.selectedScreen = screens.START_GAME

                    if btn_exit.collidepoint(mx, my):
                        self.exit()

        pygame.display.flip()

    def start_game(self):
        self.clock.tick(MAX_TICK)
        self.screen.fill(BLACK)
        self.screen.blit(self.background, (0, 0))

        if (self.start_ticks == 0):
            self.start_ticks = pygame.time.get_ticks()

        showText(self, f"Vida: {player.life}", 11, WHITE, 20, HEIGHT - 12)
        showText(
            self, f"Tempo: {(pygame.time.get_ticks()-self.start_ticks)/1000}", 11, WHITE, 80, HEIGHT - 12)

        self.keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.exit()

            if player.animate == False and player.life > 0:
                if self.keys[pygame.K_s] or self.keys[pygame.K_w] or self.keys[pygame.K_a] or self.keys[pygame.K_d]:
                    player.move(self.keys)

        if player.rect.y < 85:
            enemy = Enemy(x=self.savePosX[self.saveFrogs], y=self.savePosY,
                          player_speed=0, sprite_dir=FROG_SPRITE_DIR)
            allSprites.add(enemy)
            self.saveFrogs += 1

            if self.saveFrogs == 5:
                self.finishTime = (pygame.time.get_ticks() -
                                   self.start_ticks)/1000
                self.selectedScreen = screens.MAIN_MENU

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
