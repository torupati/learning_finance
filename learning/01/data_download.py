from os import path
import datetime as dt
import pandas_datareader.data as web

# sony = TYO 6758
ticker_symbol="6758"
ticker_symbol_dr=ticker_symbol + ".JP"

start='2022-01-01'
end = dt.date.today()
 
df = web.DataReader(ticker_symbol_dr, data_source='stooq', start=start,end=end)
df.insert(0, "code", ticker_symbol, allow_duplicates=False)

df.to_csv( path.join(path.dirname(__file__) ,'s_stock_data_'+ ticker_symbol_dr + '.csv') )

import pandas as pd
# NASDAQ: AAPL
#start = dt.datetime(2022, 1, 1)
#end = dt.date.today()
#out_file = path.join(path.dirname(__file__) ,'s_stock_data_'+ 'TSLA' + '.csv')
#print(out_file)
#df = web.DataReader('TSLA', 'yahoo', start=start, end=end)
#print(df)
#df.to_csv( out_file )
