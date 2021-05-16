import progressbar

from multiprocessing import Pool
import yfinance as yf
import time


def f(ticker):
    print('f')
    stock = yf.Ticker(ticker)
    info = stock.info
    if ticker != 'AA':
        return info
    else:
        print('ho')


def h():
    print('success')


def i():
    print('error')


def g():
    start = time.perf_counter()
    if __name__ == '__main__':
        example_tickers = ['AA', 'GOOG', 'TSLA', 'A', 'GME']
        with Pool() as p:
            for ticker in example_tickers:
                p.apply_async(f, ticker, callback=h, error_callback=i)

    end = time.perf_counter()
    print(end - start)


g()
