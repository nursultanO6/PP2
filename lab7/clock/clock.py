import pygame
import datetime as dt
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 600))
bg = pygame.image.load("clock.png")

imagemh = pygame.image.load("min_hand.png")
imagesh = pygame.image.load("sec_hand.png")

clock = pygame.time.Clock()

def blitRotateCenter(surf, image, topleft, angle):

    rotated_image = pygame.transform.rotate(image, -(topleft % 60) * 6 + angle)
    new_rect = rotated_image.get_rect(center = image.get_rect(center = (400, 300)).center)

    surf.blit(rotated_image, new_rect)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    curtime = dt.datetime.now()
    minuts = curtime.minute
    seconds = curtime.second

    screen.fill("BLACK")


    screen.blit(bg, (0,0))
    
    blitRotateCenter(screen, imagesh, seconds, 60)
    blitRotateCenter(screen, imagemh, minuts, -45)
    pygame.display.flip()
    clock.tick(60)