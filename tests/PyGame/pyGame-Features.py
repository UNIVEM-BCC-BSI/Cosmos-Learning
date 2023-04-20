import pygame
from sys import exit

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

testImage = pygame.image.load("./tests/PyGame/starSprite.png")
#Permite carregar uma imagem para mais tarde ser usada como Surface

testText = pygame.font.Font(None, 50)
#Gera uma fonte de tipo e tamanho especificado
textSurface = testText.render("Testando PyGame",False,"orange")
#Esta passando os argumentos em ordem: Text, Antialias, Color
#É uma Surface, está gerendo uma Surface com conteudo especificado, se o antialias for True
#o texto fica mais "arredondado"


while True:
    for event in pygame.event.get():
        #Gera uma lista de eventos registrados pelo pygame
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            #Fecha o interpretador do código impedindo o while True de continuar
                
    screen.blit(testSurface, (200,0))
    #Posiciona o testSurface dentro da Screen
    testSurface.blit(blue, (0,0))
    #Se estiver fora do alcance do display usado não vai renderizar
    screen.blit(green, (200,50))
    #Perceba que pygame permite sobreposição
    
    screen.blit(testImage, (500,100))
    #A tupla esta passando a margem que o objeto deve ter em X e Y
    #Lembrando que o ponto X = 0 e Y = 0 no pygame é no canto superior esquerdo
    
    screen.blit(textSurface,(500, 200))
    
    
    pygame.display.update()
    #Sem isso a tela fica completamente preta
    Clock.tick(60)
    #Limita a quantidade maxima de frames por segundo