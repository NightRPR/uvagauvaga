import pygame
import sys
import random
from files import *
pygame.mixer.init()
pygame.font.init()

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

    def process_draw(self, screen):
        pygame.font.init()
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height), self.border)
        font = pygame.font.SysFont(self.font, self.text_size, True)
        data = self.text
        ts = font.render(data, False, black)
        screen.blit(ts, (self.x - 1, self.y))
