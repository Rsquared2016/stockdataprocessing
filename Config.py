class Config:
    def __init__(self):
        self.token = open('Token.txt', 'r').read()
        self.insName = 'EUR_USD'
        self.maxLength = 100  # ticks
        self.period = 5  # s
        self.write_back_log = False
        self.back_log_path = 'BackLog'
        self.account_id = open('Account.txt', 'r').read()
        self.stop_loss_value = 0.05
        self.take_profit_value = 0.05
        self.lot_size = 1000
