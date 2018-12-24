#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 30 00:04:28 2018

@author: naveen
"""
from  all_file import Compiling_data as p
from  all_file import Getting_data as g


import os
      
    
       
class all_main(object):
    def run(self):
        #to get the data at run time

        g.get_data()

        # to covert data into usable form 

       	p.compile_data()

       # to open the graphical user interface 
        os.system("python3 tjinter.py")
       

if __name__ == '__main__':
    all_main().run()
   
