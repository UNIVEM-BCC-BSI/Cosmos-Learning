import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((800,500))
clock = pygame.time.Clock()
pygame.display.set_caption("Navegando entre as telas do pygame")
background = pygame.image.load("tests/PyGame/testBackground.png")

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

creditosNames = [font.render("Créditos", True, "blue"),
                 font.render("B", True, "blue"),
                 font.render("C", True, "blue")]
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
    screen.fill("red")

def showCreditos():
    global screen, scroolOffset, scroolSpeed, background, creditOffsetX, creditosNames, creditsMarginY, creditsOffsetY, creditsTextHeight, creditsGoBack
    
    screen.blit(background, (0,scroolOffset))
    screen.blit(background, (0,scroolOffset-background.get_height()))
    increaseSpeed()
    checkResetBackground()
    
    screen.blit(creditsGoBack, (0,0))
    for i in range(len(creditosNames)):
        screen.blit(creditosNames[i], (creditOffsetX-(creditosNames[i].get_width()/2),(creditsOffsetY+(creditsTextHeight*i)+creditsMarginY)))
        
    
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
            sys.exit()
        
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
                
            elif (mouse[0] == True and mousePosition[0]>=0 and 
                  mousePosition[0]<= creditsGoBack.get_width() and 
                  currentScreen == "creditos"):
                currentScreen = "home"
    
    
    clock.tick(60)
    pygame.display.update()
    