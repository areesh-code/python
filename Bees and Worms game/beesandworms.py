import pygame
import random


pygame.init()


WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bees and Worms Game")


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (34, 139, 34)


bee_image = pygame.image.load("bee.png")  
bee_image = pygame.transform.scale(bee_image, (50, 50))

worm_image = pygame.image.load("worm.png")  
worm_image = pygame.transform.scale(worm_image, (50, 50))

food_image = pygame.image.load("food.png")  
food_image = pygame.transform.scale(food_image, (30, 30))


background = pygame.image.load("grass.png")  
background = pygame.transform.scale(background, (WIDTH, HEIGHT))


clock = pygame.time.Clock()
FPS = 60


class Worm(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = worm_image
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT - 50)
        self.speed = 5

    def update(self, keys):
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < WIDTH:
            self.rect.x += self.speed
        if keys[pygame.K_UP] and self.rect.top > 0:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] and self.rect.bottom < HEIGHT:
            self.rect.y += self.speed


class Bee(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = bee_image
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH - self.rect.width)
        self.rect.y = random.randint(0, HEIGHT // 2)
        self.speed = random.randint(2, 4)

    def update(self):
        self.rect.x += self.speed
        if self.rect.right >= WIDTH or self.rect.left <= 0:
            self.speed = -self.speed


class Food(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = food_image
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH - self.rect.width)
        self.rect.y = random.randint(0, HEIGHT - self.rect.height)


worm = Worm()
bees = pygame.sprite.Group()
foods = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()

for _ in range(5):
    bee = Bee()
    bees.add(bee)
    all_sprites.add(bee)

for _ in range(3):
    food = Food()
    foods.add(food)
    all_sprites.add(food)

all_sprites.add(worm)


running = True
score = 0
while running:
    screen.blit(background, (0, 0))

   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

   
    keys = pygame.key.get_pressed()
    worm.update(keys)
    bees.update()

    
    if pygame.sprite.spritecollideany(worm, bees):
        print("Game Over! You were caught by a bee!")
        running = False

    food_collisions = pygame.sprite.spritecollide(worm, foods, True)
    score += len(food_collisions)

    
    for _ in range(len(food_collisions)):
        new_food = Food()
        foods.add(new_food)
        all_sprites.add(new_food)

  
    all_sprites.draw(screen)

 
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
