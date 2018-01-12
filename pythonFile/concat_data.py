# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 12:20:27 2018

@author: msarkar
"""

import pandas as pd


if __name__ == '__main__':
    df1 = pd.read_json('train16.json')
    df1 = df1.dropna()
    df2 = pd.read_json('train1.json')
    df2 = df2.dropna() 
    df3 = pd.read_json('train6.json')
    df3 = df3.dropna()
    
    df = pd.concat([df1, df2, df3])
    df = df.reset_index()
    df.to_json("train.json")
    
    