from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.fundamentaldata import FundamentalData
from alpha_vantage.alphavantage import AlphaVantage as av
from datetime import datetime
from db_functions import *
import pandas as pd

import win32com.client
import pythoncom, threading

search_date = datetime.now().date().strftime('%Y-%m-%d')

API_KEY = 'N6TFQ260IIKQFBER'

ts = TimeSeries(key=API_KEY)
fd = FundamentalData(key=API_KEY)


# Get json object with the intraday data and another with  the call's metadata
# data, meta_data = ts.get_intraday('GME')
# data, meta_data = fd.get_company_overview('GME')


#
# input_search = input('Enter Ticker: ')
#
# search, meta_search = ts.get_symbol_search(input_search)
# results = [i for i in search['1. symbol']]
# for i, code in enumerate(results):
#     print(str(i)+'. ' + str(code))
#
# string_range = [str(i) for i in range(0, len(results))]
#
# input_search_2 = '-1'
# while input_search_2 not in string_range:
#     input_search_2 = input('Enter Number: ')


def wipe_stocks_data():
    connie = create_connection()
    c = connie.cursor()
    c.execute('DELETE FROM stocks')
    connie.commit()
    connie.close()


def ingest_to_sql():
    if threading.current_thread().getName() != 'MainThread':
        pythoncom.CoInitialize()
        threading.Thread(ingest_to_sql_2())


def ingest_to_sql_2():
    # Read to a dataframe
    stocks_data = ['GME', 'GOOGL', 'AMZN', 'TSLA']
    # Clear stocks data prior to adding to table.
    wipe_stocks_data()

    # bar = Bar('Processing', max=len(stocks_data))
    for stock in stocks_data:
        company_data = fd.get_company_overview(stock)
        stock_data = ts.get_intraday(stock)[0].values()
        print(stock_data)
        add_to_sql_table('stocks',
                         code=stock,
                         exchange=company_data['Exchange'],
                         name=company_data['Name'],
                         price=stock_data['1. open'],
                         price_day_change=-1,
                         currency=company_data['Currency'],
                         high52=company_data['52WeekHigh'],
                         low52=company_data['52WeekLow'],
                         pe=company_data['PERatio'],
                         industry=company_data['Industry'],
                         # description = stock_data['description'],
                         marketCap=company_data['MarketCapitalization'],
                         volume=stock_data['5. volume'],
                         lastTradeTime=-1,
                         website=company_data['Description'])
        # bar.next()
    # bar.finish()


ingest_to_sql_2()
