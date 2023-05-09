import pygame
import random
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800,500), pygame.FULLSCREEN)
clock = pygame.time.Clock()
pygame.display.set_caption("Teste projeto finalizado")
background = pygame.image.load("tests/PyGame/testBackground.png")

#CLASSES

#QUESTION SYSTEM
class Pergunta():
    def __init__(self, screen,textoPergunta, listaRespostas, indexRespostaCorreta):
        self.tela = screen
        self.text = textoPergunta
        self.sizePergunta = list(textoPergunta.get_rect())
        self.respostas = listaRespostas
        self.correta = listaRespostas[indexRespostaCorreta]
        self.solved = False
        self.reorganizar()
    
    def solve(self):
        self.solved = True
    
    def isSolved(self):
        return self.solved
    
    def gotRight(self, selectedAnswer):
        if selectedAnswer == self.correta:
            return True
        else:
            return False
    
    def reorganizar(self):
        respostas = self.respostas.copy()
        newRespostas = []
        for i in range(len(respostas)):
            lista = random.choice(respostas)
            respostas.pop(respostas.index(lista))
            newRespostas.append(lista)
        
        self.respostas = newRespostas.copy()
            
        
            
            
        
        
    def update(self):
        self.tela.blit(self.text, ((self.tela.get_width()/2-self.sizePergunta[2]/2),100))
        
        for i in range(len(self.respostas)):
            mouse = list(pygame.mouse.get_pressed())
            mousePosition = list(pygame.mouse.get_pos())
            
            self.tela.blit(self.respostas[i], (200, (100+self.text.get_height()+50 + ((20 + self.respostas[i].get_height())*i))))

#GAMEPLAY
class Player():
    def __init__(self, tela, playerSprite, disparoSprite, vida, fontVida, fontVidaSize, startXPos, startYPos, Xspeed, Yspeed, limitXPos, limitYPos, disparoCooldown, disparoDano, shootSpeed):
        self.tela = tela
        self.playerImage = pygame.image.load(playerSprite)
        self.size = list(self.playerImage.get_rect())
        self.shootImage = pygame.image.load(disparoSprite)
        self.vida = vida
        self.font = pygame.font.Font(fontVida, fontVidaSize)
        self.x = startXPos
        self.y = startYPos
        self.Xspeed = Xspeed
        self.ySpeed = Yspeed
        self.limitPos = [limitXPos, limitYPos]
        self.cooldown = disparoCooldown
        self.shootDamage = disparoDano
        self.shootSpeed = shootSpeed
        self.now = pygame.time.get_ticks()
        self.lastShoot = pygame.time.get_ticks()
        self.derrotado = False
        self.vidaSurfaces = []
        surfaceSize = 200 // vida
        for i in range(self.vida):
            addSurface = pygame.surface.Surface((surfaceSize,25))
            addSurface.fill("red")
            self.vidaSurfaces.append(addSurface)

    def checkContact(self, disparo):
        inicioHitboxX = self.x
        fimHitboxX = self.x + self.size[2]
        fimHitboxY = self.y
        inicioHitboxY = self.y + self.size[3]
        
        if disparo.x >= inicioHitboxX and disparo.x <= fimHitboxX and disparo.y <= inicioHitboxY and disparo.y >= fimHitboxY:
            self.sofrerDano(disparo.dano)
            return True

    def sofrerDano(self, qtndDano):
        self.vida -= qtndDano
        if self.vida <= 0 :
            self.derrotado = True
        
    def update(self):
        if self.derrotado == False:
            
            self.now = pygame.time.get_ticks()
            keys = pygame.key.get_pressed()
            
            if 0 <= self.y and keys[pygame.K_w]:
                #Se existe pygame.K_w dentro de keys
                self.y -= self.ySpeed
            if self.limitPos[1] >= self.y and keys[pygame.K_s]:
                self.y += self.ySpeed
            
            if 0 <= self.x and keys[pygame.K_a]:
                self.x -= self.Xspeed
            if self.limitPos[0] >= self.x and keys[pygame.K_d]:
                self.x += self.Xspeed
            
            if keys[pygame.K_SPACE]:
                nowDisparo = pygame.time.get_ticks()
                if nowDisparo - lastDisparo >= cooldownDisparo:
                    disparos.append(Tiro(self.tela, self.x, self.y, self.shootSpeed, self.shootDamage))
                    #permite manter varios disparos ao mesmo tempo
            
            self.tela.blit(self.playerImage, (self.x, self.y))
            self.updateVida()
        else:
            pass
            #Sistema para voltar para tela de inicio
        
    def updateVida(self):
        #textoVida = "Vida: " + str(self.vida)
        #textoVida = self.font.render(textoVida, True, "white")
        #self.tela.blit(textoVida, (0,0))
        for i in range(self.vida):
            self.tela.blit(self.vidaSurfaces[i], (self.vidaSurfaces[i].get_width()*i,0))
        
