import pygame
import sys


pygame.init()
screen = pygame.display.set_mode((800,500))
clock = pygame.time.Clock()
pygame.display.set_caption("Navegando entre as telas do pygame")

font = pygame.font.Font(None, 60)

gameTitle = font.render("Cosmos Learning", True, "blue")
startText = font.render("Iniciar", True, "blue")

startButtonBackground = pygame.surface.Surface((300,100))
startButtonBackground.fill("red")
startButtonSize = list(startButtonBackground.get_rect())
#[0] = alguma coisa
#[1] = alguma coisa
#[2] = width
#[3] = height
startButtonOffset = [
    screen.get_width()/2,
    300
]

currentScreen = "home"

def showHomeScreen():
    screen.blit(gameTitle, ((screen.get_width()/2)-(gameTitle.get_width()/2),100))
    screen.blit(startButtonBackground, (startButtonOffset[0]-(startButtonBackground.get_width()/2),300))
    startButtonBackground.blit(startText, ((startButtonBackground.get_width()/2)-(startText.get_width()/2),(startButtonBackground.get_height()/2)-(startText.get_height()/2)))
    #[0] = X [1] = Y

def showGame():
    screen.fill("red")

def showCreditos():
    pass

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
            
            if mouse[0] == True and  mousePosition[0]>= startButtonOffset[0] and mousePosition[0]<= (startButtonOffset[0]+startButtonSize[2]) and mousePosition[1]>=startButtonOffset[1] and mousePosition[1]<=(startButtonOffset[1]+startButtonSize[3]):
                currentScreen = "game"
    
    
    clock.tick(60)
    pygame.display.update()
    