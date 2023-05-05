import pygame
import random

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Define constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

# Define classes
class Egg(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30, 40))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, SCREEN_WIDTH - self.rect.width)
        self.rect.y = 0
        self.speed_y = random.randint(5, 10)
        
    def update(self):
        self.rect.y += self.speed_y
        if self.rect.y > SCREEN_HEIGHT:
            self.kill()

class Wolf(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((60, 80))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.centerx = SCREEN_WIDTH / 2
        self.rect.bottom = SCREEN_HEIGHT - 10
        self.speed_x = 0
        
    def update(self):
        self.rect.x += self.speed_x
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH

# Initialize Pygame
pygame.init()

# Create screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Catch the Egg!")

# Create sprite groups
all_sprites = pygame.sprite.Group()
egg_sprites = pygame.sprite.Group()
wolf_sprite = Wolf()
all_sprites.add(wolf_sprite)

# Create timer
spawn_timer = pygame.time.Clock()

# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                wolf_sprite.speed_x = -5
            elif event.key == pygame.K_RIGHT:
                wolf_sprite.speed_x = 5
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT and wolf_sprite.speed_x < 0:
                wolf_sprite.speed_x = 0
            elif event.key == pygame.K_RIGHT and wolf_sprite.speed_x > 0:
                wolf_sprite.speed_x = 0
                
    # Create eggs
    if spawn_timer.tick(FPS) > 500:
        egg_sprite = Egg()
        all_sprites.add(egg_sprite)
        egg_sprites.add(egg_sprite)
        
    # Update sprites
    all_sprites.update()
    
    # Draw screen
    screen.fill(WHITE)
    all_sprites.draw(screen)
    pygame.display.flip()

# Quit Pygame
pygame.quit()
