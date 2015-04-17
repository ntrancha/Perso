#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

import threading
import thread
import math, operator
import pyscreenshot as ImageGrab
from PIL import Image
from random import randint
import numpy
import sys
import os
import sys_nk
import verif
import maps_nk
import mouve_nk
import check_nk
import global_nk

def check_pv():
    sys_nk.sav(sys_nk.screen(2330,984,20,3), '../img/pv/pv010.jpg')
    if sys_nk.compare(sys_nk.ouvre('../img/pv/pv10.jpg'), sys_nk.ouvre('../img/pv/pv010.jpg')) == 0:
        return 10
    sys_nk.sav(sys_nk.screen(2310,984,20,3), '../img/pv/pv09.jpg')
    if sys_nk.compare(sys_nk.ouvre('../img/pv/pv9.jpg'), sys_nk.ouvre('../img/pv/pv09.jpg'))  == 0:
        return 9
    sys_nk.sav(sys_nk.screen(2290,984,20,3), '../img/pv/pv08.jpg')
    if sys_nk.compare(sys_nk.ouvre('../img/pv/pv8.jpg'), sys_nk.ouvre('../img/pv/pv08.jpg')) == 0:
        return 8
    sys_nk.sav(sys_nk.screen(2270,984,20,3), '../img/pv/pv07.jpg')
    if sys_nk.compare(sys_nk.ouvre('../img/pv/pv7.jpg'), sys_nk.ouvre('../img/pv/pv07.jpg')) == 0:
        return 7
    sys_nk.sav(sys_nk.screen(2250,984,20,3), '../img/pv/pv06.jpg')
    if sys_nk.compare(sys_nk.ouvre('../img/pv/pv6.jpg'), sys_nk.ouvre('../img/pv/pv06.jpg')) == 0:
        return 6
    sys_nk.sav(sys_nk.screen(2230,984,20,3), '../img/pv/pv05.jpg')
    if sys_nk.compare(sys_nk.ouvre('../img/pv/pv5.jpg'), sys_nk.ouvre('../img/pv/pv05.jpg')) == 0:
        return 5
    sys_nk.sav(sys_nk.screen(2210,984,20,3), '../img/pv/pv04.jpg')
    if sys_nk.compare(sys_nk.ouvre('../img/pv/pv4.jpg'), sys_nk.ouvre('../img/pv/pv04.jpg')) == 0:
        return 4
    sys_nk.sav(sys_nk.screen(2190,984,20,3), '../img/pv/pv03.jpg')
    if sys_nk.compare(sys_nk.ouvre('../img/pv/pv3.jpg'), sys_nk.ouvre('../img/pv/pv03.jpg')) == 0:
        return 3
    sys_nk.sav(sys_nk.screen(2170,984,20,3), '../img/pv/pv02.jpg')
    if sys_nk.compare(sys_nk.ouvre('../img/pv/pv2.jpg'), sys_nk.ouvre('../img/pv/pv02.jpg')) == 0:
        return 2
    sys_nk.sav(sys_nk.screen(2150,984,20,3), '../img/pv/pv0.jpg')
    if sys_nk.compare(sys_nk.ouvre('../img/pv/pv.jpg'), sys_nk.ouvre('../img/pv/pv0.jpg')) == 0:
        return 1
    return 0

