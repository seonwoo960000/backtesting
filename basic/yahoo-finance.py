import yfinance as yf


def getInformation():
    single_data = yf.download('AAPL', start='2019-01-01')

    multiple_data = yf.download(['AAPL', 'MU'], start='2019-01-01')



def main():
    getInformation()


if __name__ == '__main__':
    main()
