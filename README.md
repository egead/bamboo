# Bamboo 🎍

Analysis of Chinese Stocks with Pandas 🐼

<img src="bamboo1.jpg" alt="bamboologo" width="80" height="80">

### Index 

#### Notebooks

* **[RollingCorr.ipynb](RollingCorr.ipynb)** : Using rolling windows to do the same thing as in TimeLagCorr.ipynb but with rolling
* **[VWAP_Analysis.ipynb](VWAP_Analysis.ipynb)** : Demonstrating vwap plot functions from [bamboo_plots.py](bamboo_plots.py) and toying with data (in progress)
* **[EWMA.ipynb](EWMA.ipynb)**: Using plot functions from [bamboo_plots.py](bamboo_plots.py) to choose an $\alpha$ value, and more (in progress)
* **[MeanTWs.ipynb](MeanTWs.ipynb)** : Notebook that resamples data on 1, 5 and 10 minute timewindows using .mean() (ie. Takes the mean value when resampling)
* **[LastTWs.ipynb](LastTWs.ipynb)** : Just like [MeanTWs.ipynb](MeanTWs.ipynb) but takes the last value on the given time window. 

#### Modules
* **[bamboo_utils.py](bamboo_utils.py)**: Random functions. Better organization needed in the future.
* **[bamboo_plots.py](bamboo_plots.py)**: Plotting functions.
  
#### Scripts

* **[save_vwaps.py](save_vwaps.py)** : calculates and add vwap values as a column to dataframes
* **[ltpscript.py](ltpscript.py)**: saves ltp columns as .csv files

#### Folders
* **[Archive](Archive)** : Old files that are no longer relevant, ones explaining how code works, or freestyle experimentation
* **[Stock_Prices](Stock_Prices)** : Columns: TimeStamp, Price (StockName (Starts with SSE))
* **[RESAMPS](RESAMPS)** : Data resampled in Mean_TimeWindows.ipynb. using 1 min time windows. Resamp_5Mins and Resamp_10Mins are resampled the same way for 5 and 10 min time windows. Also the vwaps folder.
* **[Concat_DFs](Concat_DFs)** : Concatenated [Stock_Prices](Stock_Prices) folders by day

