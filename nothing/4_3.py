
from random import *
from all_colors import*
import pygame
pygame.init()
size = (800, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Моя Игра')
BACKGROUND = (135, 206, 235)
screen.fill(BACKGROUND)

snowflake = pygame.Surface((50, 50))
snowflake.set_colorkey((0, 0, 0))

pygame.draw.circle(snowflake, (255, 255, 255), (25, 25), 10)
pygame.draw.line(snowflake, (255, 255, 255), (25, 5), (25, 45), 5)
pygame.draw.line(snowflake, (255, 255, 255), (5, 25), (45, 25), 5)
pygame.draw.line(snowflake, (255, 255, 255), (10, 10), (40, 40), 5)
pygame.draw.line(snowflake, (255, 255, 255), (10, 40), (40, 10), 5)




snowflakes = []
pos = (0, 0)
screen.blit(snowflake, pos)



FPS = 60
clock = pygame.time.Clock()
running = True


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    for i in range(10):
        pos = [randint(0, 800), randint(0, 600)]
        pygame.draw.circle(snowflake, (255, 255, 255), (25, 25), 10)
        pygame.draw.line(snowflake, (255, 255, 255), (25, 5), (25, 45), 5)
        pygame.draw.line(snowflake, (255, 255, 255), (5, 25), (45, 25), 5)
        pygame.draw.line(snowflake, (255, 255, 255), (10, 10), (40, 40), 5)
        pygame.draw.line(snowflake, (255, 255, 255), (10, 40), (40, 10), 5)






    #screen.fill(BACKGROUND)
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
