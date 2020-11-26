import matplotlib.pyplot as matlib
import numpy as np
import pandas as pd
import pandas_datareader as web

ret = web.DataReader(
    'GOOG', data_source='yahoo',
    start='3/14/2009', end='4/14/2014')

print(ret.tail())

ret['Log Ret'] = np.log(ret['Adj Close']/ret['Adj Close'].shift(1))
ret['Volatility'] = ret['Log Ret'].rolling(252).std() * np.sqrt(252)
print(ret.columns)

matlib.plot(ret['Volatility'])
matlib.show()
# ret[['Adj Close', 'Volatility']].plt(subplots=True, color='blue', figsize=(8,6))
