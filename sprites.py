import pygame
import random
from constants import *


class Chicken(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.image = pygame.image.load('assets/images/chicken.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (CHICKEN_X, CHICKEN_Y)
        self.velocity = 0
        self.gravity = GRAVITY

    def update(self):
        # Обновление состояния курицы
        self.velocity += self.gravity
        self.rect.y += self.velocity
        if self.rect.bottom > GROUND_HEIGHT:
            self.rect.bottom = GROUND_HEIGHT
            self.velocity = 0

    def jump(self):
        # Прыжок курицы
        if self.rect.bottom == GROUND_HEIGHT:
            self.velocity -= JUMP_POWER


class Egg(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.image = pygame.image.load('assets/images/egg.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(EGG_MIN_X, EGG_MAX_X), EGG_START_Y)
        self.velocity = self.game.speed

    def update(self):
        # Обновление состояния яйца
        self.rect.y += self.velocity
        if self.rect.top > SCREEN_HEIGHT:
            self.kill()

    def catch(self):
        # Перехват яйца
        self.game.score += 1
        self.game.sound.play_catch()
        self.kill()


class FakeEgg(Egg):
    def __init__(self, game):
        super().__init__(game)
        self.image = pygame.image.load('assets/images/fake_egg.png').convert_alpha()

    def catch(self):
        # Перехват ложного яйца
        self.game.score -= 1
        self.game.sound.play_fail()
        self.kill()


class Bomb(Egg):
    def __init__(self, game):
        super().__init__(game)
        self.image = pygame.image.load('assets/images/bomb.png').convert_alpha()

    def catch(self):
        # Перехват бомбы
        self.game.sound.play_explosion()
        self.game.game_over = True
        self.kill()


class Wolf(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.image = pygame.image.load('assets/images/wolf.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(WOLF_MIN_X, WOLF_MAX_X), WOLF_START_Y)
        self.velocity = WOLF_SPEED

    def update(self):
        # Обновление состояния волка
        self.rect.y += self.velocity
        if self.rect.top > SCREEN_HEIGHT:
            self.kill()