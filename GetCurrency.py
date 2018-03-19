import urllib.request


class GetCurrency():

    def __init__(self, url):
        self.data = urllib.request.urlopen(url).read()

    def get_currency_data(self):
        return self.data
