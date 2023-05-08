import pandas as pd
import os 
from os import walk, mkdir
from genericpath import exists
import re

# ts (time stamp, nanoseconds), ltp (last trade price), trade_size(last trade size, + means buy trade)

day_paths = list()
base_path="/media/ege/DATA/FULLCHINA/{}"
for root, dirs, files in walk("/media/ege/DATA/FULLCHINA/"):
    for dirr in dirs:
        if dirr.startswith('2'):
            day_paths.append(dirr)

#1 Minute Time Windows 
path_resamp = "/media/ege/DATA/FULLCHINA/MeanResamp_1Min/"

if not exists(path_resamp):
    mkdir(path_resamp)

for day in day_paths:
    if not exists(path_resamp+day+"/"):
        mkdir(path_resamp+day+"/")

for day in day_paths: 
    print(day)
    for root, dirs, files in walk(base_path.format(day)+"/"):
        
        for file in files:
            print(file)
            if "checkpoint" in file:
                pass
            elif file.endswith('.csv'):
                #if exists(path_resamp+day+"/"+file):
                 #   pass
                df = pd.read_csv(base_path.format(day)+"/"+file)
                df['ts']=pd.to_datetime(df['ts'], unit='ns', errors='ignore')
                df.set_index('ts',inplace=True)
                df = df.loc[:, ['ltp',"trade_size","level_qty:ask:0","level_qty:bid:0","level_price:ask:0"]]
                df_resample = df.resample('T').mean()
                df_resample.to_csv(path_resamp+day+"/"+file)
                print("done")

#5 Minute Time Windows
path_resamp5 = "/media/ege/DATA/FULLCHINA/MeanResamp_5Min/"
if not exists(path_resamp5):
    print("Path initiated")
    mkdir(path_resamp5)

for day in day_paths:
    if not exists(path_resamp5+day+"/"):
        mkdir(path_resamp5+day+"/")

for day in day_paths: 
    print(day)
    for root, dirs, files in walk(base_path.format(day)+"/"):
        for file in files:
            if "checkpoint" in file:
                pass
            elif file.endswith('.csv'):
                #if exists(path_resamp5+day+"/"+file):
                 #   pass
                df = pd.read_csv(base_path.format(day)+"/"+file)
                df['ts']=pd.to_datetime(df['ts'], unit='ns', errors='ignore')
                df.set_index('ts',inplace=True)
                df = df.loc[:, ['ltp',"trade_size","level_qty:ask:0","level_qty:bid:0","level_price:ask:0"]]
                df_resample = df.resample('5T').mean()
                df_resample.to_csv(path_resamp5+day+"/"+file)
                print("done")

#10 Minute Time Windows
path_resamp10 = "/media/ege/DATA/FULLCHINA/MeanResamp_10Mins/"
if not exists(path_resamp10):
    mkdir(path_resamp10)

for day in day_paths:
    if not exists(path_resamp+day+"/"):
        mkdir(path_resamp10+day+"/")

for day in day_paths: 
    print(day)
    for root, dirs, files in walk(base_path.format(day)+"/"):
        for file in files:
            if "checkpoint" in file:
                pass
            elif file.endswith('.csv'):
                #if exists(path_resamp10+day+"/"+file):
                 #   pass
                df = pd.read_csv(base_path.format(day)+"/"+file)
                df['ts']=pd.to_datetime(df['ts'], unit='ns', errors='ignore')
                df.set_index('ts',inplace=True)
                df = df.loc[:, ['ltp',"trade_size","level_qty:ask:0","level_qty:bid:0","level_price:ask:0"]]
                df_resample = df.resample('10T').mean()
                df_resample.to_csv(path_resamp10+day+"/"+file)
                print("done")
