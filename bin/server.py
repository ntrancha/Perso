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

def screen(x, y, w, h):
    return ImageGrab.grab(bbox=(x, y, (x + w), (y + h)))

def compare(image1, image2):
    h1 = image1.histogram()
    h2 = image2.histogram()
    return math.sqrt(reduce(operator.add,map(lambda a,b: (a-b)**2, h1, h2))/len(h1))

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
        paus("1")
        return ouvre(fichier1)
    return image1

def sav(fichier, dest):
    try:
        fichier.save(dest)
    except:
        return 0
    return 1

def aff(fichier):
    try:
        fichier.show()
    except:
        return 0
    return 1

def contenu(fichier):
    try:
        mon_fichier = open(fichier, "r")
        f_contenu = mon_fichier.read()
        mon_fichier.close()
    except:
        paus("1")
        return contenu(fichier)
    return f_contenu 

def execute(ordre): 
    try:
        os.system(ordre) 
    except:
        return 0
    return 1

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

def paus(time): 
    com = "sleep " + time
    execute(com)
    return 1

def jouer():
    deplace(2240, 35)
    execute('./click.sh 2240 35 10 1')
    return 1

def rapide():
    deplace(2280, 100)
    execute('./click.sh 2280 100 10 1')
    return 1

def coop():
    deplace(2450, 100)
    execute('./click.sh 2450 100 10 1')
    return 1

def pret():
    deplace(2875, 1020)
    execute('./click.sh 2875 1020 10 1')
    return 1

def perso():
    deplace(2875, 500)
    execute('./click.sh 2875 500 10 1')
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

def verif_all(x,y,w,h,name)
    img = '../img/' + name + '.jpg'
    img2 = '../img/' + name + '2.jpg'
    sav(screen(x,y,w,h), img2)
    ret = compare(ouvre(img), ouvre(img2))
    delete(img2)
    return ret

def verif_menu():
    return verif_all(3790,1050,40,20, 'screen')

def verif_jaune():
    return verif_all(3755,130,8,8, 'jaune')

def verif_partie():
    return verif_all(2093,26,13, 'jouer')

def verif_maps():
    sav(screen(3590,800,20,20), '../img/maps2.jpg')
    if compare(ouvre('../img/val.jpg'), ouvre('../img/maps2.jpg')) == 0:
        return 7
    if compare(ouvre('../img/baie.jpg'), ouvre('../img/maps2.jpg')) == 0:
        return 1
    if compare(ouvre('../img/jardin.jpg'), ouvre('../img/maps2.jpg')) == 0:
        return 3
    if compare(ouvre('../img/jardin2.jpg'), ouvre('../img/maps2.jpg')) == 0:
        return 3
    if compare(ouvre('../img/mine.jpg'), ouvre('../img/maps2.jpg')) == 0:
        return 4
    if compare(ouvre('../img/temple.jpg'), ouvre('../img/maps2.jpg')) == 0:
        return 6
    if compare(ouvre('../img/dragon.jpg'), ouvre('../img/maps2.jpg')) < 5:
        return 2
    if compare(ouvre('../img/reine.jpg'), ouvre('../img/maps2.jpg')) < 5:
        return 5
    return -1

def verif_talent():
    sav(screen(2022,1030,2,12), '../img/talent2.jpg')
    sav(screen(2037,1030,2,12), '../img/talent4.jpg')
    sav(screen(1987,740,4,20), '../img/talent6.jpg')
    ret = compare(ouvre('../img/talent.jpg'), ouvre('../img/talent2.jpg'))
    ret += compare(ouvre('../img/talent3.jpg'), ouvre('../img/talent4.jpg'))
    ret += compare(ouvre('../img/talent5.jpg'), ouvre('../img/talent6.jpg'))
    delete('../img/talent2.jpg')
    delete('../img/talent4.jpg')
    delete('../img/talent6.jpg')
    return ret

def verif_dead():
    return verif_all(2110,1035,20,10, 'dead')

def verif_logo_dead():
    return verif_all(2870,810,30,30, 'logo_dead')

def verif_logo():
    return verif_all(1958,20,30,30, 'logo')

def check_jaune():
    etat = contenu('../tmp/etat.txt')
    execute('echo "0" > ../tmp/jaune.txt')
    if verif_jaune() == 0 and verif_logo() < 20:
        if int(etat) != 1 and int(etat) != 2:
            print "Lobby"
        execute('echo "1" > ../tmp/jaune.txt')
        return 1
    return 0

