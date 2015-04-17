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

def verif_all(x,y,w,h,name):
    name2 = name + "2"
    return sys_nk.screen_compare(x,y,w,h, name, name2, '../img/status/')

def verif_menu():
    return verif_all(3790,1050,40,20, 'screen')

def verif_jaune():
    return verif_all(3755,130,8,8, 'jaune')

def verif_partie():
    return verif_all(2093,26,13,4, 'jouer')

def verif_maps():
    sys_nk.sav(sys_nk.screen(3610,850,20,20), '../img/map/maps3.jpg')
    if sys_nk.compare_file('reine0', 'maps3', '../img/map/') < 2:
        return 5
    sys_nk.sav(sys_nk.screen(3590,800,20,20), '../img/map/maps2.jpg')
    if sys_nk.compare_file('val', 'maps2', '../img/map/') == 0:
        return 7
    if sys_nk.compare_file('baie', 'maps2', '../img/map/') == 0:
        return 1
    if sys_nk.compare_file('jardin', 'maps2', '../img/map/') == 0:
        return 3
    if sys_nk.compare_file('jardin2', 'maps2', '../img/map/') == 0:
        return 3
    if sys_nk.compare_file('mine', 'maps2', '../img/map/') == 0:
        return 4
    if sys_nk.compare_file('temple', 'maps2', '../img/map/') == 0:
        return 6
    if sys_nk.compare_file('dragon', 'maps2', '../img/map/') < 5:
        return 2
    if sys_nk.compare_file('reine', 'maps2', '../img/map/') < 5:
        return 5
    return -1

def verif_talent():
    ret = sys_nk.screen_compare(2022,1030,2,12, 'talent', 'talent2', '../img/status/')
    ret += sys_nk.screen_compare(2037,1030,2,12, 'talent3', 'talent4', '../img/status/')
    ret += sys_nk.screen_compare(1987,740,4,20, 'talent5', 'talent6', '../img/status/')
    return ret

def verif_playe():
    if verif_all(2845,0,70,6, 'playe0') < 5:
        return 0
    if verif_all(2845,0,70,6, 'playe') < 1:
        return 0
    if verif_all(2845,0,70,6, 'playe1') < 1:
        return 0
    return 1

def verif_score():
    return verif_all(3482,155,20,20, 'score')

def verif_player():
    return verif_all(2123,1030,20,20, 'player')

def verif_dead():
    return verif_all(2110,1035,20,10, 'dead')

def verif_dead2():
    return verif_all(2110,1035,20,10, 'dead0')

def verif_dead3():
    return verif_all(2110,1035,20,10, 'dead1')

def verif_dead4():
    return verif_all(2110,1035,20,10, 'dead4')

def verif_dead5():
    return verif_all(2110,1035,20,10, 'dead5')

def verif_dead6():
    return verif_all(2110,1035,20,10, 'dead6')

def verif_logo_dead():
    return verif_all(2870,810,30,30, 'logo_dead')

def verif_logo():
    return verif_all(1958,20,30,30, 'logo')
