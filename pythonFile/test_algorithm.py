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
    #result = np.zeros(20)
    result = 0
    partision = [.1,.2,.3,.4,.5,.6,.7,.8,.9]
    loaddata.loadData()
    for j in range(len(partision)):
        for i in range(10):
            concat_data.dataConcat(partision[j])
            train_naive_bayes.train()
            result += test_naive_bayes.test()
           
        print("test result : "+str(partision[j]*100)+"% train set:"+ str(result/10))