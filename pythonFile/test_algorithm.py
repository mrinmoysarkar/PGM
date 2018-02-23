# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 17:45:27 2018

@author: msarkar
"""

import loaddata
import concat_data
import train_naive_bayes
import test_naive_bayes
import numpy as np

if __name__ == '__main__':
    result = np.zeros(20) 
    loaddata.loadData()
    for j in range(13):
        for i in range(20):
            concat_data.dataConcat(j+1)
            train_naive_bayes.train()
            result += test_naive_bayes.test()
        print(result/20)