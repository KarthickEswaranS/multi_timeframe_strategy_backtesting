from backtesting import Backtest
from src.strategy.base import Base
from src.strategy.multi_tf import MultiTf
from src.utilis.logger import Logger

class Backtesting():

    def __init__(self):
        self.B = Base()
        self.logger = Logger("backtest_trades.csv")
        self.start_engine()

    def start_engine(self):
        df = self.B.backesting_entry_conform()
     
        bkt = Backtest(df,
                       strategy=MultiTf, 
                       cash=10000000, 
                       commission=0.001)
        
        stats = bkt.run()
        trade_stats = stats['_trades']

        self.logger.log(trade_stats.to_string())
        # print(self.logger)

        # print(stats)
        bkt.plot()

b = Backtesting()