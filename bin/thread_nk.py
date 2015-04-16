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
        print "STATUS"
        status = check_nk.check_status()
        global_nk.G_status = int(status)
        global_nk.G_etat = int(status)
        print int(status)
        if status == 1 or status == 2:
            global_nk.G_maps = 0
            global_nk.G_partie = 0

def thread_check_game(name, n):
    if global_nk.G_go == 1:
        if global_nk.G_partie == 1:
            print "GAME"
            maps = 0
            check_nk.check_score("A", 0)
            if global_nk.G_maps == 0:
                maps = check_nk.check_map()
            if global_nk.G_player == 0:
                check_nk.check_talent()
                if check_nk.check_mort() == 0:
                    global_nk.G_pv = check_nk.check_pv()
                    global_nk.G_mana = check_nk.check_mana()

def thread_check_map(name, n):
    if global_nk.G_go == 1:
        if global_nk.G_partie == 1:
            if global_nk.G_maps != 0:
                print "1:"
                maps_nk.check_maps()
