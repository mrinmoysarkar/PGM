# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 10:33:50 2018

@author: msarkar
"""

# sampling in a bayesian network
import numpy as np
import matplotlib.pyplot as plt


class node():
    def __init__(self, no_of_par):
        self.no_of_par = no_of_par
        self.mu = np.zeros([no_of_par+1,1]);
        self.sig = np.zeros([no_of_par+1,no_of_par+1])
    def rand_init(self):
        self.mu = np.random.rand(no_of_par+1,1);
        self.sig = np.random.rand(no_of_par+1,no_of_par+1)   
    def is_sample_of_node(self, X):
        if self.no_of_par == 0:
            flag = X>self.mu-2*self.sig and X<self.mu+2*self.sig
            return flag
        elif self.no_of_par > 0:
            sig22 = np.linalg.inv(self.sig[1:no_of_par+1,1:no_of_par+1])
            arg1 = np.matmul(self.sig[0,1:no_of_par+1],sig22)
            mu_bar = self.mu[0,0] + np.matmul(arg1,\
                          (X[1:no_of_par+1,0]-self.mu[1:no_of_par+1,0]))
            sig_bar = self.sig[1,1] - np.matmul(arg1,self.sig[1:no_of_par+1,0])
            flag = X[0,0]>mu_bar-2*sig_bar and X[0,0]<mu_bar+2*sig_bar
            return flag
    def __str__(self):
        return "mean: " + str(self.mu) + "  \nsig: " + str(self.sig)

no_of_node = 3
bnet = np.zeros([no_of_node,no_of_node],dtype=bool)
bnet[0,1]=True
bnet[2,1]=True
node_list =[]

for i in range(no_of_node):
    no_of_par = 0
    for j in range(no_of_node):
        no_of_par += 1 if bnet[j,i] else 0
    n = node(no_of_par)
    n.rand_init()
    node_list.append(n)
    
sampling_order = [0,2,1]

no_of_train_sample = 200
train_set = np.zeros([no_of_train_sample, no_of_node])

random_sample = np.random.rand(1000,1)-0.5


i=0
k=0
while 1:
    for j in range(len(sampling_order)):
        n = node_list[sampling_order[j]]
        while 1:
            if n.no_of_par == 0 and n.is_sample_of_node(random_sample[i,0]):
                train_set[k,sampling_order[j]] = random_sample[i,0]
                i = i+1
                break
            else:
                tem = 0
                X = np.zeros([n.no_of_par+1,1])
                X[tem,0] = random_sample[i,0]
                tem = tem+1
                for kk in range (no_of_node):
                    if bnet[kk,sampling_order[j]]:
                        X[tem,0]=train_set[k,kk] 
                        tem=tem+1
                    
                if n.is_sample_of_node(X):
                    train_set[k,sampling_order[j]] = random_sample[i,0]
                    i = i+1
                    break
            i = i+1
            if i==random_sample.size:
                break
        if i==random_sample.size:
                break
    k=k+1
    if i==random_sample.size or k==train_set.shape[0]:
                break
            
print(train_set)

for i in range(no_of_node):
    print(node_list[i])
    
print(np.mean(train_set,axis=0))
