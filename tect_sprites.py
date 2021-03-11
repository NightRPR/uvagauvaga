import pygame
import sys
from files import *
from classes import *
from defenitions import *

channel0 = pygame.mixer.Channel(0)
pygame.mixer.init()
pygame.font.init()

WIDTH = 1500
HEIGHT = 900
size = WIDTH, HEIGHT
white = (255, 255, 255)
black = (0, 0, 0)
player_speed = 7
enemy_speed = 5
cell_size = 50



def Pause():
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load('music_menu.mp3')
    pygame.mixer.music.play()
    screen = pygame.display.set_mode(size)
    gameover = False
    continue_button = Button(WIDTH - 400, 150, 276, 50, (218, 247, 166), 0, 'Calibri', 50, '    continue')
    restart_button = Button(WIDTH - 400, 205, 276, 50, (255, 87, 51), 0, 'Calibri', 50, '      restart')
    quit_button = Button(WIDTH - 400, 260, 276, 50, (144, 12, 63), 0, 'Calibri', 50, '        quit')
    pygame.mouse.set_cursor(*pygame.cursors.load_xbm('wcurs.xbm', 'wcurs.xbm'))

    while not gameover:
        pygame.mouse.set_visible(True)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if continue_button.x <= x <= continue_button.x + continue_button.width and continue_button.y <= y <= continue_button.y + continue_button.height:
                    gameover = True
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load('zvon.mp3')
                    pygame.mixer.music.play()
                    channel0.unpause()
                    pygame.time.delay(600)
                elif restart_button.x <= x <= restart_button.x + restart_button.width and restart_button.y <= y <= restart_button.y + restart_button.height:
                    gameover = True
                    enemy1.check_allive = True
                    enemy2.check_allive = True
                    key.check_used = False
                    coin.check_used = False
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load('zvon.mp3')
                    pygame.mixer.music.play()
                    pygame.time.delay(600)
                    room1()
                    sys.exit()
                elif quit_button.x <= x <= quit_button.x + quit_button.width and quit_button.y <= y <= quit_button.y + quit_button.height:
                    gameover = True
                    sys.exit()
            elif event.type == pygame.MOUSEMOTION:
                x, y = event.pos
                if continue_button.x <= x <= continue_button.x + continue_button.width and continue_button.y <= y <= continue_button.y + continue_button.height:
                    continue_button.border = 5
                    continue_button.process_draw(screen.convert())
                else:
                    continue_button.border = 0
                    continue_button.process_draw(screen.convert())

                if restart_button.x <= x <= restart_button.x + restart_button.width and restart_button.y <= y <= restart_button.y + restart_button.height:
                    restart_button.border = 5
                    restart_button.process_draw(screen.convert())
                else:
                    restart_button.border = 0
                    restart_button.process_draw(screen.convert())

                if quit_button.x <= x <= quit_button.x + quit_button.width and quit_button.y <= y <= quit_button.y + quit_button.height:
                    quit_button.border = 5
                    quit_button.process_draw(screen)
                else:
                    quit_button.border = 0
                    quit_button.process_draw(screen)

            if event.type == pygame.QUIT:
                gameover = True
                sys.exit()

            screen.blit(image_pause.convert(), (0, 0))
            restart_button.process_draw(screen)
            continue_button.process_draw(screen)
            quit_button.process_draw(screen)
            pygame.display.flip()
            pygame.time.wait(10)


def logo():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.time.set_timer(pygame.USEREVENT, 8000)
    gameover = False
    channel1 = pygame.mixer.Channel(1)
    channel0 = pygame.mixer.Channel(0)
    channel1.play(music_logo)
    font = pygame.font.SysFont('Algerian', 30, True)
    ts = font.render('pooj productions', False, white)
    screen.blit(ts, (595, 555))
    while not gameover:
        pygame.mouse.set_visible(False)
        for event in pygame.event.get():
            if event.type == pygame.USEREVENT:
                gameover = True
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    channel0.stop()
                    channel1.stop()
                    room1()
        u = pygame.time.get_ticks()
        if 6500 < u < 6750:
            channel0.play(music_gachi_logo)
        screen.blit(image_logo, (625, 300))
        pygame.display.flip()
        pygame.time.wait(10)
    room1()


def room1():
    # Считываем поле
    read_field1()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    channel0.play(music_room1)
    while 1:
        pygame.mouse.set_visible(False)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    player.speed[0] = -player_speed
                    player.image = image_pers_left
                elif event.key == pygame.K_d:
                    player.speed[0] = player_speed
                    player.image = image_pers_right
                elif event.key == pygame.K_w:
                    player.speed[1] = -player_speed
                elif event.key == pygame.K_s:
                    player.speed[1] = player_speed
                elif event.key == pygame.K_SPACE:
                    channel0.pause()
                    Pause()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_a and player.speed[0] == -player_speed:
                    player.speed[0] = 0
                elif event.key == pygame.K_d and player.speed[0] == player_speed:
                    player.speed[0] = 0
                elif event.key == pygame.K_w and player.speed[1] == -player_speed:
                    player.speed[1] = 0
                elif event.key == pygame.K_s and player.speed[1] == player_speed:
                    player.speed[1] = 0
        # print(coin.check_used)
        # Проверяем пересечение всего и вся
        check_collide1(image_mob1_right, image_mob1_left)

        # Проверяем, использованы ли предметы
        check_items_exists1(key)

        # Отрисовка
        draw_all1(screen)

        player.update()
        enemy1.update()
        pygame.display.update()
        pygame.time.delay(10)


def room2():
    channel0.play(music_room2)
    # Считываем поле
    read_field2()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    while 1:
        pygame.mouse.set_visible(False)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    player.speed[0] = -player_speed
                    player.image = image_pers_left
                elif event.key == pygame.K_d:
                    player.speed[0] = player_speed
                    player.image = image_pers_right
                elif event.key == pygame.K_w:
                    player.speed[1] = -player_speed
                elif event.key == pygame.K_s:
                    player.speed[1] = player_speed
                elif event.key == pygame.K_SPACE:
                    channel0.pause()
                    Pause()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_a and player.speed[0] == -player_speed:
                    player.speed[0] = 0
                elif event.key == pygame.K_d and player.speed[0] == player_speed:
                    player.speed[0] = 0
                elif event.key == pygame.K_w and player.speed[1] == -player_speed:
                    player.speed[1] = 0
                elif event.key == pygame.K_s and player.speed[1] == player_speed:
                    player.speed[1] = 0

        # print(coin.check_used)
        # Проверяем пересечение всего и вся
        check_collide2(image_mob2_right, image_mob2_left)

        # Проверяем, использованы ли предметы
        check_items_exists2(coin)

        # Отрисовка
        draw_all2(screen)

        player.update()
        enemy2.update()
        pygame.display.update()
        pygame.time.delay(10)


if __name__ == '__main__':
    logo()
