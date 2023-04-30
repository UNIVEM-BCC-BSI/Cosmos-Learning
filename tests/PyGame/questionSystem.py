import pygame
import random
from sys import exit

#TODO fazer sistema de click nas respostasz

pygame.init()
screen = pygame.display.set_mode((800,500))
pygame.display.set_caption("Teste de sistema de perguntas")
clock =pygame.time.Clock()

fontPergunta = pygame.font.Font(None, 50)
fontResposta = pygame.font.Font(None, 35)

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
    

while True:
    con = 0
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse = list(pygame.mouse.get_pressed())
            mousePosition = list(pygame.mouse.get_pos())
            for i in range(len(objetos[con].respostas)):
                if (mouse[0] and mousePosition[0]>=200 and
                mousePosition[0] <= 200+objetos[con].respostas[i].get_height() and
                mousePosition[1]>= 100+objetos[con].text.get_height()+50 + ((20 + objetos[con].respostas[i].get_height())*i)):
                    print(objetos[con].gotRight(objetos[con].respostas[i]))
    
    objetos[con].update()
    
    
    
    
    clock.tick(60)        
    pygame.display.update()
    