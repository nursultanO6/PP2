import pygame
pygame.init()
screen = pygame.display.set_mode((600, 600))
clock = pygame.time.Clock()
red = (255, 0, 0)

bx, by = 25, 25
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, red, (bx, by), 25)

    SPEED = 15
    key = pygame.key.get_pressed()
    if key[pygame.K_w]  and by > 25 :
        by += -SPEED
    if key[pygame.K_s] and by < 575:
        by += SPEED
    if key[pygame.K_d] and bx < 575:
        bx += SPEED
    if key[pygame.K_a] and bx > 25:
        bx += -SPEED

        
    pygame.display.update()
    clock.tick(60)