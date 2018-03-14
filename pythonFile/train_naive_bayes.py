# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 10:56:51 2018

@author: msarkar
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.mlab as mlab





#if __name__ == '__main__':
def train(plot=False):
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
    
    if plot:
    #print(parameter_df['Hold']['mu'].keys())
        features = list(parameter_df['Hold']['mu'].keys())
        features.remove('index')
        print(len(features))
        plt.figure(figsize=(30,15))
        for j in range(len(features)):
            plt.subplot(3,3,j+1)
            legend_str = ['','','','']
            for i in range(parameter_df.shape[1]):
                if features[j] == 'xacc' or features[j] == 'yacc' or features[j] == 'zacc':
                    mu = parameter_df[label_df['label'][i]]["mu"][features[j]]
                    sigma = parameter_df[label_df['label'][i]]["sig"][features[j]]
                else: 
                    mu = np.rad2deg(parameter_df[label_df['label'][i]]["mu"][features[j]])
                    sigma = np.rad2deg(parameter_df[label_df['label'][i]]["sig"][features[j]])
                x = np.linspace(mu - 3*sigma, mu + 3*sigma, 100)
                plt.plot(x,mlab.normpdf(x, mu, sigma))
                legend_str[i] = label_df['label'][i]
#    mu = parameter_df[label_df['label'][1]]["mu"][0]
#    sigma = parameter_df[label_df['label'][1]]["sig"][0]
#    x = np.linspace(mu - 3*sigma, mu + 3*sigma, 100)
#    plt.plot(x,mlab.normpdf(x, mu, sigma))
            plt.legend(legend_str)
            plt.title(features[j])
        plt.show()
        