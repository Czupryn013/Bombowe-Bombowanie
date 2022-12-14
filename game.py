import sys

import pygame
import random
import menu

pygame.init()

WIDTH = 900
HEIGHT = 700
FPS = 60
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
menu_ = menu.Menu(WIDTH, HEIGHT, FPS)
BONUS = 1 #multipier bonus
max_hp =5
PLAYER_SPEED = 7
BOMB_SPEED = 3
BULLET_SPEED = 7
BULLET_RNG = 100
ON_DEATH = 25
CITY_HIT = pygame.USEREVENT +1
PlAYER_HIT = pygame.USEREVENT +2
BOMB_DMG = 5
B_SIZE = (20, 15)
P_SIZE = (100, 40)
C_SIZE = (WIDTH // 3, 100)
max_bombs = 5
PLANE = pygame.transform.scale(pygame.image.load("assets/bombowiec.png"), P_SIZE)
PLANE2 = pygame.transform.scale(pygame.image.load("assets/bombowiec2.png"), P_SIZE)
BOMB = pygame.transform.scale(pygame.image.load("assets/bomba.png"), B_SIZE)
BOMB = pygame.transform.rotate(BOMB, 50)

BOMB2 = pygame.transform.scale(pygame.image.load("assets/bomba1.png"), (25, 18))
BOMB2 = pygame.transform.rotate(BOMB2, 50)

CITY = pygame.transform.scale(pygame.image.load("assets/berlin_city.png"), C_SIZE)

pygame.display.set_caption("Bombowe Bombowanie")


def handleBombs(bombs, explo, city):
    for bomb in bombs:
        bomb[0].y += BOMB_SPEED #opadanie w dół
        if bomb[1] == "l":
            bomb[0].x -= 0.5
        if bomb[1] == "r": #siła w bok, nwm czemu wartości są rożne, jak jest 0.5 przy r to nie dziala
            bomb[0].x += 1

        if city.colliderect(bomb[0]): #sprawdzanie czy bomba trafiła w miasto
            pygame.event.post(pygame.event.Event(CITY_HIT))
            explosion = bomb[0]
            explosion.y += random.randint(0,40)
            explo.append([explosion, 30])
            bombs.remove(bomb)
        elif bomb[0].y > HEIGHT or bomb[0].x > WIDTH or bomb[0].x < -1: #sprawdzanie jest poza ekranem
            bombs.remove(bomb)

def shoot_aad(city, player):
    salve = []
    for i in range(3):
        if i == 0:
            x_offset = -30
        elif i == 1:
            x_offset = 0
        else:
            x_offset = 30
        y_offset = random.randint(-5,5)
        salve.append([city.x + C_SIZE[0] /2 + x_offset, city.y + y_offset])

    x = 0
    if city.x + C_SIZE[0] / 2 > player.x:  # po lewej
        x = (city.x + C_SIZE[0] / 2) - (player.x + P_SIZE[0] /2)
        x -= x *2
    else:  # po prawej
        x = (player.x + P_SIZE[0] /2) - (city.x + C_SIZE[0] // 2)
    y = city.y - player.y
    dist = (x ** 2 + y ** 2) ** 0.5
    moves = dist / BULLET_SPEED
    # ^ 3h bólu

    return [salve, (x/moves, y/moves)] #0 = x i y pocisku, 1 = ile ma się ruszyć

def handle_aad(player, bullets):
    for salve in bullets:
        for bullet in salve[0]:
            move = salve[1]
            bullet[0] += move[0]
            bullet[1] -= move[1]
            #checking for hit
            hitbox = pygame.Rect(bullet[0], bullet[1], 4,4)
            if player.colliderect(hitbox):
                pygame.event.post(pygame.event.Event(PlAYER_HIT))
                salve[0].remove(bullet)
            elif bullet[1] < 0 or bullet[0] < 0 or bullet[0] > WIDTH:
                salve[0].remove(bullet)
        #removing salve from list when all bullets were removed
        if len(salve[0]) == 0:
            bullets.remove(salve)

def playerMovment(keys, player, last):
    tmp = ""
    if keys[pygame.K_w] and player.y - PLAYER_SPEED > 0:
        player.y -= PLAYER_SPEED
    if keys[pygame.K_s] and player.y + PLAYER_SPEED < 250:
        player.y += PLAYER_SPEED

    if keys[pygame.K_a] and player.x - PLAYER_SPEED > 0:
        tmp = "l"
        player.x -= PLAYER_SPEED
    elif keys[pygame.K_d] and player.x + P_SIZE[0] +  PLAYER_SPEED < WIDTH:
        tmp = "r"
        player.x += PLAYER_SPEED
    elif last == "r" and player.x + P_SIZE[0] +  PLAYER_SPEED < WIDTH:
        player.x += PLAYER_SPEED // 1.5
    elif last == "l" and player.x - PLAYER_SPEED > 0:
        player.x -= PLAYER_SPEED // 1.5
    return tmp

def draw_text(content,color, size, x,y, centered = False):
    font = pygame.font.SysFont("arialblack", size)
    text = font.render(str(content), True, color)
    if centered:
        width = text.get_rect().width
        WIN.blit(text, (x -( width // 2),y))
    else:
        WIN.blit(text, (x, y))

def draw_bar(cur,maX, cur_color, max_color, x,y, reverse = False):
    for i in range(maX):
        bar = pygame.Rect(x + (i*15), y, 10,20)
        if not reverse:
            color = cur_color
            if i +1 > cur:
                color = max_color
        else: #zajeło mi to godzine, nwm co ja robie
            color = cur_color #nwm jak to działa ale działa
            if i +1 > maX - cur:
                color = max_color

        pygame.draw.rect(WIN, color,bar)

def draw(bombs, player,city, last,explo, score,player_hp, bullets, dmg_text):
    WIN.fill((87,140,209))
    #player
    if last == "l":
        WIN.blit(PLANE2, (player.x, player.y))
    elif last == "r":
        WIN.blit(PLANE, (player.x, player.y))

    #city
    WIN.blit(CITY, (city.x , city.y))
    pygame.draw.rect(WIN, (255, 0, 0), pygame.Rect(city.x + C_SIZE[0] /2, city.y, 5, 5))

    #bombz and explożyns
    for bomb in bombs:
        WIN.blit(BOMB, (bomb[0].x, bomb[0].y))
    for exp in explo:
        if exp[1] == 0:
            explo.remove(exp)
        else:
            WIN.blit(BOMB2, (exp[0].x, exp[0].y))
            exp[1] -= 1
    #aad bullets
    for salve in bullets:
        for bullet in salve[0]:
            pygame.draw.circle(WIN, (150, 150, 150), (bullet[0], bullet[1]),5)

    #score
    draw_text(score, (255,0,100), 40, WIDTH //2, 10, centered= True)
    #ammo/bombs
    draw_bar(len(bombs), max_bombs, (100, 100, 100), (170, 170, 170), 10, 5, reverse=True)
    #hp
    draw_bar(player_hp[0], player_hp[1], (0,255,0), (150,150,150), 10, 30)
    #dmg pop up
    if dmg_text and dmg_text[1] != 0:
        dmg_text[1] -= 1
        draw_text(dmg_text[0], (100, 100, 100), 20, WIDTH - 170, 10, centered=True)

    pygame.display.update()

def main(score):
    player_hp = [max_hp, max_hp] #0 = current hp, 1 = max hp
    player = pygame.Rect(WIDTH // 2, 100, P_SIZE[0], P_SIZE[1])
    city = pygame.Rect(WIDTH // 2 - (C_SIZE[0] // 2), HEIGHT - 100, C_SIZE[0], C_SIZE[1])
    explo = []
    bombs = []
    bullets = []
    alive = True
    clock = pygame.time.Clock()
    last = "r"
    dmg_text = None
    while alive:
        clock.tick(FPS)
        player_hp[1] = max_hp
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and len(bombs) < max_bombs:
                    bomb = pygame.Rect(player.x + (P_SIZE[1] // 2), player.y + 15, B_SIZE[0], B_SIZE[1])
                    bombs.append((bomb, last)) #0 bomb rect, "l" or "r"
                if event.key == pygame.K_ESCAPE:
                    score = menu_.main_menu(score)
            if event.type == CITY_HIT:
                score += BOMB_DMG * BONUS
                dmg_text = [f"Player delt: {5 * BONUS} dmg to the city!" , 100]
                print(f"Player delt: {5 * BONUS} dmg to the city!")
                if random.randint(0, 10) == 1: bullets.append(shoot_aad(city, player))
            if event.type == PlAYER_HIT:
                player_hp[0] -= 1
        keys = pygame.key.get_pressed()
        tmp = playerMovment(keys, player, last)
        if random.randint(0,BULLET_RNG) == 13: bullets.append(shoot_aad(city,player))
        if tmp != "": last=tmp
        handleBombs(bombs, explo, city)
        handle_aad(player,bullets)
        draw(bombs, player, city, last, explo,score, player_hp, bullets, dmg_text)

        if player_hp[0] <= 0:
            score -= ON_DEATH
            alive = False

    return score




