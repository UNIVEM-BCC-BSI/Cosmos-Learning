for inimigo in inimigos:

        #todo tirar inimigo quando morre

        if inimigo.vivo == True:

            inimigo.update(apertado)

        else:

            inimigos.pop(inimigos.index(inimigo))