def check_jouer():
    jouer = contenu('../tmp/jouer.txt')
    execute('echo "0" > ../tmp/jouer.txt')
    if verif_menu() == 0 and verif_partie() == 0 and verif_jaune() == 0:
        if int(jouer) == 0:
            print "Jouer"
        execute('echo "1" > ../tmp/jouer.txt')
        return 1
    return 0

def check_mort():
    mort = contenu('../tmp/mort.txt')
    execute('echo "0" > ../tmp/mort.txt')
    if verif_logo_dead() == 0:
        if int(mort) == 0:
            print "Mort"
        execute('echo "1" > ../tmp/mort.txt')
        return 1
    return 0

def check_partie():
    partie = contenu('../tmp/partie.txt')
    execute('echo "0" > ../tmp/partie.txt')
    if verif_dead() == 0:
        if int(partie) == 0:
            print "Partie en cours"
        execute('echo "1" > ../tmp/partie.txt')
        return 1
    return 0

def check_map():
    #execute('echo "0" > ../tmp/maps.txt')
    maps = verif_maps()
    if maps > 0:
        print "Maps : " + str(maps)
        stri = 'echo "' + str(maps) + '" > ../tmp/maps.txt'
        execute(stri)
        return 1
    return 0

def check_talent():
    execute('echo "0" > ../tmp/talent.txt')
    if verif_talent() == 0:
        print "Talent"
        execute('echo "1" > ../tmp/talent.txt')
        return 1
    return 0

def check_pv():
    sav(screen(2330,984,20,3), '../img/pv010.jpg')
    if compare(ouvre('../img/pv10.jpg'), ouvre('../img/pv010.jpg')) == 0:
        return 10
    sav(screen(2310,984,20,3), '../img/pv09.jpg')
    if compare(ouvre('../img/pv9.jpg'), ouvre('../img/pv09.jpg'))  == 0:
        return 9
    sav(screen(2290,984,20,3), '../img/pv08.jpg')
    if compare(ouvre('../img/pv8.jpg'), ouvre('../img/pv08.jpg')) == 0:
        return 8
    sav(screen(2270,984,20,3), '../img/pv07.jpg')
    if compare(ouvre('../img/pv7.jpg'), ouvre('../img/pv07.jpg')) == 0:
        return 7
    sav(screen(2250,984,20,3), '../img/pv06.jpg')
    if compare(ouvre('../img/pv6.jpg'), ouvre('../img/pv06.jpg')) == 0:
        return 6
    sav(screen(2230,984,20,3), '../img/pv05.jpg')
    if compare(ouvre('../img/pv5.jpg'), ouvre('../img/pv05.jpg')) == 0:
        return 5
    sav(screen(2210,984,20,3), '../img/pv04.jpg')
    if compare(ouvre('../img/pv4.jpg'), ouvre('../img/pv04.jpg')) == 0:
        return 4
    sav(screen(2190,984,20,3), '../img/pv03.jpg')
    if compare(ouvre('../img/pv3.jpg'), ouvre('../img/pv03.jpg')) == 0:
        return 3
    sav(screen(2170,984,20,3), '../img/pv02.jpg')
    if compare(ouvre('../img/pv2.jpg'), ouvre('../img/pv02.jpg')) == 0:
        return 2
    sav(screen(2150,984,20,3), '../img/pv0.jpg')
    if compare(ouvre('../img/pv.jpg'), ouvre('../img/pv0.jpg')) == 0:
        return 1
    return 0

