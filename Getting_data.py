#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 29 23:47:27 2018

@author: naveen
"""
import all_file.TickerList as lst
import datetime as dt
from datetime import timedelta
import os
import pandas_datareader.data as web

def get_data():
    
  try:  
    #this is used to create the directory if the directory does ot exist 
    if not os.path.exists('stock_dfs'):
        os.makedirs('stock_dfs')
    
    #this line of code is use to set the start and the end date for the data 
    start = dt.datetime(2010,1,1)
    end = dt.datetime.now()
    print("retriving the data see the directories ! ")
    print("Will take some Minute ")
    for ticker in lst.lst1:
        #if the data is no present then extract from internet 
       
        if not os.path.exists('stock_dfs/{}.csv'.format(ticker)):
            #web crawling  useing pandas data reader and morningstar API
           
            df = web.DataReader(ticker, 'morningstar', start, end)
            df.reset_index(inplace=True)
            
            #setting the index of the dataset
            df.set_index("Date", inplace=True)
            
            #dropping the symoble column from dataset 
            df = df.drop("Symbol", axis=1)
            
            #to save the data in  CSV  formate in the dirctory stock_dfs
            df.to_csv('stock_dfs/{}.csv'.format(ticker))
        else:
            #this else part execute when the path and data file exist in the loacl disk
            try:
                #open the dataset in read mode
                fd=open('stock_dfs/{}.csv'.format(ticker),'r')
                linelist=fd.readlines()
                lastdate=linelist[-1].split(",")[0]
                #finding th elast date of dataset so we can use it update the dataset by making start date 
                start=dt.datetime.strptime(lastdate,"%Y-%m-%d") +timedelta(days=1)
               #close the dataset 
                fd.close()
                #open the data set again in append mode
                fd=open('stock_dfs/{}.csv'.format(ticker),'a')
                #using pandas data reader getting the data 
                df = web.DataReader(ticker, 'morningstar', start, end)
                 
                df.reset_index(inplace=True)
                #setting the index of the dataset
                df.set_index("Date", inplace=True)
                
                #dropping the symoble column from dataset 
                df = df.drop("Symbol", axis=1)
                #df.to_csv('stock_dfs/{}.csv'.format(ticker))
           
            
                for index,row in df.iterrows():
                    #iterating the the data frame 
                    s=index.strftime('%Y-%m-%d')+","+str(row["Close"])+","+str(row["High"])+","+str(row["Low"])+","+str(row["Open"])+","+str(row["Volume"])+ "\n"
                    #and then appending the data into existing data file
                    fd.write(s)
                    #after appending the data closeing the dataset 
                fd.close()
                print("data updated",ticker)
            except Exception as e:
                print("data updated ",ticker)
  except Exception as e:
        
        print("Data updated")