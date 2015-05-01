#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

#import global_nk
from Tkinter import *

class Interface(Frame):

    def canevas(self):
        zone_dessin = Canvas(self, width=500, height=500, bg='yellow',bd=8,relief="ridge")
        zone_dessin.pack(side="left")
        zone_dessin = Canvas(self, width=500, height=500, bg='red',bd=8,relief="ridge")
        zone_dessin.pack(side="right")

    def frame(self):
        # frame 1
        Frame1 = Frame(fenetre, borderwidth=2, relief=GROOVE, bg="red")
        Frame1.pack(side=LEFT)

        # frame 2
        Frame2 = Frame(fenetre, borderwidth=2, relief=GROOVE)
        Frame2.pack(side=LEFT, padx=10, pady=10)

        # frame 3 dans frame 2
        Frame3 = Frame(Frame2, bg="white", borderwidth=2, relief=GROOVE)
        Frame3.pack(side=RIGHT, padx=5, pady=5)

        # Ajout de labels
        Label(Frame1, text="Frame 1").pack(padx=100, pady=100)
        Label(Frame2, text="Frame 2").pack(padx=10, pady=10)
        Label(Frame3, text="Frame 3",bg="white").pack(padx=10, pady=10)


    def __init__(self, fenetre, **kwargs):
        #Frame.__init__(self, fenetre, width=368, height=176, **kwargs)
        Frame.__init__(self, fenetre)
        self.pack()
        self.nb_clic = 0
        fenetre.title("NK")
        self.menu_bar()
        self.frame()
        
    def test_interface(self):
        # Création de nos widgets
        
        self.bouton_quitter = Button(self, text="Quitter", command=self.quit)
        self.bouton_quitter.pack(side="left")
        
        self.bouton_cliquer = Button(self, text="Cliquez ici", fg="red", command=self.stop)
        self.bouton_cliquer.pack(side="right")
        zone_dessin = Canvas(self, width=500, height=500, bg='yellow',bd=8,relief="ridge")
        zone_dessin.pack()
        zone_dessin.create_rectangle(100,100,200,200)

        fenetre['bg']='white'



    def menu_bar(self):
        menubar = Menu(self)
    
        menu1 = Menu(menubar, tearoff=0)
        menu1.add_command(label="Start", command=self.start)
        menu1.add_command(label="Reset", command=self.test)
        menu1.add_separator()
        menu1.add_command(label="Quitter", command=self.quit)
        menubar.add_cascade(label="Menu", menu=menu1)

        menu3 = Menu(menubar, tearoff=0)
        menu3.add_command(label="A propos", command=self.test)
        menu3.add_command(label="Manuel", command=self.test)
        menubar.add_cascade(label="Aide", menu=menu3)

        fenetre.config(menu=menubar)

    
    def stop(self):
        #global_nk.setter('go', 0)
        print "stop"

    def start(self):
        self.Frame1["text"] = "toto"

    def cliquer(self):
        self.nb_clic += 1
        self.message["text"] = "Vous avez cliqué {} fois.".format(self.nb_clic)

    def destroy(self):
        print "KILL"

    def test(self):
        print "Menu"

if __name__=='__main__':
    fenetre = Tk()
    interface = Interface(fenetre)
    interface.mainloop()
    interface.destroy()
