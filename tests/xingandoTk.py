from tkinter import *

def eu():
    global tituloLabel
    tituloLabel.config(text="eu")

def amo():
    global tituloLabel
    tituloLabel.config(text="amo")

def tkinter():
    global tituloLabel
    tituloLabel.config(text="tkinter")


window  = Tk()
window.title("Caro tkinter")

frameGeral = Frame(master=window, background="purple")
frameTitulo = Frame(master=frameGeral, background="grey", pady=200, padx=300)
frameBtn = Frame(master=frameGeral, background="black", pady=20, padx=300)

tituloLabel = Label(master=frameTitulo,background="cyan", text="Eu n gosto do tkinter", pady=70)

btn1 = Button(master=frameBtn, background="red", text="Eu", padx=70, command= lambda: eu())
#O lamda permite passar a função com argumentos
btn2 = Button(master=frameBtn, background="blue", text="não", padx=70, command=lambda: amo())
btn3 = Button(master=frameBtn, background="green", text="gosto do tkinter", padx=70, command=lambda: tkinter())

tituloLabel.pack(fill=X)
btn1.pack(side=LEFT)
btn2.pack(side=LEFT)
btn3.pack(side=LEFT)

frameGeral.pack(fill=BOTH)
frameTitulo.pack(fill=BOTH)
frameBtn.pack()

#window.geometry("700x500")


window.mainloop()


