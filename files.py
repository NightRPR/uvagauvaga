import pygame
WIDTH = 1500
HEIGHT = 900
white = (255, 255, 255)
black = (0, 0, 0)
player_speed = 7
enemy_speed = 5
cell_size = 50
pygame.mixer.init()


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
image_pause = pygame.image.load('pause_bg.png')

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


