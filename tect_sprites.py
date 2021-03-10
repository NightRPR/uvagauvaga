import pygame
import sys
import random
from files import *
from classes import *
from defenitions import *
pygame.mixer.init()
pygame.font.init()

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
    channel0 = pygame.mixer.Channel(0)
    channel0.play(music_room1)
    while 1:
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

        #print(coin.check_used)
        #Проверяем пересечение всего и вся
        check_collide1(image_mob1_right, image_mob1_left)

        #Проверяем, использованы ли предметы
        check_items_exists1(key)

        #Отрисовка
        draw_all1(screen)

        player.update()
        enemy1.update()
        pygame.display.update()
        pygame.time.delay(10)


def Pause():
    exit(0)

def room2():
    channel0 = pygame.mixer.Channel(0)
    channel0.play(music_room2)
    #Считываем поле
    read_field2()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
        
    while 1:
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
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_a and player.speed[0] == -player_speed:
                    player.speed[0] = 0
                elif event.key == pygame.K_d and player.speed[0] == player_speed:
                    player.speed[0] = 0
                elif event.key == pygame.K_w and player.speed[1] == -player_speed:
                    player.speed[1] = 0
                elif event.key == pygame.K_s and player.speed[1] == player_speed:
                    player.speed[1] = 0

        #print(coin.check_used)
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