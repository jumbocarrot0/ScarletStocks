# from db_deets import *
import win32com.client as win32
import datetime, pythoncom, threading
from functools import wraps, partial
from time import sleep
import progressbar
from atexit import register

returned_values = []


# ---------------- OLD EXCEL METHODS TO GET STOCK DATA - PYASX IS USED NOW ----------------------
#

# def wipe_stocks_data():
#     connie = create_connection()
#     c = connie.cursor()
#     c.execute('''DELETE FROM stocks''')
#     connie.commit()
#     connie.close()
#
#
# @excel_function
# def ingest_to_sql_2(excel, workbook):
#     # Set max columns so all print
#     pd.set_option('display.max_columns', None)
#
#     # Read to a dataframe
#     stocks_data = pd.read_excel('StocksBook.xlsx', sheet_name='stocks')
#     del stocks_data['stockName']
#     # Clear stocks data prior to adding to table.
#     wipe_stocks_data()
#     stocks_data.to_sql('stocks', con=create_connection(), if_exists='append', index=False)
#
#     # print(stocks_data)


# @excel_function
# def add_cell(excel, workbook, value):
#     excel.Visible = 1
#     # excel.Workbooks.Add()
#     worksheet = workbook.Worksheets(1)
#     excelUp = -4162
#     worksheet_height = worksheet.Cells(worksheet.Rows.Count, "A").End(excelUp).Row
#     # 1st number is row, 2nd is column
#     excel.Cells(worksheet_height + 1, 1).Value = value
#     stockInfo = ['Name', '[Ticker Symbol]', 'Price', 'Change', 'Currency', '[52 week high]', '[52 week low]', '[P/E]',
#                  'Industry', 'Exchange', 'Description', '[Market cap]', 'Volume', '[Last trade time]']
#     for cellNumb in range(2, 16):
#         excel.Cells(worksheet_height + 1, cellNumb).Value = '=A' + str(worksheet_height + 1) + '.' + stockInfo[
#             cellNumb - 2]


# @excel_function

# Uses win32com to read excel file as pandas requires a save file


# Wrapper to execute the given function as a seperate python instance with threading
# so it can be run alongside a flask instance.
def parallelExecute(func):
    # print('parallelExecute')

    @wraps(func)
    def wrapper(*args, **kwargs):
        global returned_values
        # print('parallelExecute2')
        if threading.current_thread().getName() != 'MainThread':
            # print('parallelExecute3')
            pythoncom.CoInitialize()
            # print('args', args)
            threading.Thread(target=func, args=tuple(args), kwargs=dict(kwargs))
        # local_returned_values = returned_values
        # return local_returned_values

    return wrapper


def excel_function(func):
    # print('excel_function1')

    # if func is None:
    #     print('excel_function_noneException')
    #     return partial(excel_function, openStocksBook=openStocksBook)

    @wraps(func)
    def wrapper(*args, **kwargs):
        # print('excel_function2')
        if 0 == 1:
            excel = win32.Dispatch('Excel.Application')
            file = r'C:\Users\HARRINGAJ\OneDrive - Iona College\Units 3+4\Digital Solutions\IA2\IA2 Example Project\StocksBook.xlsx'
            workbook = excel.Workbooks.Open(file)
            workbook.Refreshall()
        else:
            excel = win32.Dispatch('Excel.Application')
            workbook = excel.Workbooks.Add()
        excel.Visible = False
        workbook.Refreshall()
        func(excel, workbook, *args, **kwargs)
        workbook.Close(SaveChanges=False)
        excel.Quit()
        # return local_returned_values

    return wrapper


def read_workbook(excel, workbook, columns):
    global returned_values

    worksheet = workbook.Worksheets(1)
    excelUp = -4162  # https://docs.microsoft.com/en-us/office/vba/api/excel.xldirection
    rowCount = excel.Cells(worksheet.Rows.Count, "A").End(excelUp).Row

    widgets = [progressbar.Counter('Counter: %(value)05d'),
               ' rows read (', progressbar.Timer(), ') ']
    bar = progressbar.ProgressBar(widgets=widgets)
    for i in bar(range(1, rowCount + 1)):
        returned_values.append([])
        for column in columns:
            # print(i, column)
            # 1st number is row, 2nd is column
            returned_values[-1].append(excel.cells(i, column).Value)
        # print('returned_values:', returned_values)

    # return returned_values


def get_historic_data(ticker, start_date):
    global returned_values
    returned_values = []
    # print('historic_data_2')
    if threading.current_thread().getName() != 'MainThread':
        pythoncom.CoInitialize()
        threading.Thread(get_historic_data_2(ticker, start_date))
    return returned_values


@excel_function
def get_historic_data_2(excel, workbook, ticker, start_date):
    worksheet = workbook.Sheets.Add(Before=None, After=workbook.Sheets(workbook.Sheets.count))
    worksheet.Name = "HistoricData"
    local_tz = datetime.timezone(datetime.timedelta(hours=10), name='UTC+10')
    # 1st number is row, 2nd is column
    worksheet.Cells(1, 1).Formula2 = '=STOCKHISTORY("TICKER", TODAY()-DELTA, TODAY(), 0, 0)'.replace(
        'TICKER', ticker).replace(
        'DELTA', str((datetime.datetime.now(tz=local_tz) - start_date).days))
    retries = 0
    max_retries = 10000
    # -2146826237 - #VALUE!
    # -2146826273 - #BUSY!
    # Waits until either the STOCKHISTORY function has loaded or throws a #VALUE! error
    while excel.Cells(1, 1).Value == -2146826273 and retries < max_retries:
        # print('Cell Value:', excel.Cells(1, 1).Value)
        retries += 1
        pass
    if excel.Cells(1, 1).Value == -2146826237:
        return

    read_workbook(excel, workbook, [1, 2])
