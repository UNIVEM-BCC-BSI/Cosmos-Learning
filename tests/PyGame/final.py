import pygame
import random
from random import randint
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800,500), pygame.FULLSCREEN)
clock = pygame.time.Clock()
pygame.display.set_caption("Teste projeto finalizado")
#Fazer array de backgrounds aq, para nivel
background = pygame.image.load("tests/PyGame/testBackground.png")
levelBackgrounds = [background, background]
currentLevel = -1


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
class Level():
    def __init__(self, tela, backgroundSurface, inputCooldown, spawnCooldown, vida, vidaSurface, qtndCompletar, inimigoSprite, dano,inimigoSpeed, inicioNumero, fimNumero, font):
        global scroolOffset
        
        scroolOffset = 0
        self.tela = tela
        self.vida = vida
        self.inicio = inicioNumero
        self.fim = fimNumero
        self.defeated = False
        self.requisito = qtndCompletar
        self.spriteInimigo = inimigoSprite
        self.listaInimigos = []
        self.font = font
        self.inimigoSpeed = inimigoSpeed
        self.now = pygame.time.get_ticks()
        self.lastInput = pygame.time.get_ticks()
        self.inputCooldown = inputCooldown
        self.spawnCooldown = spawnCooldown
        self.lastSpawn = pygame.time.get_ticks()
        self.background = backgroundSurface
        self.vidaSurfaces = [vidaSurface for i in range(self.vida)]
        self.dano = dano
        self.entrada = ""
        
    def sofrerDano(self, dano):
        self.vida -= dano
        if self.vida <= 0:
            self.defeated = True
            
    def spawnarInimigo(self):
        enemy = Inimigo(self.tela, self.spriteInimigo, self.dano,self.font,
                        100, 700, -100, self.inimigoSpeed, self.inicio, self.fim)
        
        self.listaInimigos.append(enemy)
        
    def update(self):
        global scroolOffset, scroolSpeed
        
        
        self.now = pygame.time.get_ticks()
        
        screen.blit(self.background, (0,scroolOffset))
        screen.blit(self.background, (0, scroolOffset-self.background.get_height()))
        scroolOffset += scroolSpeed
        scroolSpeed += 0.01
        
        if scroolOffset >= self.background.get_height():
            scroolOffset = 0
        
        if self.now-self.lastSpawn > self.spawnCooldown:
            self.spawnarInimigo()
            self.lastSpawn = pygame.time.get_ticks()
        
        keys = pygame.key.get_pressed()
    

        incluidos = self.font.render(self.entrada, True, "white")

        self.tela.blit(incluidos, (350,50))

        apertado = ""

        

        if self.now-self.lastInput>self.inputCooldown:
        

            if keys[pygame.K_0]:

                self.entrada += "0"

                self.lastInput = pygame.time.get_ticks()

            elif keys[pygame.K_1]:

                self.entrada += "1"

                self.lastInput = pygame.time.get_ticks()

            elif keys[pygame.K_2]:

                self.entrada += "2"

                self.lastInput = pygame.time.get_ticks()

            elif keys[pygame.K_3]:

                self.entrada += "3"

                self.lastInput = pygame.time.get_ticks()

            elif keys[pygame.K_4]:

                self.entrada += "4"

                self.lastInput = pygame.time.get_ticks()

            elif keys[pygame.K_5]:

                self.entrada += "5"

                self.lastInput = pygame.time.get_ticks()

            elif keys[pygame.K_6]:

                self.entrada += "6"

                self.lastInput = pygame.time.get_ticks()

            elif keys[pygame.K_7]:

                self.entrada += "7"

                self.lastInput = pygame.time.get_ticks()

            elif keys[pygame.K_8]:

                self.entrada += "8"

                self.lastInput = pygame.time.get_ticks()

            elif keys[pygame.K_9]:

                self.entrada += "9"

                self.lastInput = pygame.time.get_ticks()


        if keys[pygame.K_SPACE]:
            apertado = self.entrada
            self.entrada = ""
            
          
        self.updateVida()
          
        for inimigo in self.listaInimigos:

        #todo tirar inimigo quando morre

            if inimigo.vivo == True:

                inimigo.update(apertado)
                if inimigo.getY() > 500:
                    self.sofrerDano(inimigo.dano)

            else:

                self.listaInimigos.pop(self.listaInimigos.index(inimigo))
    
    def updateVida(self):
        #textoVida = "Vida: " + str(self.vida)
        #textoVida = self.font.render(textoVida, True, "white")
        #self.tela.blit(textoVida, (0,0))
        for i in range(self.vida):
            self.tela.blit(self.vidaSurfaces[i], (self.vidaSurfaces[i].get_width()*i,0))
                
        
            
        

        





