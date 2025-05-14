from all_colors import*
import pygame
pygame.init()
size = (800, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('рисовалка')
backgroun_color = (255, 255, 255)
FPS = 60
brush_color = (0, 0, 0)
brush_width = 5
clock = pygame.time.Clock()
running = True
canvas = pygame.Surface(screen.get_size())
canvas.fill(backgroun_color)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    mouse_pos = pygame.mouse.get_pos()

    pygame.draw.circle(canvas, brush_color, mouse_pos, brush_width)



    screen.blit(canvas, (0,0))
    pygame.display.flip()
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
