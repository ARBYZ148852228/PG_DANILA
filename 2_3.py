from winreg import REG_DWORD
from random import choice
from pygame.constants import *
from all_colors import *
import pygame
pygame.init()
size = (1280, 720)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Моя Игра')
BACKGROUND = (255, 255, 255)
screen.fill(BACKGROUND)
FPS = 60
width, height = 100, 100
x, y = 50, 50
color = RED
speed = 10
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()

    if keys[K_LEFT]:
        x -= speed
    if keys[K_RIGHT]:
        x += speed
    if keys[K_UP]:
        y -= speed
    if keys[K_DOWN]:
        y += speed



    if x < 0:
       x = 0
       color = choice(COLORS)
       continue
    if x > 1280 - width:
        x = 1280 - width
        color = choice(COLORS)
        continue
    if y < 0:
       y = 0
       color = choice(COLORS)
       continue
    if y > 720 - height:
       y = 720 - height
       color = choice(COLORS)
       continue









    screen.fill(BACKGROUND)
    pygame.draw.rect(screen, color, (x, y, width, height))


    pygame.display.update()
    clock.tick(FPS)

pygame.quit()