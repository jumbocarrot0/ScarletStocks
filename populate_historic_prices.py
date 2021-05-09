from db_functions import *
from excel_to_sql import get_historic_data_2
import progressbar
import datetime
from dateutil.parser import parse


stocks_data = select_specific_columns('stocks', 'code')
# stocks_data = [{'code': 'GME'}, {'code': 'ANZ'}, {'code': 'BHP'}]


format_stock_name = progressbar.FormatCustomText(
    'Current Stock: %(stock)s, Date: %(date)s',
    dict(
        stock='N/A',
        date='N/A'
    ),
)

widgets = ['Processed: ', progressbar.Counter('Counter: %(value)05d'),
           ' stocks (', progressbar.Timer(), ') ', format_stock_name]
bar = progressbar.ProgressBar(widgets=widgets)
for stock in bar((stock for stock in stocks_data)):
    format_stock_name.update_mapping(stock=stock['code'])
    stock_history = None
    while stock_history is None:
        stock_history = get_historic_data_2('XASX:' + stock['code'], datetime.date(2015, 1, 1))
    for stock_date, price in stock_history:
        stock_date = parse(str(stock_date))
        format_stock_name.update_mapping(date=stock_date)
        add_to_sql_table('historic_prices',
                         code=stock['code'],
                         exchange='Australian Securities Exchange',
                         price=str(price),
                         date=stock_date)
