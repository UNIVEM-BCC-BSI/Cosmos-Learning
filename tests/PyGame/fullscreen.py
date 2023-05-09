import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800,500), pygame.FULLSCREEN)
clock = pygame.time.Clock()

background = pygame.Surface((500,300))
background.fill("red")

while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    screen.blit(background, (0,0))
    clock.tick(60)
    pygame.display.update()