import matplotlib.pyplot as matlib
import numpy as np
import pandas as pd
import pandas_datareader as web


class SpotPriceRetriever():
    """
    Example class to retrieve historical prices from web sources
    """
    def retrieveSpots(self, ticker: str, source: str):

        ret = web.DataReader(
            ticker, data_source=source,
            start='3/14/2009', end='4/14/2014')

        print(ret.tail())

    def plotVolTicks(self):
        self.ret['Log Ret'] = np.log(self.ret['Adj Close']/self.ret['Adj Close'].shift(1))
        self.ret['Volatility'] = self.ret['Log Ret'].rolling(252).std() * np.sqrt(252)
        print(self.ret.columns)

        matlib.plot(self.ret['Volatility'])
        matlib.show()
        # ret[['Adj Close', 'Volatility']].plt(subplots=True, color='blue', figsize=(8,6))


#a = SpotPriceRetriever()

#a.retrieveSpots('TSLA', 'yahoo')
a = web.data.YahooOptions('AAPL')
opts = a.get_all_data()
print(opts.tail())
