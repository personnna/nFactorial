# Размер экрана
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Количество кадров в секунду
FPS = 60

# Скорость яиц
EGG_SPEED = 5

# Вероятность появления яиц и бомб
EGG_PROBABILITY = 0.05
BOMB_PROBABILITY = 0.1

# Максимальное количество бомб и фальшивых яиц на экране
MAX_BOMBS = 1
MAX_FAKE_EGGS = 1

# Скорость движения облаков
CLOUD_SPEED = 1

# Скорость движения травы
GRASS_SPEED = 2

# Скорость движения деревьев
TREE_SPEED = 3

# Уровни сложности
LEVELS = {
    1: {'score': 10, 'speed': 5},
    2: {'score': 20, 'speed': 6},
    3: {'score': 30, 'speed': 7},
    4: {'score': 40, 'speed': 8},
    5: {'score': 50, 'speed': 9},
}

# Файлы звуковых эффектов
EXPLOSION_SOUND_FILE = 'sounds/explosion.wav'
JUMP_SOUND_FILE = 'sounds/jump.wav'
SCORE_SOUND_FILE = 'sounds/score.wav'
GAME_OVER_SOUND_FILE = 'sounds/game_over.wav'

# Шрифты
SCORE_FONT_FILE = 'fonts/Roboto-Regular.ttf'
GAME_OVER_FONT_FILE = 'fonts/Roboto-Bold.ttf'

# Цвета для шрифтов
SCORE_COLOR = WHITE
GAME_OVER_COLOR = RED

# Путь к файлу с шрифтом
FONT_PATH = SCORE_FONT_FILE
