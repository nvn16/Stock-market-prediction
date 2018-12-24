#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 29 23:52:49 2018

@author: naveen
"""
from all_file import Extract_feature as p
from collections import Counter
from sklearn import svm, cross_validation, neighbors
from sklearn.ensemble import VotingClassifier, RandomForestClassifier

#defining the machine learning function  
def do_ml(ticker):
    #handling the exception 
    try:
        #calling the extracting feature whc return x,y ,df
        #value of the percentage change into x vriable
        #the value(0,1,-1) into variable y fro lable
        #df represent data frame
        X, y, df = p.extract_featuresets(ticker)
        
        #dividing the x and y into traing and testing data set 
        #where traing set consist 75% of data 
        #where 25 % of data used for testing 
        X_train, X_test, y_train, y_test = cross_validation.train_test_split(X,
                                                                             y,
                                                                        test_size=0.25)
        #this used nearest neighbors classifire for classification 
        #clf = neighbors.KNeighborsClassifier()
        
        #thi used the support vector machine(svm) classifier
        #clf=svm.LinearSVC()
    
        #this is another mechanism  for classification called voting classifier
        #voting classifer use more then one classification algorith and give the result of those alge ehich gives 
        #the best result 
        
        
        
    
        clf = VotingClassifier([('lsvc',svm.LinearSVC()),
                            ('knn',neighbors.KNeighborsClassifier()),
                            ('rfor',RandomForestClassifier())])

    
        #fitting the model 
        clf.fit(X_train, y_train)
        
        #finding the confidence 
        confidence = clf.score(X_test, y_test) *100
        
        print('accuracy:',confidence)
        
        #predicting the vlaue
        predictions = clf.predict(X_test)
        
        #printing the count of 1,0,-1 of prediction value
        print('predicted class counts:',Counter(predictions))
        
        #assigning the counting value to a variable a
        a = Counter(predictions)
        #extracting the value of 1,0,-1
        b = a[0]
        c = a[1]
        d = a[-1]
        
        #camparison between the count of 1,0,-1
        if(b>c and b>d):
            
            #if the count of 0 is greater the hold the stock 
            return "HOLD"
        
        elif(c>b and c>d):
            #if the count of 1 is grater then buy stock 
            return "BUY"
        else:
            #else just sell the sock if -1 count is grater 
            return "SELL"
            
        
        print()
        print()
    except Exception as e:
        print()
    
#do_ml(name)
