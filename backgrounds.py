import pygame
from constants import *

class Background:
    def __init__(self):
        self.image = pygame.image.load(BACKGROUND_IMAGE).convert()
        self.rect = self.image.get_rect()
        self.x = 0

    def draw(self, screen):
        screen.blit(self.image, (self.x, 0))
        screen.blit(self.image, (self.x + self.rect.width, 0))
        if self.x <= -self.rect.width:
            self.x = 0
        self.x -= BACKGROUND_SPEED