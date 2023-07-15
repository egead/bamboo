import pandas as pd
import os
from bamboo_utils import vwap, mkabsentdir
import numpy as np

base_path="/media/ege/DATA/bamboo/RESAMPS"
path_vw = base_path+"/vwaps"

mkabsentdir(path_vw)

dirnames_list = os.listdir(base_path)
dirnames_list = np.delete(dirnames_list,[4,5]).tolist()

for dirname in dirnames_list:
    mkabsentdir(os.path.join(path_vw,dirname))
    for day_dir in os.listdir(os.path.join(base_path,dirname)):
        print(day_dir)
        mkabsentdir(os.path.join(path_vw,dirname,day_dir))
        for root,dirs,files in os.walk(os.path.join(base_path,dirname,day_dir)):
            for file in files:
                if file.startswith("S") and file.endswith(".csv") and "checkpoint" not in file:
                    df = pd.read_csv(os.path.join(base_path,dirname,day_dir,file))
                    df.trade_size = df.trade_size.abs()
                    df = df.dropna()
                    df_vw = vwap(df)
                    df_vw.to_csv(os.path.join(path_vw,dirname,day_dir,file))