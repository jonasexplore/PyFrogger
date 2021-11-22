import pygame
import sys


def showText(game, text: str, size: int, color, x: int, y: int):
    font = pygame.font.Font(game.font, size)
    text = font.render(text, True, color)
    rect = text.get_rect()
    rect.midtop = (x, y)

    game.screen.blit(text, rect)


sys.modules[__name__] = showText
