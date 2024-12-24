import pygame
import sys

# Initialize pygame
pygame.init()

# Constants
ROW_COUNT = 6
COL_COUNT = 7
SQUARE_SIZE = 100
RADIUS = int(SQUARE_SIZE / 2 - 5)
WIDTH = COL_COUNT * SQUARE_SIZE
HEIGHT = (ROW_COUNT + 1) * SQUARE_SIZE
SIZE = (WIDTH, HEIGHT)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
FONT_COLOR = (255, 255, 255)

# Initialize screen
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Connect Four")

# Fonts
font = pygame.font.SysFont("monospace", 50)

# Functions
def create_board():
    return [[0] * COL_COUNT for _ in range(ROW_COUNT)]

def draw_board(board):
    for row in range(ROW_COUNT):
        for col in range(COL_COUNT):
            pygame.draw.rect(screen, BLUE, (col * SQUARE_SIZE, (row + 1) * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
            pygame.draw.circle(screen, BLACK, (col * SQUARE_SIZE + SQUARE_SIZE // 2, (row + 1) * SQUARE_SIZE + SQUARE_SIZE // 2), RADIUS)

    for row in range(ROW_COUNT):
        for col in range(COL_COUNT):
            if board[row][col] == 1:
                pygame.draw.circle(screen, RED, (col * SQUARE_SIZE + SQUARE_SIZE // 2, HEIGHT - (row * SQUARE_SIZE + SQUARE_SIZE // 2)), RADIUS)
            elif board[row][col] == 2:
                pygame.draw.circle(screen, YELLOW, (col * SQUARE_SIZE + SQUARE_SIZE // 2, HEIGHT - (row * SQUARE_SIZE + SQUARE_SIZE // 2)), RADIUS)
    pygame.display.update()

def is_valid_location(board, col):
    return board[0][col] == 0

def get_next_open_row(board, col):
    for row in range(ROW_COUNT - 1, -1, -1):
        if board[row][col] == 0:
            return row

def drop_piece(board, row, col, piece):
    board[row][col] = piece

def winning_move(board, piece):
    # Check horizontal locations
    for row in range(ROW_COUNT):
        for col in range(COL_COUNT - 3):
            if all(board[row][col + i] == piece for i in range(4)):
                return True

    # Check vertical locations
    for col in range(COL_COUNT):
        for row in range(ROW_COUNT - 3):
            if all(board[row + i][col] == piece for i in range(4)):
                return True

    # Check positively sloped diagonals
    for row in range(ROW_COUNT - 3):
        for col in range(COL_COUNT - 3):
            if all(board[row + i][col + i] == piece for i in range(4)):
                return True

    # Check negatively sloped diagonals
    for row in range(3, ROW_COUNT):
        for col in range(COL_COUNT - 3):
            if all(board[row - i][col + i] == piece for i in range(4)):
                return True

    return False

def print_winner(winner):
    label = font.render(f"Player {winner} wins!", True, FONT_COLOR)
    screen.blit(label, (40, 10))
    pygame.display.update()
    pygame.time.wait(3000)

# Game loop
board = create_board()
game_over = False
turn = 0

# Draw initial board
draw_board(board)

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEMOTION:
            pygame.draw.rect(screen, BLACK, (0, 0, WIDTH, SQUARE_SIZE))
            posx = event.pos[0]
            color = RED if turn == 0 else YELLOW
            pygame.draw.circle(screen, color, (posx, SQUARE_SIZE // 2), RADIUS)
        pygame.display.update()

        if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.draw.rect(screen, BLACK, (0, 0, WIDTH, SQUARE_SIZE))

            # Get column from mouse position
            posx = event.pos[0]
            col = posx // SQUARE_SIZE

            # Check if the move is valid
            if is_valid_location(board, col):
                row = get_next_open_row(board, col)
                drop_piece(board, row, col, turn + 1)

                if winning_move(board, turn + 1):
                    print_winner(turn + 1)
                    game_over = True

                turn = (turn + 1) % 2
                draw_board(board)

pygame.quit()

