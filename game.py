import pygame
import random
from constants import *
from fonts import ScoreFont

class Egg(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images/egg.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, SCREEN_WIDTH - self.rect.width)
        self.rect.y = -self.rect.height

    def update(self):
        self.rect.y += EGG_SPEED
        if self.rect.top > SCREEN_HEIGHT:
            self.kill()

class FakeEgg(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images/fake_egg.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, SCREEN_WIDTH - self.rect.width)
        self.rect.y = -self.rect.height

    def update(self):
        self.rect.y += EGG_SPEED
        if self.rect.top > SCREEN_HEIGHT:
            self.kill()

class Bomb(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images/bomb.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, SCREEN_WIDTH - self.rect.width)
        self.rect.y = -self.rect.height

    def update(self):
        self.rect.y += EGG_SPEED
        if self.rect.top > SCREEN_HEIGHT:
            self.kill()

class Cloud(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images/cloud.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(-SCREEN_WIDTH, SCREEN_WIDTH)
        self.rect.y = random.randint(-200, 200)

    def update(self):
        self.rect.x += CLOUD_SPEED
        if self.rect.left > SCREEN_WIDTH:
            self.rect.right = 0

class Grass(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images/grass.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(-SCREEN_WIDTH, SCREEN_WIDTH)
        self.rect.y = SCREEN_HEIGHT - self.rect.height

    def update(self):
        self.rect.x += GRASS_SPEED
        if self.rect.left > SCREEN_WIDTH:
            self.rect.right = 0

class Tree(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images/tree.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(-SCREEN_WIDTH, SCREEN_WIDTH)
        self.rect.y = SCREEN_HEIGHT - self.rect.height

    def update(self):
        self.rect.x += TREE_SPEED
        if self.rect.left > SCREEN_WIDTH:
            self.rect.right = 0

def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Catch the Eggs")

    clock = pygame.time.Clock()

    all_sprites = pygame.sprite.Group()
    eggs = pygame.sprite.Group()
    fake_eggs = pygame.sprite.Group()
    bombs = pygame.sprite.Group()
    clouds = pygame.sprite.Group()
    grass = pygame.sprite.Group()
    trees = pygame.sprite.Group()

    player_image = pygame.image.load("images/player.png").convert_alpha()
    player_rect = player_image.get_rect()
    player_rect.bottom = SCREEN_HEIGHT
    player_speed = 0

    score = 0
    score_font = ScoreFont()
   
