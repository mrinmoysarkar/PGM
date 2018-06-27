# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 12:20:27 2018

@author: msarkar
"""

import pandas as pd
import random
import numpy as np

if __name__ == '__main__':
    all_data_set = list(np.linspace(1,7,7,dtype=np.int)) + list(np.linspace(10,22,13,dtype = np.int))
    df = pd.read_json('train'+str(all_data_set[0])+'.json')
    for i in range(len(all_data_set)-1):
        df1 = pd.read_json('train'+str(all_data_set[i+1])+'.json')
        df1 = df1.dropna()
        df = pd.concat([df, df1])
#        df = df.reset_index()
    
#    df2 = pd.read_json('train1.json')
#    df2 = df2.dropna() 
#    df3 = pd.read_json('train6.json')
#    df3 = df3.dropna()
#    
#    df = pd.concat([df1, df2, df3])
    df = df.reset_index()
    df.to_json("dataset.json")