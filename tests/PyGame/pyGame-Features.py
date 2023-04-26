import pygame
from sys import exit
from random import randrange


#TODO diminuir a vida do inimigo
#TODO adicionar dano aos disparos
#TODO retrabalhar sistema de movimento dos inimigos

#-----------------------------------------
#O principal conceito no pygame é o de
#Surface, pois é com base nele que se
#cria objetos e os controla, existem
#dois tipos de superfície, uma delas
#é a janela e as outra são os itens
#postos dentro da janela, vale lembrar
#que é permitido colocar um item dentro
#de outro item
#------------------------------------------

class Enemy:
    def __init__(self,tela, vida, spawnPositionX, spawnPositionY, atirador, caminhoDisparo, chancesDeAtirar,disparoSpeed, speedX, speedLimitX,speedY, caminhoImagem):
        self.vida = vida
        self.tela = tela
        self.x = spawnPositionX
        self.y = spawnPositionY
        self.deveAtirar = atirador
        self.disparoX = spawnPositionX
        self.disparoY = spawnPositionY
        self.image = pygame.image.load(caminhoImagem)
        self.speedX = speedX
        self.LimitX = speedLimitX
        self.speedY = speedY
        self.derrotado = False
        self.chanceShoot = chancesDeAtirar
        self.disparoSpeed = disparoSpeed
        
    def update(self):
        if self.derrotado == False:
            self.tela.blit(self.image, (self.x, self.y))
            if self.x >=0 and self.x <= self.tela.get_width():
                self.x += self.speedX
            else:
                self.x -= self.speedX
            
            self.y += self.speedY
            if randrange(0,self.chanceShoot) == 1:
                return True
            else:
                return False
            #Provavelmente vai precisar mexer no sistema de tiro inimigo depois
        
    def atirar(self):
        self.tela.blit(self.image, (self.disparoX,self.disparoY))
        self.disparoY += self.disparoSpeed
        
    def sofrerDano(self, qtndDano):
        self.vida -= qtndDano

class Tiro:
    def __init__(self, tela, posicaoXPai, posicaoYPai, velocidadeTiro, dano):
        global lastDisparo
        #Fala que a variavel esta em escopo global
        lastDisparo = pygame.time.get_ticks()
        #Recebe a quantidade de milisegundos desde o pygame.init
        self.x = posicaoXPai
        self.y = posicaoYPai
        self.speed = velocidadeTiro
        self.image = pygame.image.load("tests/PyGame/starSprite.png")
        self.tela = tela
        self.dano = dano
        
    def update(self):
        self.tela.blit(self.image, (self.x,self.y))
        self.y -= self.speed
        


pygame.init()
#Inicia o PyGame
screen = pygame.display.set_mode((800,500))
#Gera uma janela de width 800 e height 500
screen.fill("white")
#Preenche toda a Superfice com a cor desejada
pygame.display.set_caption("Olá PyGame")
#Muda o nome da janela

#pygame.display.toggle_fullscreen()
#Torna em tela cheia com a resolução definida no screen
Clock = pygame.time.Clock()
#Gera um objeto do tipo Clock

#pygame.display.set_mode((300,200))
#Sobrescreve o display.set_mode anterior

testSurface = pygame.Surface((200,100))
#Gera uma Surface (Superficie) de width 200 e height 100
testSurface.fill("red")

blue = pygame.Surface((100,50))
blue.fill("blue")

green = pygame.Surface((100,50))
green.fill("green")

testImage = pygame.image.load("tests/PyGame/starSprite.png")
#Permite carregar uma imagem para mais tarde ser usada como Surface
background = pygame.image.load("tests/PyGame/testBackground.png")
scrollSpeed = 1
scrollOffset = 0



testText = pygame.font.Font(None, 50)
#Gera uma fonte de tipo e tamanho especificado
textSurface = testText.render("Testando PyGame",False,"orange")
#Esta passando os argumentos em ordem: Text, Antialias, Color
#É uma Surface, está gerendo uma Surface com conteudo especificado, se o antialias for True
#o texto fica mais "arredondado"

