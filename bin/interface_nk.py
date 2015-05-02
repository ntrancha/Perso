#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

import global_nk
from Tkinter import *
from tkMessageBox import *

class Interface(Frame):

    def infos(self):
        self.zone_info.create_text(250, 20, text="Débug", font="Arial 16 italic", fill="red")
        self.zone_info.create_text(50, 45, text="Status", font="Arial 16 italic", fill="blue")
        self.zone_info.create_text(50, 70, text="Jaune", font="Arial 16 italic", fill="blue")
        self.zone_info.create_text(50, 95, text="Jouer", font="Arial 16 italic", fill="blue")
        self.zone_info.create_text(50, 120, text="Maps", font="Arial 16 italic", fill="blue")
        self.zone_info.create_text(50, 145, text="Mort", font="Arial 16 italic", fill="blue")
        self.zone_info.create_text(50, 170, text="Partie", font="Arial 16 italic", fill="blue")
        self.zone_info.create_text(50, 195, text="Talent", font="Arial 16 italic", fill="blue")
        self.zone_info.create_text(50, 220, text="Pv", font="Arial 16 italic", fill="blue")
        self.zone_info.create_text(50, 245, text="Mana", font="Arial 16 italic", fill="blue")
        self.zone_info.create_text(50, 270, text="Score", font="Arial 16 italic", fill="blue")
        self.zone_info.create_text(50, 295, text="Player", font="Arial 16 italic", fill="blue")
        self.zone_info.create_text(150, 45, text="Na", font="Arial 16 italic", fill="blue")
        self.zone_info.create_text(150, 70, text="Na", font="Arial 16 italic", fill="blue")
        self.zone_info.create_text(150, 95, text="Na", font="Arial 16 italic", fill="blue")
        self.zone_info.create_text(150, 120, text="Na", font="Arial 16 italic", fill="blue")
        self.zone_info.create_text(150, 145, text="Na", font="Arial 16 italic", fill="blue")
        self.zone_info.create_text(150, 170, text="Na", font="Arial 16 italic", fill="blue")
        self.zone_info.create_text(150, 195, text="Na", font="Arial 16 italic", fill="blue")
        self.zone_info.create_text(150, 220, text="Na", font="Arial 16 italic", fill="blue")
        self.zone_info.create_text(150, 245, text="Na", font="Arial 16 italic", fill="blue")
        self.zone_info.create_text(150, 270, text="Na", font="Arial 16 italic", fill="blue")
        self.zone_info.create_text(150, 295, text="Na", font="Arial 16 italic", fill="blue")
        

    def canevas(self):
        self.zone_info = Canvas(self, width=500, height=500, bg='white',bd=8,relief="ridge")
        self.infos()
        self.zone_info.pack(side="left")
        self.zone_dessin2 = Canvas(self, width=500, height=500, bg='red',bd=8,relief="ridge")
        self.zone_dessin2.focus_set()
        self.zone_dessin2.bind("<Key>", self.clavier)
        self.photo = PhotoImage(file ='../img/status/test.gif')
        self.zone_dessin2.create_image(120, 90, image = self.photo)
        self.zone_dessin2.pack(side="right")

    def __init__(self, fenetre, **kwargs):
        #Frame.__init__(self, fenetre, width=368, height=176, **kwargs)
        Frame.__init__(self, fenetre)
        self.pack()
        fenetre.title("NK")
        self.menu_bar()
        self.canevas()

    def menu_bar(self):
        menubar = Menu(self)
    
        self.menu1 = Menu(menubar, tearoff=0)
        self.menu1.add_command(label="Start", command=self.start)
        self.menu1.add_command(label="Reset", command=self.test)
        self.menu1.add_separator()
        self.menu1.add_command(label="Quitter", command=self.quit)
        menubar.add_cascade(label="Menu", menu=self.menu1)

        menu3 = Menu(menubar, tearoff=0)
        menu3.add_command(label="A propos", command=self.test)
        menu3.add_command(label="Manuel", command=self.test)
        menubar.add_cascade(label="Aide", menu=menu3)

        fenetre.config(menu=menubar)

    
    def stop(self):
        #global_nk.setter('go', 0)
        print "stop"

    def start(self):
        self.menu1.entryconfig(0, label="Coucou")
        self.zone_info.itemconfigure(13, text="toto")
        self.zone_info.itemconfigure(14, text="OK")
        #self.photo = PhotoImage(file ='test2.gif')
        #self.zone_dessin2.create_image(120, 90, image = self.photo)

    def cliquer(self):
        self.nb_clic += 1
        self.imessage["text"] = "Vous avez cliqué {} fois.".format(self.nb_clic)

    def destroy(self):
        print "KILL"

    def test(self):
        showinfo('Titre 3', 'Vous avez peur!')
        print "Menu"

    def clavier(self, event):
        touche = event.keysym
        #self.frame(1)
        if touche == 'q':
            self.quit()
        print(touche)

if __name__=='__main__':
    fenetre = Tk()
    interface = Interface(fenetre)
    interface.mainloop()
    interface.destroy()
