from all_colors import *  # Предположим, этот модуль содержит нужные цвета
import pygame.mixer
pygame.mixer.init()
import pygame
pygame.init()

# Настройки окна
size = (1280, 720)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Моя Игра')
BACKGROUND = (255, 255, 255)
screen.fill(BACKGROUND)
screen_rect = screen.get_rect()

# Корабль (синий квадрат)
ship = pygame.Rect(300, 200, 50, 100)
ship.right = screen_rect.right  # Корабль будет справа
ship.centery = screen_rect.centery  # Корабль по центру вертикально

# Ракета (маленький красный квадрат)
missile = pygame.Rect(50, 50, 10, 10)
missile.left = screen_rect.left  # Ракета слева
missile.centery = screen_rect.centery  # Ракета по центру вертикально

# Скорости ракеты и корабля
missile_speed_x = 0
missile_speed_y = 0
ship_speed_y = 2  # Скорость вертикального движения корабля

# Флаги состояния игры
ship_alive = True  # Жив ли корабль?
missile_alive = True  # Жив ли ракета?
missile_launched = False  # Запущена ли ракета?

# Здоровье корабля
hp_ship = 1

# Частота кадров
FPS = 60
clock = pygame.time.Clock()

# Основная логика игры
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not missile_launched:
                missile_launched = True
                missile_speed_x = 3  # Ракета летит вправо
                missile_speed_y = 0  # Нет вертикальной скорости

    # Движения корабля
    if ship_alive:
        ship.move_ip(0, ship_speed_y)  # Корабль движется вверх/вниз

        # Изменение направления движения корабля при достижении границ
        if ship.top <= 0 or ship.bottom >= screen_rect.bottom:
            ship_speed_y *= -1  # Меняем направление движения

    # Движение ракеты
    if missile_alive:
        missile.move_ip(missile_speed_x, missile_speed_y)

    # Проверка столкновения ракеты с кораблем
    if missile.collidepoint(ship.center):
        print("Попал!")
        ship_alive = False  # Корабль разрушен
        missile_alive = False  # Ракета исчезает

    # Рисование фона и объектов
    screen.fill(BACKGROUND)
    if ship_alive:
        pygame.draw.rect(screen, BLUE, ship)  # Отображаем корабль
    if missile_alive:
        pygame.draw.rect(screen, RED, missile)  # Отображаем ракету

    # Обновляем экран
    pygame.display.flip()

    # Ограничение частоты кадров
    clock.tick(FPS)

# Завершение работы Pygame
pygame.quit()