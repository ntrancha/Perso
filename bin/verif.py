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
    img = '../img/status/' + name + '.jpg'
    img2 = '../img/status/' + name + '2.jpg'
    sys_nk.sav(sys_nk.screen(x,y,w,h), img2)
    ret = sys_nk.compare(sys_nk.ouvre(img), sys_nk.ouvre(img2))
    sys_nk.delete(img2)
    return ret

def verif_menu():
    return verif_all(3790,1050,40,20, 'screen')

def verif_jaune():
    return verif_all(3755,130,8,8, 'jaune')

def verif_partie():
    return verif_all(2093,26,13,4, 'jouer')

def verif_maps():
    sys_nk.sav(sys_nk.screen(3590,800,20,20), '../img/map/maps2.jpg')
    if sys_nk.compare(sys_nk.ouvre('../img/map/val.jpg'), sys_nk.ouvre('../img/map/maps2.jpg')) == 0:
        return 7
    if sys_nk.compare(sys_nk.ouvre('../img/map/baie.jpg'), sys_nk.ouvre('../img/map/maps2.jpg')) == 0:
        return 1
    if sys_nk.compare(sys_nk.ouvre('../img/map/jardin.jpg'), sys_nk.ouvre('../img/map/maps2.jpg')) == 0:
        return 3
    if sys_nk.compare(sys_nk.ouvre('../img/map/jardin2.jpg'), sys_nk.ouvre('../img/map/maps2.jpg')) == 0:
        return 3
    if sys_nk.compare(sys_nk.ouvre('../img/map/mine.jpg'), sys_nk.ouvre('../img/map/maps2.jpg')) == 0:
        return 4
    if sys_nk.compare(sys_nk.ouvre('../img/map/temple.jpg'), sys_nk.ouvre('../img/map/maps2.jpg')) == 0:
        return 6
    if sys_nk.compare(sys_nk.ouvre('../img/map/dragon.jpg'), sys_nk.ouvre('../img/map/maps2.jpg')) < 5:
        return 2
    if sys_nk.compare(sys_nk.ouvre('../img/map/reine.jpg'), sys_nk.ouvre('../img/map/maps2.jpg')) < 5:
        return 5
    return -1

def verif_talent():
    sys_nk.sav(sys_nk.screen(2022,1030,2,12), '../img/status/talent2.jpg')
    sys_nk.sav(sys_nk.screen(2037,1030,2,12), '../img/status/talent4.jpg')
    sys_nk.sav(sys_nk.screen(1987,740,4,20), '../img/status/talent6.jpg')
    ret = sys_nk.compare(sys_nk.ouvre('../img/status/talent.jpg'), sys_nk.ouvre('../img/status/talent2.jpg'))
    ret += sys_nk.compare(sys_nk.ouvre('../img/status/talent3.jpg'), sys_nk.ouvre('../img/status/talent4.jpg'))
    ret += sys_nk.compare(sys_nk.ouvre('../img/status/talent5.jpg'), sys_nk.ouvre('../img/status/talent6.jpg'))
    sys_nk.delete('../img/status/talent2.jpg')
    sys_nk.delete('../img/status/talent4.jpg')
    sys_nk.delete('../img/status/talent6.jpg')
    return ret

def verif_playe():
    if verif_all(2845,0,70,6, 'playe') == 1:
        return 1
    if verif_all(2845,0,70,6, 'playe1') == 1:
        return 1
    return 0

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
