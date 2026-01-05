from src.utilis.data import Data
import talib as ta

class Base():

    def __init__(self):
        self.D = Data()

    def trend_conform(self, symbol, interval ,start_dt, end_dt, testnet:bool):

        df = self.D.clean_data(symbol, interval, start_dt, end_dt ,testnet)

        df['ema_7'] = ta.EMA(df['Close'], 7)
        df['ema_21'] = ta.EMA(df['Close'], 21)
        df['engulf'] = ta.CDLENGULFING(df['Open'], df['High'], df['Low'], df['Close'])

        df['long_conf'] = (
            (df['ema_7'].shift(1)  > df['ema_21'].shift(1))&
            (df['Close'].shift(1)  > df['ema_7'].shift(1))&
            (df['engulf'].shift(1) == 80)
        )

        df['short_conf'] = (
            (df['ema_7'].shift(1)  < df['ema_21'].shift(1))&
            (df['Close'].shift(1)  < df['ema_7'].shift(1))&
            (df['engulf'].shift(1) == -80)
        )

        return df
    
    def backesting_entry_conform(self):

        df1h = self.trend_conform('BTCUSDT', '1h', '1-1-2022', '30-12-2022', False)
        df15m = self.D.clean_data('BTCUSDT', '15m', '1-1-2022', '30-12-2022', False)

        df15m['long_1h'] = df1h['long_conf'].reindex(df15m.index, method='ffill')
        df15m['short_1h'] = df1h['short_conf'].reindex(df15m.index, method='ffill')
   
        return df15m
    
    def live_entry_conform(self):

        df15m = self.trend_conform('BTCUSDT', '15m', '30 days ago UTC"', None, True)
        df5m = self.D.clean_data('BTCUSDT', '5m', '30 days ago UTC"', None, True)

        df5m['long_15m'] = df15m['long_conf'].reindex(df5m.index, method='ffill')
        df5m['short_15m'] = df15m['short_conf'].reindex(df5m.index, method='ffill')

        return df5m


b = Base()
