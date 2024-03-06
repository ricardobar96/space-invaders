import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption('Space Invaders, by Ricardo Baloira')
icon = pygame.image.load('space-invaders-icon.png')
pygame.display.set_icon(icon)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((98, 186, 89))
    pygame.display.update()