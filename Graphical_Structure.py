### Infos ###
_version_ = "0.0.1"
_author_ = "Maxime Vincent"
_name_ = "Avatar_Generator"
_description_ = "Création d'avatar selon une image ou la camera embarquée"
#############

# L'importation des librairies
import PIL
from PIL import Image, ImageTk
import pytesseract
from tkinter import *
import cv2

width, height = 960, 650
webcam = cv2.VideoCapture(0)
webcam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
webcam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

# Création d'une fenêtre avec la classe Tk :
window = Tk()
# Création d'un titre pour la fenêtre :
window.title(_name_)
# Définir les dimensions par défaut la fenêtre principale :
window.geometry("960x550")
# Empêcher l'utilisateur de modifier la taille de la fenêtre principale :
window.resizable(width=False, height=False)

# Création d'une barre de menu utilisateur :
menuBar = Menu(window)
# Configuration du menu dans la fenêtre :
window.config(menu = menuBar)
# Assigner l'onglet "File" à la barre de menu :
menufile = Menu(menuBar, tearoff=0)
# Définition de "File" dans la barre de menu :
menuBar.add_cascade(label="File", menu=menufile)
# Ajout de l'option "Quit" dans l'onglet "File" :
menufile.add_command(label="Quit", command=window.destroy)

canvas = Label(window)
canvas.pack()

def show_frame():
    _, frame = webcam.read()
    frame = cv2.flip(frame, 1)
    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    img = PIL.Image.fromarray(cv2image)
    imgtk = ImageTk.PhotoImage(image=img)
    canvas.imgtk = imgtk
    canvas.configure(image=imgtk)
    canvas.after(10, show_frame)

# Appeler la fonction d'affichage du flux de la webcam :
show_frame()

# Affichage de la fenêtre créée :
window.mainloop()