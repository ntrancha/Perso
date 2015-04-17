#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

import math, operator
import pyscreenshot as ImageGrab
from PIL import Image
from random import randint
import numpy
import sys
import os

def screen_compare(x, y, w, h, file1, file2, path):
    f2 = path + file2 + '.jpg'
    f1 = path + file1 + '.jpg'
    sav(screen(x, y, w, h), f2)
    ret = compare_file(file1, file2, path)
    delete(f2)
    return ret

def compare_file(file1, file2, path):
    f1 = path + file1 + '.jpg'
    f2 = path + file2 + '.jpg'
    return compare(ouvre(f1), ouvre(f2))

def screen(x, y, w, h):
    return ImageGrab.grab(bbox=(x, y, (x + w), (y + h)))

def compare(image1, image2):
    h1 = image1.histogram()
    h2 = image2.histogram()
    rms = math.sqrt(reduce(operator.add,map(lambda a,b: (a-b)**2, h1, h2))/len(h1))
    return rms

def comp(img1, img2):
    if img1.size != img2.size or img1.getbands() != img2.getbands():
        return -1

    s = 0
    for band_index, band in enumerate(img1.getbands()):
        m1 = numpy.array([p[band_index] for p in img1.getdata()]).reshape(*img1.size)
        m2 = numpy.array([p[band_index] for p in img2.getdata()]).reshape(*img2.size)
        s += numpy.sum(numpy.abs(m1-m2))
    return s

def ouvre(fichier1):
    try:
        image1 = Image.open(fichier1)
    except:
        print "Bug ouverture: "+fichier1
        return -1
    return image1

def sav(fichier, dest):
    try:
        fichier.save(dest)
    except:
        return 0
    return 1

def aff(fichier):
    fichier.show()
    return 1

def contenu(fichier):
    try:
        mon_fichier = open(fichier, "r")
        f_contenu = mon_fichier.read()
        mon_fichier.close()
    except:
        print "Error open:"+ fichier
        #return contenu(fichier)
    return f_contenu

def execute(ordre):
    try:
        os.system(ordre)
    except:
        return 0
    return 1

def clear_console():
    execute('clear')

def commande(ordre):
    com = "{0} > tempo.txt".format(ordre)
    execute(com)
    cont = contenu('tempo.txt')
    delete('tempo.txt')
    return cont

def delete(fichier):
    try:
        os.remove(fichier)
    except:
        return 0
    return 1

def upaus(time):
    com = "./pause " + time
    execute(com)
    return 1

def paus(time):
    com = "sleep " + time
    execute(com)
    return 1

def get_x():
    return commande('./get_x.sh')

def get_y():
    return commande('./get_y.sh')

def deplace(x2, y2):
    x = get_x()
    y = get_y()
    xp = ((x2 - int(x) ) / randint(10,20)) + int(x)
    yp = ((y2 - int(y) ) / randint(10,20)) + int(y)
    commande = "xdotool mousemove " + str(xp) + " " + str(yp)
    execute(commande)
    if int(x) < int(x2):
        if int(xp) < int(x2) - 5:
            deplace(int(x2), int(y2))
    if int(x) > int(x2):
        if int(xp) > int(x2) + 5:
            deplace(int(x2), int(y2))
    if int(y) < int(y2):
        if int(yp) < int(y2) - 5:
            deplace(int(x2), int(y2))
    if int(y) > int(y2):
        if int(yp) > int(y2) + 5:
            deplace(int(x2), int(y2))
