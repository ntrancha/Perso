#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

import threading
import thread
import math, operator
import pyscreenshot as ImageGrab
from PIL import Image
from random import randint
import numpy
import sys
import os
import sys_nk
import verif
import maps_nk

def jouer():
    sys_nk.deplace(2240, 35)
    sys_nk.execute('./click.sh 2240 35 10 1')
    return 1

def rapide():
    sys_nk.deplace(2280, 100)
    sys_nk.execute('./click.sh 2280 100 10 1')
    return 1

def coop():
    sys_nk.deplace(2450, 100)
    sys_nk.execute('./click.sh 2450 100 10 1')
    return 1

def pret():
    sys_nk.deplace(2875, 1020)
    sys_nk.execute('./click.sh 2875 1020 10 1')
    return 1

def perso():
    sys_nk.deplace(2875, 500)
    sys_nk.execute('./click.sh 2875 500 10 1')
    return 1
