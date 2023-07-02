# <font color = red> BOLLINGER BAND </font>

- Bollinger band belongs to one of the popular trading Indicators. It is a technical analysis tool used in stock market research and investment, which uses moving averages, Lower and Upper Bollinger Bound and window (20 data points)

- Before jumping on to explore Bollinger Bands, it is essential to know what Simple Moving Average (SMA) is. Simple Moving Average is nothing but the average price of a stock given a specified period of time. Now, Bollinger Bands are trend lines plotted above and below the SMA of the given stock at a specific standard deviation level. To understand Bollinger Bands better, have a look at the following chart that represents the Bollinger Bands of the Tesla stock calculated with SMA 20

- Bollinger Bands are great to observe the volatility of a given stock over a period of time. The volatility of a stock is observed to be lower when the space or distance between the upper and lower band is less. Similarly, when the space or distance between the upper and lower band is more, the stock has a higher level of volatility. While observing the chart, you can observe a trend line named ‘MIDDLE BB 20’ which is nothing but SMA 20 of the Tesla stock. The formula to calculate both upper and lowers bands of stock are as follows:

## Formula:
> UPPER_BB = STOCK SMA + SMA STANDARD DEVIATION * 2
> 
> LOWER_BB = STOCK SMA - SMA STANDARD DEVIATION * 2

- Now that we have an understanding of what Bollinger Bands is, so let’s gain some intuitions on the trading strategy we are going to build using Bollinger Bands.

- About the trading strategy: We are going to implement a basic trading strategy using the Bollinger Bands indicator which will shoot a buy signal if the stock price of the previous day is greater than the previous day's lower band and the current stock price is lesser than the current day’s lower band. Similarly, if the stock price of the previous day is lesser than the previous day’s upper band and the current stock price is greater than the current day’s upper band, the strategy will reveal a sell signal. Our Bollinger Bands trading strategy can be represented as follows:

## Formula: 
> IF PREV_STOCK > PREV_LOWERBB & CUR_STOCK < CUR_LOWER_BB => BUY
>
> IF PREV_STOCK < PREV_UPPERBB & CUR_STOCK > CUR_UPPER_BB => SELL


<font color = red >Link of youtube:</font>https://www.youtube.com/watch?v=13oogPJwWAM

The code is done on the basic of above formulas.