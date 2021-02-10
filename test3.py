import pygame
import sys
import random
bg1 = pygame.image.load("room1_back.png")
bg1 = pygame.transform.scale(bg1, (bg1.get_width() // 1, bg1.get_height() // 1))
bg2 = pygame.image.load("room2_back.png")
bg2 = pygame.transform.scale(bg2, (bg2.get_width() // 1, bg2.get_height() // 1))

image1 = pygame.image.load("gg_right.png")
image1 = pygame.transform.scale(image1, (image1.get_width() // 11, image1.get_height() // 11))
image2 = pygame.image.load("gg_left.png")
image2 = pygame.transform.scale(image2, (image2.get_width() // 11, image2.get_height() // 11))
image3 = pygame.image.load("mob1_right.png")
image3 = pygame.transform.scale(image3, (image3.get_width() // 4, image3.get_height() // 4))
image4 = pygame.image.load("mob1_left.png")
image4 = pygame.transform.scale(image4, (image4.get_width() // 4, image4.get_height() // 4))
image5 = pygame.image.load("mob2_right.png")
image5 = pygame.transform.scale(image5, (image5.get_width() // 4, image5.get_height() // 4))
image6 = pygame.image.load("mob2_left.png")
image6 = pygame.transform.scale(image6, (image6.get_width() // 4, image6.get_height() // 4))
image_coin = pygame.image.load("coin.png")
image_coin = pygame.transform.scale(image_coin, (image_coin.get_width() // 10, image_coin.get_height() // 10))
image_door = pygame.image.load("door.png")
image_door = pygame.transform.scale(image_door, (image_door.get_width() // 4, image_door.get_height() // 4))
image_key = pygame.image.load("key.png")
image_key = pygame.transform.scale(image_key, (image_key.get_width() // 4, image_key.get_height() // 4))
image_win = pygame.image.load("you_won.png")
image_menu = pygame.image.load("menu.png")
image_lose = pygame.image.load("you_died.png")
image_lose = pygame.transform.scale(image_lose, (image_lose.get_width() // 2, image_lose.get_height() // 2))
image_fight = pygame.image.load("fight.png")
image_fight = pygame.transform.scale(image_fight, (image_fight.get_width() // 2, image_fight.get_height() // 2))
image_pause = pygame.image.load("pause_back.png")

class Pers:
    image = image1

    def __init__(self, x = None, y = None, filename = None, check_allive = True):
        if filename:
            self.image = filename
        self.rect = self.image.get_rect()
        self.rect.x = x - self.rect.width
        self.rect.y = y
        self.check_allive = check_allive

    #def process_logic(self):

    def process_draw(self, screen):
        screen.blit(self.image, self.rect)

    def collides_with(self, b):
        return self.rect.colliderect(b.rect)

class Button:
    def __init__(self, x=None, y=None, wdth=None, hght=None, color = (0, 0, 0), border = 0, font = 'Calibri', text_size = 50, text = None):
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
        ts = font.render(data, False, [0, 0, 0])
        screen.blit(ts, (self.x - 1, self.y))

class Target:
    def __init__(self, x=None, y=None, color = (255, 0, 0), R = 50):
        self.color = color
        self.x = x
        self.y = y
        self.R = R

    def process_draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.R)

class Door:
    image = image_door

    def __init__(self, x=None, y=None, filename=None):
        if filename:
            self.image = filename
        self.rect = self.image.get_rect()
        self.rect.x = x - self.rect.width
        self.rect.y = y

    def process_draw(self, screen):
        screen.blit(self.image, self.rect)

    def collides_with(self, b):
        return self.rect.colliderect(b.rect)

class Item:
    image = image_key

    def __init__(self, x=None, y=None, filename=None):
        if filename:
            self.image = filename
        self.rect = self.image.get_rect()
        self.rect.x = x - self.rect.width
        self.rect.y = y
        self.check_used = 0

    def process_draw(self, screen):
        screen.blit(self.image, self.rect)

    def collides_with(self, b):
        return self.rect.colliderect(b.rect)