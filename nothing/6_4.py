def draw_pallate():
    pallete.fill(background_color)
    for i in range(12):
        color_rect = pygame.Rect(i * size, 0, size, size)
        pygame.draw.rect(pallete, COLORS[i], color_rect)
    border_rect = pygame.Rect(CUR_INDEX * size, 0, size, size)
    pygame.draw.rect(pallete, border_color, border_rect, width=3)
    screen.blit(pallete, pallete_rect.topleft)

from all_colors import*
import pygame
pygame.init()
size = (800, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('рисовалка')
background_color = (255, 255, 255)
FPS = 60
size = 50
brush_color = (0, 0, 0)
brush_width = 30
border_color = (0, 0, 0)
CUR_INDEX = 0
clock = pygame.time.Clock()
running = True
canvas = pygame.Surface(screen.get_size())
canvas.fill(background_color)
pallete_rect = pygame.Rect(10, 10, size * 12, size)
pallete = pygame.Surface(pallete_rect.size)
pallete.fill(background_color)
dragging_pallete = False
for i in range(12):
    color_rect = pygame.Rect(i * size, 0, size, size)
    pygame.draw.rect(pallete, COLORS[i], color_rect)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONUP and event.button == 3:
            print('asd')
            dragging_pallete = False


        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
            if pallete_rect.collidepoint(event.pos):
                print('potashili')
                dragging_pallete = True
                offset = (event.pos[0] - pallete_rect.left,
                          event.pos[1] - pallete_rect.top)
            else:
                pygame.draw.circle(canvas, brush_color, mouse_pos, brush_width)

        if dragging_pallete:
            new_pos = (mouse_pos[0] - offset[0],
                       mouse_pos[1] - offset[1])
            pallete_rect.topleft = new_pos

    mouse_pos = pygame.mouse.get_pos()
    mouse_pressed = pygame.mouse.get_pressed()
    if mouse_pressed[0]:
        print(mouse_pos)
        if pallete_rect.collidepoint(mouse_pos):
            selected_color_index = ((mouse_pos[0] - pallete_rect.left) // size)
            CUR_INDEX = selected_color_index
            brush_color = COLORS[CUR_INDEX]
        else:
          pygame.draw.circle(canvas, brush_color, mouse_pos, brush_width)






    screen.blit(canvas, (0,0))
    screen.blit(pallete, (0,0))
    pygame.display.flip()
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
