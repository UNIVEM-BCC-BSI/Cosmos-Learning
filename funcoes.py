<<<<<<< HEAD
import random


#Como passar argumentos para a função pelo botao do tkinter
#This can be done using a lambda, like so:
#button = Tk.Button(master=frame, text='press', command= lambda: action(someNumber))
#This is a simple way to bind the argument without an explicit wrapper method or modifying the original action.

class Player:
    "Gerencia os pontos do jogador, aumentando e os diminuindo"
    def __init__(self):
        self.pontos = 0

    def aumentarPontos(self, qtnd):
        "Aumenta o valor da variavel pontos na quantidade informada"
        
        self.pontos += qtnd

    def diminuirPontos(self, qtnd):
        "Reduz o valor da variável pontos na quantidade informada "
        
        self.pontos -= qtnd

class Pergunta:
    "Cada pergunta deve ser inicializada como um objeto inserindo um array e o index da resposta correta nesse array"
    def __init__(self, respostas, indexDaCorreta):
        "respostas deve ser um array e o index deve ser o index da resposta correta"
        self.respostas = respostas
        self.respostaCorreta = respostas[indexDaCorreta]
        
    def checar(self, respostaSelecionada):
        if respostaSelecionada == self.respostaCorreta:
            return True
        else:
            return False
        
    def reorganizar(self):
        "Dada as 5 respostas, irá reogarnizar e retornar um array contendo a nova ordem de respostas"
        respostas = self.respostas
        con = 1
        new_respostas = []
        while con <=5:
            adicionarResposta = random.choice(respostas)
            new_respostas.append(adicionarResposta)
            respostas.remove(adicionarResposta)
            con+=1
        
        self.respostas = new_respostas
=======
import random


#Como passar argumentos para a função pelo botao do tkinter
#This can be done using a lambda, like so:
#button = Tk.Button(master=frame, text='press', command= lambda: action(someNumber))
#This is a simple way to bind the argument without an explicit wrapper method or modifying the original action.

class Player:
    "Gerencia os pontos do jogador, aumentando e os diminuindo"
    def __init__(self):
        self.pontos = 0

    def aumentarPontos(self, qtnd):
        "Aumenta o valor da variavel pontos na quantidade informada"
        
        self.pontos += qtnd

    def diminuirPontos(self, qtnd):
        "Reduz o valor da variável pontos na quantidade informada "
        
        self.pontos -= qtnd

class Pergunta:
    "Cada pergunta deve ser inicializada como um objeto inserindo um array e o index da resposta correta nesse array"
    def __init__(self, respostas, indexDaCorreta):
        "respostas deve ser um array e o index deve ser o index da resposta correta"
        self.respostas = respostas
        self.respostaCorreta = respostas[indexDaCorreta]
        
    def checar(self, respostaSelecionada):
        if respostaSelecionada == self.respostaCorreta:
            return True
        else:
            return False
        
    def reorganizar(self):
        "Dada as 5 respostas, irá reogarnizar e retornar um array contendo a nova ordem de respostas"
        respostas = self.respostas
        con = 1
        new_respostas = []
        while con <=5:
            adicionarResposta = random.choice(respostas)
            new_respostas.append(adicionarResposta)
            respostas.remove(adicionarResposta)
            con+=1
        
        self.respostas = new_respostas
>>>>>>> 6856231f7414b6442cfebe73b251d1a57800fe55
        