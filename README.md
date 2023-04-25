# Bamboo 🎍

Analysis of Chinese Stocks with Pandas 🐼
<img src="bamboo1.jpg" alt="bamboologo" width="100" height="150">

### Index 

* **[corrfuncs.py](corrfuncs.py)** : correlation functions 
* **[RollingCorr.ipynb](RollingCorr.ipynb)** : Using rolling windows to do the same thing as in TimeLagCorr.ipynb but with rolling 
* **[TimeLagCorr.ipynb](TimeLagCorr.ipynb)** : Notebook about how some of the functions on corrfuncs.py work and derived. Basic testing of timelagcorr function
* **[Mean_TimeWindows.ipynb](Mean_TimeWindows.ipynb)** : Notebook that resamples data on 1, 5 and 10 minute timewindows using .mean() (ie. Takes the mean value when resampling)
* **[Last_TimeWindows.ipynb](Last_TimeWindows.ipynb)** : Just like Mean_TimeWindows.ipynb but takes the last value on the given time window. 
* **[Correlation_Matrix.ipynb](Correlation_Matrix.ipynb)** : An old notebook used for experimenting with both resampling and an old version of timelagcorr function. Uploaded for archive purposes.

#### Folders

* **[Stock_Prices](Stock_Prices)** : Columns: TimeStamp, Price (StockName (Starts with SSE))
* **[Resampled_Data](Resampled_Data)** : Data resampled in Mean_TimeWindows.ipynb. using 1 min time windows. Resamp_5Mins and Resamp_10Mins are resampled the same way for 5 and 10 min time windows. 
* **[LastResamp_1Mins](LastResamp_1Mins)**, **[LastResamp_5Mins](LastResamp_5Mins)**, **[LastResamp_10Mins](LastResamp_10Mins)** -> Data resampled in Last_TimeWindows.ipynb 
* **[Concat_DFs](Concat_DFs)** : Concatenated Stock_Prices folders by day

#### Scripts

* **[save_vwaps.py](save_vwaps.py)** : python script to calculate and add vwap values as a column to dataframes
