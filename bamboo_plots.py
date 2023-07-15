import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns
import matplotlib.dates as mdates


def process_ewmas(df,a1,a2,a3,a4):
    """
    Plots EWMA vs Original Return Values for 4 alpha values

    Parameters:
    df: pd.Dataframe object
    a1, a2, a3, a4: float, alpha values

    Returns
    Calculated ewma values in a list
    """
    ewma_1 = df['returns'].ewm(alpha=a1).mean()
    ewma_2 = df['returns'].ewm(alpha=a2).mean()
    ewma_3 = df['returns'].ewm(alpha=a3).mean()
    ewma_4 = df['returns'].ewm(alpha=a4).mean()
    ewma_df =  pd.DataFrame({
        'original_returns':df['returns'],
        a1:ewma_1,
        a2:ewma_2,
        a3:ewma_3,
        a4:ewma_4
    })
    
    fig,axs = plt.subplots(2,2,figsize=(20,15))
    axs[0,0].plot(df.index, df['returns'], label='Returns',linewidth=1)
    axs[0,0].plot(ewma_1.index, ewma_1, label='EWMA Returns(alpha={})'.format(a1),linewidth=1)
    axs[0,0].set_xticks([])
    axs[0,0].legend()
    axs[0,1].plot(df.index, df['returns'], label='Returns',linewidth=1)
    axs[0,1].plot(ewma_2.index, ewma_2, label='EWMA Returns(alpha={})'.format(a2),linewidth=1)
    axs[0,1].set_xticks([])
    axs[0,1].legend()
    axs[1,0].plot(df.index, df['returns'], label='Returns',linewidth=1)
    axs[1,0].plot(ewma_3.index, ewma_3, label='EWMA Returns(alpha={})'.format(a3),linewidth=1)
    axs[1,0].set_xticks([])
    axs[1,0].legend()
    axs[1,1].plot(df.index, df['returns'], label='Returns',linewidth=1)
    axs[1,1].plot(ewma_4.index, ewma_4, label='EWMA Returns(alpha={})'.format(a4),linewidth=1)
    axs[1,1].set_xticks([])
    axs[1,1].legend()

    plt.tight_layout()
    plt.show();
    return ewma_df 

def corr_ewmas(ewma_df):
    sns.heatmap(ewma_df.corr(),cmap='YlGnBu',annot=True);

def plot_vwap(df):
    plt.figure(figsize=(8, 6), dpi=80)
    plt.plot(df["ltp"], label="Price")
    plt.plot(df["vwap"],label="vwap")
    plt.legend()
    plt.xlabel("Time")
    plt.ylabel("Price")
    plt.title('Price Chart with VWAP')
    plt.grid()
    plt.show();

def plot_vwap_trading_areas(df):
    plt.figure(figsize=(16, 12), dpi=80)

    plt.plot(df['ts'], df['ltp'], label='Price')
    plt.plot(df['ts'], df['vwap'], label='VWAP')

    # Adding buy and sell markers
    buy_points = df[df['ltp'] > df['vwap']]
    sell_points = df[df['ltp'] < df['vwap']]

    plt.scatter(buy_points['ts'], buy_points['ltp'], marker='^', color='green', label='Buy')
    plt.scatter(sell_points['ts'], sell_points['ltp'], marker='v', color='red', label='Sell')

    plt.legend()
    plt.grid()
    plt.xlabel('Timestamp')
    plt.xticks(rotation=45) 
    plt.ylabel('Price')
    plt.title('Price vs. VWAP with Trading Areas')
    plt.gca().xaxis.set_major_locator(mdates.AutoDateLocator())
    plt.gca().xaxis.set_major_formatter(mdates.AutoDateFormatter())

    plt.show()
