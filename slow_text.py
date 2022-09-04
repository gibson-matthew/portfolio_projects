#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 31 08:25:05 2022

@author: barrelrider
"""
import time

# Text to be iterated
output = "My name is Matthew, and this is a slow line of output."

# Iterates output variable
def slow_text():
    for i in output:
        for x in i:
            print(x, end='')
            time.sleep(0.3)
            
# Program Start
slow_text()
