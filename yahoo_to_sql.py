# Yahoo finance has no function to get a list of available ticker codes, unlike pyasx.
# The get_all_tickers module returns list of tickers for New York Stock Exchange (NYSE),
# The Nasdaq market (NASDAQ) and NYSE American (NYSEAMERICAN)

import yfinance as yf
# Technically the module used is a branch of the original to fix a critical bug
from get_all_tickers.get_tickers import get_tickers
import datetime
from db_functions import *
import time

# Multiprocessing is used to speed up process
from multiprocessing import Pool
from json.decoder import JSONDecodeError


# NYSE = get_tickers(NYSE=True, NASDAQ=False, AMEX=False)
# NASDAQ = get_tickers(NYSE=False, NASDAQ=True, AMEX=False)
# AMEX = get_tickers(NYSE=False, NASDAQ=False, AMEX=True)
# print(NYSE)
# print(NASDAQ)
# print(AMEX)
# print(len(NYSE), len(NASDAQ), len(AMEX))
# Output: 2665 4206 253

# These are functions to get all stocks from the three exchanges available into the database.
# A list of all stocks from one exchange is gathered before being sent to the update_all_yahoo_stocks function
def update_all_nyse_stocks():
    ticker_list = get_tickers(NYSE=True, NASDAQ=False, AMEX=False)
    update_all_yahoo_stocks(ticker_list, 'NYSE')


def update_all_nasdaq_stocks():
    ticker_list = get_tickers(NYSE=False, NASDAQ=True, AMEX=False)
    update_all_yahoo_stocks(ticker_list, 'NASDAQ')


def update_all_amex_stocks():
    ticker_list = get_tickers(NYSE=False, NASDAQ=False, AMEX=True)
    update_all_yahoo_stocks(ticker_list, 'NYSEAMERICAN')


def get_stock_data(ticker):
    print(ticker)
    try:
        # Gather relevant stock info before retuning as a dictionary
        stock_data = yf.Ticker(ticker)
        stock_info = stock_data.info
        stock_price = stock_data.history(period='5d', interval='1d')
        if 'website' in stock_info:
            stock_website = stock_info['website']
        else:
            stock_website = None
        sql_data = {'code': stock_info['symbol'],
                    'name': stock_info['longName'],
                    'price': stock_price['Open'][4],
                    'price_day_change': stock_price['Open'][4] - stock_price['Open'][3],
                    'high52': stock_info['fiftyTwoWeekHigh'],
                    'low52': stock_info['fiftyTwoWeekLow'],
                    # Sort of a guess, but this seems to give the correct PE value
                    'pe': stock_info['forwardPE'],
                    'industry': stock_info['industry'],
                    'description': stock_info['longBusinessSummary'],
                    'marketCap': stock_info['marketCap'],
                    'volume': stock_info['volume'],
                    'lastTradeTime': datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=10))),
                    'website': stock_website,
                    'suspended': 0}
        return sql_data
    # These check to return any stock with missing data as a none, which will be removed later.
    # Could be implemented better to not just delete these stocks, but it works well enough.
    except KeyError as e:
        print(repr(e), ticker)
        return {}
    except JSONDecodeError as e:
        print(repr(e), ticker)
        return {}
    except IndexError as e:
        print(repr(e), ticker)
        return {}


def update_all_yahoo_stocks(ticker_list, exchange):
    # Get a list of stocks already in the database, and from that see which stocks need to be added to
    # the database and which are already in and must be updated.
    current_stocks = [i['code'] for i in select_conditions('stocks', 'code', exchange=exchange)]
    stocks_to_update = [i for i in ticker_list if i in current_stocks]
    stocks_to_add = [i for i in ticker_list if i not in current_stocks]

    print('add:', stocks_to_add)
    print('update:', stocks_to_update)

    if __name__ == '__main__':
        # Allows multiple stocks to be analysed in parallel, making the process a lot faster (albeit still fairly slow)
        with Pool() as p:
            # print('check2')
            sql_data_add = p.map(get_stock_data, stocks_to_add, 10)
            sql_data_update = p.map(get_stock_data, stocks_to_update, 10)

        # Fancy method to remove any None values, i.e. stocks that had missing data
        sql_data_add = list(filter({}.__ne__, sql_data_add))
        sql_data_update = list(filter({}.__ne__, sql_data_update))

        print('add:', sql_data_add)
        print('update:', sql_data_update)

        # Finally adds collected data to the sql database. The dictionary can be passed
        # into the function as a series of keyword arguments
        for row in sql_data_add:
            add_to_sql_table('stocks', exchange=exchange, **row)
        for row in sql_data_update:
            update_sql_table('stocks', conditions={'code': row['code'], 'exchange': exchange}, exchange=exchange, **row)


start = time.perf_counter()

# update_all_nyse_stocks()
update_all_nasdaq_stocks()
# update_all_amex_stocks()

end = time.perf_counter()
print(end - start)
