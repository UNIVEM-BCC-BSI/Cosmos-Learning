import pygame
from sys import exit

#TODO fazer um metodo para retornar a posição dos tiros, player e inimigos
#TODO fazer a classe jogador

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
    def __init__(self,tela, vida, spawnPositionX, spawnPositionY, atirador, caminhoDisparo, cooldownDisparo,disparoSpeed, dano,speedX, speedLimitX,speedY, caminhoImagem, isMovingLeft):
        self.vida = vida
        self.tela = tela
        self.x = spawnPositionX
        self.y = spawnPositionY
        self.deveAtirar = atirador
        self.image = pygame.image.load(caminhoImagem)
        self.size = list(self.image.get_rect())
        self.disparo = pygame.image.load(caminhoDisparo)
        self.disparoDano = dano
        self.speedX = speedX
        self.LimitX = speedLimitX
        self.speedY = speedY
        self.lastShoot = pygame.time.get_ticks()
        self.shootCooldown = cooldownDisparo
        self.now = pygame.time.get_ticks()
        self.disparoSpeed = disparoSpeed
        self.isMovingLeft = isMovingLeft
        self.rect = list(self.image.get_rect())
               
        #self.image.fill("red")
        #print('Oi')
        #remover depois
        
    def update(self):
        global disparosInimigos
            
        if not self.y > self.tela.get_height() + 100:
            if self.x > self.tela.get_width():
                self.isMovingLeft = True
            elif self.x < 0:
                self.isMovingLeft = False
            if self.isMovingLeft:
                self.x -= self.speedX
            else:
                self.x += self.speedX
                
            self.y += self.speedY
            
            self.tela.blit(self.image, (self.x, self.y))
            #print(self.x, self.y)
    
            self.now = pygame.time.get_ticks()
            if self.now - self.lastShoot >= self.shootCooldown:
                disparosInimigos.append(TiroInimigo(self.tela,self.disparo, self.disparoSpeed, self.disparoDano, self.x + (self.rect[2]/2), self.y + (self.rect[3]/2)))        
                self.lastShoot = pygame.time.get_ticks()    
                #Provavelmente vai precisar mexer no sistema de tiro inimigo depois
        
    def getLife(self):
        return self.vida
        
    def checkContact(self, disparo):
        inicioHitboxX = self.x
        fimHitboxX = self.x + self.size[2]
        fimHitboxY = self.y
        inicioHitboxY = self.y + self.size[3]
        
        if disparo.x >= inicioHitboxX and disparo.x <= fimHitboxX and disparo.y <= inicioHitboxY and disparo.y >= fimHitboxY:
            return True    
    
    def sofrerDano(self, qtndDano):
        self.vida -= qtndDano

class TiroInimigo():
    def __init__(self, tela,disparo, speed, dano, spawnX, spawnY):
        #print("Disparo")
        self.tela = tela
        self.image = disparo   
        self.speed = speed
        self.dano = dano
        self.size = list(self.image.get_rect())
        self.x = spawnX
        self.y = spawnY
        self.hit = False
    
    def getXPos(self):
        return self.x + self.size[2]
    
    def getYPos(self):
        return self.y + self.size[3]
    
    def checkContact(self, jogador):
        inicioHitboxX = self.x
        fimHitboxX = self.x + self.size[2]
        fimHitboxY = self.y
        inicioHitboxY = self.y + self.size[3]
        
        if jogador.x >= inicioHitboxX and jogador.x <= fimHitboxX and jogador.y <= inicioHitboxY and jogador.y >= fimHitboxY:
            return True 
    
    def update(self):
        self.tela.blit(self.image, (self.x,self.y))
        self.y += self.speed

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
        self.size = self.image.get_rect().centerx
        self.tela = tela
        self.dano = dano
    
    def getXPos(self):
        return self.size + self.x
    
    def getYPos(self):
        return self.y
    
    
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

#print(background.get_rect())
#retorna left top width height, lembrando que width e height se referem
#ao tamanho da imagem, contando os pixeis vazios

#lista = list(background.get_rect())
#print(lista)
#funciona por algum motivo

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
cooldownSpawn = 3500
#Ta um bom cooldown pra testes

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
        if disparo.getYPos() < -100:
            disparos.pop(disparos.index(disparo))
            
    #for disparo in disparosInimigos:
    #    disparo.atirar()
    
    nowSpawn = pygame.time.get_ticks()
    if nowSpawn-lastSpawn>=cooldownSpawn:
        inimigos.append(Enemy(screen, 10, 100, 100, True, "tests/PyGame/starSprite.png", 300, 2, 5, 5, screen.get_width(), 1, "tests/PyGame/starSprite.png", True))
        lastSpawn = pygame.time.get_ticks()
        
    for inimigo in inimigos:   
        inimigo.update()
        for disparo in disparos:
            if inimigo.checkContact(disparo):
                inimigo.sofrerDano(disparo.dano)
                disparos.pop(disparos.index(disparo))
                #parece não estar sofrendo dano
        if inimigo.getLife() <= 0:
            inimigos.pop(inimigos.index(inimigo))
        
    for disparo in disparosInimigos:
        disparo.update()
        #Depois atualizar isso pra pegar a hitbox do player, como no inimigo
        if disparo.getXPos() == testImage.get_rect().centerx + testImageX and disparo.getYPos() == testImageY:
            disparosInimigos.pop(disparosInimigos.index(disparo))
            #Dar dano ao player ou coisa parecida
            
    pygame.display.update()
    #Sem isso a tela fica completamente preta
    
    Clock.tick(60)
    #Limita a quantidade maxima de frames por segundo