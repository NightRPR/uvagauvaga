import pygame
import sys
import random

pygame.mixer.init()
pygame.font.init()
channel0 = pygame.mixer.Channel(0)
channel1 = pygame.mixer.Channel(1)

image_pers_right = pygame.image.load("gg_right.png")
image_pers_right = pygame.transform.scale(image_pers_right,
                                          (image_pers_right.get_width() // 13, image_pers_right.get_height() // 13))
image_pers_left = pygame.image.load("gg_left.png")
image_pers_left = pygame.transform.scale(image_pers_left,
                                         (image_pers_left.get_width() // 13, image_pers_left.get_height() // 13))
image_mob1_right = pygame.image.load("mob1_right.png")
image_mob1_right = pygame.transform.scale(image_mob1_right,
                                          (image_mob1_right.get_width() // 6, image_mob1_right.get_height() // 6))
image_mob1_left = pygame.image.load("mob1_left.png")
image_mob1_left = pygame.transform.scale(image_mob1_left,
                                         (image_mob1_left.get_width() // 6, image_mob1_left.get_height() // 6))
image_mob2_right = pygame.image.load("mob2_right.png")
image_mob2_right = pygame.transform.scale(image_mob2_right,
                                          (image_mob2_right.get_width() // 7, image_mob2_right.get_height() // 7))
image_mob2_left = pygame.image.load("mob2_left.png")
image_mob2_left = pygame.transform.scale(image_mob2_left,
                                         (image_mob2_left.get_width() // 7, image_mob2_left.get_height() // 7))
image_logo = pygame.image.load("pooj.jpg")
image_logo = pygame.transform.scale(image_logo, (image_logo.get_width() // 3, image_logo.get_height() // 3))
image_pause = pygame.image.load('pause_bg.png')
image_fight = pygame.image.load("fight.png")
image_fight = pygame.transform.scale(image_fight, (image_fight.get_width() // 2, image_fight.get_height() // 2))
image_win = pygame.image.load("you_won.png")
image_lose = pygame.image.load("you_died.png")
image_lose = pygame.transform.scale(image_lose, (image_lose.get_width() // 2, image_lose.get_height() // 2))

image_key = pygame.image.load('key.png')
image_key = pygame.transform.scale(image_key, (image_key.get_width() // 4, image_key.get_height() // 4))
image_coin = pygame.image.load('coin.png')
image_coin = pygame.transform.scale(image_coin, (image_coin.get_width() // 10, image_coin.get_height() // 10))
image_wall = pygame.image.load("wall.png")

image_wall = pygame.transform.scale(image_wall, (image_wall.get_width() // 1, image_wall.get_height() // 1))
image_door = pygame.image.load("door.png")
image_door = pygame.transform.scale(image_door, (image_door.get_width() // 4, image_door.get_height() // 4))

bg1 = pygame.image.load("pol1.png")
bg1 = pygame.transform.scale(bg1, (bg1.get_width() // 1, bg1.get_height() // 1))

music_logo = pygame.mixer.Sound('volvo.mp3')
music_logo.set_volume(0.2)
music_gachi_logo = pygame.mixer.Sound('Oh yes sir.mp3')
music_door_open = pygame.mixer.Sound('door.mp3')
music_room1 = pygame.mixer.Sound('rooms.mp3')
music_room1.set_volume(0.6)
music_room2 = pygame.mixer.Sound('dungeon.mp3')
music_items = pygame.mixer.Sound('Dungeon master.mp3')
music_fight = pygame.mixer.Sound('fight.mp3')
music_fight.set_volume(0.5)


class Pers(pygame.sprite.Sprite):
    def __init__(self, x, y, filename):
        pygame.sprite.Sprite.__init__(self)
        self.image = filename
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = [0, 0]

    def update(self):
        if self.rect.right > WIDTH:
            if self.speed[0] > 0:
                self.speed[0] = 0
        if self.rect.left < 0:
            if self.speed[0] < 0:
                self.speed[0] = 0
        if self.rect.bottom > HEIGHT:
            if self.speed[1] > 0:
                self.speed[1] = 0
        if self.rect.top < 0:
            if self.speed[1] < 0:
                self.speed[1] = 0
        if self.speed[0] != 0 and self.speed[1] != 0:
            self.rect.x += 5 * self.speed[0] // player_speed
            self.rect.y += 5 * self.speed[1] // player_speed
        else:
            self.rect.x += self.speed[0]
            self.rect.y += self.speed[1]


class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, filename):
        pygame.sprite.Sprite.__init__(self)
        self.image = filename
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = [enemy_speed, 0]
        self.check_allive = True

    def update(self):
        if self.rect.right > WIDTH:
            self.speed[0] *= -1
        if self.rect.left < 0:
            self.speed[0] *= -1
        if self.rect.bottom > HEIGHT:
            self.speed[1] *= -1
        if self.rect.top < 0:
            self.speed[1] *= -1
        self.rect.x += self.speed[0]
        self.rect.y += self.speed[1]


class Item(pygame.sprite.Sprite):
    def __init__(self, x, y, filename):
        pygame.sprite.Sprite.__init__(self)
        self.image = filename
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.check_used = False


class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y, filename):
        pygame.sprite.Sprite.__init__(self)
        self.image = filename
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Door(pygame.sprite.Sprite):
    def __init__(self, x, y, filename):
        pygame.sprite.Sprite.__init__(self)
        self.image = filename
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Button:
    def __init__(self, x=None, y=None, wdth=None, hght=None, color=(0, 0, 0), border=0, font='Calibri', text_size=50,
                 text=None):
        self.color = color
        self.x = x
        self.y = y
        self.width = wdth
        self.height = hght
        self.font = font
        self.text_size = text_size
        self.text = text
        self.border = border

    def check_motion(self, screen, event, color):
        if event.type == pygame.MOUSEMOTION:
            x, y = event.pos
            global cnt
            if x >= self.x and x <= self.x + self.width and y >= self.y and y <= self.y + self.height:
                self.color = (255, 255, 255)
                self.process_draw(screen)
                cnt = 1
            else:
                self.color = color
                self.process_draw(screen)
                cnt = 0
            if cnt == 0:
                cnt = 1

    def process_draw(self, screen):
        pygame.font.init()
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height), self.border)
        font = pygame.font.SysFont(self.font, self.text_size, True)
        data = self.text
        ts = font.render(data, False, black)
        screen.blit(ts, (self.x - 1, self.y))


class Target:
    def __init__(self, x=None, y=None, color=(255, 0, 0), R=50):
        self.color = color
        self.x = x
        self.y = y
        self.R = R

    def process_draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.R)


WIDTH = 1500
HEIGHT = 900
size = WIDTH, HEIGHT
white = (255, 255, 255)
black = (0, 0, 0)
player_speed = 8
enemy_speed = 7
cell_size = 50


def read_field1():
    f = open('field1.txt', 'r')
    data = f.readlines()
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == '1':
                w = Wall(j * cell_size, i * cell_size, image_wall)
                walls1.add(w)
            if data[i][j] == '@':
                player.rect.x, player.rect.y = j * cell_size, i * cell_size
            if data[i][j] == 'k':
                key.rect.x, key.rect.y = j * cell_size, i * cell_size
            if data[i][j] == 'c':
                coin.rect.x, coin.rect.y = j * cell_size, i * cell_size
            if data[i][j] == 'e':
                enemy1.rect.x, enemy1.rect.y = j * cell_size, i * cell_size
            if data[i][j] == 'd':
                door1.rect.x, door1.rect.y = j * cell_size, i * cell_size


def read_field2():
    f = open('field2.txt', 'r')
    data = f.readlines()
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == '1':
                w = Wall(j * cell_size, i * cell_size, image_wall)
                walls2.add(w)
            if data[i][j] == '@':
                player.rect.x, player.rect.y = j * cell_size, i * cell_size
            if data[i][j] == 'k':
                key.rect.x, key.rect.y = j * cell_size, i * cell_size
            if data[i][j] == 'c':
                coin.rect.x, coin.rect.y = j * cell_size, i * cell_size
            if data[i][j] == 'e':
                enemy2.rect.x, enemy2.rect.y = j * cell_size, i * cell_size
            if data[i][j] == 'd':
                door2.rect.x, door2.rect.y = j * cell_size, i * cell_size


key = Item(0, 0, image_key)
coin = Item(0, 0, image_coin)
door1 = Door(0, 0, image_door)
door2 = Door(0, 0, image_door)
player = Pers(0, 0, image_pers_right)
enemy1 = Enemy(0, 0, image_mob1_right)
enemy2 = Enemy(0, 0, image_mob2_right)

items1 = pygame.sprite.Group()
items1.add(key)
items2 = pygame.sprite.Group()
items2.add(coin)
walls1 = pygame.sprite.Group()
walls2 = pygame.sprite.Group()
doors1 = pygame.sprite.Group()
doors1.add(door1)
doors2 = pygame.sprite.Group()
doors2.add(door2)
enemies1 = pygame.sprite.Group()
enemies1.add(enemy1)
enemies2 = pygame.sprite.Group()
enemies2.add(enemy2)


def check_items_exists1(*it):
    for i in it:
        if i not in items1:
            i.check_used = True


def check_collide1(enemy_im_l, enemy_im_r):
    f = open('field1.txt', 'r')
    data = f.readlines()
    xz = pygame.sprite.spritecollide(player, enemies1, True)
    u = pygame.sprite.spritecollide(player, items1, True)
    # if u:
    #    channel1 = pygame.mixer.Channel(1)
    #    channel1.play(music_items)

    player_and_walls_hit_list = pygame.sprite.spritecollide(player, walls1, False)
    enemy_and_walls_hit_list = pygame.sprite.spritecollide(enemy1, walls1, False)
    for w in player_and_walls_hit_list:
        if player.rect.bottom >= w.rect.top and player.rect.bottom <= w.rect.top + 15:
            if player.rect.right > w.rect.left:
                player.rect.bottom = w.rect.top
        elif player.rect.top <= w.rect.bottom and player.rect.top >= w.rect.bottom - 15:
            player.rect.top = w.rect.bottom
        if player.rect.right >= w.rect.left and player.rect.right <= w.rect.left + 15:
            if player.rect.bottom > w.rect.top + 15:
                player.rect.right = w.rect.left
        elif player.rect.left <= w.rect.right and player.rect.left >= w.rect.right - 15:
            player.rect.left = w.rect.right

    for w in enemy_and_walls_hit_list:
        tr = [0, 1, 2, 3]
        j = enemy1.rect.x // 50 + 1
        i = enemy1.rect.y // 50 + 1
        # print(i, j)
        if enemy1.rect.bottom >= w.rect.top and enemy1.rect.bottom <= w.rect.top + 7:
            if enemy1.rect.right > w.rect.left:
                # enemy1.speed[1] *= -1
                enemy1.rect.bottom = w.rect.top - 10
                del tr[2]
                if data[i][j - 1] == '1':
                    del tr[1]
                if data[i][j + 1] == '1':
                    del tr[0]
                # print('down')
        elif enemy1.rect.top <= w.rect.bottom and enemy1.rect.top >= w.rect.bottom - 7:
            # enemy1.speed[1] *= -1
            enemy1.rect.top = w.rect.bottom + 10
            del tr[3]
            if data[i][j - 1] == '1':
                del tr[1]
            if data[i][j + 1] == '1':
                del tr[0]
            # print('up')
        elif enemy1.rect.right >= w.rect.left and enemy1.rect.right <= w.rect.left + 7:
            if enemy1.rect.bottom > w.rect.top:
                # enemy1.speed[0] *= -1
                enemy1.rect.right = w.rect.left - 10
                if data[i - 1][j] == '1':
                    del tr[3]
                if data[i + 1][j] == '1':
                    del tr[2]
                del tr[0]
                # print('right')
        elif enemy1.rect.left <= w.rect.right and enemy1.rect.left >= w.rect.right - 7:
            # enemy1.speed[0] *= -1
            enemy1.rect.left = w.rect.right + 10
            if data[i - 1][j] == '1':
                del tr[3]
            if data[i + 1][j] == '1':
                del tr[2]
            del tr[1]
            # print('left')
        y = random.choice(tr)
        # print(tr)
        # print(y)
        if y == 0:
            enemy1.speed = [enemy_speed, 0]
            enemy1.image = enemy_im_l
        elif y == 1:
            enemy1.speed = [-enemy_speed, 0]
            enemy1.image = enemy_im_r
        elif y == 2:
            enemy1.speed = [0, enemy_speed]
        else:
            enemy1.speed = [0, -enemy_speed]
        break

    if pygame.sprite.collide_rect(player, door1):
        if key.check_used:
            channel1 = pygame.mixer.Channel(1)
            channel1.play(music_door_open)
            room2()
        else:
            if player.rect.bottom >= door1.rect.top and player.rect.bottom <= door1.rect.top + 15:
                if player.rect.right > door1.rect.left:
                    player.rect.bottom = door1.rect.top
            elif player.rect.top <= door1.rect.bottom and player.rect.top >= door1.rect.bottom - 15:
                player.rect.top = door1.rect.bottom
            if player.rect.right >= door1.rect.left and player.rect.right <= door1.rect.left + 15:
                if player.rect.bottom > door1.rect.top + 15:
                    player.rect.right = door1.rect.left
            elif player.rect.left <= door1.rect.right and player.rect.left >= door1.rect.right - 15:
                player.rect.left = door1.rect.right

    if pygame.sprite.collide_rect(player, enemy1):
        if enemy1.check_allive == True:
            if fight() == 1:
                enemy1.check_allive = False
            else:
                game_over()


def draw_all1(screen):
    screen.blit(bg1.convert(), (0, 0))
    screen.blit(player.image, player.rect)
    doors1.draw(screen)
    items1.draw(screen)
    walls1.draw(screen)
    if enemy1.check_allive == True:
        enemies1.draw(screen)


def check_items_exists2(*it):
    for i in it:
        if i not in items2:
            i.check_used = True


def check_collide2(enemy_im_l, enemy_im_r):
    f = open('field2.txt', 'r')
    data = f.readlines()
    xz = pygame.sprite.spritecollide(player, enemies2, True)
    u = pygame.sprite.spritecollide(player, items2, True)
    # if u:
    #    channel1 = pygame.mixer.Channel(1)
    #    channel1.play(music_items)
    player_and_walls_hit_list = pygame.sprite.spritecollide(player, walls2, False)
    enemy_and_walls_hit_list = pygame.sprite.spritecollide(enemy2, walls2, False)
    for w in player_and_walls_hit_list:
        if player.rect.bottom >= w.rect.top and player.rect.bottom <= w.rect.top + 15:
            if player.rect.right > w.rect.left:
                player.rect.bottom = w.rect.top
        elif player.rect.top <= w.rect.bottom and player.rect.top >= w.rect.bottom - 15:
            player.rect.top = w.rect.bottom
        if player.rect.right >= w.rect.left and player.rect.right <= w.rect.left + 15:
            if player.rect.bottom > w.rect.top + 15:
                player.rect.right = w.rect.left
        elif player.rect.left <= w.rect.right and player.rect.left >= w.rect.right - 15:
            player.rect.left = w.rect.right

    for w in enemy_and_walls_hit_list:
        tr = [0, 1, 2, 3]
        j = enemy2.rect.x // 50 + 1
        i = enemy2.rect.y // 50 + 1
        # print(i, j)
        if enemy2.rect.bottom >= w.rect.top and enemy2.rect.bottom <= w.rect.top + 7:
            if enemy2.rect.right > w.rect.left:
                # enemy2.speed[1] *= -1
                enemy2.rect.bottom = w.rect.top - 10
                del tr[2]
                if data[i][j - 1] == '1':
                    del tr[1]
                if data[i][j + 1] == '1':
                    del tr[0]
                # print('down')
        elif enemy2.rect.top <= w.rect.bottom and enemy2.rect.top >= w.rect.bottom - 7:
            # enemy2.speed[1] *= -1
            enemy2.rect.top = w.rect.bottom + 10
            del tr[3]
            if data[i][j - 1] == '1':
                del tr[1]
            if data[i][j + 1] == '1':
                del tr[0]
            # print('up')
        elif enemy2.rect.right >= w.rect.left and enemy2.rect.right <= w.rect.left + 7:
            if enemy2.rect.bottom > w.rect.top:
                # enemy2.speed[0] *= -1
                enemy2.rect.right = w.rect.left - 10
                if data[i - 1][j] == '1':
                    del tr[3]
                if data[i + 1][j] == '1':
                    del tr[2]
                del tr[0]
                # print('right')
        elif enemy2.rect.left <= w.rect.right and enemy2.rect.left >= w.rect.right - 7:
            # enemy2.speed[0] *= -1
            enemy2.rect.left = w.rect.right + 10
            if data[i - 1][j] == '1':
                del tr[3]
            if data[i + 1][j] == '1':
                del tr[2]
            del tr[1]
            # print('left')
        y = random.choice(tr)
        # print(tr)
        # print(y)
        if y == 0:
            enemy2.speed = [enemy_speed, 0]
            enemy2.image = enemy_im_l
        elif y == 1:
            enemy2.speed = [-enemy_speed, 0]
            enemy2.image = enemy_im_r
        elif y == 2:
            enemy2.speed = [0, enemy_speed]
        else:
            enemy2.speed = [0, -enemy_speed]
        break

    if pygame.sprite.collide_rect(player, door2):
        if coin.check_used:
            win()
        else:
            if player.rect.bottom >= door2.rect.top and player.rect.bottom <= door2.rect.top + 15:
                if player.rect.right > door2.rect.left:
                    player.rect.bottom = door2.rect.top
            elif player.rect.top <= door2.rect.bottom and player.rect.top >= door2.rect.bottom - 15:
                player.rect.top = door2.rect.bottom
            if player.rect.right >= door2.rect.left and player.rect.right <= door2.rect.left + 15:
                if player.rect.bottom > door2.rect.top + 15:
                    player.rect.right = door2.rect.left
            elif player.rect.left <= door2.rect.right and player.rect.left >= door2.rect.right - 15:
                player.rect.left = door2.rect.right

    if pygame.sprite.collide_rect(player, enemy2):
        if enemy2.check_allive == True:
            if fight() == 1:
                enemy2.check_allive = False
            else:
                game_over()


def draw_all2(screen):
    screen.blit(bg1.convert(), (0, 0))
    screen.blit(player.image, player.rect)
    doors2.draw(screen)
    items2.draw(screen)
    walls2.draw(screen)
    enemies2.draw(screen)


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
    pygame.mouse.set_cursor(*pygame.cursors.load_xbm('pcur.xbm', 'pcur.xbm'))
    player.speed = [0, 0]

    while not gameover:
        pygame.mouse.set_visible(True)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if continue_button.x <= x <= continue_button.x + continue_button.width and continue_button.y <= y <= continue_button.y + continue_button.height:
                    gameover = True
                    channel0.unpause()
                    pygame.mixer.music.stop()
                elif restart_button.x <= x <= restart_button.x + restart_button.width and restart_button.y <= y <= restart_button.y + restart_button.height:
                    gameover = True
                    enemy1.check_allive = True
                    enemy2.check_allive = True
                    key.check_used = False
                    coin.check_used = False
                    enemies1.add(enemy1)
                    enemies2.add(enemy2)
                    items1.add(key)
                    items2.add(coin)
                    pygame.mixer.music.stop()
                    menu()
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
                    menu()
        u = pygame.time.get_ticks()
        if 6500 < u < 6750:
            channel0.play(music_gachi_logo)
        screen.blit(image_logo, (625, 300))
        pygame.display.flip()
        pygame.time.wait(10)
    menu()


def menu():
    screen = pygame.display.set_mode(size)
    gameover = False

    start_button = Button(WIDTH - 400, 150, 276, 50, (218, 247, 166), 0, 'Calibri', 50, '         play')
    quit_button = Button(WIDTH - 400, 205, 276, 50, (255, 87, 51), 0, 'Calibri', 50, '        quit')
    pygame.mouse.set_cursor(*pygame.cursors.load_xbm('pcur.xbm', 'pcur.xbm'))
    pygame.mouse.set_visible(True)
    while not gameover:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if x >= start_button.x and x <= start_button.x + start_button.width and y >= start_button.y and y <= start_button.y + start_button.height:
                    gameover = True
                    room1()
                elif x >= quit_button.x and x <= quit_button.x + quit_button.width and y >= quit_button.y and y <= quit_button.y + quit_button.height:
                    gameover = True
                    sys.exit()
            elif event.type == pygame.MOUSEMOTION:
                x, y = event.pos
                if x >= start_button.x and x <= start_button.x + start_button.width and y >= start_button.y and y <= start_button.y + start_button.height:
                    start_button.border = 5
                    start_button.process_draw(screen)
                else:
                    start_button.border = 0
                    start_button.process_draw(screen)
                if x >= quit_button.x and x <= quit_button.x + quit_button.width and y >= quit_button.y and y <= quit_button.y + quit_button.height:
                    quit_button.border = 5
                    quit_button.process_draw(screen)
                else:
                    quit_button.border = 0
                    quit_button.process_draw(screen)
            if event.type == pygame.QUIT:
                gameover = True
            screen.blit(image_pause, (0, 0))
            start_button.process_draw(screen)
            quit_button.process_draw(screen)
            pygame.display.flip()
            pygame.time.wait(10)
    sys.exit()


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


def fight():
    channel0.pause()
    channel1.play(music_fight)
    pygame.mouse.set_cursor(*pygame.cursors.broken_x)
    a = pygame.mixer.music.get_pos()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.time.set_timer(pygame.USEREVENT, 5000)
    gameover = False
    check = False
    cnt = 0
    target = Target(WIDTH // 2, HEIGHT // 2)
    pygame.mouse.set_visible(True)
    while not gameover:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if ((x - target.x) ** 2 + (y - target.y) ** 2) ** 0.5 <= target.R:
                    target.x, target.y = random.randint(200, WIDTH - 200), random.randint(300, HEIGHT - 200)
                    cnt += 1
                    pygame.mixer.music.load('oof.mp3')
                    pygame.mixer.music.play()
                    pygame.time.delay(200)
            if cnt >= 5:
                check = True
                gameover = True
                channel1.stop()
                channel0.unpause()
            if event.type == pygame.USEREVENT:
                gameover = True
        screen.fill(black)
        screen.blit(image_fight, (WIDTH // 2 - 170, 50))
        target.process_draw(screen)
        pygame.display.flip()
        pygame.time.wait(10)

    player.speed = [0, 0]
    return check


def game_over():
    channel1.stop()
    screen = pygame.display.set_mode(size)
    gameover = False
    channel0.pause()
    pygame.mouse.set_cursor(*pygame.cursors.diamond)
    pygame.mixer.music.load('lol.mp3')
    pygame.mixer.music.play()
    pygame.time.delay(500)
    key.check_used = 0
    coin.check_used = 0
    exit_button = Button((WIDTH // 2) - 75, (HEIGHT // 2) + 35, 150, 50, (255, 0, 0), 0, 'Calibri', 50, 'Выйти')
    restart_button = Button((WIDTH // 2) - 75, (HEIGHT // 2) - 25, 150, 50, (255, 0, 0), 0, 'Calibri', 50, 'Заново')
    enemy1.check_allive = True
    enemy2.check_allive = True
    enemies1.add(enemy1)
    enemies2.add(enemy2)
    items1.add(key)
    items2.add(coin)
    player.speed = [0, 0]

    while not gameover:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if x >= exit_button.x and x <= exit_button.x + exit_button.width and y >= exit_button.y and y <= exit_button.y + exit_button.height:
                    gameover = True
                elif x >= restart_button.x and x <= restart_button.x + restart_button.width and y >= restart_button.y and y <= restart_button.y + restart_button.height:
                    pygame.mixer.music.stop()
                    menu()
            exit_button.check_motion(screen, event, (255, 0, 0))
            restart_button.check_motion(screen, event, (255, 0, 0))
            if event.type == pygame.QUIT:
                gameover = True

            screen.fill(black)
            screen.blit(image_lose, (WIDTH // 2 - 300, 0))
            exit_button.process_draw(screen)
            restart_button.process_draw(screen)
            pygame.display.flip()
            pygame.time.wait(10)
    sys.exit()


def win():
    channel1.stop()
    pygame.mouse.set_visible(True)
    # pygame.mouse.set_cursor(*pygame.cursors.load_xbm('wcur.xbm', 'wcur.xbm'))
    channel0.stop()
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load('win.mp3')
    pygame.mixer.music.play()
    screen = pygame.display.set_mode(size)
    gameover = False
    key.check_used = 0
    coin.check_used = 0
    exit_button = Button((WIDTH // 2) - 90, (HEIGHT // 2) - 35, 150, 50, (0, 0, 255), 0, 'Calibri', 50, 'Выйти')
    restart_button = Button((WIDTH // 2) - 95, (HEIGHT // 2) + 25, 160, 50, (0, 0, 255), 0, 'Calibri', 50, 'Заново')
    enemy1.check_allive = True
    enemy2.check_allive = True
    enemies1.add(enemy1)
    enemies2.add(enemy2)
    items1.add(key)
    items2.add(coin)
    player.speed = [0, 0]

    while not gameover:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if x >= exit_button.x and x <= exit_button.x + exit_button.width and y >= exit_button.y and y <= exit_button.y + exit_button.height:
                    gameover = True
                elif x >= restart_button.x and x <= restart_button.x + restart_button.width and y >= restart_button.y and y <= restart_button.y + restart_button.height:
                    menu()
            exit_button.check_motion(screen, event, (0, 0, 255))
            restart_button.check_motion(screen, event, (0, 0, 255))
            if event.type == pygame.QUIT:
                gameover = True
            screen.fill((255, 255, 255))
            screen.blit(image_win, (WIDTH // 2 - 276, HEIGHT // 2 - 120))
            exit_button.process_draw(screen)
            restart_button.process_draw(screen)
            pygame.display.flip()
            pygame.time.wait(10)
    sys.exit()
    room2()


if __name__ == '__main__':
    logo()
