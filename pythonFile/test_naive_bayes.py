# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 11:40:25 2018

@author: msarkar
"""


import pandas as pd
import numpy as np


def gaussian(x, mu, sig):
    return np.exp(-np.power(x - mu, 2.) / (2 * np.power(sig, 2.)))

def classify(sample, parameter):
    keys = parameter.keys()
    correct_label = sample["state"]
    sample_keys = list(sample.keys())
    sample_keys.remove("state")
    n = keys.shape[0]
    m = len(sample_keys)
    prb = []
    for i in range(n):
        ky1 = keys[i]
        p = 1
        for j in range(m):
            ky2 = sample_keys[j]
            mu = parameter[ky1]["mu"][ky2]
            sig = parameter[ky1]["sig"][ky2]
            x = sample[ky2]
            px = gaussian(x,mu,sig)
            p *= px
        #p *= parameter[ky1]["prior"]
        prb += [p]
    if keys[prb.index(max(prb))] == correct_label:
        return 1
    else:
        return 0
    
            

#if __name__ == '__main__':
def test():
    l=1
    l1 = list(np.linspace(1,7,7,dtype=np.int)) + list(np.linspace(10,22,13,dtype = np.int))
    ll = len(l1)
    output = np.zeros(ll)
    for l in range(ll):
        file_name = 'train' + str(l1[l]) + '.json'
        train_data_df = pd.read_json(file_name)
        train_data_df = train_data_df.dropna()
        #label_df = pd.read_json('label.json')
        parameter_df = pd.read_json('parameter.json')
    
        n = train_data_df.shape[0]
        #m = label_df.shape[0]
        correct = 0
        for i in range(n):
            sample_df = train_data_df.iloc[i]
            correct += classify(sample_df, parameter_df)
        
        #print(n,correct)
        correct_percent = round(correct*100/n,2)
        print('test Data '+ str(l1[l]) + ': '+ str(correct_percent)+'%')
        output[l] = correct_percent
    return output