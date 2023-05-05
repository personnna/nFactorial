import pygame
from constants import *

class Sounds:
    def __init__(self):
        # Инициализация звуковых эффектов
        pygame.mixer.music.load(MUSIC_PATH)
        pygame.mixer.music.set_volume(MUSIC_VOLUME)
        self.explosion_sound = pygame.mixer.Sound(EXPLOSION_PATH)
        self.pickup_sound = pygame.mixer.Sound(PICKUP_PATH)

    def play_music(self):
        # Воспроизведение музыки
        pygame.mixer.music.play(-1)

    def play_explosion(self):
        # Воспроизведение звука взрыва
        self.explosion_sound.play()

    def play_pickup(self):
        # Воспроизведение звука подбора яйца
        self.pickup_sound.play()
