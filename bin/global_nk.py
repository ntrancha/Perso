#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

import sys_nk

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
