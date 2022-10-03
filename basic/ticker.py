from datetime import datetime, timedelta
from functools import reduce

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

    def get_buy_price(self):
        return self.get_close_price(self.start)

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


class TickerGroup:
    def __init__(self, tickers):
        self.tickers = tickers
        self.names = set()
        for t in tickers:
            self.names.add(t['ticker'].ticker_code)

    def get_ticker_names(self):
        return self.names

    def get_yesterday_total_price(self):
        yesterday = datetime.strftime(datetime.now() - timedelta(1), '%Y-%m-%d')
        return reduce(lambda x, y: x + y, [t['count'] * t['ticker'].get_close_price(yesterday) for t in self.tickers])


def test_ticker_group():
    apple = Ticker('AAPL', '2020-01-02')
    microsoft = Ticker('MSFT', '2020-01-02')
    ticker_group = TickerGroup([
        {'ticker': apple, 'count': 10},
        {'ticker': microsoft, 'count': 20}
    ])
    print(apple.get_close_price(datetime.strftime(datetime.now() - timedelta(1), '%Y-%m-%d')))
    print(microsoft.get_close_price(datetime.strftime(datetime.now() - timedelta(1), '%Y-%m-%d')))
    print(ticker_group.get_yesterday_total_price())


def main():
    test_ticker_group()


if __name__ == '__main__':
    main()
