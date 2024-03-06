import pygame
import random

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

invader_img = pygame.image.load('invader.png')
invader_x = random.randint(0, 726)
invader_y = random.randint(20, 200)
invader_x_change = 0.3
invader_y_change = 50

bullet_img = pygame.image.load('bullet.png')
bullet_x = 0
bullet_y = 526
bullet_x_change = 0
bullet_y_change = 1
bullet_visible = False

def player(x, y):
    screen.blit(player_img, (x, y))

def invader(x, y):
    screen.blit(invader_img, (x, y))

def shoot(x, y):
    global bullet_visible
    bullet_visible = True
    screen.blit(bullet_img, (x + 14, y + 10))

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

    invader_x += invader_x_change

    if invader_x <= 10:
        invader_x_change = 0.3
        invader_y += invader_y_change
    elif invader_x >= 726:
        invader_x_change = -0.3
        invader_y += invader_y_change

    if bullet_y <= 64:
        bullet_y = 526
        bullet_visible = False

    if bullet_visible:
        shoot(bullet_x, bullet_y)
        bullet_y -= bullet_y_change

    player(player_x, player_y)
    invader(invader_x, invader_y)

    pygame.display.update()