#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

import sys_nk
import maps_nk
import check_nk
import global_nk
from threading import Thread, RLock
import thread

verrou = RLock()

def thread_check(name, n):
    thread.start_new_thread(thread_check_process, ("A", 0))
    thread.start_new_thread(thread_check_status, ("A", 0))
    thread.start_new_thread(thread_check_game, ("A", 0))
    thread.start_new_thread(thread_check_map, ("A", 0))

def thread_check_process(name, n):
    while global_nk.getter('go') == 1:
        check_nk.check_go()

def thread_check_status(name, n):
    while global_nk.getter('go') == 1:
        status = check_nk.check_status()
        old = global_nk.getter('etat')
        global_nk.setter('status', int(status))
        global_nk.setter('etat', int(status))
        if old != status:
            sys_nk.clear_console()
            print "-------------------"
            print "STATUS: " + str(status)
        if status == 1 or status == 2:
            if old == status:
                global_nk.init()
        global_nk.debug()

def thread_check_game(name, n):
    while global_nk.getter('go') == 1:
        if global_nk.getter('partie') == 1:
            maps = 0
            check_nk.check_score("A", 0)
            if global_nk.getter('maps') == 0:
                maps = check_nk.check_map()
            if global_nk.getter('player') == 0:
                check_nk.check_talent()
                if check_nk.check_mort() == 0:
                    old_pv = global_nk.getter('pv')
                    old_mana = global_nk.getter('mana')
                    pv = check_nk.check_pv()
                    mana = check_nk.check_mana()
                    if pv != 0:
                        global_nk.setter('pv', pv)
                    if mana != 0:
                        global_nk.setter('mana', mana)
                    if old_pv != global_nk.getter('pv'):
                        print "Pv: "+str(global_nk.getter('pv'))
                    if old_mana != global_nk.getter('mana'):
                        print "Mana"+str(global_nk.getter('mana'))

def thread_check_map(name, n):
    while global_nk.getter('go') == 1:
        if global_nk.getter('partie') == 1:
            if global_nk.getter('maps') != 0:
                maps_nk.check_maps(global_nk.getter('maps'))
