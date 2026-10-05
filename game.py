from tkinter import *
from tkinter import messagebox
from traceback import print_tb

from PIL import Image, ImageTk
import random

root = Tk()
root.config(background="black")
root.geometry("1024x680")


posSuelo = 580

class Object():

    def __init__(self, posX, posY, height, width, saltando):
        self.posX = posX
        self.posY = posY
        self.height = height
        self.width = width
        self.saltando = saltando
        


        imagen = Image.open("player.png")
        imagen = imagen.resize((100, 100))

        self.imagen = ImageTk.PhotoImage(imagen)

        self.label = Label (
            root,
            image=self.imagen
        )


        self.label.place (
            x=self.posX,
            y=self.posY,
            height=self.height,
            width=self.width
        )

    def gravedad(self): # la gravedad va sumando 10 px hasta que toque el suelo (580)
    
            if self.posY < posSuelo and self.saltando == False: 

                self.posY += 10
    
                self.label.place (
                    x=self.posX,
                    y=self.posY
                )
    
            root.after(50, self.gravedad)

    def saltar(self):

        if player1.posY == posSuelo:

            self.saltando = True

            self.saltandoMovimiento(15)

    def saltandoMovimiento(self, contador):

        if contador > 0:

            self.posY -= 10


            
            self.label.place (
                x=self.posX,
                y=self.posY
            )

            root.after(
                10,
                self.saltandoMovimiento,
                contador - 1
            )

        else:

            self.saltando = False


    

    def mover(self, event):

        self.teclas = set()


            
        if event.keysym == "Up":
           self.saltar()

        if event.keysym == "Left":
            self.posX -= 10

        if event.keysym == "Right":
            self.posX += 10



        obstacle1.hitbox()
        


        self.label.place (
            x=self.posX, 
            y=self.posY
        )





class Obstacle:

    def __init__(self, posX, posY, height, width):

        self.posX = posX
        self.posY = posY
        self.height = height
        self.width = width


        self.label = Label(
            root,
            background='red'
        )

        self.label.place (
            x=self.posX,
            y=self.posY,
            height=self.height,
            width=self.width
        )

    def hitbox(self):


        if (player1.posX + player1.width > self.posX and
            player1.posX < self.posX + self.width and
            player1.posY + player1.height > self.posY and
            player1.posY < self.posY + self.height):

            print('has muerto tontopolla')

            

            player1.posX = 0

    def moverObs(self):

        
            
        self.posX -= 10

        self.label.place (
            x=self.posX,
            y=self.posY
        )

        root.update()

        root.after(10, self.moverObs)

        if (self.posX + self.width) <= 0:

            self.posX = 1024
            self.height = random.randint(50, 150)
            self.width = random.randint(10, 100)
            self.posY = posSuelo



            self.label.place (
                x=self.posX,
                y=self.posY,
                height=self.height,
                width=self.width
            )
        self.hitbox()
            
            
            
    
    


player1 = Object(20, 400, 100, 100, False)

obstacle1 = Obstacle(300, posSuelo - 100, 100, 30)

player1.gravedad()
obstacle1.moverObs()


tejo = Object(70, 100, 190, 200)

messagebox.showinfo()





root.bind("<KeyPress>", player1.mover)


root.mainloop()