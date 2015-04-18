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
    print 'jaune: ' + str(getter('jaune'))
    print 'jouer: ' + str(getter('jouer'))
    print 'maps: ' + str(getter('maps'))
    print 'mort: ' + str(getter('mort'))
    print 'partie: ' + str(getter('partie'))
    print 'talent: ' + str(getter('talent'))
    print 'status: ' + str(getter('status'))
    print 'go: ' + str(getter('go'))
    print 'pv: ' + str(getter('pv'))
    print 'mana: ' + str(getter('mana'))
    print 'score: ' + str(getter('score'))
    print 'player: ' + str(getter('player'))
