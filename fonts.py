import pygame
from constants import *

class ScoreFont:
    def __init__(self):
        self.font = pygame.font.Font(FONT_PATH, 50)

    def render(self, text):
        return self.font.render(text, True, SCORE_COLOR)


class GameOverFont:
    def __init__(self):
        self.font = pygame.font.Font(FONT_PATH, 80)

    def render(self, text):
        return self.font.render(text, True, GAME_OVER_COLOR)
