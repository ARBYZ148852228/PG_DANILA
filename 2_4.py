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
x, y = 50, 50
color = BLUE
speed = 5
clock = pygame.time.Clock()
running = True
rect = pygame.Rect(0, 100, 200, 150)


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    rect.x += speed
    if rect.x > screen.get_width():
        rect.x = -rect.width







    screen.fill(BACKGROUND)
    pygame.draw.rect(screen, BLUE, rect)
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()