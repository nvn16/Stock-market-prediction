#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 29 23:51:01 2018

@author: naveen


"""

import numpy as np
from all_file import Proccesing_data 
from collections import Counter

    

#the buy_sell_hold function use to assign the value if the calculated percentage change is grater then 1% =0.01 then 1 
#if the   percentage change is the less then 1% then -1
#else the value will assign to 0
def buy_sell_hold(*args):
    cols = [c for c in args]
    requirement = 0.01
    for col in cols:
        if col > requirement:
            return 1
        if col < -requirement:
            return -1
    return 0

# thsi function used to extract the feature
def extract_featuresets(ticker):
    #for handling the exception 
    try:
        #caling the process_data_for_labels function 
        tickers, df =Proccesing_data.process_data_for_labels(ticker)
        #using map calling buy_sell_hold function 
        #this will retuen th elist of (0,1,-1)
        df['{}_target'.format(ticker)] = list(map( buy_sell_hold,
           #these are the parameter which is get from the process data for lables mathed
                                                   df['{}_1d'.format(ticker)],
                                                   df['{}_2d'.format(ticker)],
                                                   df['{}_3d'.format(ticker)],
                                                   df['{}_4d'.format(ticker)],
                                                   df['{}_5d'.format(ticker)],
                                                   df['{}_6d'.format(ticker)],
                                                   df['{}_7d'.format(ticker)]))
       
        #converting the value of the df into list 
        vals = df['{}_target'.format(ticker)].values.tolist()
        
        #converting that value of  that list into sting  
        str_vals = [str(i) for i in vals]
        
        #prining the count of 1,-1,0 in that data which represent the bhaviour of the stock 
        print('Data spread:', Counter(str_vals))
        
        #used to replace  the na with the 0
        df.fillna(0, inplace=True)
        
        #used to replace the infinite and negative infinite  and nan too
        df = df.replace([np.inf, -np.inf], np.nan)
        
        #droping the na 
        df.dropna(inplace=True)
        
        #calculating percentage change in the close column for every stock company 
        df_vals = df[[ticker for ticker in tickers]].pct_change()
        
        #afetr finding the percentage chnage 
        #used to replace the infinite and negative infinite  and nan too
        df_vals = df_vals.replace([np.inf, -np.inf], 0)
        
        #used to replace  the na with the 0
        df_vals.fillna(0, inplace=True)
        #storing the value of the percentage change into x vriable
        X = df_vals.values
        
        #storing the value(0,1,-1) into variable y
        y = df['{}_target'.format(ticker)].values
       
        
        #returning the variable x,y and dataframe df 
        return X, y, df
    
    except Exception as e:
        print()