#Posição X do testImage
testImageX = 500 
testImageY = 100

disparos = []
inimigos = []
disparosInimigos = []

cooldownDisparo = 300
cooldownSpawn = 10000

#diferença de ticks necessaria para poder atirar
lastDisparo = pygame.time.get_ticks()
lastSpawn = pygame.time.get_ticks()



while True:
    
    #screen.fill("black")
    #Como o metodo blit desenha na tela, sempre a pinta de preto para permitir
    #a movimentação do personagem
    
    
    for event in pygame.event.get():
        #Gera uma lista de eventos registrados pelo pygame
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            #Fecha o interpretador do código impedindo o while True de continuar

        #Outro jeito de fazer pra pegar as teclas pressionadas

#        if event.type == pygame.KEYDOWN:
#            if event.key == pygame.K_w:
#                testImageY -= 1
#                #decrementa pq (0,0) é no canto superior esquerdo
#            if event.key == pygame.K_s:
#                testImageY += 1
#                #incrementa pq (0,0) é no canto superior esquerdo
#            if event.key == pygame.K_a:
#                testImageX -= 1
#            if event.key == pygame.K_d:
#                testImageX += 1
    
                
    screen.blit(background, (0,scrollOffset))
    screen.blit(background, (0, scrollOffset-background.get_height()))
    
    scrollOffset += scrollSpeed
    scrollSpeed += 0.01
    
    if scrollOffset >= background.get_height():
        scrollOffset = 0
        
    #Um outro jeito de checar as teclas apertadas
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        #Se existe pygame.K_w dentro de keys
        testImageY -= 1
    if keys[pygame.K_s]:
        testImageY += 1
    if keys[pygame.K_a]:
        testImageX -= 1
    if keys[pygame.K_d]:
        testImageX += 1
    if keys[pygame.K_SPACE]:
        nowDisparo = pygame.time.get_ticks()
        if nowDisparo - lastDisparo >= cooldownDisparo:
            disparos.append(Tiro(screen, testImageX, testImageY, 2,5))
            #permite manter varios disparos ao mesmo tempo
    
    screen.blit(testSurface, (200,0))
    #Posiciona o testSurface dentro da Screen
    #A cada frama atualiza a posição
    
    testSurface.blit(blue, (0,0))
    #Se estiver fora do alcance do display usado não vai renderizar
    
    screen.blit(green, (200,50))
    #Perceba que pygame permite sobreposição
    
    screen.blit(testImage, (testImageX, testImageY))
    #Perceber que fica desenhando em cima da imagem anterior enquanto move
    
    #A tupla esta passando a margem que o objeto deve ter em X e Y
    #Lembrando que o ponto X = 0 e Y = 0 no pygame é no canto superior esquerdo
    
    screen.blit(textSurface,(500, 200))
    
    #Como os disparos são os ultimos a serem desenhados na tela
    #garante que sempre serão mostrados em cima de qualquer surface
    for disparo in disparos:
        disparo.update()
        if disparo.y < -screen.get_height()-100:
            disparos.pop(disparos.index(disparo))
            
    for disparo in disparosInimigos:
        disparo.atirar()
    
    nowSpawn = pygame.time.get_ticks()
    if nowSpawn-lastSpawn>=cooldownSpawn:
        inimigos.append(Enemy(screen, 10, randrange(0, screen.get_width()+1), 100, True, "tests/PyGame/starSprite.png",50, 2, 2, 10, 1, "tests/PyGame/starSprite.png"))
        lastSpawn = pygame.time.get_ticks()
        
    for inimigo in inimigos:
        
        for disparo in disparos:
            if inimigo.x == disparo.x and inimigo.y == disparo.y:
                inimigo.derrotado = True
        if inimigo.update():
            disparosInimigos.append(inimigo)
            
    
    
    pygame.display.update()
    #Sem isso a tela fica completamente preta
    
    Clock.tick(60)
    #Limita a quantidade maxima de frames por segundo