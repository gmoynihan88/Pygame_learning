import pygame
from sys import exit

pygame.init() 
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('dog game')
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)

sky_surf = pygame.image.load('graphics/Sky.png').convert()
ground_surf = pygame.image.load('graphics/ground.png').convert()
text_surf = test_font.render('My Game', False, 'Black')

snail_surf = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_rect = snail_surf.get_rect(midbottom = (600, 300))

player_surf = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()
player_rect =player_surf.get_rect(midbottom = (80, 300))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(sky_surf, (0,0))
    screen.blit(ground_surf, (0,300))
    screen.blit(text_surf, (300,50))

    snail_rect.x -= 4
    screen.blit(snail_surf,snail_rect)
    if snail_rect.x < -100: snail_rect.x = 800
    screen.blit(player_surf,player_rect)

    if player_rect.colliderect(snail_rect):
        print('collison')

    pygame.display.update()
    clock.tick(60)
