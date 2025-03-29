from all_colors import*
from random import choice
import math
import pygame
pygame.init()

size = (1280, 720)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Моя Игра')
BACKGROUND = (255, 255, 255)
screen.fill(BACKGROUND)
FPS = 60
clock = pygame.time.Clock()
running = True
dragging = False
filling = False
RECTANGLE_COLOR = (255, 0, 0)
rectangles = []

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            top_left = event.pos
            size = 0,0
            dragging = True

        elif event.type == pygame.MOUSEMOTION and dragging:
            right_bottom = event.pos
            size = (right_bottom[0] - top_left[0], right_bottom[1] - top_left[1])

        elif event.type == pygame.MOUSEBUTTONUP:
            right_bottom = event.pos
            size = (right_bottom[0] - top_left[0], right_bottom[1] - top_left[1])
            dragging = False
            rect = pygame.Rect(top_left, size)
            color = choice(COLORS)
            rectangles.append((rect, color))




    screen.fill(BACKGROUND)
    pygame.draw.rect(screen, RECTANGLE_COLOR, (top_left, size), 1)
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
