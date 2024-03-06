import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption('Space Invaders, by Ricardo Baloira')
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)

player_img = pygame.image.load('player.png')
player_x = 368
player_y = 526
player_x_change = 0

def player(x, y):
    screen.blit(player_img, (player_x, player_y))

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
    player(player_x, player_y)

    pygame.display.update()