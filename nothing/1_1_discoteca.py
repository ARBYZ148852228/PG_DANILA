from all_colors import *
import random

# pygame.mixer.init()
# pygame.mixer.music.load('')
# pygame.mixer.music.play(-1)


pygame.init()
size = (1280, 720)
screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
pygame.display.set_caption('Discoteca')
BACKGROUND = (255, 255, 255)
screen.fill(BACKGROUND)
FPS = 0
clock = pygame.time.Clock()
running = True

COLORS = [BLACK, WHITE, RED, GREEN, BLUE, YELLOW, CYAN, MAGENTA,
          GRAY, ORANGE, PINK, BROWN,PURPLE, LIME, NAVY, OLIVE,
          MAROON, TEAL, SILVER, GOLD]

timer = 0





while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()
    clock.tick(FPS)
    if event.type == pygame.QUIT:
        running = False
    BACKGROUND = random.choice(COLORS)
    screen.fill(BACKGROUND)


    pygame.display.flip()

    pygame.time.delay(random.randint(200, 800))
    pygame.display.update()


pygame.quit()
