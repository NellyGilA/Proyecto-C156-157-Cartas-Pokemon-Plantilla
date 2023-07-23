from tkinter import *
#Importación módulos ImageTk e Image de la biblioteca PIL
from PIL import ImageTk, Image
import random
root=Tk()
root.title("Juego Pokémon sin fin")

root.geometry("800x600")
root.configure(background="orange")

img=ImageTk.PhotoImage(Image.open ("button.jpg"))

#Tarea 1: cargar 12 imágenes de las cartas de Pokémon.
pikachu =ImageTk.PhotoImage(Image.open ("pikachu.jpg"))
bulbasour =ImageTk.PhotoImage(Image.open ("bulbasour.jpg"))
Charmender =ImageTk.PhotoImage(Image.open ("charmender.jpg"))
Squirtle =ImageTk.PhotoImage(Image.open ("squirtle.jpg"))
Ratata =ImageTk.PhotoImage(Image.open ("ratata.jpg"))
nidoking =ImageTk.PhotoImage(Image.open ("nidoking.jpg"))
jigglypuff =ImageTk.PhotoImage(Image.open ("jigglypuff.jpg"))
meowth =ImageTk.PhotoImage(Image.open ("meowth.jpg"))
#Agregar aquí las 4 imágenes mas

#Creación la etiqueta para mostrar al jugador 1:
player1 = Label(root, text = "Jugador 1", bg = "red", fg = "white")
player1.place(relx = 0.1, rely = 0.3 , anchor =  CENTER)

#Tarea 2: Creación la etiqueta para mostrar al jugador 2:


#Creación etiqueta para mostrar la puntuación del jugador 1:
player_1_score_label = Label(root , bg = "royal blue", fg = "white")
player_1_score_label.place(relx = 0.1, rely = 0.4 , anchor =  CENTER)

#Tarea 3: Creación etiqueta para mostrar la puntuación del jugador 2:


#Listas de imágenes de Pokémones y lista los poderes
#Tarea 4: completa la lista pokemon_list, con las 4 imágenes agregadas en la Tarea 1 
pokemon_list = [pikachu,bulbasour,Charmender,Squirtle,Ratata,jigglypuff,meowth]
power_list = [200,60,100,50,50,40,70,60,70,30,70]

label = Label(root)
label.place(relx = 0.5, rely = 0.5 , anchor =  CENTER)

#Inicialización de variable player1_score con el valor 0
#Función para el jugador 1 
player1_score = 0
def player1():
    global player1_score
    random_no = random.randint(0,10)
    random_pokemon = pokemon_list[random_no]
    label["image"]=random_pokemon
    
    random_power_list = power_list[random_no]
    player1_score = player1_score + random_power_list
    player_1_score_label["text"] = str( player1_score)

#Botón para el jugador 1
player_1_btn = Button(root, image = img, command = player1)
player_1_btn.place(relx = 0.1, rely = 0.6 , anchor =  CENTER)

#Tarea 5: Inicialización de variable player2_score con el valor 0
#Tarea 6: Función para el jugador 2     


#Tarea 7: Botón para el jugador 2


root.mainloop()