def check_mana():
    sys_nk.sav(sys_nk.screen(2310,1022,20,3), '../img/mana/mana010.jpg')
    if sys_nk.compare(sys_nk.ouvre('../img/mana/mana10.jpg'), sys_nk.ouvre('../img/mana/mana010.jpg')) == 0:
        return 10
    sys_nk.sav(sys_nk.screen(2290,1022,20,3), '../img/mana/mana09.jpg')
    if sys_nk.compare(sys_nk.ouvre('../img/mana/mana9.jpg'), sys_nk.ouvre('../img/mana/mana09.jpg'))  == 0:
        return 9
    sys_nk.sav(sys_nk.screen(2270,1022,20,3), '../img/mana/mana08.jpg')
    if sys_nk.compare(sys_nk.ouvre('../img/mana/mana8.jpg'), sys_nk.ouvre('../img/mana/mana08.jpg')) == 0:
        return 8
    sys_nk.sav(sys_nk.screen(2250,1022,20,3), '../img/mana/mana07.jpg')
    if sys_nk.compare(sys_nk.ouvre('../img/mana/mana7.jpg'), sys_nk.ouvre('../img/mana/mana07.jpg')) == 0:
        return 7
    sys_nk.sav(sys_nk.screen(2230,1022,20,3), '../img/mana/mana06.jpg')
    if sys_nk.compare(sys_nk.ouvre('../img/mana/mana6.jpg'), sys_nk.ouvre('../img/mana/mana06.jpg')) == 0:
        return 6
    sys_nk.sav(sys_nk.screen(2210,1022,20,3), '../img/mana/mana05.jpg')
    if sys_nk.compare(sys_nk.ouvre('../img/mana/mana5.jpg'), sys_nk.ouvre('../img/mana/mana05.jpg')) == 0:
        return 5
    sys_nk.sav(sys_nk.screen(2190,1022,20,3), '../img/mana/mana04.jpg')
    if sys_nk.compare(sys_nk.ouvre('../img/mana/mana4.jpg'), sys_nk.ouvre('../img/mana/mana04.jpg')) == 0:
        return 4
    sys_nk.sav(sys_nk.screen(2170,1022,20,3), '../img/mana/mana03.jpg')
    if sys_nk.compare(sys_nk.ouvre('../img/mana/mana3.jpg'), sys_nk.ouvre('../img/mana/mana03.jpg')) == 0:
        return 3
    sys_nk.sav(sys_nk.screen(2150,1022,20,3), '../img/mana/mana02.jpg')
    if sys_nk.compare(sys_nk.ouvre('../img/mana/mana2.jpg'), sys_nk.ouvre('../img/mana/mana02.jpg')) == 0:
        return 2
    sys_nk.sav(sys_nk.screen(2130,1022,20,3), '../img/mana/mana01.jpg')
    if sys_nk.compare(sys_nk.ouvre('../img/mana/mana1.jpg'), sys_nk.ouvre('../img/mana/mana01.jpg')) == 0:
        return 1
    return 0

def check_jaune():
    global_nk.G_jaune = 0
    if verif.verif_jaune() == 0 and verif.verif_logo() < 20:
        global_nk.G_jaune = 1
        return 1
    return 0

def check_jouer():
    global_nk.G_jouer = 0
    if verif.verif_menu() == 0 and verif.verif_partie() == 0 and verif.verif_jaune() == 0:
        global_nk.G_jouer = 1
        return 1
    return 0

def check_go():
    global_nk.G_go = int(sys_nk.contenu('../tmp/go.txt'))

def check_mort():
    global_nk.G_mort = 0
    if verif.verif_logo_dead() == 0:
        global_nk.G_mort = 1
        return 1
    return 0

def check_partie():
    global_nk.G_partie = 0
    #if verif.verif_player() < 3:
    if verif.verif_player() < 1:
        global_nk.G_partie = 1
        print "player"
        global_nk.G_player = 1
        return 1
    if verif.verif_playe() == 0:
        global_nk.G_partie = 1
        return 1
    if verif.verif_dead() == 0:
        global_nk.G_partie = 1
        return 1
    if verif.verif_dead2() == 0:
        global_nk.G_partie = 1
        return 1
    if verif.verif_dead3() == 0:
        global_nk.G_partie = 1
        return 1
    if verif.verif_dead4() == 0:
        global_nk.G_partie = 1
        return 1
    if verif.verif_dead5() == 0:
        global_nk.G_partie = 1
        return 1
    if verif.verif_dead6() == 0:
        global_nk.G_partie = 1
        return 1
    return 0

def check_score(name, m):
    if verif.verif_score() == 0:
        print "score"
        global_nk.G_score = 1
        return 1
    return 0

def check_map():
    maps = verif.verif_maps()
    if maps > 0:
        print "Maps : " + str(maps)
        global_nk.G_maps = int(maps)
        #display(int(maps))
        return int(maps)
    return 0

def check_talent():
    global_nk.G_talent = 0
    if verif.verif_talent() == 0:
        print "Talent"
        global_nk.G_talent = 1
        return 1
    return 0

def check_status():
    prev = global_nk.G_partie
    if global_nk.G_partie == 1:
        if check_partie() == 0:
            if check_jaune() == 1:
                check_jouer()
    elif global_nk.G_partie != 1:
        jaune = check_jaune()
        if jaune == 1:
            check_jouer()
        if jaune == 0:
            check_partie()
    if global_nk.G_partie == 1:
        return 3
    if global_nk.G_jaune == 1:
        if global_nk.G_jouer == 1:
            return 2
        return 1
    global_nk.G_partie = prev
    return prev

def display(maps):
    if maps == 1:
        print "baie"
        return "baie"
    if maps == 2:
        print "dragon"
        return "dragon"
    if maps == 3:
        print "jardin"
        return "jardin"
    if maps == 4:
        print "mine"
        return "mine"
    if maps == 5:
        print "reine"
        return "reine"
    if maps == 6:
        print "temple"
        return "temple"
    if maps == 7:
        print "val"
        return "val"
