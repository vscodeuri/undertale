import time
from tkinter import *
from tkinter import messagebox

from PIL import Image, ImageTk

import random


# hacer el movimiento mas smooth
# Movimiento fluido
# Diagonales
# Sistema de colisiones reutilizable
# Lista de obstáculos
# Sistema de vida/muerte
# Reinicio
# Diferentes enemigos
# Menú
# Game Over
# Separar archivos
# Herencia
# Sistema de estados (def checkCollisions return True and Fals)

root = Tk()
root.config(background="black")
root.geometry("1024x680")

posSuelo = 580

class Player:
    def __init__(self, health, posX, posY, height, width):
        self.health = health
        self.posX = posX
        self.posY = posY
        self.height = height
        self.width = width

        self.velocidad = 10

        self.arriba = False
        self.abajo = False
        self.izquierda = False
        self.derecha = False
        # que listo soy:
        try:
            corazon = Image.open("corazonPlayer.png").convert("RGBA")
        except:
            corazon = Image.open("development/corazonPlayer.png").convert("RGBA")

        corazon = corazon.resize((20, 20))

        self.imagen = ImageTk.PhotoImage(corazon)

        self.hitbox = Frame(root, width=self.width, height=self.height, bg="black")
        self.hitbox.place(x=self.posX, y=self.posY)





        self.label = Label (
            root,
            image=self.imagen,
            bg="black"
        )

        self.label.place(
            x=self.posX,
            y=self.posY,
            height=self.height,
            width=self.width
        )

        root.bind("<KeyPress>", self.keyDown)
        root.bind("<KeyRelease>", self.keyUp)





    def keyDown(self, event): # esta funcion es para que cuando presiones la tecla, los eventos de las direcciones se activen
        if event.keysym == "Up":
            self.arriba = True

        if event.keysym == "Down":
            self.abajo = True

        if event.keysym == "Left":
            self.izquierda = True

        if event.keysym == "Right":
            self.derecha = True

        self.movePlayer(event)
        self.boundaries()

    def keyUp(self, event): # una vez la tecla se deje de presionar todos los eventos van a false

        if event.keysym == "Up":
            self.arriba = False

        if event.keysym == "Down":
            self.abajo = False

        if event.keysym == "Left":
            self.izquierda = False

        if event.keysym == "Right":
            self.derecha = False





    def movePlayer(self, event): # cuando de le a cada direccion, que sume los px correspondentes

        if event.keysym == "Up" and self.arriba:
            self.posY -= self.velocidad

        if event.keysym == "Down" and self.abajo:
            self.posY += self.velocidad

        if event.keysym == "Left" and self.izquierda:
            self.posX -= self.velocidad

        if event.keysym == "Right" and self.derecha:
            self.posX += self.velocidad



        self.label.place ( # actualiza la posicion para que se vea en pantalla el cambio
            x=self.posX,
            y=self.posY
        )

        

    def boundaries(self):
        if self.posX < 170: # left wall
            self.posX = 170

        if (self.posX + self.width) > 870: # right wall
            self.posX = 870 - self.width

        if self.posY < 210: # top wall
            self.posY = 210

        if (self.posY + self.height) > 510: # bottom wall
            self.posY = 510 - self.height

        self.label.place (
            x=self.posX,
            y=self.posY
        )

    def contador(self):

        contador = 0

        contadorText = Label(root, font='arial 16', text='Muertes: ', background='black')
        contadorText.place(x=100, y=100)

    

class Obstacle:
    
    def __init__(self, posX, posY, height, width):
        self.posX = posX
        self.posY = posY
        self.height = height
        self.width = width

        self.label = Label (
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
        if (player.posX + player.width > self.posX and
            player.posX < self.posX + self.width and
            player.posY + player.height > self.posY and
            player.posY < self.posY + self.height):

            print('has muerto tontopolla.')

            player.posX = 0
            player.posY = 0


    def moveObject(self):


        self.posY += 10

        self.label.place (
            x=self.posX,
            y=self.posY
        )


        if (self.posY - self.height) >= posSuelo: # si llega al final

            self.posY = 0 - self.height
            self.posX = random.randint(200, 900)

            self.label.place (
                x=self.posX,
                y=self.posY
            )

        root.after(10, self.moveObject)

        self.hitbox()








    



    

    





box = Label(root, background='black', borderwidth=2, relief="solid", highlightcolor='white', highlightthickness=7, height=20, width=100)
box.place(x=160, y=200)



player = Player(92, 170, 210, 30, 30)
enemy = Obstacle(400, 50, 100, 20)
enemy2 = Obstacle(200, -300, 100, 20)
enemy3 = Obstacle(400, -600, 100, 20)

enemy.moveObject()
enemy2.moveObject()
enemy3.moveObject()








root.mainloop()