class Inimigo():
    def __init__(self, tela, objetoSprite, dano, font,inicioXSpawn, fimXSpawn, ySpawn, speed, inicioNum, fimNum):
        self.tela = tela
        self.image = objetoSprite
        self.dano = dano
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
            
    def getY(self):
        return self.y+(self.size[3]/2)


#END CLASSES

#GAMEPLAY VARIABLES

# disparos = []
# inimigos = []
# disparosInimigos = []

# cooldownDisparo = 300
# cooldownSpawn = 3500
#Ta um bom cooldown pra testes

#diferença de ticks necessaria para poder atirar
# lastDisparo = pygame.time.get_ticks()
# lastSpawn = pygame.time.get_ticks()

now = pygame.time.get_ticks()
cooldown = 500
last = pygame.time.get_ticks()

fontGame = pygame.font.Font(None, 30)


#maxVida = 10
#jogador = Player(screen, "tests/PyGame/starSprite.png", "tests/PyGame/starSprite.png", maxVida, None, 30, 400, 400, 2, 2, screen.get_width(), screen.get_height(), cooldownDisparo, 5, 4)

#QUESTION SYTEM VARIABLES
fontPergunta = pygame.font.Font(None, 50)
fontResposta = pygame.font.Font(None, 35)


# perguntas = [{
#     "question" : "Quanto é um mais um?",
#     "answers" : [1,2,3],
#     "indexCorreta" : 1
# },
# {
#     "question" : "Quanto é dois mais dois?",
#     "answers" : [2,4,6],
#     "indexCorreta" : 1
# }
#            ]

#talvez de pau
#objetos = []

    
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


scroolSpeed = 0.1
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
    global screen, currentScreen,scroolOffset, scroolSpeed, background, gameTitle, startButtonBackground, startButtonOffset, startText
    
    for event in pygame.event.get():
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
 
currentLevel = 0
spriteInimigo = pygame.image.load("./tests/PyGame/inimigo_1.png")
spriteInimigo = pygame.transform.scale(spriteInimigo, (50,50))

background = pygame.image.load("./tests/PyGame/background.png")
background = pygame.transform.scale(background, (800,500))
vermelho = pygame.surface.Surface((50,25))
vermelho.fill("red")

niveis = [
    Level(screen, background, 500, 1000, 10, vermelho, 5, spriteInimigo,1, 1, 1, 10, fontGame),
    Level(screen, background, 500, 1000, 10, vermelho, 5, spriteInimigo, 1, 2, 10, 20, fontGame),
    Level(screen, background, 500, 1000, 10, vermelho, 5, spriteInimigo, 1, 3, 20, 30, fontGame)
]

 
def showGame():
    
    niveis[currentLevel].update()
        
    
        
    
        


    


def showCreditos():
    global screen, currentScreen,scroolOffset, scroolSpeed, background, creditOffsetX, creditosNames, creditsMarginY, creditsOffsetY, creditsTextHeight, creditsGoBack, currentScreen
    
    for event in pygame.event.get():
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
        
            if (mouse[0] == True and mousePosition[0]>=0 and 
                  mousePosition[0]<= creditsGoBack.get_width() and 
                  currentScreen == "creditos"):
                currentScreen = "home"
    
    screen.blit(background, (0,scroolOffset))
    screen.blit(background, (0,scroolOffset-background.get_height()))
    increaseSpeed()
    checkResetBackground()
    
    screen.blit(creditsGoBack, (0,0))
    for i in range(len(creditosNames)):
        screen.blit(creditosNames[i], (creditOffsetX-(creditosNames[i].get_width()/2),(creditsOffsetY+(creditsTextHeight*i)+creditsMarginY)))

show = None



#COISAS DENTRO DO WHILE TRUE
while True:
    
    screen.fill("black")
    
    if currentScreen == "home":
        showHomeScreen()
    elif currentScreen == "game":
        showGame()
    elif currentScreen == "creditos":
        showCreditos()
    elif currentScreen == "perguntar" and nextLevel == True:
        showPergunta(True)
    elif currentScreen == "perguntar" and nextLevel == False:
        showPergunta(False)
    elif currentScreen == "selectQuestion":
        selectQuestion()
    elif currentScreen == "selectLevel":
        selectLevel()
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            
    clock.tick(60)
    pygame.display.update()