import pandas as pd
import os 
from os import walk, mkdir
from genericpath import exists
import numpy as np

day_paths = list()
base_path="/media/ege/DATA/bamboo/RESAMPS/{}"
for root, dirs, files in walk("/media/ege/DATA/bamboo/RESAMPS/"):
    for dirname in dirs:
        if dirname.startswith("2"):
            print(dirname)

def vwap(df):
    s_i = df.trade_size.values              
    p_i = df.ltp.values
    return df.assign(vwap=(p_i * s_i).cumsum() / s_i.cumsum())

path_vw = "/media/ege/DATA/bamboo/RESAMPS/vwaps/"
if not exists(path_vw):
    mkdir(path_vw)
"""    
for day in day_paths:
   mkdir(path_vw+day+"/")
    
for day in day_paths: 
    print(day)
    for root, dirs, files in walk(base_path.format(day)+"/"):
        for file in files:
            print(base_path.format(day)+"/"+file)
            if "checkpoint" in file:
                pass
            elif file.endswith('.csv'):
                df = pd.read_csv(base_path.format(day)+"/"+file)
                df.trade_size = df.trade_size.abs()
                df_vw = vwap(df)
                df_vw.to_csv(path_vw+day+"/"+file)
                """