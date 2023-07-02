# Importing the Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style('darkgrid')
plt.rcParams['figure.figsize'] = (20, 10)

# Importing the data
df = pd.read_csv('./Wipro.csv').set_index("Date")

# Plotting the graph of close price with respect to the date
plt.figure(figsize = (20, 10))
plt.plot(df.index, df.close)
plt.xlabel('Date', fontsize = 20)
plt.ylabel('Closing Prices', fontsize = 20)
plt.title('WIPRO Stock Price', fontsize = 20)
plt.show()

"""Calculating the Simple Moving Average of 20 days """

def simlple_MA (data, windows):  #windows = Time interval
    simple_moving_avg = data.rolling(window = windows).mean()
    return simple_moving_avg

df['Simple_MA_20'] = simlple_MA(df.close, 20)

""" Now we will calculate the Bollinger Band
As we know that the formulat for Bollinger band for upper band is SMA + 2* sd and for Lower Band is SMA - 2 * SD
So we will implement this in our code """

def Bollinger_band (data, simple_moving_avg, windows):
    standard_deviation = data.rolling(window = windows).std()
    upper_band = simple_moving_avg + (2 * standard_deviation)
    lower_band = simple_moving_avg - (2 * standard_deviation)
    
    return upper_band, lower_band

# Adding 2 new columns and implementing the above function in it.
df['Upper_band'], df['Lower_band']  = Bollinger_band(df.close, df.Simple_MA_20, 20)

# plotting the Bollinger band graph to see is our above code is working correctely or not.
df['close'].plot(label = 'CLOSE PRICES', color = 'skyblue')
df['Upper_band'].plot(label = 'UPPER BB 20', linestyle = '--', linewidth = 1, color = 'black')
df['Simple_MA_20'].plot(label = 'MIDDLE BB 20', linestyle = '--', linewidth = 1.2, color = 'grey')
df['Lower_band'].plot(label = 'LOWER BB 20', linestyle = '--', linewidth = 1, color = 'black')
plt.legend(loc = 'upper left')
plt.title('WIPRO BOLLINGER BANDS', fontsize = 20)
plt.show()

# Implementing the trading stretegy for Bollinger Band
def implement_Bollinger_Band_strategy(data, lower_bb, upper_bb):
    buy_price = []
    sell_price = []
    bollinger_band_signal = []
    signal = 0

    try:
        bollinger_band_signal = [0] * len(data)
        buy_price = [np.nan] * len(data)
        sell_price = [np.nan] * len(data)

        for i in range(1, len(data)):
            if data[i-1] > lower_bb[i-1] and data[i] < lower_bb[i]:
                if signal != 1:
                    buy_price[i] = data[i]
                    signal = 1
                    bollinger_band_signal[i] = signal

            elif data[i-1] < upper_bb[i-1] and data[i] > upper_bb[i]:
                if signal != -1:
                    sell_price[i] = data[i]
                    signal = -1
                    bollinger_band_signal[i] = signal

    except Exception as e:
        print("An error occurred:", str(e))
        # Handle the exception here if needed

    else:
        print("The code executed successfully without any exceptions.")
        # Code to be executed if no exceptions occurred

    finally:
        return buy_price, sell_price, bollinger_band_signal




buy_price, sell_price, bollinger_band_signal = implement_Bollinger_Band_strategy(df['close'],df['Lower_band'], df['Upper_band'])

# Plotting the graph to see our Buy ans Sell Signal is working correctely or not.
df['close'].plot(label = 'CLOSE PRICES', alpha = 0.3)
df['Upper_band'].plot(label = 'UPPER BB', linestyle = '--', linewidth = 1, color = 'black')
df['Simple_MA_20'].plot(label = 'MIDDLE BB', linestyle = '--', linewidth = 1.2, color = 'grey')
df['Lower_band'].plot(label = 'LOWER BB', linestyle = '--', linewidth = 1, color = 'black')

plt.scatter(df.index, buy_price, marker = '^', color = 'green', label = 'BUY', s = 200)
plt.scatter(df.index, sell_price, marker = 'v', color = 'red', label = 'SELL', s = 200)

plt.title('WIPRO BB STRATEGY TRADING SIGNALS', fontsize = 20)
plt.legend(loc = 'upper left')
plt.show()
