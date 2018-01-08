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

def load_data(file_path,table_name):
    con = sqlite3.connect(filePath)
    df = pd.read_sql_query("SELECT * from " + table_name, con)
    con.close()
    return df


if __name__ == "__main__":
    file_path = '../../2017-12-04_Original_scenarios_remix/1.sqlite3'
    table_name = "mavlink_attitude"
    attitude_df = load_data(file_path, table_name)
    
    table_name = "mavlink_scaled_imu2"
    imu_df = load_data(file_path, table_name)
    
    table_name = "system_state"
    state_df = load_data(file_path,table_name)
    
    #plt.plot(acce['xacc'],color='green',linewidth=3,label='hello',marker='^')
    #plt.legend()
    #plt.show()
    
#    #attitude_df.plot.hist()
#    xacc = acce_df['time_boot_ms']#['xacc']
#    z=xacc.mean()
#    time_stamp = attitude_df['time_boot_ms']
#    
#    #print(attitude_df.index[attitude_df['time_boot_ms']<=42079][-1])
#    
#    n = attitude_df.shape[0]
#    class_label_start_indexes = [0]
#    #print(attitude_df.describe())
#    index1 = attitude_df.index[attitude_df['time_boot_ms']<42079][-1]
#    states = ["Hold"]*index1
#    class_label_start_indexes += [index1+1]
#    index2 = attitude_df.index[attitude_df['time_boot_ms']<76932][-1]
#    states += ["Fly Orbit and Observe"]*(index2-index1)
#    index1 = index2
#    class_label_start_indexes += [index1+1]
#    index2 = attitude_df.index[attitude_df['time_boot_ms']<222611][-1]
#    states += ["Fly Search Pattern"]*(index2-index1)
#    index1 = index2
#    class_label_start_indexes += [index1+1]
#    index2 = attitude_df.index[attitude_df['time_boot_ms']<294892][-1]
#    states += ["Survey Target"]*(indx2-indx1)
#    index1 = index2
#    class_label_start_indexes += [index1+1]
#    index2 = attitude_df.index[attitude_df['time_boot_ms']<414069][-1]
#    states += ["Fly Orbit and Observe"]*(index2-index1+1)
#    #indx1 = indx2
#    #indx2 = attitude_df.index[attitude_df['time_boot_ms']>=414069][-1]
#    #print(indx2)
#    #states += ["Fly Orbit and Observe"]*(indx2-indx1)
#    
#    train_data_df = pd.concat([attitude_df,pd.DataFrame({"state":states})],axis=1)
#    #acce_df = acce_df.append(acce_df.tail(1))
#    train_data_df = pd.concat([train_data_df, acce_df],axis=1)
#    
#    
#    str_date = "2017-12-04 21:08:48.897135"
#    d_date1 = datetime.strptime(str_date , '%Y-%m-%d %H:%M:%S.%f')
#    
#    str_date = "2017-12-04 21:09:32.797271"
#    d_date2 = datetime.strptime(str_date , '%Y-%m-%d %H:%M:%S.%f')
#    d_date = math.ceil(d_date2.timestamp()*1000-d_date1.timestamp()*1000)
#    
#    
#    print(d_date)
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
    
    train_data_df.to_csv("train.csv")
    
    
    
    
    
    
    
    
    
    
    
    
    
        
        
        