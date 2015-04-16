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
import global_nk

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

def verif_all(x,y,w,h,maps,num2):
    num = str(num2)
    img = '../img/maps/' + maps + '/' + maps + '_cb'+num+'.jpg'
    img1 = '../img/maps/' + maps + '/' + maps + '_cr'+num+'.jpg'
    img0 = '../img/maps/' + maps + '/' + maps + '_cj'+num+'.jpg'
    img2 = '../img/maps/' + maps + '/' + maps + '_c'+num+'.jpg'
    sys_nk.sav(sys_nk.screen(x,y,w,h), img2)
    ret = sys_nk.compare(sys_nk.ouvre(img), sys_nk.ouvre(img2))
    if ret < 1:
        return 1
    ret = sys_nk.compare(sys_nk.ouvre(img1), sys_nk.ouvre(img2))
    if ret < 1:
        return 2
    ret = sys_nk.compare(sys_nk.ouvre(img0), sys_nk.ouvre(img2))
    if ret < 1:
        return 0
    sys_nk.delete(img2)
    return -1

def maps_baie():
    return 1

def maps_dragon():
    verif_all(3654,899,7,5,'dragon', 1)
    verif_all(3651,955,7,5,'dragon', 2)
    verif_all(3613,1030,7,5,'dragon', 3)
    verif_all(3574,955,7,5,'dragon', 4)
    verif_all(3573,899,7,5,'dragon', 5)
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
    verif_all(3521,877,7,5,'val', 1)
    verif_all(3547,946,7,5,'val', 2)
    verif_all(3564,983,7,5,'val', 3)
    verif_all(3689,933,7,5,'val', 4)
    verif_all(3665,865,7,5,'val', 5)
    verif_all(3648,825,7,5,'val', 6)
    return 1
