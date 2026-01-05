from src.trading.exchange import Exchange
from binance.client import Client
import pandas as pd

class Data(Exchange):

    def __init__(self):
        super().__init__()
        
    def clean_data(self, symbol, interval , start_dt, end_dt, live:bool):

        bc = Client(self.testnet_key, self.testnet_secret ,testnet=live)

        timeframes = {
            '1m': Client.KLINE_INTERVAL_1MINUTE ,
            '5m' : Client.KLINE_INTERVAL_5MINUTE ,
            '15m': Client.KLINE_INTERVAL_15MINUTE ,
            '1h' : Client.KLINE_INTERVAL_1HOUR ,
        }

        duration = timeframes.get(interval)

        if duration is None:
            print('only 1hr, 15m  timeframe interval is valid')

        data = bc.get_historical_klines(
            symbol= symbol, 
            interval= duration, 
            start_str = start_dt, 
            end_str = end_dt
        )

        df = pd.DataFrame(data)
        df.columns = ['Open Time', 'Open', 'High', 'Low', 'Close', 'Volume', 'Close Time',
                        'Quote Asset Volume', 'Number of Trades', 'Taker Buy Base Asset Volume',
                        'Taker Buy Quote Asset Volume', 'Ignore']
        
        df['Open Time'] = pd.to_datetime(df['Open Time'] , unit ='ms') 
        df['Close Time'] = pd.to_datetime(df['Close Time'], unit ='ms') 
        df.set_index('Open Time', inplace=True)

        ch_numeric = ['Open', 'High', 'Low', 'Close', 'Volume', 'Quote Asset Volume', 'Taker Buy Base Asset Volume', 'Taker Buy Quote Asset Volume']
        df[ch_numeric] = df[ch_numeric].astype(float)

        drop = ['Number of Trades','Quote Asset Volume', 'Taker Buy Base Asset Volume', 'Taker Buy Quote Asset Volume','Ignore']
        df = df.drop(columns=drop)
    
        return df

