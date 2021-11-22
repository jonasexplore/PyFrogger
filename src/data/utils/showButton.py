import pygame
import sys

from src.config.default import *


def showButton(game, color, x, y, w=120, h=40) -> pygame.Rect:
    btn = pygame.Rect(x, y, w, h)
    pygame.draw.rect(game.screen, color, btn, border_radius=3)

    return btn


sys.modules[__name__] = showButton
