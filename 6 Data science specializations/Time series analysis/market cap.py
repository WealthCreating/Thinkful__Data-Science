import pandas as pd
import numpy as np
import ccxt

df = []

exchange = ccxt.bittrex({'options': {'adjustForTimeDifference': True}})
for item in exchange.fetch_ohlcv('BTC/USDT', '1d'):
	df.append(item[:2])

df = pd.DataFrame(df, columns=['date', 'price'])
df.to_csv('BTC historical prices.csv')
