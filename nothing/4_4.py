#добавить звуки
#при отскоке от ракетки скорость увеличится
#отображение скорости мяча
#завершить игру
#и вообще все сделает дима

from all_colors import*
import pygame, sys
pygame.init()
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 720
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('GPT PIN-PONG')

PADDLE_WIDTH = 25
PADDLE_HEIGHT = 100
PADDLE_SPEED = 10

BALL_SIZE = 20
BALL_SPEED_X = 7
BALL_SPEED_Y = 7

paddle1_rect = pygame.Rect(0, SCREEN_HEIGHT//2 - PADDLE_HEIGHT//2,
                           PADDLE_WIDTH, PADDLE_HEIGHT)

paddle2_rect = pygame.Rect(SCREEN_WIDTH - PADDLE_WIDTH,
                           SCREEN_HEIGHT//2 - PADDLE_HEIGHT//2,
                           PADDLE_WIDTH, PADDLE_HEIGHT)

ball_rect = pygame.Rect(SCREEN_WIDTH//2 - BALL_SIZE//2,
                        SCREEN_HEIGHT//2 - BALL_SIZE//2,
                        BALL_SIZE, BALL_SIZE)

score1 = 0
score2 = 0

font = pygame.font.SysFont("Impact", 32)



FPS = 60
clock = pygame.time.Clock()
running = True

aim_mode =True

if len(sys.argv) > 1:
    if sys.argv[1] == '--human':
        aim_mode = False


def update_aim():
    if ball_rect.x > SCREEN_WIDTH // 2:
        if ball_rect.centery < paddle2_rect.centery:
            paddle2_rect.y -= PADDLE_SPEED
        elif ball_rect.centery > paddle2_rect.centery:
            paddle2_rect.y += PADDLE_SPEED

        if paddle2_rect.top < 0:
            paddle2_rect.top = 0
        if paddle2_rect.bottom > SCREEN_HEIGHT:
            paddle2_rect.bottom = SCREEN_HEIGHT
    else:
        paddle2_rect.centery += (SCREEN_HEIGHT // 2 - paddle2_rect.centery) / PADDLE_SPEED

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, WHITE, paddle1_rect)
    pygame.draw.rect(screen, WHITE, paddle2_rect)
    pygame.draw.line(screen, WHITE, (SCREEN_WIDTH//2, 0), (SCREEN_WIDTH//2, SCREEN_HEIGHT))
    pygame.draw.ellipse(screen, WHITE, ball_rect)

    score_text = font.render(f'{score1}  {score2}', True, WHITE)
    screen.blit(score_text,(SCREEN_WIDTH//2 -score_text.get_width() //2, 10))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        paddle1_rect.y -= PADDLE_SPEED
        if paddle1_rect.top <= 0:
            paddle1_rect.top = 0
    if keys[pygame.K_s]:
        paddle1_rect.y += PADDLE_SPEED
        if paddle1_rect.bottom >= SCREEN_HEIGHT:
            paddle1_rect.bottom = SCREEN_HEIGHT
    if not aim_mode:
        if keys[pygame.K_UP]:
            paddle2_rect.y -= PADDLE_SPEED
            if paddle2_rect.top <= 0:
                paddle2_rect.top = 0
        if keys[pygame.K_DOWN]:
            paddle2_rect.y += PADDLE_SPEED
            if paddle2_rect.bottom >= SCREEN_HEIGHT:
                paddle2_rect.bottom = SCREEN_HEIGHT
    else: update_aim()

    ball_rect.x += BALL_SPEED_X
    ball_rect.y += BALL_SPEED_Y

    if ball_rect.y >= SCREEN_HEIGHT or ball_rect.y <= 0:
        BALL_SPEED_Y = -BALL_SPEED_Y

    #ЕСЛИ ПОВЕРХНОСТЬ МЯЧА СТОЛКНУЛАСЬ С ПОВЕРХНОСТЬЮ ПЕРВОЙ РАКЕТКИ ИЛИ
    #ПОВЕРХНОСТЬ МЯЧА СТОЛКНУЛАСЬ С ПОВЕРХНОСТЬЮ 2 РАКЕТКИ: СКОРОСТЬ МЯЧА
    #ПО ОСИ X УМНОЖИТЬ НА -1

    if paddle1_rect.colliderect(ball_rect) or paddle2_rect.colliderect(ball_rect):
        BALL_SPEED_X *= -1

    if ball_rect.left >= SCREEN_WIDTH or ball_rect.right <= 0:
        ball_rect.x = SCREEN_WIDTH // 2
        ball_rect.y = SCREEN_HEIGHT // 2










    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()




