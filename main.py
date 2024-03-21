import pygame
import random
import math
from pygame import mixer

pygame.init()

screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption('Space Invaders, by Ricardo Baloira')
icon = pygame.image.load('images/icon.png')
pygame.display.set_icon(icon)
background = pygame.image.load('images/background.jpg')

mixer.music.load('sound/Breakdown_Full.mp3')
mixer.music.set_volume(0.2)
mixer.music.play(-1)

player_img = pygame.image.load('images/player.png')
player_x = 368
player_y = 526
player_x_change = 0

invader_img = []
invader_x = []
invader_y = []
invader_x_change = []
invader_y_change = []
number_invaders = 10

for i in range(number_invaders):
    invader_img.append(pygame.image.load('images/invader.png'))
    invader_x.append(random.randint(0, 726))
    invader_y.append(random.randint(20, 200))
    invader_x_change.append(0.1)
    invader_y_change.append(50)

bullets = []
bullet_img = pygame.image.load('images/bullet.png')
bullet_x = 0
bullet_y = 526
bullet_x_change = 0
bullet_y_change = 1
bullet_visible = False

score = 0
font = pygame.font.Font('font/Faster.otf', 32)
text_x = 10
text_y = 10

end_font = pygame.font.Font('font/Faster.otf', 52)

def end_text():
    final_text = end_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(final_text, (230, 200))

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
                bullet_sound = mixer.Sound('sound/shoot.wav')
                bullet_sound.play()
                new_bullet = {
                    "x": player_x,
                    "y": player_y,
                    "speed": -1
                }
                bullets.append(new_bullet)
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

        if invader_y[i] > 500:
            for e in range(number_invaders):
                invader_y[e] = 1000
            end_text()
            break

        invader_x[i] += invader_x_change[i]
        if invader_x[i] <= 10:
            invader_x_change[i] = 0.1
            invader_y[i] += invader_y_change[i]
        elif invader_x[i] >= 726:
            invader_x_change[i] = -0.1
            invader_y[i] += invader_y_change[i]
        for bullet in bullets:
            collision_bullet_invader = hit(invader_x[i], invader_y[i], bullet["x"], bullet["y"])
            if collision_bullet_invader:
                invader_sound = mixer.Sound('sound/hit.wav')
                invader_sound.play()
                bullets.remove(bullet)
                bullet_y = 526
                bullet_visible = False
                score += 10
                invader_x[i] = random.randint(0, 726)
                invader_y[i] = random.randint(20, 200)
                break

        invader(invader_x[i], invader_y[i], i)

    for bullet in bullets:
        bullet["y"] += bullet["speed"]
        screen.blit(bullet_img, (bullet["x"] + 16, bullet["y"] + 10))
        if bullet["y"] < 0:
            bullets.remove(bullet)

    if bullet_y <= 64:
        bullet_y = 526
        bullet_visible = False

    if bullet_visible:
        shoot(bullet_x, bullet_y)
        bullet_y -= bullet_y_change

    player(player_x, player_y)

    show_score(text_x, text_y)

    pygame.display.update()