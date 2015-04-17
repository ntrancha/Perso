#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

import sys_nk
import thread_nk

G_etat = 0
G_jaune = 0
G_jouer = 0
G_maps = 0
G_mort = 0
G_partie = 0
G_talent = 0
G_status = 0
G_go = 1
G_pv = 0
G_mana = 0
G_score = 0
G_player = 0

def get_etat():
    with thread_nk.verrou:
        return G_etat

def set_etat(val):
    with thread_nk.verrou:
        G_etat = val

def get_jaune():
    with thread_nk.verrou:
        return G_jaune

def set_jaune(val):
    with thread_nk.verrou:
        G_jaune = val

def get_jouer():
    with thread_nk.verrou:
        return G_jouer

def set_jouer(val):
    with thread_nk.verrou:
        G_jouer = val

def get_maps():
    with thread_nk.verrou:
        return G_maps

def set_maps(val):
    with thread_nk.verrou:
        G_maps = val

def get_mort():
    with thread_nk.verrou:
        return G_mort

def set_mort(val):
    with thread_nk.verrou:
        G_mort = val

def get_partie():
    with thread_nk.verrou:
        return G_partie

def set_partie(val):
    with thread_nk.verrou:
        G_partie = val

def get_talent():
    with thread_nk.verrou:
        return G_talent

def set_talent(val):
    with thread_nk.verrou:
        G_talent = val

def get_status():
    with thread_nk.verrou:
        return G_status

def set_status(val):
    with thread_nk.verrou:
        G_status = val

def get_go():
    with thread_nk.verrou:
        return G_go

def set_go(val):
    with thread_nk.verrou:
        G_go = val

def get_pv():
    with thread_nk.verrou:
        return G_pv

def set_pv(val):
    with thread_nk.verrou:
        G_pv = val

def get_mana():
    with thread_nk.verrou:
        return G_mana

def set_mana(val):
    with thread_nk.verrou:
        G_mana = val

def get_sccore():
    with thread_nk.verrou:
        return G_score

def set_score(val):
    with thread_nk.verrou:
        G_score = val

def get_player():
    with thread_nk.verrou:
        return G_player

def set_player(val):
    with thread_nk.verrou:
        G_player = val


def init():
    #sys_nk.execute("rm -rf ../tmp/*")
    sys_nk.execute('echo "1" > ../tmp/go.txt')
    global G_etat
    global G_jaune
    global G_jouer
    global G_maps
    global G_mort
    global G_partie
    global G_talent
    global G_status
    global G_go
    global pv
    global mana
    global G_score
    global G_player
    G_etat = 0
    G_jaune = 0
    G_jouer = 0
    G_maps = 0
    G_mort = 0
    G_partie = 0
    G_talent = 0
    G_status = 0
    G_go = 1
    G_pv = 0
    G_mana = 0
    G_score = 0
    G_player = 0