class Enemy:
    def __init__(self, tela, vida, spawnPositionX, spawnPositionY, atirador, caminhoDisparo, cooldownDisparo,disparoSpeed, dano, speedX, speedLimitX, speedY, caminhoImagem, isMovingLeft):
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
         
        #print(type(self.image.get_rect()))
               
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
    
    def getXPos(self):
        return self.x + self.size[2]
    
    def getYPos(self):
        return self.y + self.size[3]
    
    def checkContact(self, jogador):
        inicioHitboxX = self.x
        fimHitboxX = self.x + self.size[2]
        fimHitboxY = self.y
        inicioHitboxY = self.y + self.size[3]
        
        if (jogador.x >= inicioHitboxX and jogador.x <= fimHitboxX and
            jogador.y <= inicioHitboxY and
            jogador.y >= fimHitboxY):
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

#END CLASSES

#GAMEPLAY VARIABLES
testText = pygame.font.Font(None, 50)
#Gera uma fonte de tipo e tamanho especificado
textSurface = testText.render("Testando PyGame",False,"orange")
#Esta passando os argumentos em ordem: Text, Antialias, Color
#É uma Surface, está gerendo uma Surface com conteudo especificado, se o antialias for True
#o texto fica mais "arredondado"

#Posição X do testImage

disparos = []
inimigos = []
disparosInimigos = []

cooldownDisparo = 300
cooldownSpawn = 3500
#Ta um bom cooldown pra testes

#diferença de ticks necessaria para poder atirar
lastDisparo = pygame.time.get_ticks()
lastSpawn = pygame.time.get_ticks()

jogador = Player(screen, "tests/PyGame/starSprite.png", "tests/PyGame/starSprite.png", 10, None, 30, 400, 400, 2, 2, screen.get_width(), screen.get_height(), cooldownDisparo, 5, 4)

#QUESTION SYTEM VARIABLES
fontPergunta = pygame.font.Font(None, 50)
fontResposta = pygame.font.Font(None, 35)
perguntas = [{
    "question" : "Quanto é um mais um?",
    "answers" : [1,2,3],
    "indexCorreta" : 1
},
{
    "question" : "Quanto é dois mais dois?",
    "answers" : [2,4,6],
    "indexCorreta" : 1
}
           ]


objetos = []

for i in perguntas:
    adicionarTextoPergunta = fontPergunta.render(i["question"], True, "red")
    adicionarRespostas = []
    for j in i["answers"]:
        j = str(j)
        listaRespostas = fontResposta.render(j, True, "red")
        adicionarRespostas.append(listaRespostas)
    
    adicionar = Pergunta(screen, adicionarTextoPergunta, adicionarRespostas, i["indexCorreta"])
    objetos.append(adicionar)
    
#HOME VARIABLES
font = pygame.font.Font(None, 60)

gameTitle = font.render("Cosmos Learning", True, "blue")
startText = font.render("Iniciar", True, "blue")
homeCreditsText = font.render("Créditos", True, "blue")

startButtonBackground = pygame.surface.Surface((300,100))

#startButtonBackground.set_alpha(0)
#assim desaparece ate o texto de inicio de jogo

startButtonBackground.fill("red")
startButtonSize = list(startButtonBackground.get_rect())
startButtonWidthOffset = 400
startButtonHeightOffset = 300
#[0] = alguma coisa
#[1] = alguma coisa
#[2] = width
#[3] = height

startButtonOffset = [
    startButtonWidthOffset,
    startButtonHeightOffset
]

creditosNames = [font.render("Créditos", True, "white"),
                 font.render("Lucas Meirelles de Souza", True, "white"),
                 font.render("Guilherme Ramos Vaz", True, "white"),
                 font.render("Leandro Poletti de Oliveira", True, "white"),
                 font.render("Luan Alexandre Mazzotti Girotto", True, "white"),
                 font.render("Pedro Santilli de Souza", True, "white")
                 ]
creditOffsetX = 400
creditsOffsetY = 100
creditsMarginY = 50
creditsTextHeight = font.get_height()
creditsGoBack = font.render("Voltar", True, "blue")


scroolSpeed = 1
increaseAmount = 0.1
scroolOffset = 0

currentScreen = "home"

def resetSpeed(initialSpeed):
    return [initialSpeed,0]

def checkResetBackground():
    global scroolOffset, background
    
    if scroolOffset >= background.get_height():
        scroolOffset = 0

def increaseSpeed():
    global scroolOffset, scroolSpeed, increaseAmount
    
    scroolOffset += scroolSpeed
    scroolSpeed += increaseAmount

