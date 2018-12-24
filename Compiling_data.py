#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 29 23:48:15 2018

@author: naveen
"""
import pandas as pd
import all_file.TickerList as lst

def compile_data():

    #craeting the blank  blank datafrem using pandas  
    new_data_frame  = pd.DataFrame()
    
    try:
        #enumerate return the count of the element
        for count, ticker in enumerate(lst.lst1):
            
            #reading the existing table  from local disk
            df = pd.read_csv('stock_dfs/{}.csv'.format(ticker))
            
            #setting the date as index 
            df.set_index('Date', inplace=True)
            
            #renaming the Close column with the name of ticker(the name of the stock )
            df.rename(columns={'Close': ticker},inplace=True)
            
            #checking the df if the df has the first column as symbol
            if(df.columns[0]=='Symbol'):
                
                #droppping the column using is not usable further in proccess
                df.drop(['Symbol','Open', 'High', 'Low', 'Volume'], 1, inplace=True)
                
            else:
                
                #droppping the column using is not usable further in proccess
                df.drop(['Open', 'High', 'Low', 'Volume'], 1, inplace=True)
       
            if new_data_frame .empty:
                
                #if the newley creted data frame have no data then the modified data get added to it
                new_data_frame  = df
                
            else:
                
                #if the newley creted data frame have  data then the modified data get joned  to it
                new_data_frame  = new_data_frame.join(df, how='outer')

            if count % 20 == 0:
                print("compiling the data")
    except Exception as e:
        print(e)
        
        
    #storing th compiled data into other csv file which is stored into local file 
    new_data_frame .to_csv('sp500_joined_closes.csv')


#compile_data()