import pygame
import random
import math

pygame.init()

screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption('Space Invaders, by Ricardo Baloira')
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)
background = pygame.image.load('background.jpg')

player_img = pygame.image.load('player.png')
player_x = 368
player_y = 526
player_x_change = 0

invader_img = []
invader_x = []
invader_y = []
invader_x_change = []
invader_y_change = []
number_invaders = 6

for i in range(number_invaders):
    invader_img.append(pygame.image.load('invader.png'))
    invader_x.append(random.randint(0, 726))
    invader_y.append(random.randint(20, 200))
    invader_x_change.append(0.3)
    invader_y_change.append(50)

bullet_img = pygame.image.load('bullet.png')
bullet_x = 0
bullet_y = 526
bullet_x_change = 0
bullet_y_change = 1
bullet_visible = False

score = 0
font = pygame.font.Font('Faster.otf', 32)
text_x = 10
text_y = 10

def show_score(x, y):
    text = font.render(f'Score: {score}', True, (255, 255, 255))
    screen.blit(text, (x, y))

def player(x, y):
    screen.blit(player_img, (x, y))

def invader(x, y, inv):
    screen.blit(invader_img[inv], (x, y))

def shoot(x, y):
    global bullet_visible
    bullet_visible = True
    screen.blit(bullet_img, (x + 14, y + 10))

def hit(x_1, x_2, y_1, y_2):
    distance = math.sqrt(math.pow(x_1 - x_2, 2) + math.pow(y_2 - y_1, 2))
    if distance < 27:
        return True
    else:
        return False

running = True
while running:

    screen.blit(background, (-100, -200))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x_change = -0.5
            if event.key == pygame.K_RIGHT:
                player_x_change = 0.5
            if event.key == pygame.K_SPACE:
                if not bullet_visible:
                    bullet_x = player_x
                    shoot(bullet_x, bullet_y)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_x_change = 0

    player_x += player_x_change

    if player_x <= 10:
        player_x = 10
    elif player_x >= 726:
        player_x = 726

    for i in range(number_invaders):
        invader_x[i] += invader_x_change[i]
        if invader_x[i] <= 10:
            invader_x_change[i] = 0.3
            invader_y[i] += invader_y_change[i]
        elif invader_x[i] >= 726:
            invader_x_change[i] = -0.3
            invader_y[i] += invader_y_change[i]
        collision = hit(invader_x[i], invader_y[i], bullet_x, bullet_y)
        if collision:
            bullet_y = 526
            bullet_visible = False
            score += 10
            invader_x[i] = random.randint(0, 726)
            invader_y[i] = random.randint(20, 200)

        invader(invader_x[i], invader_y[i], i)

    if bullet_y <= 64:
        bullet_y = 526
        bullet_visible = False

    if bullet_visible:
        shoot(bullet_x, bullet_y)
        bullet_y -= bullet_y_change

    player(player_x, player_y)

    show_score(text_x, text_y)

    pygame.display.update()