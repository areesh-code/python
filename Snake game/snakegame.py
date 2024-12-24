import pygame
import random
import sys


pygame.init()


WIDTH, HEIGHT = 800, 600
CELL_SIZE = 20
FPS = 12  


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (34, 139, 34)
RED = (255, 69, 0)
DARK_GRAY = (50, 50, 50)
LIGHT_GREEN = (144, 238, 144)


pygame.font.init()
FONT = pygame.font.SysFont("Arial", 28, bold=True)
GAME_OVER_FONT = pygame.font.SysFont("Arial", 54, bold=True)


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()


snake = [(100, 100), (90, 100), (80, 100)]  
snake_direction = 'RIGHT'
food = [(random.randrange(0, WIDTH // CELL_SIZE) * CELL_SIZE, 
         random.randrange(0, HEIGHT // CELL_SIZE) * CELL_SIZE)]
score = 0

def draw_grid():
    """ Draws grid for better visuals. """
    for x in range(0, WIDTH, CELL_SIZE):
        pygame.draw.line(screen, DARK_GRAY, (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, CELL_SIZE):
        pygame.draw.line(screen, DARK_GRAY, (0, y), (WIDTH, y))

def draw_snake():
    """ Draws snake with smooth colors. """
    for i, (x, y) in enumerate(snake):
        if i == 0:  
            pygame.draw.rect(screen, LIGHT_GREEN, (x, y, CELL_SIZE, CELL_SIZE), border_radius=4)
        else:
            pygame.draw.rect(screen, GREEN, (x, y, CELL_SIZE, CELL_SIZE), border_radius=2)


def draw_food():
    """ Draws the food. """
    for x, y in food:
        pygame.draw.ellipse(screen, RED, (x + 2, y + 2, CELL_SIZE - 4, CELL_SIZE - 4))

def display_score():
    """ Displays the score on screen. """
    score_surface = FONT.render(f"Score: {score}", True, WHITE)
    screen.blit(score_surface, (10, 10))

def move_snake():
    """ Updates snake's position. """
    global snake, snake_direction, food, score

    
    head_x, head_y = snake[0]
    if snake_direction == 'UP':
        head_y -= CELL_SIZE
    elif snake_direction == 'DOWN':
        head_y += CELL_SIZE
    elif snake_direction == 'LEFT':
        head_x -= CELL_SIZE
    elif snake_direction == 'RIGHT':
        head_x += CELL_SIZE

    
    new_head = (head_x, head_y)
    snake = [new_head] + snake[:-1]

    
    for fx, fy in food:
        if new_head == (fx, fy):
            score += 10
            snake.append(snake[-1])  
            food.remove((fx, fy))
            
            food.append((random.randrange(0, WIDTH // CELL_SIZE) * CELL_SIZE,
                         random.randrange(0, HEIGHT // CELL_SIZE) * CELL_SIZE))

def check_collisions():
    """ Checks collisions with walls and itself. """
    head_x, head_y = snake[0]
    if head_x < 0 or head_x >= WIDTH or head_y < 0 or head_y >= HEIGHT or (head_x, head_y) in snake[1:]:
        return True
    return False

def game_over():
    """ Displays Game Over screen. """
    screen.fill(BLACK)
    game_over_text = GAME_OVER_FONT.render("GAME OVER", True, RED)
    score_text = FONT.render(f"Final Score: {score}", True, WHITE)
    screen.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, HEIGHT // 2 - 50))
    screen.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, HEIGHT // 2 + 10))
    pygame.display.flip()
    pygame.time.wait(3000)

def main():
    """ Main game loop. """
    global snake_direction

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_UP, pygame.K_w) and snake_direction != 'DOWN':
                    snake_direction = 'UP'
                elif event.key in (pygame.K_DOWN, pygame.K_s) and snake_direction != 'UP':
                    snake_direction = 'DOWN'
                elif event.key in (pygame.K_LEFT, pygame.K_a) and snake_direction != 'RIGHT':
                    snake_direction = 'LEFT'
                elif event.key in (pygame.K_RIGHT, pygame.K_d) and snake_direction != 'LEFT':
                    snake_direction = 'RIGHT'
        
        move_snake()
        if check_collisions():
            game_over()
            break

        screen.fill(BLACK)
        draw_grid()
        draw_snake()
        draw_food()
        display_score()

        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    main()
