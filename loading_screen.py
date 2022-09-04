#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 31 08:15:45 2022

@author: barrelrider
"""
import os, time

# LOADING SCREEN
def loading_screen():
    while True:
        print('Loading', end='')
        time.sleep(1)
        print('.', end='')
        time.sleep(1)
        print('.', end='')
        time.sleep(1)
        print('.', end='')
        time.sleep(1)
        os.system('clear')
        
# PROGRAM START
loading_screen()

