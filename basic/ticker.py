from datetime import datetime

import yfinance as yf


class Ticker:
    def __init__(self, _ticker_code, _start, **end):
        self.ticker_code = _ticker_code
        self.start = _start
        self.end = end or datetime.today().strftime('%Y-%m-%d')
        self.api_result = yf.download(self.ticker_code, start=self.start, end=self.end)

    def get_result(self):
        return self.api_result

    def get_open_result(self):
        return self.api_result['Open']

    def get_close_result(self):
        return self.api_result['Close']

    def get_close_price(self, date):
        try:
            return self.api_result['Close'].iloc.obj[date]
        except:
            return 'Invalid date or some price data might not exist'

    def get_price_diff(self, start, end):
        return self.getClosePrice(end) - self.getClosePrice(start)

    def get_yield_by_close_date(self, start, end):
        return self.getPriceDiff(start, end) / self.getClosePrice(start)

    @staticmethod
    def get_yield(start, end):
        return (end - start) / start


def main():
    print('ticker.py')

if __name__ == '__main__':
    main()
