### Infos ###
_version_ = "0.0.1"
_author_ = "Maxime Vincent"
_name_ = "Avatar_Generator"
_description_ = "Création d'avatar selon une image ou la camera embarquée"
#############

# L'importation de l’ensemble des éléments du paquet tkinter :
from tkinter import *


# Création d'une fenêtre avec la classe Tk :
window = Tk()
# Création d'un titre pour la fenêtre :
window.title(_name_)
# Définir les dimensions par défaut la fenêtre principale :
window.geometry("800x600")
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


# Affichage de la fenêtre créée :
window.mainloop()
