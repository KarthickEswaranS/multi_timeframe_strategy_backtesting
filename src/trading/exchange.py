import keyring as key

class Exchange:

    def __init__(self):
        self.testnet_key = key.get_password('binance_testnet', 'testnet_key')
        self.testnet_secret = key.get_password('binance_testnet', 'testnet_secret')
    
e = Exchange()