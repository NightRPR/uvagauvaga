import pygame
import sys
import random

WIDTH = 1440
HEIGHT = 864
white = (255, 255, 255)
black = (0, 0, 0)
player_speed = 7
object_speed = 5

image_pers_right = pygame.image.load("gg_right.png")
image_pers_right = pygame.transform.scale(image_pers_right, (image_pers_right.get_width() // 11, image_pers_right.get_height() // 11))
image_pers_left = pygame.image.load("gg_left.png")
image_pers_left = pygame.transform.scale(image_pers_left, (image_pers_left.get_width() // 11, image_pers_left.get_height() // 11))
image_key = pygame.image.load('key.png')
image_key = pygame.transform.scale(image_key, (image_key.get_width() // 4, image_key.get_height() // 4))
image_coin = pygame.image.load('coin.png')
image_coin = pygame.transform.scale(image_coin, (image_coin.get_width() // 10, image_coin.get_height() // 10))
image_wall = pygame.image.load("wall.jpg")
image_wall = pygame.transform.scale(image_wall, (image_wall.get_width() // 1, image_wall.get_height() // 1))
image_door = pygame.image.load("door.png")
image_door = pygame.transform.scale(image_door, (image_door.get_width() // 4, image_door.get_height() // 4))

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


class Item(pygame.sprite.Sprite):
    def __init__(self, x, y, filename):
        pygame.sprite.Sprite.__init__(self)
        self.image = filename
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.check_used = False

def check_items_exists(*it):
    for i in it:
        if i not in items:
            i.check_used = True

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
door = Door(14 * 48 + 10, 0, image_door)
player = Pers(100, 200, image_pers_right)
items = pygame.sprite.Group()
walls = pygame.sprite.Group()
doors = pygame.sprite.Group()
items.add(key, coin)
doors.add(door)

f = open('field.txt', 'r')
data = f.readlines()
for i in range(len(data)):
    for j in range(len(data[i])):
        if data[i][j] == '1':
            w = Wall(j * 48, i * 48, image_wall)
            walls.add(w)

while pygame.sprite.collide_rect(key, player) or len(pygame.sprite.spritecollide(key, doors, False)) > 0 or len(pygame.sprite.spritecollide(key, walls, False)) > 0:
    key.x, key.y = random.randint(50, 500), random.randint(100, 400)
while pygame.sprite.collide_rect(coin, player) or len(pygame.sprite.spritecollide(coin, doors, False)) > 0 or len(pygame.sprite.spritecollide(coin, walls, False)) > 0:
    coin.x, coin.y = random.randint(500, 950), random.randint(100, 400)

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

        pygame.sprite.spritecollide(player, items, True)
        walls_hit_list = pygame.sprite.spritecollide(player, walls, False)
        #doors_hit_list = pygame.sprite.spritecollide(player, doors, False)
        for w in walls_hit_list:
            if player.rect.bottom >= w.rect.top and player.rect.bottom <= w.rect.top + 15:  # Moving down; Hit the top side of the wall
                if player.rect.right > w.rect.left:
                    player.rect.bottom = w.rect.top
            elif player.rect.top <= w.rect.bottom and player.rect.top >= w.rect.bottom - 15:  # Moving up; Hit the bottom side of the wall
                player.rect.top = w.rect.bottom
            if player.rect.right >= w.rect.left and player.rect.right <= w.rect.left + 15:  # Moving right; Hit the left side of the wall
                if player.rect.bottom > w.rect.top + 15:
                    player.rect.right = w.rect.left  # +1
            elif player.rect.left <= w.rect.right and player.rect.left >= w.rect.right - 15:  # Moving left; Hit the right side of the wall
                player.rect.left = w.rect.right  # -1
        if pygame.sprite.collide_rect(player, door):
            room2

        check_items_exists(key, coin)
        print(key.check_used)
        print(coin.check_used)

        screen.fill(black)
        screen.blit(player.image, player.rect)
        doors.draw(screen)
        items.draw(screen)
        walls.draw(screen)
        pygame.display.update()
        pygame.time.delay(20)
        player.update()


def room2():
    print('Wellcome to the club')

if __name__ == '__main__':
    room1()