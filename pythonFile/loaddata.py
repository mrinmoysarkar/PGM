# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 10:53:03 2018

@author: msarkar
"""

import pandas as pd
import sqlite3
import matplotlib.pyplot as plt
from datetime import datetime
import math
import numpy as np

def load_data(file_path,table_name):
    con = sqlite3.connect(file_path)
    df = pd.read_sql_query("SELECT * from " + table_name, con)
    con.close()
    return df


if __name__ == "__main__":
        
    l1 = list(np.linspace(1,7,7,dtype=np.int)) + list(np.linspace(10,22,13,dtype = np.int))
    ll = len(l1)
    for l in range(ll):
        file_path = '../../2017-12-04_Original_scenarios_remix/'+str(l1[l])+'.sqlite3'
        table_name = "mavlink_attitude"
        attitude_df = load_data(file_path, table_name)
        
        table_name = "mavlink_scaled_imu2"
        imu_df = load_data(file_path, table_name)
    
        table_name = "system_state"
        state_df = load_data(file_path,table_name)
        states = []
        n = state_df.shape[0]
        t0 = state_df['timestamp'][0]
        t0 = datetime.strptime(t0 , '%Y-%m-%d %H:%M:%S.%f')
        t0 = t0.timestamp()*1000
        index1 = 0
        all_states = state_df['state']
        for i in range(n-1):
            t = state_df['timestamp'][i+1]
            t = datetime.strptime(t , '%Y-%m-%d %H:%M:%S.%f')
            t = t.timestamp()*1000
            dt = math.ceil(t-t0)
            #print(dt)
            index2 = attitude_df.index[attitude_df['time_boot_ms']<dt][-1]
            states += [all_states[i]]*(index2-index1)
            index1 = index2
        
        train_data_df = pd.DataFrame({"state":states})
        attitude_feature = ["roll", "pitch", "yaw", "rollspeed", "pitchspeed", "yawspeed"]
    
        n = len(attitude_feature)
        for i in range(n):
            train_data_df = pd.concat([train_data_df,pd.DataFrame({attitude_feature[i]:attitude_df[attitude_feature[i]]})],axis = 1)    
    
    
        imu_feature = ["xacc", "yacc", "zacc"]
        n = len(imu_feature)
        for i in range(n):
            train_data_df = pd.concat([train_data_df,pd.DataFrame({imu_feature[i]:imu_df[imu_feature[i]]})],axis = 1)
    
        train_data_df.to_json("train"+str(l1[l])+".json")
    
        label_df = pd.DataFrame({"label":all_states.unique()})
        label_df.to_json("label.json")
    
    
    
    
    
    
    
    
    
    
    
        
        
        