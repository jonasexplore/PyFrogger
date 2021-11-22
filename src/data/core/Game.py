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
savedFrogs = pygame.sprite.Group()

# Enimies spawn
enemiesSprites = [
    CAR_SPRITE_DIR, CAR_SPRITE_DIR,
    CAR_SPRITE_DIR, CAR_SPRITE_DIR,
    CAR_SPRITE_DIR, CAR_SPRITE_DIR,
    CAR_SPRITE_DIR, CAR_SPRITE_DIR,
    FLY_SPRITE_DIR, FLY_SPRITE_DIR,
    FLY_SPRITE_DIR, FLY_SPRITE_DIR]

enimiesPosX = [
    -330, -160, 50, -100,
    -100, -10, -150, -10,
    -10, -100, -150, -10]

enimiesPosY = [
    427, 427, 427, 389,
    351, 313, 285, 285,
    199, 161, 123, 85]

enemiesSpeed = [5, 5, 5, 4, 3, 3, 2, 2, 3, 4, 5, 4]

for i in range(0, len(enimiesPosX)):
    enemy = Enemy(
        x=enimiesPosX[i],
        y=enimiesPosY[i],
        player_speed=enemiesSpeed[i],
        sprite_dir=enemiesSprites[i]
    )

    allSprites.add(enemy)
    enemyGroup.add(enemy)

player = Player()
allSprites.add(player)


class Game:
    def __init__(self) -> None:
        pygame.init()
        self.isRunning = True

        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.background = pygame.image.load(BACKGROUND_PATH)
        self.selectedScreen = screens.MAIN_MENU

        self.saveFrogs = 0
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
        player.life = MAX_PLAYER_LIFE

    def textWhite(self, text, size, x, y):
        showText(self, text, size, WHITE, x, y)

    def textBlack(self, text, size, x, y):
        showText(self, text, size, BLACK, x, y)

    def main_menu(self):
        self.clock.tick(MAX_TICK)
        self.screen.fill(MEDIUMSEAGREEN)

        # Logo
        logo = pygame.image.load(LOGO)
        logo_rect = logo.get_rect()
        logo = pygame.transform.scale(
            logo, (logo_rect.width/2, logo_rect.height/2))
        logo_rect = logo_rect.move((WIDTH / 4, 30))

        self.screen.blit(logo, logo_rect)

        # Half width and height
        half_w = WIDTH / 2
        half_h = HEIGHT / 2

        # Buttons
        btn_start = showButton(self, DARKGREEN, WIDTH / 2.5, half_h - 30)
        btn_exit = showButton(self, DARKGREEN, WIDTH / 2.5, half_h + 30)
        self.textWhite('START', 24, half_w + 8, half_h - 25)
        self.textWhite('EXIT', 24, half_w + 8, half_h + 35)

        self.textBlack(f"Tempo da última partida: {self.finishTime} segundos!",
                       16, half_w + 8, 120)
        self.textBlack(f"Esse jogo foi desenvolvido por",
                       14, half_w, HEIGHT - 60)
        self.textBlack(f"Jonas Brito, Estefanny David e Laryssa Bezerra",
                       14, half_w, HEIGHT - 40)

        self.keys = pygame.key.get_pressed()
        mx, my = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == pygame.BUTTON_LEFT:
                    if btn_start.collidepoint(mx, my):
                        self.initialize()
                        self.selectedScreen = screens.START_GAME

                    if btn_exit.collidepoint(mx, my):
                        self.exit()

        pygame.display.flip()

    def start_game(self):
        self.clock.tick(MAX_TICK)
        self.screen.fill(BLACK)
        self.screen.blit(self.background, (0, 0))

        if self.start_ticks == 0:
            self.start_ticks = pygame.time.get_ticks()

        if self.saveFrogs == 0:
            savedFrogs.empty()

        seconds = (pygame.time.get_ticks()-self.start_ticks)/1000
        self.textWhite(f"Vida: {player.life}", 11, 20, HEIGHT - 12)
        self.textWhite(f"Tempo: {seconds}", 11, 80, HEIGHT - 12)

        self.keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.exit()

            if player.animate == False and player.life > 0:
                if self.keys[pygame.K_s] or self.keys[pygame.K_w] or self.keys[pygame.K_a] or self.keys[pygame.K_d]:
                    player.move(self.keys)

        if player.rect.y < 85:
            savedFrog = Enemy(x=self.savePosX[self.saveFrogs], y=self.savePosY,
                              player_speed=0, sprite_dir=FROG_SPRITE_DIR)
            savedFrogs.add(savedFrog)
            self.saveFrogs += 1

            if self.saveFrogs == MAX_SAVE_FROGS:
                self.finishTime = (
                    pygame.time.get_ticks() - self.start_ticks)/1000
                self.selectedScreen = screens.MAIN_MENU

            player.initialPosition()

        collision = pygame.sprite.spritecollide(
            player, enemyGroup, False, pygame.sprite.collide_mask)

        allSprites.draw(self.screen)
        savedFrogs.draw(self.screen)

        if collision:
            player.loseLife()
            if player.life == 0:
                self.initialize()
                self.selectedScreen = screens.MAIN_MENU
            pass
        else:
            if player.life > 0:
                allSprites.update()

        pygame.display.flip()
