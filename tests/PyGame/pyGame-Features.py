import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800,500))
pygame.display.set_caption("Konichiwa PyGame")
#pygame.display.toggle_fullscreen()
Clock = pygame.time.Clock()

testSurface = pygame.Surface((200,100))
testSurface.fill("red")
blue = pygame.Surface((100,50))
blue.fill("blue")
green = pygame.Surface((100,50))
green.fill("green")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
                
    screen.blit(testSurface, (200,0))
    testSurface.blit(blue, (0,0))
    #Se estiver fora do alcance do display usado não vai renderizar
    screen.blit(green, (200,50))
    #Perceba que pygame permite sobreposição
    
    pygame.display.update()
    Clock.tick(60)
    #Limita a quantidade maxima de frames por segundo