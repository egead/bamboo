import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

def crosscorr(s1, s2, lag=0):
    """ Lag-N cross correlation. 
    Parameters
    ----------
    s1, s2 : pandas.Series objects of equal length
    lag : int, default 0

    Returns
    ----------
    crosscorr : float
    """
    #s1,s2=s1.replace(np.nan,0,inplace=True),s2.replace(np.nan,0,inplace=True)
    #For some reason, the line above produces an error: 'NoneType' object has no attribute 'corr'
    #Will look into that later 
    return s1.corr(s2.shift(lag))

def timelagcorr(df1,i,j,lag=0):
    """ Computes Lag-N correlation coefficent of two values in a dataframe. 
    
    Parameters
    ----------
    df1 : pandas.Dataframe
    lag : int, default 0
    i,j : int, Used for indexing the dataframe
    
    Returns
    ----------
    np.corrcoef: float
    """
    df1.replace(np.nan,0,inplace=True)
    df2 = df1.shift(lag)
    df2.replace(np.nan,0,inplace=True)   
    #X[i,j]=np.corrcoef(veci,vecj)
    return np.corrcoef(df1.iloc[i].values,df2.iloc[j].values)[0,1]

def corrcoefs(df1,lag=0):
    """ Correlation Coefficients 
    Parameters
    ----------
    lag : int, default 0
    df1 : pandas.Dataframe

    Returns
    ----------
    corrcoefs: list of correlation coefficients
    """
    cols = df1.T.columns
    idx = cols.copy()
    corrcoefs=list()
    
    for i in range(len(cols)):
        for j in range(len(idx)):
            corrcoefs.append(timelagcorr(df1,i,j,lag))
            #print(i,j,timelagcorr(df1,i,j,lag))
    return [cols,idx,corrcoefs]

def timelagcorrM(df1,lag=0): 
    """ Lag-N cross correlation matrix. 
    Parameters
    ----------
    lag : int, default 0
    df1 : pandas.Dataframe

    Returns
    ----------
    dfcorr: pd.Dataframe Correlation Matrix
    """
    cols = df1.columns
    idx = df1.columns
    data=list()
    df2=df1.shift(periods=lag).fillna(0)
    #Fill the empty dataframe
    for i in range(len(df1.columns)):
        for j in range(len(df1.columns)):
            data.append(np.corrcoef(df1.iloc[:,i],df2.iloc[:,j])[0,1])
    print(len(df1.columns))      
    dataArr = np.array(data)
    dataArr=np.reshape(dataArr, (len(df1.columns),len(df1.columns)))
    dfcorr =pd.DataFrame(data=dataArr,columns=cols,index=idx)
    print(np.corrcoef(df1["SSE_600370"],df2["SSE_600200"])[0,1])
    return dfcorr #Return to this function in future it does not work properly yet

def laggedcorr(df,lag=0):
    df_copy = df.rolling(lag).corr(pairwise=True).dropna().reset_index()
    df_copy = df_copy.loc[df_copy["level_0"]==str(lag)]
    df_copy.drop("level_0",axis=1,inplace=True)
    df_copy.set_index("level_1",inplace=True)
    return df_copy

def laggedheatmap(df):
    f, ax = plt.subplots(figsize=(12, 6))
    heatmap = sns.heatmap(df,
                    cmap = "OrRd",
                      annot = False,
                      )

    sns.set_style({'xtick.bottom': True}, {'ytick.left': True})

    
    
