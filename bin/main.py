#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

import global_nk
import thread_nk
import interface_nk
from Tkinter import *

if __name__=='__main__':
    global_nk.init()
    thread_nk.thread_check("A", 0)
    fenetre = Tk()
    interface = interface_nk.Interface(fenetre)
    interface.mainloop()
    interface.destroy()
