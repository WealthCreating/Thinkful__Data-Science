'''
1. Plot the time series, along with any logical or necessary differences to get a stationary dataset
2. Generate and interpret a PACF for the time series (and/or its differences)
3. Generate 5 ARIMA specifications and evaluate their efficacy at modeling your dataset
4. Finally choose one specification and make the case for that as a logical model for your dataset.
'''

import pandas as pd
import numpy as np
import scipy
from datetime import datetime
import time
import datetime as dt
import matplotlib.pyplot as plt
%matplotlib inline

df = pd.read_csv('C:/Users/18047/Documents/Main/6 Data science specializations/Time series analysis/BTC historical prices.csv')
df = df[df.columns[1:]]
df['date'] /= 1000
df['date'] = pd.to_datetime(df['date'], unit='s')


plt.plot(df['date'], df['price'])
plt.xticks(rotation=60)
plt.title('BTC/USD price')
plt.show()

df['diff_1'] = df['price'] - df['price'].shift()

from statsmodels.tsa.stattools import pacf
df_pacf = pd.DataFrame(pacf(df['diff_1'][1:]))
df_pacf.plot(kind='bar')
plt.title("BTC Diff PACF")
plt.show()

from statsmodels.tsa.arima_model import ARIMA
orders = [(0, 1, 0), (1, 0, 0), (1, 0, 1), (1, 1, 1), (5, 0, 5)]
for order in orders:
	model = ARIMA(df['price'], order=order)
	model_fit = model.fit()
	print(model_fit.summary())
	print('\n\n\n')

model = ARIMA(df['price'], order=(1, 0, 0))
model_fit = model.fit()

residuals = pd.DataFrame(model_fit.resid)
residuals.plot(legend=False)
plt.title('Time Series of Residuals')
plt.show()

residuals.hist(bins=20)
plt.title('Histogram of Residuals')
plt.show()
