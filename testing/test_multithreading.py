from multiprocessing import Pool
import yfinance as yf
import time


def f(stock):
    stock = yf.Ticker(stock)
    info = stock.info
    return info


start = time.perf_counter()

if __name__ == '__main__':
    example_tickers = ['AA', 'GOOG', 'TSLA', 'A', 'GME']
    with Pool(5) as p:
        print(p.map(f, example_tickers))

end = time.perf_counter()
print(end - start)
