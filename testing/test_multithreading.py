import progressbar

from multiprocessing import Pool
import yfinance as yf
import time


def f(ticker):
    stock = yf.Ticker(ticker)
    info = stock.info
    if ticker != 'AA':
        return info
    else:
        print('ho')


def g():
    start = time.perf_counter()
    if __name__ == '__main__':
        example_tickers = ['AA', 'GOOG', 'TSLA', 'A', 'GME']
        with Pool() as p:
            print(p.map(f, example_tickers))
        print(example_tickers)

    end = time.perf_counter()
    print(end - start)


g()
