import pygame
<<<<<<< HEAD



pygame.init()


WIDTH, HEIGHT = 1920, 1080
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Полет самолета")


background = pygame.image.load("sky.png")
plane1 = pygame.image.load("plane1.png")
plane2 = pygame.image.load("plane2.png")

plane2 = pygame.image.load("plane2.png")


plane1_x, plane1_y = 100, 100
speed = 5


clock = pygame.time.Clock()


running = True
while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Движение первого самолета (клавиши)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and plane1_x > 0:
        plane1_x -= speed
    if keys[pygame.K_RIGHT] and plane1_x < WIDTH - plane1.get_width():
        plane1_x += speed
    if keys[pygame.K_UP] and plane1_y > 0:
        plane1_y -= speed
    if keys[pygame.K_DOWN] and plane1_y < HEIGHT - plane1.get_height():
        plane1_y += speed

    # Позиция второго самолета (мышь)
    mouse_x, mouse_y = pygame.mouse.get_pos()
    plane2_x = mouse_x - plane2.get_width() // 2
    plane2_y = mouse_y - plane2.get_height() // 2


    screen.blit(background, (0, 0))
    screen.blit(plane1, (plane1_x, plane1_y))
    screen.blit(plane2, (plane2_x, plane2_y))

    pygame.display.flip()


pygame.quit()
=======
pygame.init()
size = (1280, 720)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('рисование линий')
BACKGROUND = (0, 0, 0)
screen.fill(BACKGROUND)
FPS = 60
clock = pygame.time.Clock()
running = True

points = []

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            points.append(event.pos)

        for i in range (len(points) -1):
            start_point = points[i]
            end_point = points[i + 1]
            pygame.draw.line(screen, (255, 255, 255), start_point, end_point, 3)





    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
>>>>>>> c5cb33f2468db3d1c9dc8539981cfb1894e2b1a7
