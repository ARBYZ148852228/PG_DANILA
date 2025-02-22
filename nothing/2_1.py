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

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()
    clock.tick(FPS)
    if event.type == pygame.QUIT:
        running = False

    if event.type == pygame.KEYDOWN:
        print(f"Press {event.key}")
    if event.type == pygame.KEYUP:
        print(f"Release {event.key}")


    screen.fill(BACKGROUND)
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
