from all_colors import*
import pygame
pygame.init()
size = (800, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Моя Игра')
BACKGROUND = (255, 255, 0)
screen.fill(BACKGROUND)
FPS = 60
clock = pygame.time.Clock()
running = True

r = pygame.Rect(0, 0, 400, 200)
r.center = screen.get_rect().center
pygame.draw.rect(screen, GREEN, r)

my_surface = pygame.Surface((200, 100))
my_surface.fill(WHITE)
pygame.draw.circle(my_surface, RED, (100, 50), 40)

my_surface.set_colorkey((WHITE)) # прозрачный белый
my_surface.set_alpha(128)

# screen.blit(my_surface, (400, 300))


my_rect = my_surface.get_rect()
my_rect.center = (400,300)
screen.blit(my_surface, my_rect)



while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False



    # screen.fill(BACKGROUND)
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
