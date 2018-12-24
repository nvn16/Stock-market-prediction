#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  4 15:37:56 2018

@author: naveen
"""


from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk,FigureCanvasTk
from matplotlib.figure import Figure
import matplotlib.animation as animation
from matplotlib import style
from  all_file import Machine_learning as ml
import tkinter as tk
from tkinter import ttk
import pandas as pd
import numpy as np

LARGE_FONT= ("Verdana", 12)
style.use("ggplot")
f = Figure(figsize=(10,6), dpi=100)
a = f.add_subplot(111)




class SeaofBTCapp(tk.Tk):

    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)

        tk.Tk.wm_title(self, "Stock market pridiction")
        
        #craeting frame 
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage,PageOne, BTCe_Page):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()


#this is implementation of the first or start page 
class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text=("""Hii there !
            By clicking on Agree your accept are terms and condition"""), font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        
        #creating the button
        button1 = ttk.Button(self, text="Agree",
                            command=lambda: controller.show_frame(BTCe_Page))
        button1.pack()

        #creating the button
        button2 = ttk.Button(self, text="Disagree",
                            command=quit)
        button2.pack()


#this one used for graph representation page 
class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page One!!!", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()




class BTCe_Page(tk.Frame):
    
    
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        #this use for lableing in the graph
        label = tk.Label(self, text="Stock Market Prediction !", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

       #creating the button
        button1 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()
        
        #letting the user putting the stock name 
        self.label = tk.Label(self, text="enter the stock name.")
        self.label.pack()
        
        self.digits = tk.StringVar()
        self.e1=tk.Entry(self, textvariable=self.digits)
        self.e1.pack()
        
        # creating the button
        self.buttontext = tk.StringVar()
        self.buttontext.set("Stock")
        tk.Button(self,
                  textvariable=self.buttontext,
                  command=self.animate
                  ).pack()
        
        
        
        #creating the canvas for graph represntations 
        canvas = FigureCanvasTkAgg(f, self)
        FigureCanvasTk.draw
        
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        
        #used to plote theh navgation bar on the graph
        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
       
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        
        
        
    #this method used for plotting the graph 
    def animate(self):
        
        try:
            StkName=self.e1.get()
            #converting theh stock name into uper latter
            S_Name=StkName.upper()
            print(S_Name)
            
            #used to call the machine learning method and predict the result 
            #and storing the output of machine learnig into output variable 
            self.output=ml.do_ml(S_Name)
            
            #printing th output
            print(self.output)
            
            #craeting the file name using user input 
            stockname=self.e1.get().upper()+".csv"
            
            #reading the cdv fil frrm the local disk
            df=pd.read_csv("stock_dfs/"+stockname)
            
            #getting the last seven days data 
            df1=df[-9:]
            y=df1["Close"]
            #onverting date column into numpy array 
            date=np.array(df1["Date"])
            
            #plotting the date on x axis of graph
            xlab = df1["Date"]
            date=np.array(df1["Date"])
           
           #used to clear the canvas 
            a.clear()
            
            #printing the result of machine earing on the x axis 
            a.set_xlabel(self.output)
            a.set_xticklabels(xlab, rotation='horizontal', fontsize=8 )
            
            #used to plot 
            a.plot(y)
        
            
            
            
        except Exception as e:
      
            pass
            
        
        





app = SeaofBTCapp()
ani= animation.FuncAnimation(f, BTCe_Page.animate, interval=10)
app.mainloop()
