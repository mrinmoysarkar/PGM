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
    all_data_set = list(np.linspace(1,7,7,dtype=np.int)) + list(np.linspace(10,22,13,dtype = np.int))

    result = np.zeros(20)
    #result = 0
    partision = [1, 3, 4, 6, 7, 10, 11, 12, 14, 15, 16, 17, 20, 22]
    loaddata.loadData()
    no_of_trial = 1
    for j in range(len(partision)):
        result = 0
        for i in range(no_of_trial):
            concat_data.dataConcat(j)#partision[j])
            train_naive_bayes.train(plot=False)
            result += test_naive_bayes.test1()
           
        #print("test result : "+str(partision[j]*100)+"% train set:"+ str(result/no_of_trial))
        
        for i in range(20):
            print("test set: ",all_data_set[i]," correct: ", result[i]/no_of_trial)
            pass
        print("\n\n\n")