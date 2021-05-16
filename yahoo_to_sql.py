# Yahoo finance has no function to get a list of available ticker codes.
# The get_all_tickers module returns list of tickers for New York Stock Exchange (NYSE),
# The Nasdaq market (NASDAQ) and NYSE American (NYSEAMERICAN)

import yfinance as yf
# Technically the module used is a branch of the original to fix a critical bug
from get_all_tickers.get_tickers import get_tickers
import datetime
from db_functions import *
import time


# NYSE = get_tickers(NYSE=True, NASDAQ=False, AMEX=False)
# NASDAQ = get_tickers(NYSE=False, NASDAQ=True, AMEX=False)
# AMEX = get_tickers(NYSE=False, NASDAQ=False, AMEX=True)
# print(NYSE)
# print(NASDAQ)
# print(AMEX)
# print(len(NYSE), len(NASDAQ), len(AMEX))


def update_all_nyse_stocks():
    ticker_list = get_tickers(NYSE=True, NASDAQ=False, AMEX=False)
    update_all_yahoo_stocks(ticker_list, 'NYSE')


def update_all_nasdaq_stocks():
    ticker_list = get_tickers(NYSE=False, NASDAQ=True, AMEX=False)
    update_all_yahoo_stocks(ticker_list, 'NASDAQ')


def update_all_amex_stocks():
    ticker_list = get_tickers(NYSE=False, NASDAQ=False, AMEX=True)
    update_all_yahoo_stocks(ticker_list, 'NYSEAMERICAN')


def update_all_yahoo_stocks(ticker_list, exchange):
    print('check1')
    current_stocks = [i['code'] for i in select_conditions('stocks', 'code', exchange=exchange)]

    format_stock_name = progressbar.FormatCustomText(
        'Current Stock: %(stock)s',
        dict(
            stock='N/A'
        ),
    )
    widgets = [progressbar.Counter('Counter: %(value)05d'),
               ' stocks refreshed (', progressbar.Timer(), ') ', format_stock_name]
    bar = progressbar.ProgressBar(widgets=widgets)
    for ticker in bar(ticker_list):
        format_stock_name.update_mapping(stock=ticker)
        # print(stock['ticker'])
        stock_data = yf.Ticker(ticker)
        stock_info = stock_data.info
        # Gets last 5 days worth of stock, technically only needs last two days to calculate price_day_change
        stock_price = stock_data.history(period='5d', interval='1d')
        if 'website' in stock_info:
            website = stock_info['website']
        else:
            website = None

        if ticker in current_stocks:
            add_to_sql_table('stocks',
                             code=stock_info['symbol'],
                             exchange=exchange,
                             name=stock_info['shortName'],
                             price=stock_price['Open'][4],
                             price_day_change=stock_price['Open'][4] - stock_price['Open'][3],
                             high52=stock_info['fiftyTwoWeekHigh'],
                             low52=stock_info['fiftyTwoWeekLow'],
                             # Sort of a guess, but this seems to give the correct PE value
                             pe=stock_info['forwardPE'],
                             industry=stock_info['industry'],
                             description=stock_info['longBusinessSummary'],
                             marketCap=stock_info['marketCap'],
                             volume=stock_info['volume'],
                             lastTradeTime=datetime.datetime.now(
                                 tz=datetime.timezone(datetime.timedelta(hours=10), name='UTC+10')),
                             website=website,
                             suspended=0)
        else:
            update_sql_table('stocks',
                             conditions={'code': ticker, 'exchange': exchange},
                             code=stock_info['symbol'],
                             exchange=exchange,
                             name=stock_info['shortName'],
                             price=stock_price['Open'][4],
                             price_day_change=stock_price['Open'][4] - stock_price['Open'][3],
                             high52=stock_info['fiftyTwoWeekHigh'],
                             low52=stock_info['fiftyTwoWeekLow'],
                             # Sort of a guess, but this seems to give the correct PE value
                             pe=stock_info['forwardPE'],
                             industry=stock_info['industry'],
                             description=stock_info['longBusinessSummary'],
                             marketCap=stock_info['marketCap'],
                             volume=stock_info['volume'],
                             lastTradeTime=datetime.datetime.now(
                                 tz=datetime.timezone(datetime.timedelta(hours=10), name='UTC+10')),
                             website=website,
                             suspended=0)
        print('check5')

example_tickers = ['AA', 'GOOG', 'TSLA', 'A', 'GME']

start = time.perf_counter()
for stock in example_tickers:
    stock = yf.Ticker(stock)
    info = stock.info
    print(info)
end = time.perf_counter()
print(end - start)
# history = stock.history(period='5d', interval='1m')
# splits = stock.splits
# cashflow = stock.cashflow
# print(info)
# print(list(history))
# print(history)
# print(history['Open'][4])
# print(history['Open'][4] - history['Open'][3])

# update_all_nyse_stocks()
# update_all_nasdaq_stocks()
# update_all_amex_stocks()
