import pygame
import random
import sys


pygame.init()


WIDTH, HEIGHT = 800, 600


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Spaceship Game")


spaceship_img = pygame.image.load("spaceship.img")
spaceship_img = pygame.transform.scale(spaceship_img, (50, 50))


spaceship_x, spaceship_y = WIDTH // 2, HEIGHT - 70
spaceship_speed = 5


obstacle_width, obstacle_height = 50, 50
obstacles = []
obstacle_speed = 3


clock = pygame.time.Clock()


def create_obstacle():
    x = random.randint(0, WIDTH - obstacle_width)
    y = -obstacle_height
    obstacles.append(pygame.Rect(x, y, obstacle_width, obstacle_height))

running = True
score = 0


while running:
    screen.fill(BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and spaceship_x > 0:
        spaceship_x -= spaceship_speed
    if keys[pygame.K_RIGHT] and spaceship_x < WIDTH - 50:
        spaceship_x += spaceship_speed

   
    screen.blit(spaceship_img, (spaceship_x, spaceship_y))

   
    if random.randint(1, 30) == 1:
        create_obstacle()

   
    for obstacle in obstacles:
        obstacle.y += obstacle_speed
        pygame.draw.rect(screen, RED, obstacle)

        
        if pygame.Rect(spaceship_x, spaceship_y, 50, 50).colliderect(obstacle):
            print("Game Over! Final Score:", score)
            running = False

   
    obstacles = [obstacle for obstacle in obstacles if obstacle.y < HEIGHT]


    score += 1
    font = pygame.font.SysFont(None, 36)
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    
    pygame.display.flip()

    
    clock.tick(60)

pygame.quit()
sys.exit()
