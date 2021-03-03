import pygame
import sys
import random

WIDTH = 1500
HEIGHT = 900
white = (255, 255, 255)
black = (0, 0, 0)
player_speed = 7
enemy_speed = 5

image_pers_right = pygame.image.load("gg_right.png")
image_pers_right = pygame.transform.scale(image_pers_right, (image_pers_right.get_width() // 11, image_pers_right.get_height() // 11))
image_pers_left = pygame.image.load("gg_left.png")
image_pers_left = pygame.transform.scale(image_pers_left, (image_pers_left.get_width() // 11, image_pers_left.get_height() // 11))
image_mob_right = pygame.image.load("mob1_right.png")
image_mob_right = pygame.transform.scale(image_mob_right, (image_mob_right.get_width() // 4, image_mob_right.get_height() // 4))
image_mob_left = pygame.image.load("mob1_left.png")
image_mob_left = pygame.transform.scale(image_mob_left, (image_mob_left.get_width() // 4, image_mob_left.get_height() // 4))

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
        self.rect.x += self.speed[0]
        self.rect.y += self.speed[1]

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, filename):
        pygame.sprite.Sprite.__init__(self)
        self.image = filename
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = [enemy_speed, enemy_speed]

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

key = Item(random.randint(50, 500), random.randint(100, 400), image_key)
coin = Item(random.randint(500, 950), random.randint(100, 400), image_coin)
door = Door(14 * 50 + 10, 0, image_door)
player = Pers(100, 200, image_pers_right)
enemy = Enemy(random.randint(0, 1500), random.randint(0, 900), image_mob_right)

items = pygame.sprite.Group()
items.add(key)#, coin)
walls = pygame.sprite.Group()
doors = pygame.sprite.Group()
doors.add(door)
enemies = pygame.sprite.Group()
enemies.add(enemy)


f = open('field.txt', 'r')
data = f.readlines()
for i in range(len(data)):
    for j in range(len(data[i])):
        if data[i][j] == '1':
            w = Wall(j * 50, i * 50, image_wall)
            walls.add(w)

while pygame.sprite.collide_rect(key, player) or len(pygame.sprite.spritecollide(key, doors, False)) > 0 or len(pygame.sprite.spritecollide(key, walls, False)) > 0:
    key.x, key.y = random.randint(50, 500), random.randint(100, 400)
#while pygame.sprite.collide_rect(coin, player) or len(pygame.sprite.spritecollide(coin, doors, False)) > 0 or len(pygame.sprite.spritecollide(coin, walls, False)) > 0:
#    coin.x, coin.y = random.randint(500, 950), random.randint(100, 400)
while pygame.sprite.collide_rect(enemy, player) or len(pygame.sprite.spritecollide(enemy, doors, False)) > 0 or len(pygame.sprite.spritecollide(enemy, walls, False)) > 0:
    enemy.x, enemy.y = random.randint(0, 1500), random.randint(0, 900)

def check_items_exists(*it):
    for i in it:
        if i not in items:
            i.check_used = True

def check_collide():
    pygame.sprite.spritecollide(player, items, True)
    player_and_walls_hit_list = pygame.sprite.spritecollide(player, walls, False)
    enemy_and_walls_hit_list = pygame.sprite.spritecollide(enemy, walls, False)
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
        print(enemy.rect.bottom, enemy.rect.top)
        if enemy.rect.bottom >= w.rect.top and enemy.rect.bottom <= w.rect.top + 7:
            if enemy.rect.right > w.rect.left:
                enemy.speed[1] *= -1
                enemy.rect.bottom = w.rect.top - 10
                #print('up')
                break
        elif enemy.rect.top <= w.rect.bottom and enemy.rect.top >= w.rect.bottom - 7:
            enemy.speed[1] *= -1
            enemy.rect.top = w.rect.bottom + 10
            #print('down')
            break
        if enemy.rect.right >= w.rect.left and enemy.rect.right <= w.rect.left + 7:
            if enemy.rect.bottom > w.rect.top:
                enemy.speed[0] *= -1
                enemy.rect.right = w.rect.left - 10
                #print('left')
                break
        elif enemy.rect.left <= w.rect.right and enemy.rect.left >= w.rect.right - 7:
            enemy.speed[0] *= -1
            enemy.rect.left = w.rect.right + 10
            #print('right')
            break


    if pygame.sprite.collide_rect(player, door):
        if key.check_used:
            room2()
        else:
            if player.rect.bottom >= door.rect.top and player.rect.bottom <= door.rect.top + 15:
                if player.rect.right > door.rect.left:
                    player.rect.bottom = door.rect.top
            elif player.rect.top <= door.rect.bottom and player.rect.top >= door.rect.bottom - 15:
                player.rect.top = door.rect.bottom
            if player.rect.right >= door.rect.left and player.rect.right <= door.rect.left + 15:
                if player.rect.bottom > door.rect.top + 15:
                    player.rect.right = door.rect.left
            elif player.rect.left <= door.rect.right and player.rect.left >= door.rect.right - 15:
                player.rect.left = door.rect.right

def draw_all(screen):
    screen.blit(bg1, (0, 0))
    screen.blit(player.image, player.rect)
    doors.draw(screen)
    items.draw(screen)
    walls.draw(screen)
    enemies.draw(screen)

def room1():
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

        #Проверяем пересечение всего и вся
        check_collide()

        #Проверяем, использованы ли предметы
        check_items_exists(key)#, coin)

        #Отрисовка
        draw_all(screen)

        player.update()
        enemy.update()
        pygame.display.update()
        pygame.time.delay(10)


def room2():
    print('Wellcome to the club')

if __name__ == '__main__':
    room1()