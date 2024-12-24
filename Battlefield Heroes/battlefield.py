import pygame
import random

# Initialize pygame
pygame.init()

# Constants
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (200, 0, 0)
GREEN = (0, 200, 0)
BLUE = (0, 0, 200)
BROWN = (139, 69, 19)
SKY_BLUE = (135, 206, 235)

# Initialize screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Battlefield Game")

# Clock
clock = pygame.time.Clock()

# Load assets
player_img = pygame.image.load("player.png")
player_img = pygame.transform.scale(player_img, (50, 50))

enemy_img = pygame.image.load("enemy.png")
enemy_img = pygame.transform.scale(enemy_img, (50, 50))

bullet_img = pygame.image.load("bullet.png")
bullet_img = pygame.transform.scale(bullet_img, (10, 10))

background_img = pygame.image.load("background.png")
background_img = pygame.transform.scale(background_img, (SCREEN_WIDTH, SCREEN_HEIGHT))

# Player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = player_img
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT - 70)
        self.speed = 5

    def update(self, keys):
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < SCREEN_WIDTH:
            self.rect.x += self.speed

# Enemy class
class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = enemy_img
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.speed = random.randint(1, 3)

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > SCREEN_HEIGHT:
            self.rect.y = random.randint(-100, -40)
            self.rect.x = random.randint(0, SCREEN_WIDTH - self.rect.width)

# Bullet class
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = bullet_img
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = -7

    def update(self):
        self.rect.y += self.speed
        if self.rect.bottom < 0:
            self.kill()

# Initialize sprites
enemies = pygame.sprite.Group()
for i in range(10):
    enemy = Enemy(random.randint(0, SCREEN_WIDTH - 50), random.randint(-150, -50))
    enemies.add(enemy)

bullets = pygame.sprite.Group()
player = Player()
player_group = pygame.sprite.GroupSingle(player)

# Game loop
running = True
score = 0
font = pygame.font.Font(None, 36)

def draw_text(text, x, y, color):
    surface = font.render(text, True, color)
    screen.blit(surface, (x, y))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            bullet = Bullet(player.rect.centerx, player.rect.top)
            bullets.add(bullet)

    # Update
    keys = pygame.key.get_pressed()
    player_group.update(keys)
    enemies.update()
    bullets.update()

    # Collision detection
    for bullet in bullets:
        hits = pygame.sprite.spritecollide(bullet, enemies, True)
        if hits:
            bullet.kill()
            score += 10

    # Drawing
    screen.blit(background_img, (0, 0))
    player_group.draw(screen)
    enemies.draw(screen)
    bullets.draw(screen)
    draw_text(f"Score: {score}", 10, 10, WHITE)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()

                                                                                                                 