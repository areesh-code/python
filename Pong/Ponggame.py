import pygame
import sys
import random

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
BALL_RADIUS = 10
PADDLE_WIDTH, PADDLE_HEIGHT = 10, 100
PADDLE_SPEED = 7
BALL_SPEED = 5
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (50, 50, 50)
BLUE = (0, 128, 255)

# Setup display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")
clock = pygame.time.Clock()

# Fonts and sounds
font = pygame.font.Font(pygame.font.match_font('arial'), 36)
pong_sound = pygame.mixer.Sound(pygame.mixer.get_init() and 'pong_hit.wav' or None)
score_sound = pygame.mixer.Sound(pygame.mixer.get_init() and 'score_sound.wav' or None)

# Ball and paddles
ball = pygame.Rect(WIDTH // 2 - BALL_RADIUS, HEIGHT // 2 - BALL_RADIUS, BALL_RADIUS * 2, BALL_RADIUS * 2)
player1 = pygame.Rect(20, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
player2 = pygame.Rect(WIDTH - 20 - PADDLE_WIDTH, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)

ball_dx, ball_dy = random.choice([-BALL_SPEED, BALL_SPEED]), random.choice([-BALL_SPEED, BALL_SPEED])
player1_score, player2_score = 0, 0

# Functions
def draw_background():
    # Gradient background
    for y in range(HEIGHT):
        color = tuple([min(255, int(GRAY[i] + (y / HEIGHT) * (BLUE[i] - GRAY[i]))) for i in range(3)])
        pygame.draw.line(screen, color, (0, y), (WIDTH, y))

    # Midline
    for y in range(0, HEIGHT, 20):
        pygame.draw.rect(screen, WHITE, (WIDTH // 2 - 2, y, 4, 10))

def draw_objects():
    pygame.draw.ellipse(screen, WHITE, ball)
    pygame.draw.rect(screen, WHITE, player1)
    pygame.draw.rect(screen, WHITE, player2)

def draw_score():
    player1_text = font.render(str(player1_score), True, WHITE)
    player2_text = font.render(str(player2_score), True, WHITE)
    screen.blit(player1_text, (WIDTH // 4 - player1_text.get_width() // 2, 20))
    screen.blit(player2_text, (3 * WIDTH // 4 - player2_text.get_width() // 2, 20))

def ball_reset():
    global ball_dx, ball_dy
    ball.center = (WIDTH // 2, HEIGHT // 2)
    ball_dx, ball_dy = random.choice([-BALL_SPEED, BALL_SPEED]), random.choice([-BALL_SPEED, BALL_SPEED])

# Game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Input handling
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and player1.top > 0:
        player1.y -= PADDLE_SPEED
    if keys[pygame.K_s] and player1.bottom < HEIGHT:
        player1.y += PADDLE_SPEED
    if keys[pygame.K_UP] and player2.top > 0:
        player2.y -= PADDLE_SPEED
    if keys[pygame.K_DOWN] and player2.bottom < HEIGHT:
        player2.y += PADDLE_SPEED

    # Ball movement
    ball.x += ball_dx
    ball.y += ball_dy

    # Collision with top and bottom
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_dy *= -1
        pong_sound.play()

    # Collision with paddles
    if ball.colliderect(player1) or ball.colliderect(player2):
        ball_dx *= -1
        pong_sound.play()

    # Score handling
    if ball.left <= 0:
        player2_score += 1
        score_sound.play()
        ball_reset()
    if ball.right >= WIDTH:
        player1_score += 1
        score_sound.play()
        ball_reset()

    # Drawing
    screen.fill(BLACK)
    draw_background()
    draw_objects()
    draw_score()

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()