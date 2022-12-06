# Bamboo
Analysis of Chinese Stocks with Pandas

### Index 

corrfuncs.py -> correlation functions 
TimeLagCorr.ipynb -> Notebook about how some of the functions on corrfuncs.py work and derived. Basic testing of timelagcorr function
Mean_TimeWindows.ipynb -> Notebook that resamples data on 1, 5 and 10 minute timewindows using .mean() (ie. Takes the mean value when resampling)
Last_TimeWindows.ipynb -> Just like Mean_TimeWindows.ipynb but takes the last value on the given time window. 
Correlation_Matrix.ipynb -> An old notebook used for experimenting with both resampling and an old version of timelagcorr function. Uploaded for archive purposes.

#### Folders

Stock_Prices -> Columns: TimeStamp, Price (StockName (Starts with SSE))
Resampled_Data -> Data resampled in Mean_TimeWindows.ipynb. using 1 min time windows. Resamp_5Mins and Resamp_10Mins are resampled the same way for 5 and 10 min time windows. 
LastResamp_[1/5/10]Mins -> Data resampled in Last_TimeWindows.ipynb 
Concat_DFs -> Concatenated Stock_Prices folders by day
