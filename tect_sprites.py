import pygame
import sys
import random

pygame.mixer.init()
pygame.font.init()

WIDTH = 1500
HEIGHT = 900
white = (255, 255, 255)
black = (0, 0, 0)
player_speed = 7
enemy_speed = 5
cell_size = 50


image_pers_right = pygame.image.load("gg_right.png")
image_pers_right = pygame.transform.scale(image_pers_right, (image_pers_right.get_width() // 13, image_pers_right.get_height() // 13))
image_pers_left = pygame.image.load("gg_left.png")
image_pers_left = pygame.transform.scale(image_pers_left, (image_pers_left.get_width() // 13, image_pers_left.get_height() // 13))
image_mob1_right = pygame.image.load("mob1_right.png")
image_mob1_right = pygame.transform.scale(image_mob1_right, (image_mob1_right.get_width() // 6, image_mob1_right.get_height() // 6))
image_mob1_left = pygame.image.load("mob1_left.png")
image_mob1_left = pygame.transform.scale(image_mob1_left, (image_mob1_left.get_width() // 6, image_mob1_left.get_height() // 6))
image_mob2_right = pygame.image.load("mob2_right.png")
image_mob2_right = pygame.transform.scale(image_mob2_right, (image_mob2_right.get_width() // 7, image_mob2_right.get_height() // 7))
image_mob2_left = pygame.image.load("mob2_left.png")
image_mob2_left = pygame.transform.scale(image_mob2_left, (image_mob2_left.get_width() // 7, image_mob2_left.get_height() // 7))
image_logo = pygame.image.load("pooj.jpg")
image_logo = pygame.transform.scale(image_logo, (image_logo.get_width() // 3, image_logo.get_height() // 3))

image_key = pygame.image.load('key.png')
image_key = pygame.transform.scale(image_key, (image_key.get_width() // 4, image_key.get_height() // 4))
image_coin = pygame.image.load('coin.png')
image_coin = pygame.transform.scale(image_coin, (image_coin.get_width() // 10, image_coin.get_height() // 10))
image_wall = pygame.image.load("wall.png")
image_wall = pygame.transform.scale(image_wall, (image_wall.get_width() // 1, image_wall.get_height() // 1))
image_door = pygame.image.load("door.png")
image_door = pygame.transform.scale(image_door, (image_door.get_width() // 4, image_door.get_height() // 4))

bg1 = pygame.image.load("room1_back.png")
bg1 = pygame.transform.scale(bg1, (bg1.get_width() // 1, bg1.get_height() // 1))

music_logo = pygame.mixer.Sound('volvo.mp3')
music_gachi_logo = pygame.mixer.Sound('Oh yes sir.mp3')


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
    pygame.sprite.spritecollide(player, items1, True)
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
        j = enemy1.rect.x// 50 + 1
        i = enemy1.rect.y // 50 + 1
        print(i, j)
        if enemy1.rect.bottom >= w.rect.top and enemy1.rect.bottom <= w.rect.top + 7:
            if enemy1.rect.right > w.rect.left:
                #enemy1.speed[1] *= -1
                enemy1.rect.bottom = w.rect.top - 10
                del tr[2]
                if data[i][j - 1] == '1':
                    del tr[1]
                if data[i][j + 1] == '1':
                    del tr[0]
                #print('down')
        elif enemy1.rect.top <= w.rect.bottom and enemy1.rect.top >= w.rect.bottom - 7:
            #enemy1.speed[1] *= -1
            enemy1.rect.top = w.rect.bottom + 10
            del tr[3]
            if data[i][j - 1] == '1':
                del tr[1]
            if data[i][j + 1] == '1':
                del tr[0]
            #print('up')
        elif enemy1.rect.right >= w.rect.left and enemy1.rect.right <= w.rect.left + 7:
            if enemy1.rect.bottom > w.rect.top:
                #enemy1.speed[0] *= -1
                enemy1.rect.right = w.rect.left - 10
                if data[i - 1][j] == '1':
                    del tr[3]
                if data[i + 1][j] == '1':
                    del tr[2]
                del tr[0]
                # print('right')
        elif enemy1.rect.left <= w.rect.right and enemy1.rect.left >= w.rect.right - 7:
            #enemy1.speed[0] *= -1
            enemy1.rect.left = w.rect.right + 10
            if data[i - 1][j] == '1':
                del tr[3]
            if data[i + 1][j] == '1':
                del tr[2]
            del tr[1]
            # print('left')
        y = random.choice(tr)
        #print(tr)
        #print(y)
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

    #if len(enemy_and_walls_hit_list) > 0:
    #    x = enemy1.speed
    #    while enemy1.speed == x:
    #        y = random.randint(0, 3)
    #        if y == 0:
    #            enemy1.speed = [enemy_speed, 0]
    #        elif y == 1:
    #            enemy1.speed = [-enemy_speed, 0]
    #        elif y == 2:
    #            enemy1.speed = [0, enemy_speed]
    #        else:
    #            enemy1.speed = [0, -enemy_speed]

    if pygame.sprite.collide_rect(player, door1):
        if key.check_used:
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

def draw_all1(screen):
    screen.blit(bg1, (0, 0))
    screen.blit(player.image, player.rect)
    doors1.draw(screen)
    items1.draw(screen)
    walls1.draw(screen)
    enemies1.draw(screen)

def check_items_exists2(*it):
    for i in it:
        if i not in items2:
            i.check_used = True

def check_collide2(enemy_im_l, enemy_im_r):
    f = open('field2.txt', 'r')
    data = f.readlines()
    pygame.sprite.spritecollide(player, items2, True)
    player_and_walls_hit_list = pygame.sprite.spritecollide(player, walls2,False)
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
        print(i, j)
        if enemy2.rect.bottom >= w.rect.top and enemy2.rect.bottom <= w.rect.top + 7:
            if enemy2.rect.right > w.rect.left:
                # enemy2.speed[1] *= -1
                enemy2.rect.bottom = w.rect.top - 10
                del tr[2]
                if data[i][j - 1] == '1':
                    del tr[1]
                if data[i][j + 1] == '1':
                    del tr[0]
                print('down')
        elif enemy2.rect.top <= w.rect.bottom and enemy2.rect.top >= w.rect.bottom - 7:
            # enemy2.speed[1] *= -1
            enemy2.rect.top = w.rect.bottom + 10
            del tr[3]
            if data[i][j - 1] == '1':
                del tr[1]
            if data[i][j + 1] == '1':
                del tr[0]
            print('up')
        elif enemy2.rect.right >= w.rect.left and enemy2.rect.right <= w.rect.left + 7:
            if enemy2.rect.bottom > w.rect.top:
                # enemy2.speed[0] *= -1
                enemy2.rect.right = w.rect.left - 10
                if data[i - 1][j] == '1':
                    del tr[3]
                if data[i + 1][j] == '1':
                    del tr[2]
                del tr[0]
                print('right')
        elif enemy2.rect.left <= w.rect.right and enemy2.rect.left >= w.rect.right - 7:
            # enemy2.speed[0] *= -1
            enemy2.rect.left = w.rect.right + 10
            if data[i - 1][j] == '1':
                del tr[3]
            if data[i + 1][j] == '1':
                del tr[2]
            del tr[1]
            print('left')
        y = random.choice(tr)
        print(tr)
        print(y)
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
            print('room3')
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

def draw_all2(screen):
    screen.blit(bg1, (0, 0))
    screen.blit(player.image, player.rect)
    doors2.draw(screen)
    items2.draw(screen)
    walls2.draw(screen)
    enemies2.draw(screen)

def logo():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.time.set_timer(pygame.USEREVENT, 8000)
    pygame.init()
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


def room2():
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