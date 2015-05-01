#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

from Tkinter import *
from tkMessageBox import *

class Interface(Frame):

    def __init__(self, fenetre, **kwargs):
        Frame.__init__(self, fenetre, width=768, height=576, **kwargs)
        self.pack(fill=BOTH)
        self.nb_clic = 0
        self.message = Label(self, text="Vous navez pas cliqu sur le bouton", width=25)
        self.message.pack(side="left")
        self.bouton_quitter = Button(self, text="Quitter", command=self.quit)
        self.bouton_quitter.pack(side="left")
        self.bouton_cliquer = Button(self, text="Cliquez ici", fg="red",
                command=self.cliquer)
        self.bouton_cliquer.pack(side="right")
        fenetre['bg']='white'

        # frame 1
        self.Frame1 = Frame(fenetre, borderwidth=2, relief=GROOVE)
        self.Frame1.pack(side=LEFT, padx=30, pady=30)

        # frame 2
        Frame2 = Frame(fenetre, borderwidth=2, relief=GROOVE)
        Frame2.pack(side=LEFT, padx=10, pady=10)

        # frame 3 dans frame 2
        Frame3 = Frame(Frame2, bg="white", borderwidth=2, relief=GROOVE)
        Frame3.pack(side=RIGHT, padx=5, pady=5)

        # Ajout de labels
        Label(self.Frame1, text="Frame 1").pack(padx=10, pady=10)
        Label(Frame2, text="Frame 2").pack(padx=10, pady=10)
        Label(Frame3, text="Frame 3",bg="white").pack(padx=10, pady=10)
        self.l = LabelFrame(fenetre, text="Titre de la frame", padx=20, pady=20)
        self.l.pack(fill="both", expand="yes")
        self.inter = Label(self.l, text="A l'intérieure de la frame").pack()
        self.message2 = Label(self, text="Testons")
        self.message2.pack()

    def cliquer(self):
        self.nb_clic += 1
        self.message["text"] = "Vous avez cliqué {} fois.".format(self.nb_clic)

if __name__=='__main__':
    fenetre = Tk()
    interface = Interface(fenetre)
    interface.mainloop()
    interface.destroy()
