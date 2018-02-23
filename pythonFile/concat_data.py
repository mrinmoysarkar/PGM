# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 12:20:27 2018

@author: msarkar
"""

import pandas as pd
import random
import numpy as np

#if __name__ == '__main__':
def dataConcat(n_):
    n = n_;
    all_data_set = list(np.linspace(1,7,7,dtype=np.int)) + list(np.linspace(10,22,13,dtype = np.int))
#    data_with_all_state=[1, 3, 4, 6, 7, 10, 11, 12, 14, 15, 16, 17, 20, 22]
#    train_set_label=random.sample(data_with_all_state,n)#data_with_all_state#[16,1,6,2,5,7,17]
#    df = pd.read_json('train'+str(train_set_label[0])+'.json')
#    for i in range(len(train_set_label)-1):
#        df1 = pd.read_json('train'+str(train_set_label[i+1])+'.json')
#        df1 = df1.dropna()
#        df = pd.concat([df, df1])
        #df = df.reset_index()
    
#    df2 = pd.read_json('train1.json')
#    df2 = df2.dropna() 
#    df3 = pd.read_json('train6.json')
#    df3 = df3.dropna()
#    
#    df = pd.concat([df1, df2, df3])
#    df = df.reset_index()
#    df.to_json("train.json")
    

    df = pd.read_json('train'+str(all_data_set[0])+'.json')
    for i in range(len(all_data_set)-1):
        df1 = pd.read_json('train'+str(all_data_set[i+1])+'.json')
        df1 = df1.dropna()
        df = pd.concat([df, df1])
        
    df = df.reset_index()
    #print(df.iloc[1])
    df = df.sample(frac=1).reset_index(drop=True)
    total_sample = df.shape[0]
    train_sample = int(n*total_sample)
    
    #print(total_sample,train_sample)
    df.to_json("train.json")
    #print(df.iloc[0])
    df_train = df.iloc[0:train_sample]
    #print(df_train.shape)
    df_test = df.iloc[train_sample:total_sample]
    #print(df_test.shape)
    df_train.to_json("train.json")
    df_test.to_json("test.json")
    