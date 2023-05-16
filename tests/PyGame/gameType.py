import pygame
from sys import exit
from random import randint


class Inimigo():
    def __init__(self, tela, objetoSprite, font,inicioXSpawn, fimXSpawn, ySpawn, speed, inicioNum, fimNum):
        self.tela = tela
        self.image = objetoSprite

        self.font = font
        self.vivo = True
        self.x = randint(inicioXSpawn, fimXSpawn)
        self.y = ySpawn
        self.speed = speed
        self.num1 = randint(inicioNum, fimNum)
        self.num2 = randint(inicioNum, fimNum)
        #TODO diferentes tipos de operações?
        self.answer = list(str(self.num1 + self.num2))
        self.text = self.font.render(str(self.num1) + " + " + str(self.num2), True, "white")
        self.size = list(self.text.get_rect())

    def update(self, tecla):
        if self.vivo:
            self.tela.blit(self.image, (self.x, self.y))
            self.tela.blit(self.text, (self.x + (self.size[2]/2), self.y - 20))

            self.y += self.speed
            self.checkInput(tecla)

    def checkInput(self, tecla):
        if len(self.answer) == 0:
            self.vivo = False
        else:
            if tecla == self.answer[0]:
                self.answer.pop(0)



pygame.init()
screen = pygame.display.set_mode((800,500))
clock = pygame.time.Clock()
#Mesma bosta de sempre


font = pygame.font.Font(None, 30)


player = pygame.surface.Surface((50,50))
player.fill("red")
#Coisas do jogador

spriteInimigo = pygame.surface.Surface((100,100))
spriteInimigo.fill("red")
inimigos = [Inimigo(screen, spriteInimigo, font, 100, 700, 10, 1, 1, 9)]
#Coisas do inimigo


while True:
    screen.fill("black")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    keys = pygame.key.get_pressed()
    apertado = None

    if keys[pygame.K_0]:
        apertado = "0"
    elif keys[pygame.K_1]:
        apertado = "1"
    elif keys[pygame.K_2]:
        apertado = "2"
    elif keys[pygame.K_3]:
        apertado = "3"
    elif keys[pygame.K_4]:
        apertado = "4"
    elif keys[pygame.K_5]:
        apertado = "5"
    elif keys[pygame.K_6]:
        apertado = "6"
    elif keys[pygame.K_7]:
        apertado = "7"
    elif keys[pygame.K_8]:
        apertado = "8"
    elif keys[pygame.K_9]:
        apertado = "9"

    for inimigo in inimigos:
        #todo tirar inimigo quando morre
        if inimigo.vivo == True:
            inimigo.update(apertado)
        else:
            inimigos.pop(inimigos.index(inimigo))

    pygame.display.update()
    clock.tick(60)