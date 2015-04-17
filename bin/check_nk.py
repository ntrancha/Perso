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
import thread_nk
import verif
import maps_nk
import mouve_nk
import global_nk

def check_pv():
    if sys_nk.screen_compare(2330,984,20,3, 'pv10', 'pv010', '../img/pv/') == 0:
        return 10
    #if sys_nk.screen_compare(2310,984,20,3, 'pv9', 'pv09', '../img/pv/') == 0:
    #    return 9
    if sys_nk.screen_compare(2290,984,20,3, 'pv8', 'pv08', '../img/pv/') == 0:
        return 8
    #if sys_nk.screen_compare(2270,984,20,3, 'pv7', 'pv07', '../img/pv/') == 0:
    #    return 7
    if sys_nk.screen_compare(2250,984,20,3, 'pv6', 'pv06', '../img/pv/') == 0:
        return 6
    #if sys_nk.screen_compare(2230,984,20,3, 'pv5', 'pv05', '../img/pv/') == 0:
    #    return 5
    if sys_nk.screen_compare(2210,984,20,3, 'pv4', 'pv04', '../img/pv/') == 0:
        return 4
    #if sys_nk.screen_compare(2190,984,20,3, 'pv3', 'pv03', '../img/pv/') == 0:
    #    return 3
    if sys_nk.screen_compare(2170,984,20,3, 'pv2', 'pv02', '../img/pv/') == 0:
        return 2
    #if sys_nk.screen_compare(2150,984,20,3, 'pv', 'pv0', '../img/pv/') == 0:
    #    return 1
    return 0

def check_mana():
    if sys_nk.screen_compare(2310,1022,20,3, 'mana10', 'mana010', '../img/mana/') == 0:
        return 10
    #if sys_nk.screen_compare(2290,1022,20,3, 'mana9', 'mana09', '../img/mana/') == 0:
    #    return 9
    if sys_nk.screen_compare(2270,1022,20,3, 'mana8', 'mana08', '../img/mana/') == 0:
        return 8
    #if sys_nk.screen_compare(2250,1022,20,3, 'mana7', 'mana07', '../img/mana/') == 0:
    #    return 7
    if sys_nk.screen_compare(2230,1022,20,3, 'mana6', 'mana06', '../img/mana/') == 0:
        return 6
    #if sys_nk.screen_compare(2210,1022,20,3, 'mana5', 'mana05', '../img/mana/') == 0:
    #    return 5
    if sys_nk.screen_compare(2190,1022,20,3, 'mana4', 'mana04', '../img/mana/') == 0:
        return 4
    #if sys_nk.screen_compare(2170,1022,20,3, 'mana3', 'mana03', '../img/mana/') == 0:
    #    return 3
    if sys_nk.screen_compare(2150,1022,20,3, 'mana2', 'mana02', '../img/mana/') == 0:
        return 2
    #if sys_nk.screen_compare(2130,1022,20,3, 'mana1', 'mana01', '../img/mana/') == 0:
    #    return 1
    return 0

def check_jaune():
    global_nk.set_jaune(0)
    if verif.verif_jaune() == 0 and verif.verif_logo() < 20:
        if verif.verif_quete() == 0:
            global_nk.set_jaune(1)
            return 1
    return 0

def check_jouer():
    global_nk.set_jouer(0)
    if verif.verif_menu() == 0 and verif.verif_partie() == 0 and verif.verif_jaune() == 0:
        global_nk.set_jouer(1)
        return 1
    return 0

def check_go():
    global_nk.set_go(int(sys_nk.contenu('../tmp/go.txt')))

def check_mort():
    global_nk.set_mort(0)
    if verif.verif_logo_dead() == 0:
        global_nk.set_mort(1)
        return 1
    return 0

def check_partie():
    global_nk.set_partie(0)
    old = int(global_nk.get_player())
    #if verif.verif_player() < 3:
    if verif.verif_player() == 0:
        global_nk.set_partie(1)
        global_nk.set_player(1)
        return 1
    if verif.verif_playe() == 0:
        global_nk.set_partie(1)
        return 1
    if verif.verif_dead() == 0:
        global_nk.set_partie(1)
        return 1
    if verif.verif_dead2() == 0:
        global_nk.set_partie(1)
        return 1
    if verif.verif_dead3() == 0:
        global_nk.set_partie(1)
        return 1
    if verif.verif_dead4() == 0:
        global_nk.set_partie(1)
        return 1
    if verif.verif_dead5() == 0:
        global_nk.set_partie(1)
        return 1
    if verif.verif_dead6() == 0:
        global_nk.set_partie(1)
        return 1
    return 0

def check_score(name, m):
    old = ed_nk.get_score()
    global_nk.set_score(0)
    if verif.verif_score() == 0:
        if old != 1:
            print "Score"
        global_nk.set_score(1)
        return 1
    return 0

def check_map():
    maps = verif.verif_maps()
    if maps > 0:
        print "Maps : " + str(maps)
        global_nk.set_maps(int(maps))
        display(int(maps))
        return int(maps)
    return 0

def check_talent():
    old = global_nk.get_talent()
    global_nk.set_talent(0)
    if verif.verif_talent() == 0:
        if old != 1:
            print "Talent"
        global_nk.set_talent(1)
        return 1
    return 0

def check_status():
    prev = global_nk.get_partie()
    if global_nk.get_partie() == 1:
        if check_partie() == 0:
            if check_jaune() == 1:
                check_jouer()
    elif global_nk.get_partie() != 1:
        jaune = check_jaune()
        if jaune == 1:
            check_jouer()
        if jaune == 0:
            check_partie()
    if global_nk.get_partie() == 1:
        return 3
    if global_nk.get_jaune() == 1:
        if global_nk.get_jouer() == 1:
            return 2
        return 1
    global_nk.set_partie(prev)
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