def check_mana():
    sav(screen(2310,1022,20,3), '../img/mana010.jpg')
    if compare(ouvre('../img/mana10.jpg'), ouvre('../img/mana010.jpg')) == 0:
        return 10
    sav(screen(2290,1022,20,3), '../img/mana09.jpg')
    if compare(ouvre('../img/mana9.jpg'), ouvre('../img/mana09.jpg'))  == 0:
        return 9
    sav(screen(2270,1022,20,3), '../img/mana08.jpg')
    if compare(ouvre('../img/mana8.jpg'), ouvre('../img/mana08.jpg')) == 0:
        return 8
    sav(screen(2250,1022,20,3), '../img/mana07.jpg')
    if compare(ouvre('../img/mana7.jpg'), ouvre('../img/mana07.jpg')) == 0:
        return 7
    sav(screen(2230,1022,20,3), '../img/mana06.jpg')
    if compare(ouvre('../img/mana6.jpg'), ouvre('../img/mana06.jpg')) == 0:
        return 6
    sav(screen(2210,1022,20,3), '../img/mana05.jpg')
    if compare(ouvre('../img/mana5.jpg'), ouvre('../img/mana05.jpg')) == 0:
        return 5
    sav(screen(2190,1022,20,3), '../img/mana04.jpg')
    if compare(ouvre('../img/mana4.jpg'), ouvre('../img/mana04.jpg')) == 0:
        return 4
    sav(screen(2170,1022,20,3), '../img/mana03.jpg')
    if compare(ouvre('../img/mana3.jpg'), ouvre('../img/mana03.jpg')) == 0:
        return 3
    sav(screen(2150,1022,20,3), '../img/mana02.jpg')
    if compare(ouvre('../img/mana2.jpg'), ouvre('../img/mana02.jpg')) == 0:
        return 2
    sav(screen(2130,1022,20,3), '../img/mana01.jpg')
    if compare(ouvre('../img/mana1.jpg'), ouvre('../img/mana01.jpg')) == 0:
        return 1
    return 0

def check_status():
    if int(contenu('../tmp/partie.txt')) == 1:
        if check_partie() == 0:
            if check_jaune() == 1:
                check_jouer()
    if int(contenu('../tmp/partie.txt')) != 1:
        jaune = check_jaune()
        if jaune == 1:
            check_jouer()
        if jaune == 0:
            check_partie()
    if int(contenu('../tmp/partie.txt')) == 1:
        return 3
    if int(contenu('../tmp/jaune.txt')) == 1:
        if int(contenu('../tmp/jouer.txt')) == 1:
            return 2
        return 1
    return 0


def clear():
    execute("rm -rf ../tmp/*")
    execute('echo "0" > ../tmp/maps.txt')
    execute('echo "0" > ../tmp/etat.txt')
    execute('echo "0" > ../tmp/partie.txt')
    execute('echo "0" > ../tmp/jouer.txt')
    execute('echo "0" > ../tmp/jaune.txt')
    execute('echo "1" > ../tmp/go.txt')
    execute('echo "0" > ../tmp/mort.txt')
    execute('echo "0" > ../tmp/talent.txt')

def check(name, n):
    status = check_status()
    commande = 'echo "' + str(status) + '" > ../tmp/etat.txt'
    execute(commande)
    if status == 1 or status == 2:
        execute('echo "0" > ../tmp/maps.txt')
    paus("1")
    if int(contenu('../tmp/go.txt')) == 1:
        check(name, n)

def check2(name, n):
    if int(contenu('../tmp/partie.txt')) == 1:
        print "Check 2"
        if int(contenu('../tmp/maps.txt')) == 0:
            check_map()
        #check_talent()
        #check_mort()
        print "PV :" + str(check_pv())
        #print "MANA :" + str(check_mana())
    paus("2")
    if int(contenu('../tmp/go.txt')) == 1:
        check2(name, n)

if __name__=='__main__': 
    clear()
    thread.start_new_thread(check, ("Status", 1))
    check2("Status", 1)
    #thread.start_new_thread(check2, ("Game", 1))
    while int(contenu('../tmp/go.txt')) == 1:
        paus("2")
    #deplace(500,520)
    #sav(screen(1900,60,400,400), 'test.jpg')
    #sav(screen(1900,60,400,400), 'test2.jpg')
    #print compare(screen(2000,60,40,40), ouvre('test.jpg'))
    #print compare(screen(2000,60,40,40), ouvre('test2.jpg'))
    #print compare(ouvre('test2.jpg'), ouvre('test.jpg'))
    #print comp(screen(2000,60,40,40), ouvre('test.jpg'))
    #print comp(screen(2000,60,40,40), ouvre('test2.jpg'))
    #print comp(ouvre('test2.jpg'), ouvre('test.jpg'))
    #paus('3')
    #delete('test.jpg')
    #print commande('ls')
    #print comp(screen(10,10,10,10), ouvre('test.jpg'))
    #print compare(screen(10,10,10,10), screen(10,10,10,10))
    #print comp(screen(10,10,10,10), screen(10,10,10,10))
    #print compare(ouvre('test.jpg'), ouvre('test.jpg'))
    #print comp(ouvre('test.jpg'), ouvre('test.jpg'))

