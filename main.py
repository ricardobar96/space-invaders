import pygame
import random

pygame.init()

screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption('Space Invaders, by Ricardo Baloira')
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)

player_img = pygame.image.load('player.png')
player_x = 368
player_y = 526
player_x_change = 0

invader_img = pygame.image.load('icon.png')
invader_x = random.randint(0, 726)
invader_y = random.randint(20, 400)
invader_x_change = 0

def player(x, y):
    screen.blit(player_img, (x, y))

def invader(x, y):
    screen.blit(invader_img, (x, y))

running = True
while running:

    screen.fill((98, 186, 89))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x_change = -0.2
            if event.key == pygame.K_RIGHT:
                player_x_change = 0.2

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_x_change = 0

    player_x += player_x_change

    if player_x <= 10:
        player_x = 10
    elif player_x >= 726:
        player_x = 726

    player(player_x, player_y)
    invader(invader_x, invader_y)

    pygame.display.update()