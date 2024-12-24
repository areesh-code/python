import pygame
import random
import math
import sys


pygame.init()


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Realistic Gun Game - Enemy Shooter")


clock = pygame.time.Clock()


background = pygame.image.load("background.jpg")  
background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))


player_img = pygame.image.load("player.png")  
player_img = pygame.transform.scale(player_img, (50, 50))


enemy_img = pygame.image.load("enemy.png")  
enemy_img = pygame.transform.scale(enemy_img, (50, 50))


bullet_img = pygame.image.load("bullet.png")  
bullet_img = pygame.transform.scale(bullet_img, (10, 20))


player_x = SCREEN_WIDTH // 2
player_y = SCREEN_HEIGHT - 70
player_speed = 5


enemy_speed = 2
enemies = []


bullets = []
bullet_speed = 7


score = 0
font = pygame.font.SysFont('comicsans', 30)


def spawn_enemy():
    enemy_x = random.randint(0, SCREEN_WIDTH - 50)
    enemy_y = random.randint(-150, -50)
    enemies.append([enemy_x, enemy_y])


def draw_player(x, y):
    screen.blit(player_img, (x, y))


def draw_enemies():
    for enemy in enemies:
        screen.blit(enemy_img, (enemy[0], enemy[1]))


def draw_bullets():
    for bullet in bullets:
        screen.blit(bullet_img, (bullet[0], bullet[1]))


def draw_score():
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))


def check_collision(enemy_x, enemy_y, bullet_x, bullet_y):
    distance = math.sqrt(math.pow(enemy_x - bullet_x, 2) + math.pow(enemy_y - bullet_y, 2))
    return distance < 30


running = True
while running:
    screen.fill(BLACK)  
    screen.blit(background, (0, 0))  

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < SCREEN_WIDTH - 50:
        player_x += player_speed
    if keys[pygame.K_SPACE]:  
        bullets.append([player_x + 20, player_y])

    
    for bullet in bullets:
        bullet[1] -= bullet_speed
        if bullet[1] < 0:  
            bullets.remove(bullet)

    
    if random.randint(1, 50) == 1: 
        spawn_enemy()

    
    for enemy in enemies:
        enemy[1] += enemy_speed
        if enemy[1] > SCREEN_HEIGHT:  
            enemies.remove(enemy)

    
    for bullet in bullets:
        for enemy in enemies:
            if check_collision(enemy[0], enemy[1], bullet[0], bullet[1]):
                bullets.remove(bullet)
                enemies.remove(enemy)
                score += 1
                break

   
    draw_player(player_x, player_y)
    draw_enemies()
    draw_bullets()
    draw_score()

  
    pygame.display.update()
    clock.tick(60)  