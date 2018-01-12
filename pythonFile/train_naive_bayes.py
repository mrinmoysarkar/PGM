# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 10:56:51 2018

@author: msarkar
"""

import pandas as pd




if __name__ == '__main__':
    train_data_df = pd.read_json('train.json')
    train_data_df = train_data_df.dropna()
    label_df = pd.read_json('label.json')

    n = label_df.shape[0]
    parameter_df = pd.DataFrame()
    total_training_instance = train_data_df.shape[0]
    for i in range(n):
        data_df = train_data_df.loc[train_data_df['state'] == label_df['label'][i]]
        mu = data_df.mean()
        sig = data_df.std()
        n1 = data_df.shape[0]
        prior_prob = n1/total_training_instance
        parameter_df = pd.concat([parameter_df, pd.DataFrame({label_df['label'][i]:{"mu":mu,"sig":sig,"prior":prior_prob}})], axis = 1)
    
    parameter_df.to_json("parameter.json")