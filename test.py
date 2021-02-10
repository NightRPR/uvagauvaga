import pygame
import sys
import random
from test3 import Button, Pers, Target, Door, Item

size = width, height = 1120, 630
black = 0, 0, 0
white = 255, 255, 255
SPEED1, SPEED2 = 4, 7  # random.randint(5, 7)
cnt = 0

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

npc1 = Pers(150, 300, image3, True)
npc2 = Pers(900, 200, image5, True)
gg = Pers(0, 0, image1)
coin = Item(random.randint(400, 700), random.randint(200, 550), image_coin)
key = Item(random.randint(200, 1000), random.randint(200, 550), image_key)


def menu():
    pygame.init()
    pygame.mixer.music.load('just_test.mp3')
    pygame.mixer.music.play()
    screen = pygame.display.set_mode(size)
    gameover = False

    start_button = Button((width // 2) + 300, (height // 2) - 200, 150, 50, (255, 0, 0), 0, 'Calibri', 50, 'Играть')
    while not gameover:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if x >= start_button.x and x <= start_button.x + start_button.width and y >= start_button.y and y <= start_button.y + start_button.height:
                    gameover = True
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load('zvon.mp3')
                    pygame.mixer.music.play()
                    pygame.time.delay(600)
                    room1()
            elif event.type == pygame.MOUSEMOTION:
                x, y = event.pos
                if x >= start_button.x and x <= start_button.x + start_button.width and y >= start_button.y and y <= start_button.y + start_button.height:
                    start_button.border = 5
                    start_button.process_draw(screen)
                else:
                    start_button.border = 0
                    start_button.process_draw(screen)
            if event.type == pygame.QUIT:
                gameover = True
            screen.fill(white)
            screen.blit(image_menu, (0, 0))
            start_button.process_draw(screen)
            pygame.display.flip()
            pygame.time.wait(10)
    sys.exit()


def room1():
    pygame.init()
    pygame.mixer.music.load('dungeon.mp3')
    pygame.mixer.music.play()
    pygame.mixer.music.set_volume(0.1)
    screen = pygame.display.set_mode(size)
    gameover = False
    npc1.x = 150
    npc1.y = 300
    speed = [0, 0]
    _speed_ = 3  # random.randint(-5, 5)
    # if _speed_ < 0:
    #    _speed_ -= 4
    # else:ad
    #    _speed_ += 4
    speed_mob = [_speed_, _speed_]
    door = Door(width // 2 - 90, 0)
    gg.rect.x = width // 2
    gg.rect.y = door.rect.bottom + 20

    while not gameover:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameover = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    gg.image = image2
                    speed[0] = -SPEED1
                elif event.key == pygame.K_d:
                    gg.image = image1
                    speed[0] = SPEED1
                elif event.key == pygame.K_w:
                    speed[1] = -SPEED1
                elif event.key == pygame.K_s:
                    speed[1] = SPEED1
                elif event.key == pygame.K_SPACE:
                    speed[0], speed[1] = 0, 0
                    Pause()
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load('dungeon.mp3')
                    pygame.mixer.music.play()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_a and speed[0] == -SPEED1:
                    speed[0] = 0
                elif event.key == pygame.K_d and speed[0] == SPEED1:
                    speed[0] = 0
                elif event.key == pygame.K_w and speed[1] == -SPEED1:
                    speed[1] = 0
                elif event.key == pygame.K_s and speed[1] == SPEED1:
                    speed[1] = 0
            # if event.type == pygame.USEREVENT:
            # if timer % 2 == 0:
            #    key.rect.y -= 10
            # else:
            #    key.rect.y += 10
            # timer += 1
        if gg.rect.right >= width and speed[0] == SPEED1 or gg.rect.left <= 0 and speed[0] == -SPEED1:
            speed[0] = 0
        if gg.rect.bottom >= height and speed[1] == SPEED1 or gg.rect.top <= 0 and speed[1] == -SPEED1:
            speed[1] = 0
        if gg.collides_with(npc1) and npc1.check_allive == True:
            if fight() == False:
                gameover = True
                npc1.check_allive = True
                npc2.check_allive = True
                game_over()
            else:
                npc1.check_allive = False
                pygame.mixer.music.load('dungeon.mp3')
                pygame.mixer.music.play()
            speed[0], speed[1] = 0, 0
        if gg.collides_with(door):
            if key.check_used == 1:
                gameover = True
                room2()
            else:
                if gg.rect.right - 10 <= door.rect.left:
                    if speed[0] > 0:
                        speed[0] = 0
                if gg.rect.left + 10 >= door.rect.right:
                    if speed[0] < 0:
                        speed[0] = 0
                elif gg.rect.top + 15 >= door.rect.bottom:
                    if speed[1] < 0:
                        speed[1] = 0
        if gg.collides_with(key):
            key.check_used = 1
        if npc1.rect.right >= width:
            speed_mob[0] *= -1
            npc1.image = image4
        if npc1.rect.left <= 0:
            speed_mob[0] *= -1
            npc1.image = image3
        if npc1.rect.bottom >= height or npc1.rect.top <= 0:
            speed_mob[1] *= -1
        if npc1.collides_with(door):
            if npc1.rect.right - 10 <= door.rect.left or npc2.rect.left + 10 >= door.rect.right:
                speed_mob[0] *= -1
            if npc1.rect.top + 10 >= door.rect.bottom:
                speed_mob[1] *= -1
        if speed_mob[0] < 0:
            npc1.image = image4
        else:
            npc1.image = image3
        gg.rect.x += speed[0]
        gg.rect.y += speed[1]
        npc1.rect.x += speed_mob[0]
        npc1.rect.y += speed_mob[1]
        # screen.fill(black)
        screen.blit(bg1, (-10, 0))
        if key.check_used == 0:
            key.process_draw(screen)
        gg.process_draw(screen)
        if npc1.check_allive == True:
            npc1.process_draw(screen)
        door.process_draw(screen)
        pygame.display.flip()
        pygame.time.wait(10)
    sys.exit()


def room2():
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load('forest.mp3')
    pygame.mixer.music.play()
    screen = pygame.display.set_mode(size)
    gameover = False

    # npc2.check_allive = True
    speed = [0, 0]
    _speed_ = 5  # @random.randint(-4, 4)
    # if _speed_ < 0:
    #    _speed_ -= 3
    # else:
    #    _speed_ += 3
    speed_mob = [_speed_, _speed_]

    door1 = Door(100, height // 2 - 150)
    door2 = Door(width // 2 + 310, height - 130)
    gg.rect.x = door1.rect.right + 100
    gg.rect.y = door1.rect.bottom - 100

    # if npc2.collides_with(door1) or npc2.collides_with(door2) or npc2.collides_with(gg):
    # npc2.rect.x = width // 2
    # npc2.rect.y = height // 2

    while not gameover:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameover = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    gg.image = image2
                    speed[0] = -SPEED2
                elif event.key == pygame.K_d:
                    gg.image = image1
                    speed[0] = SPEED2
                elif event.key == pygame.K_w:
                    speed[1] = -SPEED2
                elif event.key == pygame.K_s:
                    speed[1] = SPEED2
                elif event.key == pygame.K_SPACE:
                    speed[0], speed[1] = 0, 0
                    Pause()
                    pygame.mixer.music.load('forest.mp3')
                    pygame.mixer.music.play()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_a and speed[0] == -SPEED2:
                    speed[0] = 0
                elif event.key == pygame.K_d and speed[0] == SPEED2:
                    speed[0] = 0
                elif event.key == pygame.K_w and speed[1] == -SPEED2:
                    speed[1] = 0
                elif event.key == pygame.K_s and speed[1] == SPEED2:
                    speed[1] = 0
        if gg.rect.right >= width and speed[0] == SPEED2 or gg.rect.left <= 0 and speed[0] == -SPEED2:
            speed[0] = 0
        if gg.rect.bottom >= height and speed[1] == SPEED2 or gg.rect.top <= 0 and speed[1] == -SPEED2:
            speed[1] = 0

        if npc2.rect.right >= width:
            speed_mob[0] *= -1
            npc2.image = image6
        if npc2.rect.left <= 0:
            speed_mob[0] *= -1
            npc2.image = image5
        if npc2.rect.bottom >= height or npc2.rect.top <= 0:
            speed_mob[1] *= -1
            if speed_mob[0] < 0:
                npc2.image = image6
            else:
                npc2.image = image5

        if npc2.collides_with(door1):
            if npc2.rect.top <= door1.rect.bottom or npc2.rect.bottom >= door1.rect.top:
                speed_mob[1] *= -1
            if npc2.rect.left >= door1.rect.right:
                speed_mob[0] *= -1
        if npc2.collides_with(door2):
            if npc2.rect.right <= door2.rect.left or npc2.rect.left >= door2.rect.right:
                speed_mob[0] *= -1
            if npc2.rect.bottom >= door2.rect.top:
                speed_mob[1] *= -1
        if speed_mob[0] < 0:
            npc2.image = image6
        else:
            npc2.image = image5
        if gg.collides_with(npc2) and npc2.check_allive == True:
            if fight() == False:
                gameover = True
                npc1.check_allive = True
                npc2.check_allive = True
                game_over()
            else:
                npc2.check_allive = False
                pygame.mixer.music.load('forest.mp3')
                pygame.mixer.music.play()
            speed[0], speed[1] = 0, 0
        if gg.collides_with(coin):
            coin.check_used = 1
        if gg.collides_with(door1):
            gameover = True
            room1()
        if gg.collides_with(door2):
            if coin.check_used == 1:
                gameover = True
                win()
            else:
                if gg.rect.right - 10 <= door2.rect.left:
                    if speed[0] > 0:
                        speed[0] = 0
                if gg.rect.left + 10 >= door2.rect.right:
                    if speed[0] < 0:
                        speed[0] = 0
                elif gg.rect.bottom - 15 <= door2.rect.top:
                    if speed[1] > 0:
                        speed[1] = 0
        gg.rect.x += speed[0]
        gg.rect.y += speed[1]
        npc2.rect.x += speed_mob[0]
        npc2.rect.y += speed_mob[1]
        screen.fill(black)
        screen.blit(bg2, (-10, 0))
        if coin.check_used == 0:
            coin.process_draw(screen)
        gg.process_draw(screen)
        if npc2.check_allive == True:
            npc2.process_draw(screen)
        door1.process_draw(screen)
        door2.process_draw(screen)
        pygame.display.flip()
        pygame.time.wait(10)
    sys.exit()


def fight():
    a = pygame.mixer.music.get_pos()
    pygame.mixer.music.stop()
    screen = pygame.display.set_mode((width, height))
    pygame.time.set_timer(pygame.USEREVENT, 5000)
    gameover = False
    check = False
    cnt = 0
    target = Target(width // 2, height // 2)

    while not gameover:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # gameover = True
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if ((x - target.x) ** 2 + (y - target.y) ** 2) ** 0.5 <= target.R:
                    target.x, target.y = random.randint(200, width - 200), random.randint(300, height - 200)
                    cnt += 1
                    pygame.mixer.music.load('oof.mp3')
                    pygame.mixer.music.play()
                    pygame.time.delay(200)
            if cnt >= 5:
                check = True
                gameover = True
            if event.type == pygame.USEREVENT:
                gameover = True
        screen.fill(black)
        screen.blit(image_fight, (width // 2 - 170, 50))
        target.process_draw(screen)
        pygame.display.flip()
        pygame.time.wait(10)
    return check


def game_over():
    screen = pygame.display.set_mode(size)
    gameover = False
    pygame.mixer.music.load('lose.mp3')
    pygame.mixer.music.play()
    key.check_used = 0
    coin.check_used = 0
    exit_button = Button((width // 2) - 75, (height // 2) + 35, 150, 50, (255, 0, 0), 0, 'Calibri', 50, 'Выйти')
    restart_button = Button((width // 2) - 75, (height // 2) - 25, 150, 50, (255, 0, 0), 0, 'Calibri', 50, 'Заново')

    while not gameover:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if x >= exit_button.x and x <= exit_button.x + exit_button.width and y >= exit_button.y and y <= exit_button.y + exit_button.height:
                    gameover = True
                elif x >= restart_button.x and x <= restart_button.x + restart_button.width and y >= restart_button.y and y <= restart_button.y + restart_button.height:
                    npc1.check_allive = True
                    npc2.check_allive = True
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load('zvon.mp3')
                    pygame.mixer.music.play()
                    pygame.time.delay(600)
                    room1()
            exit_button.check_motion(screen, event, (255, 0, 0))
            restart_button.check_motion(screen, event, (255, 0, 0))
            if event.type == pygame.QUIT:
                gameover = True

            screen.fill(black)
            screen.blit(image_lose, (250, 0))
            exit_button.process_draw(screen)
            restart_button.process_draw(screen)
            pygame.display.flip()
            pygame.time.wait(10)
    sys.exit()


def win():
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load('win.mp3')
    pygame.mixer.music.play()
    screen = pygame.display.set_mode(size)
    gameover = False
    key.check_used = 0
    coin.check_used = 0
    exit_button = Button((width // 2) - 90, (height // 2) - 35, 150, 50, (0, 0, 255), 0, 'Calibri', 50, 'Выйти')
    restart_button = Button((width // 2) - 95, (height // 2) + 25, 160, 50, (0, 0, 255), 0, 'Calibri', 50, 'Заново')

    while not gameover:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if x >= exit_button.x and x <= exit_button.x + exit_button.width and y >= exit_button.y and y <= exit_button.y + exit_button.height:
                    gameover = True
                elif x >= restart_button.x and x <= restart_button.x + restart_button.width and y >= restart_button.y and y <= restart_button.y + restart_button.height:
                    npc1.check_allive = True
                    npc2.check_allive = True
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load('zvon.mp3')
                    pygame.mixer.music.play()
                    pygame.time.delay(600)
                    room1()
            exit_button.check_motion(screen, event, (0, 0, 255))
            restart_button.check_motion(screen, event, (0, 0, 255))
            if event.type == pygame.QUIT:
                gameover = True

            # screen.blit(black, (-10, 0))
            screen.fill((255, 255, 255))
            screen.blit(image_win, (width // 2 - 276, height // 2 - 120))
            exit_button.process_draw(screen)
            restart_button.process_draw(screen)
            pygame.display.flip()
            pygame.time.wait(10)
    sys.exit()


def Pause():
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load('Not_mario.mp3')
    pygame.mixer.music.play()
    screen = pygame.display.set_mode(size)
    gameover = False

    # key.check_used = 0
    # coin.check_used = 0
    # menu_button = Button((width // 2) - 80, (height // 2) - 35, 140, 50, (255, 0, 0), 0, 'Calibri', 50, 'Меню')
    continue_button = Button(width - 400, 100, 276, 50, (255, 0, 0), 0, 'Calibri', 50, 'Продолжить')
    while not gameover:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                # if x >= menu_button.x and x <= menu_button.x + menu_button.width and y >= menu_button.y and y <= menu_button.y + menu_button.height:
                #    gameover = True
                #    menu()
                #    sys.exit()
                if x >= continue_button.x and x <= continue_button.x + continue_button.width and y >= continue_button.y and y <= continue_button.y + continue_button.height:
                    gameover = True
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load('zvon.mp3')
                    pygame.mixer.music.play()
                    pygame.time.delay(600)
            elif event.type == pygame.MOUSEMOTION:
                x, y = event.pos
                if x >= continue_button.x and x <= continue_button.x + continue_button.width and y >= continue_button.y and y <= continue_button.y + continue_button.height:
                    continue_button.border = 5
                    continue_button.process_draw(screen)
                else:
                    continue_button.border = 0
                    continue_button.process_draw(screen)
                    # sys.exit()

            # menu_button.check_motion(screen, event, (255, 0, 0))
            # continue_button.check_motion(screen, event, (255, 0, 0))
            if event.type == pygame.QUIT:
                gameover = True
                sys.exit()

            # screen.fill((0, 0, 0))
            screen.blit(image_pause, (0, 0))
            # menu_button.process_draw(screen)
            continue_button.process_draw(screen)
            pygame.display.flip()
            pygame.time.wait(10)
    # sys.exit()


if __name__ == '__main__':
    menu()
