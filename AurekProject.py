#Import des modules externes
from tkinter import *
import os

#Création de la fenêtre
frame = Tk()
frame.title("Aurek Project")
frame.geometry("800x450")
frame.resizable(False, False)


#Création du canvas de menu
Canvas = Canvas(bg="black", height = 450, width = 800)
Canvas.pack()

fileBackground = PhotoImage(file = os.getcwd() + "/librairies/images/terrain/background.gif")

background = menuCanvas.create_image(400,225,image= fileBackground)

#Lancement de la fenêtre
frame.mainloop()
