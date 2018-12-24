#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 29 23:50:04 2018

@author: naveen
"""



import pandas as pd



    
def process_data_for_labels(ticker):
    try:
        #this represnt:- for the how many day we want to predict
        days = 7
        
        #reading the compiled data file  from local disk 
        
        df = pd.read_csv('sp500_joined_closes.csv', index_col=0)
        
        #converting the column vlaue to list 
        tickers = df.columns.values.tolist()
        
        #this used to replace the na value(if present in the data) with the value 0
        df.fillna(0, inplace=True)
        
        for i in range(1,days+1):
            
            #this used to find the precentage change from the date to next seven days 
            df['{}_{}d'.format(ticker,i)] = (df[ticker].shift(-i) - df[ticker]) / df[ticker]
            
        # #this used to replace the na value(if present in the data) with the value 0 after the colcuation of percentage
        df.fillna(0, inplace=True)
        
        #returning the tickers(list of stock market symbol ) and the data frame 
        return tickers, df
    
    except Exception as e:
        
        #if the asked ticker(stock market symbol of a company ) is not present 
        print("Please write correct stock name")