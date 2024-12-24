import pygame
import random

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Car Racing Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (119, 136, 153)
RED = (200, 0, 0)
GREEN = (0, 200, 0)

# Load assets
car_image = pygame.image.load("car.png")  # Replace with a path to your car image
car_image = pygame.transform.scale(car_image, (50, 100))

bg_image = pygame.image.load("road.png")  # Replace with a path to your road background
bg_image = pygame.transform.scale(bg_image, (WIDTH, HEIGHT))

# Constants
FPS = 60
CAR_WIDTH = 50
CAR_HEIGHT = 100
LANE_WIDTH = WIDTH // 3

# Player class
class Player:
    def __init__(self):
        self.x = WIDTH // 2 - CAR_WIDTH // 2
        self.y = HEIGHT - CAR_HEIGHT - 20
        self.speed = 5

    def move(self, keys):
        if keys[pygame.K_LEFT] and self.x > LANE_WIDTH // 2:
            self.x -= self.speed
        if keys[pygame.K_RIGHT] and self.x < WIDTH - LANE_WIDTH // 2 - CAR_WIDTH:
            self.x += self.speed

    def draw(self):
        screen.blit(car_image, (self.x, self.y))

# Obstacle class
class Obstacle:
    def __init__(self):
        self.x = random.choice([LANE_WIDTH // 2, LANE_WIDTH + LANE_WIDTH // 2, 2 * LANE_WIDTH + LANE_WIDTH // 2])
        self.y = -CAR_HEIGHT
        self.speed = 7

    def move(self):
        self.y += self.speed

    def draw(self):
        pygame.draw.rect(screen, RED, (self.x, self.y, CAR_WIDTH, CAR_HEIGHT))

    def is_off_screen(self):
        return self.y > HEIGHT

# Game loop
clock = pygame.time.Clock()
player = Player()
obstacles = []
score = 0
running = True

while running:
    clock.tick(FPS)
    screen.blit(bg_image, (0, 0))

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Player movement
    keys = pygame.key.get_pressed()
    player.move(keys)

    # Obstacle management
    if random.randint(1, 60) == 1:  # Spawn an obstacle every ~1 second
        obstacles.append(Obstacle())

    for obstacle in obstacles:
        obstacle.move()
        obstacle.draw()
        if obstacle.is_off_screen():
            obstacles.remove(obstacle)
            score += 1

        # Check collision
        if (player.x < obstacle.x + CAR_WIDTH and
                player.x + CAR_WIDTH > obstacle.x and
                player.y < obstacle.y + CAR_HEIGHT and
                player.y + CAR_HEIGHT > obstacle.y):
            running = False

    # Draw player
    player.draw()

    # Display score
    font = pygame.font.SysFont(None, 36)
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    # Update display
    pygame.display.flip()

pygame.quit()


