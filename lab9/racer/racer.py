import pygame
import random
import time

pygame.init()

WIDTH = 400
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
background = pygame.image.load('AnimatedStreet.png')

running = True
clock = pygame.time.Clock()
FPS = 60

player_img = pygame.image.load('Player.png')
enemy_img = pygame.image.load('Enemy.png')
coin_sizes = [(30, 30), (40, 40), (50, 50)]

background_music = pygame.mixer.music.load('background.wav')
crash_sound = pygame.mixer.Sound('crash.wav')
coin_sound = pygame.mixer.Sound('coinsound.mp3')

font = pygame.font.SysFont("Verdana", 60)
game_over = font.render("Game Over", True, "black")

score = 0
N = 5 
PLAYER_SPEED = 5
ENEMY_SPEED = 10

pygame.mixer.music.play(-1)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = player_img
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH // 2 - self.rect.w // 2
        self.rect.y = HEIGHT - self.rect.h
    
    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.move_ip(-PLAYER_SPEED, 0)
        if keys[pygame.K_RIGHT]:
            self.rect.move_ip(PLAYER_SPEED, 0)
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = enemy_img
        self.rect = self.image.get_rect()
        self.generate_random_rect()
    
    def move(self):
        global ENEMY_SPEED
        self.rect.move_ip(0, ENEMY_SPEED)
        if self.rect.top > HEIGHT:
            self.generate_random_rect()
    
    def generate_random_rect(self):
        self.rect.x = random.randint(0, WIDTH - self.rect.w)
        self.rect.y = 0

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.generate_random_rect()
    
    def generate_random_rect(self):
        size = random.choice(coin_sizes) 
        self.image = pygame.transform.scale(pygame.image.load('coin.png'), size)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH - self.rect.w)
        self.rect.y = random.randint(50, HEIGHT // 2)
        
        if size == (30, 30):
            self.value = 3
        elif size == (40, 40):
            self.value = 2
        else:
            self.value = 1
    
    def move(self):
        self.rect.move_ip(0, 6)
        if self.rect.top > HEIGHT:
            self.generate_random_rect()

player = Player()
enemy = Enemy()
coin = Coin()

all_sprites = pygame.sprite.Group(player, enemy, coin)
enemy_sprites = pygame.sprite.Group(enemy)
coin_sprites = pygame.sprite.Group(coin)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.blit(background, (0, 0))
    player.move()
    enemy.move()
    coin.move()
    
    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)
    
    if pygame.sprite.spritecollideany(player, enemy_sprites):
        crash_sound.play()
        time.sleep(1)
        screen.fill("red")
        center_rect = game_over.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        screen.blit(game_over, center_rect)
        pygame.display.flip()
        time.sleep(2)
        running = False
    
    if pygame.sprite.spritecollideany(player, coin_sprites):
        coin_sound.play()
        score += coin.value
        coin.generate_random_rect()
        
        if score % N == 0:
            ENEMY_SPEED += 1
    
    score_font = pygame.font.SysFont("Verdana", 30)
    score_text = score_font.render(f"Score: {score}", True, "black")
    screen.blit(score_text, (WIDTH - 150, 20))
    
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()