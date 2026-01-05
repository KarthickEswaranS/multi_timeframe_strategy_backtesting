from backtesting import Strategy

class MultiTf(Strategy):

    def init(self):
        self.size = 5
        self.e_price = None
        self.sl_price = None
        self.tp_price = None

    def next(self):
        
        if not self.position:

            if self.data.long_1h:
               self.e_price = self.data.Close[-1]   
               self.sl_price = self.e_price *(1 - 0.02)
               self.tp_price = self.e_price *(1+ 0.06)

               self.buy(
                   size = self.size, 
                   sl= self.sl_price, 
                   tp= self.tp_price, 
                   tag= 'LONG')
            
            elif self.data.short_1h:
                self.e_price = self.data.Close[-1]
                self.sl_price = self.e_price *(1 + 0.02)
                self.tp_price = self.e_price *(1 - 0.06)

                self.sell(
                    size=self.size,
                    sl= self.sl_price, 
                    tp= self.tp_price,
                    tag= 'SHORT')
        else:

            if self.position.is_short and (self.data.Close >= self.sl_price):
                self.position.close()
            
            elif self.position.is_short and (self.data.Close <= self.tp_price):
                self.buy(size=self.size)
                self.position.close()

            if self.position.is_long and (self.data.Close <= self.sl_price):
                self.position.close()
            elif self.position.is_long and (self.data.Close >= self.tp_price):
                self.sell(size=self.size)
                self.position.close()