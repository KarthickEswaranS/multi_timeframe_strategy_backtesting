from src.trading.exchange import Exchange
from src.strategy.base import Base
from binance.client import Client
from src.utilis.logger import Logger
import time


class Executor:

    def __init__(self):
        self.logger = Logger("live_trades.csv")

        E = Exchange()
        key = E.testnet_key
        secret = E.testnet_secret
        self.tn = Client(key, secret, testnet = True)

        B = Base()
        self.df = B.live_entry_conform()

        self.quantity = 0.01
        self.symbol = 'BTCUSDT'
        self.order = None

    def get_current_price(self, symbol):
        ticker = self.tn.get_symbol_ticker(symbol = symbol)
        return float(ticker['price'])
    
    def place_buy_order(self,symbol, quantity):
        buy_order = self.tn.order_market_buy(symbol = symbol, quantity= quantity)
        return buy_order
    
    def place_sell_order(self,symbol, quantity):
        sell_order = self.tn.order_market_sell(symbol = symbol, quantity= quantity)
        return sell_order
    
e =Executor()
e.trading_bot()