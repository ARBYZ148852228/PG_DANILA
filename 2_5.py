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
x, y = 0, 0
rect_size = 200
colors = [RED, BLACK]
clock = pygame.time.Clock()
running = True



rect1 = pygame.Rect(x, y, rect_size, rect_size)
rect1.center = (screen.get_width()// 2, screen.get_height()//2)
pygame.draw.rect(screen, BLACK, rect1)

rect2 = pygame.Rect(x, y, 100, 100)
rect2.center = (screen.get_width()// 2, screen.get_height()//2)
pygame.draw.rect(screen, RED, rect2)


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False







    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()