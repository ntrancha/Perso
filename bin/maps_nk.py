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

def check_maps(maps):
    if maps == 1:
        maps_baie()
    if maps == 2:
        maps_dragon()
    if maps == 3:
        maps_jardin()
    if maps == 4:
        maps_mine()
    if maps == 5:
        maps_reine()
    if maps == 6:
        maps_temple()
    if maps == 7:
        maps_val()

def maps_baie():
    return 1

def maps_dragon():
    sys_nk.sav(sys_nk.screen(3654,899,7,5), '../img/maps/dragon/dragon_c1.jpg')
    sys_nk.sav(sys_nk.screen(3651,955,7,5), '../img/maps/dragon/dragon_c2.jpg')
    sys_nk.sav(sys_nk.screen(3613,1030,7,5), '../img/maps/dragon/dragon_c3.jpg')
    sys_nk.sav(sys_nk.screen(3574,955,7,5), '../img/maps/dragon/dragon_c4.jpg')
    sys_nk.sav(sys_nk.screen(3573,899,7,5), '../img/maps/dragon/dragon_c5.jpg')
    return 1

def maps_jardin():
    return 1

def maps_mine():
    return 1

def maps_reine():
    return 1

def maps_temple():
    return 1

def maps_val():
    #sys_nk.sav(sys_nk.screen(3521,877,7,5), '../img/maps/val/val_c1.jpg')
    #sys_nk.sav(sys_nk.screen(3547,946,7,5), '../img/maps/val/val_c2.jpg')
    #sys_nk.sav(sys_nk.screen(3564,983,7,5), '../img/maps/val/val_c3.jpg')
    #sys_nk.sav(sys_nk.screen(3689,933,7,5), '../img/maps/val/val_c4.jpg')
    #sys_nk.sav(sys_nk.screen(3665,865,7,5), '../img/maps/val/val_c5.jpg')
    #sys_nk.sav(sys_nk.screen(3648,825,7,5), '../img/maps/val/val_c6.jpg')
    return 1
