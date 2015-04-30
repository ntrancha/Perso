#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

import sys_nk
import thread_nk
from threading import Thread, RLock
import thread

G_etat = 0
v_etat = RLock()
G_jaune = 0
v_jaune = RLock()
G_jouer = 0
v_jouer = RLock()
G_maps = 0
v_maps = RLock()
G_mort = 0
v_mort = RLock()
G_partie = 0
v_partie = RLock()
G_talent = 0
v_talent = RLock()
G_status = 0
v_status = RLock()
G_go = 1
v_go = RLock()
G_pv = 0
v_pv = RLock()
G_mana = 0
v_mana = RLock()
G_score = 0
v_score = RLock()
G_player = 0
v_player = RLock()
G_statusold = 0
v_statusold = RLock()
G_statusreal = 0
v_statusreal = RLock()

def getter(var):
    ve = "v_" + var
    va = "G_" + var
    with globals()[ve]:
        return globals()[va]

def setter(var, val):
    ve = "v_" + var
    va = "G_" + var
    with globals()[ve]:
        globals()[va] = val

def init():
    #sys_nk.execute("rm -rf ../tmp/*")
    sys_nk.execute('echo "1" > ../tmp/go.txt')
    sys_nk.get_pid()
    setter('etat', 0)
    setter('jaune', 0)
    setter('jouer', 0)
    setter('maps', 0)
    setter('mort', 0)
    setter('partie', 0)
    setter('talent', 0)
    setter('status', 0)
    setter('go', 1)
    setter('pv', 0)
    setter('mana', 0)
    setter('score', 0)
    setter('player', 0)

def debug():
    print 'etat: ' + str(getter('etat'))
    print 'status: ' + str(getter('statusreal'))
    if getter('jaune') != 0:
        print 'jaune: ' + str(getter('jaune'))
    if getter('jouer') != 0:
        print 'jouer: ' + str(getter('jouer'))
    if getter('maps') != 0:
        print 'maps: ' + str(getter('maps'))
    if getter('mort') != 0:
        print 'mort: ' + str(getter('mort'))
    if getter('partie') != 0:
        print 'partie: ' + str(getter('partie'))
    if getter('talent') != 0:
        print 'talent: ' + str(getter('talent'))
    if getter('pv') != 0:
        print 'pv: ' + str(getter('pv'))
    if getter('mana') != 0:
        print 'mana: ' + str(getter('mana'))
    if getter('score') != 0:
        print 'score: ' + str(getter('score'))
    if getter('player') != 0:
        print 'player: ' + str(getter('player'))
