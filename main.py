import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption('Space Invaders, by Ricardo Baloira')
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)

player_img = pygame.image.load('player.png')
player_x = 368
player_y = 526

def player():
    screen.blit(player_img, (player_x, player_y))

running = True
while running:

    screen.fill((98, 186, 89))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player()

    pygame.display.update()