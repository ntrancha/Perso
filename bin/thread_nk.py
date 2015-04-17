#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

import sys_nk
import maps_nk
import check_nk
import global_nk
import threading
import thread

def thread_check(name, n):
    while global_nk.G_go == 1:
        thread_check_process(name, n)
        thread_check_status(name, n)
        thread_check_game(name, n)
        thread_check_map(name, n)

def thread_check_process(name, n):
    if global_nk.G_go == 1:
        check_nk.check_go()

def thread_check_status(name, n):
    if global_nk.G_go == 1:
        status = check_nk.check_status()
        old = global_nk.G_etat
        global_nk.G_status = int(status)
        global_nk.G_etat = int(status)
        if old != status:
            sys_nk.clear_console()
            print "-------------------"
            print "STATUS: " + str(status)
        if status == 1 or status == 2:
            if old == status:
                global_nk.init()

def thread_check_game(name, n):
    if global_nk.G_go == 1:
        if global_nk.G_partie == 1:
            maps = 0
            check_nk.check_score("A", 0)
            if global_nk.G_maps == 0:
                maps = check_nk.check_map()
            if global_nk.G_player == 0:
                check_nk.check_talent()
                if check_nk.check_mort() == 0:
                    old_pv = global_nk.G_pv
                    old_mana = global_nk.G_mana
                    pv = check_nk.check_pv()
                    mana = check_nk.check_mana()
                    if pv != 0:
                        global_nk.G_pv = pv
                    if mana != 0:
                        global_nk.G_mana = mana
                    if old_pv != global_nk.G_pv:
                        print "Pv: "+str(global_nk.G_pv)
                    if old_mana != global_nk.G_mana:
                        print "Mana"+str(global_nk.G_mana)

def thread_check_map(name, n):
    if global_nk.G_go == 1:
        if global_nk.G_partie == 1:
            if global_nk.G_maps != 0:
                maps_nk.check_maps()