def showHomeScreen():
    global screen, scroolOffset, scroolSpeed, background, gameTitle, startButtonBackground, startButtonOffset, startText
    
    screen.blit(background, (0,scroolOffset))
    screen.blit(background, (0,scroolOffset-background.get_height()))
    increaseSpeed()
    checkResetBackground()
    
    screen.blit(gameTitle, ((screen.get_width()/2)-(gameTitle.get_width()/2),100))
    screen.blit(startButtonBackground, (startButtonOffset[0]-(startButtonBackground.get_width()/2), 
                                        startButtonOffset[1]))
    startButtonBackground.blit(startText, ((startButtonBackground.get_width()/2)-(startText.get_width()/2),
                                           (startButtonBackground.get_height()/2)-(startText.get_height()/2)))
    #[0] = X [1] = Y
    #Falta fazer o butão de Créditos
    screen.blit(homeCreditsText,(screen.get_width()/2-(homeCreditsText.get_width()/2),(startButtonOffset[1]+startButtonBackground.get_height()+50)))
    #Fazer o código pra executar o botão
    
def showGame():
    global screen, background, scroolOffset, background, scroolSpeed, jogador, disparos, lastSpawn, cooldownSpawn, inimigos, disparosInimigos, currentScreen
    
    screen.blit(background, (0,scroolOffset))
    screen.blit(background, (0, scroolOffset-background.get_height()))
    
    scroolOffset += scroolSpeed
    scroolSpeed += 0.01
    
    if scroolOffset >= background.get_height():
        scroolOffset = 0
    
    jogador.update()
    for disparo in disparos:
        disparo.update()
        if disparo.getYPos() < -100:
            disparos.pop(disparos.index(disparo))
    
    nowSpawn = pygame.time.get_ticks()
    if nowSpawn-lastSpawn>=cooldownSpawn:
        inimigos.append(Enemy(screen, 10, 100, 100, True, "tests/PyGame/starSprite.png", 
                              300, 2, 5, 5, screen.get_width(), 1, 
                              "tests/PyGame/starSprite.png", True))
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
        if jogador.checkContact(disparo):
            disparosInimigos.pop(disparosInimigos.index(disparo))
            #Dar dano ao player ou coisa parecida
            
    if jogador.vida == 0:
        currentScreen = "home"

def showCreditos():
    global screen, scroolOffset, scroolSpeed, background, creditOffsetX, creditosNames, creditsMarginY, creditsOffsetY, creditsTextHeight, creditsGoBack
    
    screen.blit(background, (0,scroolOffset))
    screen.blit(background, (0,scroolOffset-background.get_height()))
    increaseSpeed()
    checkResetBackground()
    
    screen.blit(creditsGoBack, (0,0))
    for i in range(len(creditosNames)):
        screen.blit(creditosNames[i], (creditOffsetX-(creditosNames[i].get_width()/2),(creditsOffsetY+(creditsTextHeight*i)+creditsMarginY)))
        
def showPergunta():
    global objetos
    show = random.choice(seq)

#COISAS DENTRO DO WHILE TRUE
while True:
    
    if currentScreen == "home":
        showHomeScreen()
    elif currentScreen == "game":
        showGame()
    elif currentScreen == "creditos":
        showCreditos()
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse = list(pygame.mouse.get_pressed())
            #[0] = botao esquerdo
            #[1] = scroll
            #[2] = botao direito
            
            mousePosition = list(pygame.mouse.get_pos())
            #[0] = X
            #[1] = Y
            
            #print(mousePosition)
            #print(mouse)
            #print("--------------\nPosicao desejada:")
            #print("x:", startButtonOffset[0],"-",startButtonOffset[0]+startButtonSize[2])
            #print("y:", startButtonOffset[1],"-",startButtonOffset[1]+startButtonSize[3])
            #print("-------------")
            
            if (mouse[0] == True and  
                mousePosition[0]>= startButtonOffset[0]-startButtonBackground.get_width()/2 and 
                mousePosition[0]<= ((startButtonOffset[0]-startButtonBackground.get_width()/2)+startButtonSize[2]) and 
                mousePosition[1]>=startButtonOffset[1] and 
                mousePosition[1]<=(startButtonOffset[1]+startButtonSize[3]) and
                currentScreen == "home"
                ):
                currentScreen = "game"
            elif (mouse[0] == True and
                  mousePosition[0]>=startButtonOffset[0]-startButtonBackground.get_width()/2 and
                  mousePosition[0]<= ((startButtonOffset[0]-startButtonBackground.get_width()/2)+startButtonSize[2]) and
                  mousePosition[1]>= (startButtonOffset[1]+startButtonBackground.get_height()+50) and
                  mousePosition[1] <= ((startButtonOffset[1]+startButtonBackground.get_height()+50)+homeCreditsText.get_height()) and
                  currentScreen == "home"
                  ):
                currentScreen = "creditos"
            elif (mouse[0] == True and mousePosition[0]>=0 and 
                  mousePosition[0]<= creditsGoBack.get_width() and 
                  currentScreen == "creditos"):
                currentScreen = "home"
            
    clock.tick(60)
    pygame.display.update()