#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

import sys_nk
import maps_nk
import check_nk
import global_nk
from threading import Thread, RLock
import threading
import thread

verrou = RLock()

def thread_check(name, n):
    thread.start_new_thread(thread_check_process, ("A", 0))
    thread.start_new_thread(thread_check_status, ("A", 0))
    thread.start_new_thread(thread_check_game, ("A", 0))
    thread.start_new_thread(thread_check_map, ("A", 0))

def thread_check_process(name, n):
    while global_nk.get_go() == 1:
        check_nk.check_go()

def thread_check_status(name, n):
    while global_nk.get_go() == 1:
        status = check_nk.check_status()
        old = global_nk.get_etat()
        global_nk.set_status(int(status))
        global_nk.set_etat(int(status))
        if old != status:
            sys_nk.clear_console()
            print "-------------------"
            print "STATUS: " + str(status)
        if status == 1 or status == 2:
            if old == status:
                global_nk.init()

def thread_check_game(name, n):
    while global_nk.get_go() == 1:
        if global_nk.get_partie() == 1:
            maps = 0
            check_nk.check_score("A", 0)
            if global_nk.get_maps() == 0:
                maps = check_nk.check_map()
            if global_nk.get_player() == 0:
                check_nk.check_talent()
                if check_nk.check_mort() == 0:
                    old_pv = global_nk.get_pv()
                    old_mana = global_nk.get_mana()
                    pv = check_nk.check_pv()
                    mana = check_nk.check_mana()
                    if pv != 0:
                        global_nk.set_pv(pv)
                    if mana != 0:
                        global_nk.set_mana(mana)
                    if old_pv != global_nk.get_pv():
                        print "Pv: "+str(global_nk.get_pv())
                    if old_mana != global_nk.get_mana():
                        print "Mana"+str(global_nk.get_mana())

def thread_check_map(name, n):
    while global_nk.get_go() == 1:
        if global_nk.get_partie() == 1:
            if global_nk.get_maps() != 0:
                maps_nk.check_maps(global_nk.get_maps())
