#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

import global_nk
from Tkinter import *

class Interface(Frame):

    def __init__(self, fenetre, **kwargs):
        Frame.__init__(self, fenetre, width=768, height=576, **kwargs)
        self.pack(fill=BOTH)
        self.nb_clic = 0
        fenetre.title("NK")
        
        # Création de nos widgets
        self.message = Label(self, text="Vous n'avez pas cliqué sur le bouton.")
        self.message.pack()
        
        self.bouton_quitter = Button(self, text="Quitter", command=self.quit)
        self.bouton_quitter.pack(side="left")
        
        self.bouton_cliquer = Button(self, text="Cliquez ici", fg="red", command=self.stop)
        self.bouton_cliquer.pack(side="right")
        zone_dessin = Canvas(self, width=500, height=500, bg='yellow',bd=8,relief="ridge")
        zone_dessin.pack()
        zone_dessin.create_rectangle(100,100,200,200)

        fenetre['bg']='white'

        # frame 1
        Frame1 = Frame(fenetre, borderwidth=2, relief=GROOVE)
        Frame1.pack(side=LEFT, padx=30, pady=30)

        # frame 2
        Frame2 = Frame(fenetre, borderwidth=2, relief=GROOVE)
        Frame2.pack(side=LEFT, padx=10, pady=10)

        # frame 3 dans frame 2
        Frame3 = Frame(Frame2, bg="white", borderwidth=2, relief=GROOVE)
        Frame3.pack(side=RIGHT, padx=5, pady=5)

        # Ajout de labels
        Label(Frame1, text="Frame 1").pack(padx=10, pady=10)
        Label(Frame2, text="Frame 2").pack(padx=10, pady=10)
        Label(Frame3, text="Frame 3",bg="white").pack(padx=10, pady=10)

        menubar = Menu(fenetre)

        menu1 = Menu(menubar, tearoff=0)
        menu1.add_command(label="Créer", command=self.test)
        menu1.add_command(label="Editer", command=self.test)
        menu1.add_separator()
        menu1.add_command(label="Quitter", command=fenetre.quit)
        menubar.add_cascade(label="Fichier", menu=menu1)

        menu2 = Menu(menubar, tearoff=0)
        menu2.add_command(label="Couper", command=self.test)
        menu2.add_command(label="Copier", command=self.test)
        menu2.add_command(label="Coller", command=self.test)
        menubar.add_cascade(label="Editer", menu=menu2)

        menu3 = Menu(menubar, tearoff=0)
        menu3.add_command(label="A propos", command=self.test)
        menubar.add_cascade(label="Aide", menu=menu3)

        fenetre.config(menu=menubar)
    
    def stop(self):
        global_nk.setter('go', 0)

    def cliquer(self):
        self.nb_clic += 1
        self.message["text"] = "Vous avez cliqué {} fois.".format(self.nb_clic)

    def destroy(self):
        print "KILL"

    def test(self):
        print "Menu"
