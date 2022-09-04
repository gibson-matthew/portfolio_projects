#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 3 08:23:50 2022

@author: barrelrider
"""
### USED TO PAUSE AND REFRESH CONSOLE
import os
import time

### FIRST IMAGE FOR CONSOLE | FOR TOP AND BOTTOM OF BOX
def box_top():
    print('    ', end='')
    for i in range (0, int(new_inside)):
        print('♢', end='')
        print('♤', end='')
        print('♥', end='')
    return ''

### SECOND IMAGE FOR CONSOLE | FOR TOP AND BOTTOM OF BOX
def box_top2():
    print('    ', end='')
    for i in range (0, int(new_inside)):
        print('♥', end='')
        print('♢', end='')
        print('♤', end='')
    return ''
        
def box_top3():
    print('    ', end='')
    for i in range (0, int(new_inside)):
        print('♤', end='')
        print('♥', end='')
        print('♢', end='')
    return ''

def box_bot():
    print('    ', end='')
    for i in range (0, int(new_inside)):
        print('♤', end='')
        print('♢', end='')
        print('♥', end='')
    return ''

def box_bot2():
    print('    ', end='')
    for i in range (0, int(new_inside)):
        print('♢', end='')
        print('♥', end='')
        print('♤', end='')
    return ''

def box_bot3():
    print('    ', end='')
    for i in range (0, int(new_inside)):
        print('♥', end='')
        print('♤', end='')
        print('♢', end='')
    return ''

### CREATES BOX SIDES 
def intro():
    # INFORMATION INSIDE BOX
    global new_inside
    welcome = "      I love programming!!!!     "

    box_inside = " "  * int(33)  # LENGTH BETWEEN SIDES
    new_inside = int(8)         # LENGTH OF TOP AND BOTTOM
    while True:
        # FIRST IMAGE FOR CONSOLE | SIDES OF BOX
        print(box_top())
        print("    ♤" + box_inside + "♢")
        print("    ♥" + box_inside + "♤")
        print("    ♤" + welcome + "♥")
        print("    ♢" + box_inside + "♢")
        print("    ♥" + box_inside + "♤")
        print(box_bot()) 
        
        # REFRESHES CONSOLE FOR SECOND BOX
        time.sleep(1)
        os.system('clear')
        
        #SECOND IMAGE FOR CONSOLE | SIDES OF BOX
        print(box_top2())
        print("    ♢" + box_inside + "♥")
        print("    ♤" + box_inside + "♢")
        print("    ♢" + welcome + "♤")
        print("    ♥" + box_inside + "♥")
        print("    ♤" + box_inside + "♢")
        print(box_bot2()) 
        
        # REFRESHES CONSOLE FOR FIRST BOX
        time.sleep(1)
        os.system('clear')
        
        print(box_top3())
        print("    ♤" + box_inside + "♤")
        print("    ♢" + box_inside + "♥")
        print("    ♥" + welcome + "♢")
        print("    ♤" + box_inside + "♤")
        print("    ♢" + box_inside + "♥")
        print(box_bot3())
        
        # REFRESHES CONSOLE FOR FIRST BOX
        time.sleep(1)
        os.system('clear')
        
# PROGRAM START
intro()


