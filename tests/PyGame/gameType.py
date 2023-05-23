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

        self.answer = str(self.num1 + self.num2)

        self.text = self.font.render(str(self.num1) + " + " + str(self.num2), True, "white")

        self.size = list(self.text.get_rect())


    def update(self, tecla):

        if self.vivo:

            self.tela.blit(self.image, (self.x, self.y))

            self.tela.blit(self.text, (self.x + (self.size[2]/2), self.y - 20))


            self.y += self.speed

            self.checkInput(tecla)


    def checkInput(self, tentativa):

        if tentativa == self.answer:

            self.vivo = False



pygame.init()

screen = pygame.display.set_mode((800,500))

clock = pygame.time.Clock()

#Mesma bosta de sempre


fontGame = pygame.font.Font(None, 30)



player = pygame.surface.Surface((50,50))
player.fill("red")

#Coisas do jogador


spriteInimigo = pygame.surface.Surface((100,100))

spriteInimigo.fill("red")

inimigos = [Inimigo(screen, spriteInimigo, fontGame, 100, 700, 10, 1, 1, 9)]

#Coisas do inimigo


now = pygame.time.get_ticks()

cooldown = 500

last = pygame.time.get_ticks()

entrada = ""


while True:

    screen.fill("black")

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            pygame.quit()

            exit()


    now = pygame.time.get_ticks()

    keys = pygame.key.get_pressed()
    

    incluidos = fontGame.render(entrada, True, "white")

    screen.blit(incluidos, (350,50))

    apertado = ""
    

    if now-last>cooldown:
    

        if keys[pygame.K_0]:

            entrada += "0"

            last = pygame.time.get_ticks()

        elif keys[pygame.K_1]:

            entrada += "1"

            last = pygame.time.get_ticks()

        elif keys[pygame.K_2]:

            entrada += "2"

            last = pygame.time.get_ticks()

        elif keys[pygame.K_3]:

            entrada += "3"

            last = pygame.time.get_ticks()

        elif keys[pygame.K_4]:

            entrada += "4"

            last = pygame.time.get_ticks()

        elif keys[pygame.K_5]:

            entrada += "5"

            last = pygame.time.get_ticks()

        elif keys[pygame.K_6]:

            entrada += "6"

            last = pygame.time.get_ticks()

        elif keys[pygame.K_7]:

            entrada += "7"

            last = pygame.time.get_ticks()

        elif keys[pygame.K_8]:

            entrada += "8"

            last = pygame.time.get_ticks()

        elif keys[pygame.K_9]:

            entrada += "9"

            last = pygame.time.get_ticks()


    if keys[pygame.K_SPACE]:
        apertado = entrada
        entrada = ""
    

    for inimigo in inimigos:

        #todo tirar inimigo quando morre

        if inimigo.vivo == True:

            inimigo.update(apertado)

        else:

            inimigos.pop(inimigos.index(inimigo))


    pygame.display.update()

    clock.tick(60)