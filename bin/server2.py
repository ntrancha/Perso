#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

import sys_nk
import maps_nk
import check_nk
import global_nk
import thread_nk

if __name__=='__main__': 
    global_nk.init()
    #sys_nk.sav(sys_nk.screen(3482,155,20,20), '../img/status/?.jpg')
    #thread.start_new_thread(thread_nk.thread_check, ("A", 0))
    thread_nk.thread_check("A", 0)
    while int(sys_nk.contenu('../tmp/go.txt')) == 1:
        sys_nk.paus("2")

