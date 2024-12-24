import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Running Dog Animation")

# Define colors
WHITE = (255, 255, 255)

# Load dog image (make sure you have a dog image file)
dog_image = pygame.image.load('dog.gif')
dog_rect = dog_image.get_rect()

# Set the initial position of the dog
dog_rect.x = 0
dog_rect.y = height // 2

# Define the speed of the dog's movement
dog_speed = 5

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the dog
    dog_rect.x += dog_speed
    if dog_rect.x > width:
        dog_rect.x = -dog_rect.width  # Reset the dog's position after it moves off screen

    # Fill the screen with white color
    screen.fill(WHITE)

    # Draw the dog on the screen
    screen.blit(dog_image, dog_rect)

    # Update the display
    pygame.display.flip()

    # Set the frame rate
    pygame.time.Clock().tick(60)

# Quit Pygame
#pygame.quit()
#sys.exit()
