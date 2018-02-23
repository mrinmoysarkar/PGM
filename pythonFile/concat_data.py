# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 12:20:27 2018

@author: msarkar
"""

import pandas as pd
import random

#if __name__ == '__main__':
def dataConcat(n_):
    n = n_;
    data_with_all_state=[1, 3, 4, 6, 7, 10, 11, 12, 14, 15, 16, 17, 20, 22]
    train_set_label=random.sample(data_with_all_state,n)#data_with_all_state#[16,1,6,2,5,7,17]
    df = pd.read_json('train'+str(train_set_label[0])+'.json')
    for i in range(len(train_set_label)-1):
        df1 = pd.read_json('train'+str(train_set_label[i+1])+'.json')
        df1 = df1.dropna()
        df = pd.concat([df, df1])
        #df = df.reset_index()
    
#    df2 = pd.read_json('train1.json')
#    df2 = df2.dropna() 
#    df3 = pd.read_json('train6.json')
#    df3 = df3.dropna()
#    
#    df = pd.concat([df1, df2, df3])
    df = df.reset_index()
    df.to_json("train.json")
    
    