# Bamboo: Analysis of Chinese Stocks with Pandas 🎋🐼📈

## Project Overview 

This project is focused on analyzing Chinese stocks using Pandas, a popular data analysis library in Python. 

## Index 

* `corrfuncs.py`: correlation functions
* `RollingCorr.ipynb`: using rolling windows to do the same thing as in TimeLagCorr.ipynb but with rolling
* `TimeLagCorr.ipynb`: notebook about how some of the functions on corrfuncs.py work and derived. Basic testing of timelagcorr function 
* `Mean_TimeWindows.ipynb`: notebook that resamples data on 1, 5 and 10 minute time windows using `.mean()` function 
* `Last_TimeWindows.ipynb`: similar to Mean_TimeWindows.ipynb but takes the last value on the given time window.
* `Correlation_Matrix.ipynb`: an old notebook used for experimenting with both resampling and an old version of timelagcorr function. Uploaded for archive purposes. 
* `save_vwaps.py`: python script to calculate and add vwap values as a column to dataframes.
* `EWM.ipynb`: notebook about exponentially weighted moving averages and returns in % (using `.pct_change()`)

## Folders

* `Stock_Prices`: contains columns for TimeStamp, Price, and StockName (which starts with SSE)
* `Resampled_Data`: data resampled in Mean_TimeWindows.ipynb using 1 min time windows. Resamp_5Mins and Resamp_10Mins are resampled the same way for 5 and 10 min time windows.
* `LastResamp_[1/5/10]Mins`: data resampled in Last_TimeWindows.ipynb
* `Concat_DFs`: concatenated Stock_Prices folders by day.

