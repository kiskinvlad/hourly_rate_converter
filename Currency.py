class Currency():
    def __init__(self, ccy, base, buy, sale):
        self.ccy = ccy
        self.base = base
        self.buy = buy
        self.sale = sale

    def get_ccy(self):
        return self.ccy

    def get_base(self):
        return self.base

    def get_buy(self):
        return self.buy

    def get_sale(self):
        return self.sale
