import datetime
from dateutil.tz import tzoffset
from progress.bar import Bar

GME_info_ASX = {'ticker': 'GME',
                'name': 'GME RESOURCES LIMITED',
                'name_short': 'GME RESOURCES LTD',
                'principal_activities': 'Mineral exploration and investment.',
                'gics_industry': 'Materials',
                'gics_sector': 'Metals & Mining',
                'listing_date': datetime.datetime(1980, 8, 21, 0, 0, tzinfo=tzoffset(None, 36000)),
                'delisting_date': None,
                'website': 'http://www.gmeresources.com.au/',
                'mailing_address': 'Unit 5, 78 Marine Terrace, FREMANTLE, WA, AUSTRALIA, 6160',
                'phone_number': '+61 8 9336 3388',
                'fax_number': '+61 8 93155475',
                'registry_name': 'COMPUTERSHARE INVESTOR SERVICES PTY LIMITED',
                'registry_phone_number': '1300 850 505',
                'foreign_exempt': False, 'products': ['shares'],
                'last_dividend': {'type': '',
                                  'created_date': '',
                                  'ex_date': '',
                                  'payable_date': '',
                                  'record_date': '',
                                  'books_close_date': '',
                                  'amount_aud': '',
                                  'franked_percent': '',
                                  'comments': ''},
                'primary_share': {'ticker': 'GME',
                                  'isin': 'AU000000GME7',
                                  'type': 'Ordinary Fully Paid',
                                  'open_price': 0.06,
                                  'last_price': 0.06,
                                  'bid_price': 0.056,
                                  'offer_price': 0.06,
                                  'last_trade_date': datetime.datetime(2021, 4, 27, 0, 0, tzinfo=tzoffset(None, 36000)),
                                  'day_high_price': 0.06,
                                  'day_low_price': 0.06,
                                  'day_change_price': -0.002,
                                  'day_change_percent': '-3.226%',
                                  'day_volume': 114363,
                                  'prev_day_close_price': 0.062,
                                  'prev_day_change_percent': '0%',
                                  'year_high_price': 0.13,
                                  'year_high_date': datetime.datetime(2021, 1, 29, 0, 0, tzinfo=tzoffset(None, 39600)),
                                  'year_low_price': 0.032,
                                  'year_low_date': datetime.datetime(2020, 8, 24, 0, 0, tzinfo=tzoffset(None, 36000)),
                                  'year_open_price': 0.0263,
                                  'year_change_price': 0.0337,
                                  'year_change_percent': '128.137%',
                                  'average_daily_volume': 988936,
                                  'pe': 0,
                                  'eps': -0.0001,
                                  'annual_dividend_yield': 0,
                                  'securities_outstanding': 556866930,
                                  'market_cap': 34525750,
                                  'is_suspended': False,
                                  'indices': []}}

GME_info_AVantage = {'Symbol': 'GME',
                     'AssetType': 'Common Stock',
                     'Name': 'GameStop Corp',
                     'Description': 'GameStop Corp., a specialty retailer, provides games and entertainment products through its e-commerce properties and various stores in the United States, Canada, Australia, and Europe. The company sells new and pre-owned video game platforms; accessories, such as controllers, gaming headsets, virtual reality products, and memory cards; new and pre-owned video game software; and in-game digital currency, digital downloadable content, and full-game downloads, as well as network points cards, and prepaid digital and subscription cards. It also sells collectibles comprising licensed merchandise primarily related to the video game, television, and movie industries, as well as pop culture themes. The company operates its stores and e-commerce sites under the GameStop, EB Games, and Micromania brands; and collectibles stores under the Zing Pop Culture and ThinkGeek brand, as well as offers Game Informer, a print and digital video game publication featuring reviews of new title releases, game tips, and news regarding the video game industry. As of January 30, 2021, it operated 4,816 stores. The company was formerly known as GSC Holdings Corp. GameStop Corp. was founded in 1996 and is headquartered in Grapevine, Texas.',
                     'CIK': '1326380',
                     'Exchange': 'NYSE',
                     'Currency': 'USD',
                     'Country': 'USA',
                     'Sector': 'Consumer Cyclical',
                     'Industry': 'Specialty Retail',
                     'Address': '625 Westport Parkway, Grapevine, TX, United States, 76051',
                     'FullTimeEmployees': '12000',
                     'FiscalYearEnd': 'January',
                     'LatestQuarter': '2021-01-31',
                     'MarketCapitalization': '12973858816',
                     'EBITDA': '111300000',
                     'PERatio': 'None',
                     'PEGRatio': '0.86',
                     'BookValue': '6.688',
                     'DividendPerShare': '0',
                     'DividendYield': '0',
                     'EPS': '-10.664',
                     'RevenuePerShareTTM': '78.305',
                     'ProfitMargin': '-0.0423',
                     'OperatingMarginTTM': '-0.049', 'ReturnOnAssetsTTM': '-0.0589', 'ReturnOnEquityTTM': '-0.4095',
                     'RevenueTTM': '5089800192', 'GrossProfitTTM': '1259500000', 'DilutedEPSTTM': '-3.312',
                     'QuarterlyEarningsGrowthYOY': '2.689', 'QuarterlyRevenueGrowthYOY': '-0.033',
                     'AnalystTargetPrice': '41.79', 'TrailingPE': '0', 'ForwardPE': '36.7647',
                     'PriceToSalesRatioTTM': '2.2702', 'PriceToBookRatio': '28.8095', 'EVToRevenue': '2.5776',
                     'EVToEBITDA': '0', 'Beta': '-1.8169', '52WeekHigh': '483', '52WeekLow': '3.77',
                     '50DayMovingAverage': '184.6612', '200DayMovingAverage': '80.6704',
                     'SharesOutstanding': '70771800', 'SharesFloat': '46374448', 'SharesShort': '10696160',
                     'SharesShortPriorMonth': '14200138', 'ShortRatio': '0.36', 'ShortPercentOutstanding': '0.15',
                     'ShortPercentFloat': '0.3893', 'PercentInsiders': '19.417', 'PercentInstitutions': '108.963',
                     'ForwardAnnualDividendRate': '0', 'ForwardAnnualDividendYield': '0', 'PayoutRatio': '0',
                     'DividendDate': '2019-03-29', 'ExDividendDate': '2019-03-14', 'LastSplitFactor': '2:1',
                     'LastSplitDate': '2007-03-19'}

for i in Bar('Processing').iter(GME_info_ASX):
    x = i

GOOGL_data_AVantage = {'2021-04-23 20:00:00': {'1. open': '2305.0000',
                                               '2. high': '2305.2000',
                                               '3. low': '2305.0000',
                                               '4. close': '2305.0000',
                                               '5. volume': '1292'},
                       '2021-04-23 17:30:00': {'1. open': '2299.7500',
                                               '2. high': '2299.9300',
                                               '3. low': '2299.5000',
                                               '4. close': '2299.9300',
                                               '5. volume': '2111'},
                       '2021-04-23 17:15:00': {'1. open': '2298.7300',
                                               '2. high': '2299.5000',
                                               '3. low': '2298.7300',
                                               '4. close': '2299.5000',
                                               '5. volume': '604'},
                       '2021-04-23 17:00:00': {'1. open': '2298.7300',
                                               '2. high': '2298.7300',
                                               '3. low': '2298.7300',
                                               '4. close': '2298.7300',
                                               '5. volume': '321'},
                       '2021-04-23 16:45:00': {'1. open': '2298.0100',
                                               '2. high': '2299.9300',
                                               '3. low': '2297.6800',
                                               '4. close': '2297.9000',
                                               '5. volume': '61335'},
                       '2021-04-23 16:30:00': {'1. open': '2297.8000', '2. high': '2299.9300', '3. low': '2297.6000',
                                               '4. close': '2297.6000', '5. volume': '1800'},
                       '2021-04-23 16:15:00': {'1. open': '2299.9300', '2. high': '2299.9300', '3. low': '2298.0000',
                                               '4. close': '2299.9300', '5. volume': '24290'},
                       '2021-04-23 16:00:00': {'1. open': '2302.9800', '2. high': '2303.4200', '3. low': '2299.3000',
                                               '4. close': '2299.9400', '5. volume': '173596'},
                       '2021-04-23 15:45:00': {'1. open': '2303.5500', '2. high': '2305.6200', '3. low': '2302.4000',
                                               '4. close': '2302.5600', '5. volume': '58824'},
                       '2021-04-23 15:30:00': {'1. open': '2302.6000', '2. high': '2304.6300', '3. low': '2300.6525',
                                               '4. close': '2302.2700', '5. volume': '52245'},
                       '2021-04-23 15:15:00': {'1. open': '2302.0200', '2. high': '2303.7050', '3. low': '2301.2900',
                                               '4. close': '2302.6000', '5. volume': '51280'},
                       '2021-04-23 15:00:00': {'1. open': '2298.3500', '2. high': '2302.9600', '3. low': '2297.6640',
                                               '4. close': '2301.9550', '5. volume': '24033'},
                       '2021-04-23 14:45:00': {'1. open': '2298.9700', '2. high': '2300.1250', '3. low': '2298.3700',
                                               '4. close': '2299.1400', '5. volume': '14742'},
                       '2021-04-23 14:30:00': {'1. open': '2299.2600', '2. high': '2300.3600', '3. low': '2297.7810',
                                               '4. close': '2298.3900', '5. volume': '17804'},
                       '2021-04-23 14:15:00': {'1. open': '2297.0000', '2. high': '2300.0800', '3. low': '2297.0000',
                                               '4. close': '2300.0600', '5. volume': '19232'},
                       '2021-04-23 14:00:00': {'1. open': '2297.2000', '2. high': '2297.2000', '3. low': '2296.0000',
                                               '4. close': '2297.0300', '5. volume': '18320'},
                       '2021-04-23 13:45:00': {'1. open': '2297.7800', '2. high': '2299.7240', '3. low': '2296.8000',
                                               '4. close': '2297.4200', '5. volume': '19309'},
                       '2021-04-23 13:30:00': {'1. open': '2302.7700', '2. high': '2302.8250', '3. low': '2294.2833',
                                               '4. close': '2298.0600', '5. volume': '36375'},
                       '2021-04-23 13:15:00': {'1. open': '2303.4400', '2. high': '2304.3200', '3. low': '2300.6100',
                                               '4. close': '2302.0600', '5. volume': '29483'},
                       '2021-04-23 13:00:00': {'1. open': '2302.8050', '2. high': '2306.1175', '3. low': '2302.3500',
                                               '4. close': '2302.8293', '5. volume': '43614'},
                       '2021-04-23 12:45:00': {'1. open': '2297.1750', '2. high': '2303.9700', '3. low': '2297.1400',
                                               '4. close': '2303.0400', '5. volume': '35938'},
                       '2021-04-23 12:30:00': {'1. open': '2298.4000', '2. high': '2299.4800', '3. low': '2294.4500',
                                               '4. close': '2298.2300', '5. volume': '21630'},
                       '2021-04-23 12:15:00': {'1. open': '2295.3900', '2. high': '2302.0900', '3. low': '2295.3900',
                                               '4. close': '2297.4900', '5. volume': '57321'},
                       '2021-04-23 12:00:00': {'1. open': '2290.8699', '2. high': '2298.0000', '3. low': '2290.8699',
                                               '4. close': '2295.2150', '5. volume': '36762'},
                       '2021-04-23 11:45:00': {'1. open': '2288.5300', '2. high': '2290.7600', '3. low': '2286.7600',
                                               '4. close': '2289.9900', '5. volume': '72583'},
                       '2021-04-23 11:30:00': {'1. open': '2282.0300', '2. high': '2290.5500', '3. low': '2280.4890',
                                               '4. close': '2288.1199', '5. volume': '47759'},
                       '2021-04-23 11:15:00': {'1. open': '2278.1550', '2. high': '2281.0100', '3. low': '2275.6850',
                                               '4. close': '2279.5000', '5. volume': '28363'},
                       '2021-04-23 11:00:00': {'1. open': '2273.0900', '2. high': '2279.2500', '3. low': '2273.0900',
                                               '4. close': '2277.5700', '5. volume': '30534'},
                       '2021-04-23 10:45:00': {'1. open': '2265.2250', '2. high': '2275.0900', '3. low': '2262.5000',
                                               '4. close': '2273.1000', '5. volume': '38269'},
                       '2021-04-23 10:30:00': {'1. open': '2266.1000', '2. high': '2268.0700', '3. low': '2263.5000',
                                               '4. close': '2264.5300', '5. volume': '22396'},
                       '2021-04-23 10:15:00': {'1. open': '2264.5800', '2. high': '2268.6550', '3. low': '2261.4200',
                                               '4. close': '2264.8775', '5. volume': '57194'},
                       '2021-04-23 10:00:00': {'1. open': '2268.1200', '2. high': '2268.4600', '3. low': '2261.2500',
                                               '4. close': '2264.6300', '5. volume': '62176'},
                       '2021-04-23 09:45:00': {'1. open': '2267.0000', '2. high': '2277.1500', '3. low': '2264.8300',
                                               '4. close': '2268.0100', '5. volume': '102949'},
                       '2021-04-23 09:30:00': {'1. open': '2260.1477', '2. high': '2260.1477', '3. low': '2260.1477',
                                               '4. close': '2260.1477', '5. volume': '170'},
                       '2021-04-23 08:15:00': {'1. open': '2252.5200', '2. high': '2252.5200', '3. low': '2252.5200',
                                               '4. close': '2252.5200', '5. volume': '7130'},
                       '2021-04-23 07:45:00': {'1. open': '2260.0000', '2. high': '2260.0000', '3. low': '2260.0000',
                                               '4. close': '2260.0000', '5. volume': '340'},
                       '2021-04-22 17:15:00': {'1. open': '2255.1700', '2. high': '2255.1700', '3. low': '2255.1700',
                                               '4. close': '2255.1700', '5. volume': '207'},
                       '2021-04-22 17:00:00': {'1. open': '2257.2900', '2. high': '2257.2900', '3. low': '2257.2900',
                                               '4. close': '2257.2900', '5. volume': '23548'},
                       '2021-04-22 16:45:00': {'1. open': '2255.0000', '2. high': '2255.0000', '3. low': '2255.0000',
                                               '4. close': '2255.0000', '5. volume': '417'},
                       '2021-04-22 16:30:00': {'1. open': '2247.4284', '2. high': '2247.4284', '3. low': '2247.4284',
                                               '4. close': '2247.4284', '5. volume': '161'},
                       '2021-04-22 16:15:00': {'1. open': '2252.5200', '2. high': '2252.5200', '3. low': '2252.5200',
                                               '4. close': '2252.5200', '5. volume': '41824'},
                       '2021-04-22 16:00:00': {'1. open': '2251.6000', '2. high': '2255.0600', '3. low': '2245.0300',
                                               '4. close': '2252.8600', '5. volume': '144063'},
                       '2021-04-22 15:45:00': {'1. open': '2247.9600', '2. high': '2253.7400', '3. low': '2247.9600',
                                               '4. close': '2250.4700', '5. volume': '39579'},
                       '2021-04-22 15:30:00': {'1. open': '2247.8200', '2. high': '2251.2400', '3. low': '2243.6100',
                                               '4. close': '2247.0800', '5. volume': '50437'},
                       '2021-04-22 15:15:00': {'1. open': '2249.3300', '2. high': '2252.9200', '3. low': '2246.7800',
                                               '4. close': '2248.7250', '5. volume': '22808'},
                       '2021-04-22 15:00:00': {'1. open': '2255.0900', '2. high': '2256.2100', '3. low': '2250.0000',
                                               '4. close': '2250.3915', '5. volume': '23780'},
                       '2021-04-22 14:45:00': {'1. open': '2254.4900', '2. high': '2255.0000', '3. low': '2249.0000',
                                               '4. close': '2255.0000', '5. volume': '23370'},
                       '2021-04-22 14:30:00': {'1. open': '2251.4000', '2. high': '2255.0000', '3. low': '2246.9500',
                                               '4. close': '2255.0000', '5. volume': '37203'},
                       '2021-04-22 14:15:00': {'1. open': '2248.0000', '2. high': '2253.5800', '3. low': '2240.3200',
                                               '4. close': '2251.8800', '5. volume': '79329'},
                       '2021-04-22 14:00:00': {'1. open': '2250.7300', '2. high': '2253.7550', '3. low': '2242.5600',
                                               '4. close': '2248.9000', '5. volume': '84509'},
                       '2021-04-22 13:45:00': {'1. open': '2262.1300', '2. high': '2262.1300', '3. low': '2250.0000',
                                               '4. close': '2250.0000', '5. volume': '33897'},
                       '2021-04-22 13:30:00': {'1. open': '2266.3700', '2. high': '2266.4400', '3. low': '2254.6100',
                                               '4. close': '2263.7250', '5. volume': '69956'},
                       '2021-04-22 13:15:00': {'1. open': '2278.9900', '2. high': '2279.5700', '3. low': '2261.6900',
                                               '4. close': '2267.1650', '5. volume': '64304'},
                       '2021-04-22 13:00:00': {'1. open': '2278.7200', '2. high': '2279.3700', '3. low': '2276.5600',
                                               '4. close': '2278.9800', '5. volume': '12649'},
                       '2021-04-22 12:45:00': {'1. open': '2276.7000', '2. high': '2279.4300', '3. low': '2276.6800',
                                               '4. close': '2278.4000', '5. volume': '14240'},
                       '2021-04-22 12:30:00': {'1. open': '2273.0200', '2. high': '2276.8900', '3. low': '2271.7700',
                                               '4. close': '2276.8900', '5. volume': '16041'},
                       '2021-04-22 12:15:00': {'1. open': '2275.9450', '2. high': '2275.9450', '3. low': '2271.1100',
                                               '4. close': '2271.9288', '5. volume': '17357'},
                       '2021-04-22 12:00:00': {'1. open': '2276.4800', '2. high': '2278.8623', '3. low': '2274.9200',
                                               '4. close': '2275.5000', '5. volume': '15011'},
                       '2021-04-22 11:45:00': {'1. open': '2279.5100', '2. high': '2281.6450', '3. low': '2276.1540',
                                               '4. close': '2276.7600', '5. volume': '19567'},
                       '2021-04-22 11:30:00': {'1. open': '2281.7900', '2. high': '2283.8700', '3. low': '2280.2900',
                                               '4. close': '2281.2400', '5. volume': '15540'},
                       '2021-04-22 11:15:00': {'1. open': '2284.7100', '2. high': '2286.4700', '3. low': '2279.9450',
                                               '4. close': '2281.2600', '5. volume': '26020'},
                       '2021-04-22 11:00:00': {'1. open': '2283.1400', '2. high': '2286.5000', '3. low': '2282.0000',
                                               '4. close': '2283.6250', '5. volume': '23265'},
                       '2021-04-22 10:45:00': {'1. open': '2285.4900', '2. high': '2288.8814', '3. low': '2282.8500',
                                               '4. close': '2283.5400', '5. volume': '27359'},
                       '2021-04-22 10:30:00': {'1. open': '2282.2500', '2. high': '2286.0600', '3. low': '2280.4000',
                                               '4. close': '2285.5143', '5. volume': '18682'},
                       '2021-04-22 10:15:00': {'1. open': '2281.1100', '2. high': '2284.6800', '3. low': '2278.4050',
                                               '4. close': '2280.8800', '5. volume': '39431'},
                       '2021-04-22 10:00:00': {'1. open': '2275.0000', '2. high': '2281.7500', '3. low': '2270.8123',
                                               '4. close': '2281.2100', '5. volume': '37611'},
                       '2021-04-22 09:45:00': {'1. open': '2275.4000', '2. high': '2278.1400', '3. low': '2266.8800',
                                               '4. close': '2274.7000', '5. volume': '74313'},
                       '2021-04-22 09:30:00': {'1. open': '2274.8800', '2. high': '2274.8800', '3. low': '2274.0000',
                                               '4. close': '2274.0000', '5. volume': '1013'},
                       '2021-04-22 09:15:00': {'1. open': '2274.7500', '2. high': '2274.7500', '3. low': '2274.7500',
                                               '4. close': '2274.7500', '5. volume': '278'},
                       '2021-04-22 09:00:00': {'1. open': '2274.7600', '2. high': '2274.7600', '3. low': '2274.7600',
                                               '4. close': '2274.7600', '5. volume': '241'},
                       '2021-04-22 08:00:00': {'1. open': '2275.0000', '2. high': '2275.0000', '3. low': '2275.0000',
                                               '4. close': '2275.0000', '5. volume': '405'},
                       '2021-04-21 19:30:00': {'1. open': '2274.0000', '2. high': '2274.0000', '3. low': '2274.0000',
                                               '4. close': '2274.0000', '5. volume': '193'},
                       '2021-04-21 17:15:00': {'1. open': '2276.3900', '2. high': '2276.3900', '3. low': '2276.3900',
                                               '4. close': '2276.3900', '5. volume': '104'},
                       '2021-04-21 16:45:00': {'1. open': '2278.3500', '2. high': '2278.3500', '3. low': '2278.3500',
                                               '4. close': '2278.3500', '5. volume': '252'},
                       '2021-04-21 16:30:00': {'1. open': '2275.2700', '2. high': '2275.2700', '3. low': '2275.2700',
                                               '4. close': '2275.2700', '5. volume': '295'},
                       '2021-04-21 16:15:00': {'1. open': '2278.3500', '2. high': '2278.3500', '3. low': '2275.9100',
                                               '4. close': '2275.9100', '5. volume': '32801'},
                       '2021-04-21 16:00:00': {'1. open': '2276.0000', '2. high': '2280.0000', '3. low': '2272.2500',
                                               '4. close': '2278.3400', '5. volume': '164744'},
                       '2021-04-21 15:45:00': {'1. open': '2266.8200', '2. high': '2275.3300', '3. low': '2266.7400',
                                               '4. close': '2275.3300', '5. volume': '51236'},
                       '2021-04-21 15:30:00': {'1. open': '2264.4100', '2. high': '2266.6500', '3. low': '2263.0150',
                                               '4. close': '2266.6500', '5. volume': '25657'},
                       '2021-04-21 15:15:00': {'1. open': '2262.7550', '2. high': '2264.9800', '3. low': '2261.1900',
                                               '4. close': '2264.9700', '5. volume': '17084'},
                       '2021-04-21 15:00:00': {'1. open': '2262.8600', '2. high': '2264.1800', '3. low': '2262.5300',
                                               '4. close': '2262.7400', '5. volume': '8622'},
                       '2021-04-21 14:45:00': {'1. open': '2265.7000', '2. high': '2266.7500', '3. low': '2262.9660',
                                               '4. close': '2263.4300', '5. volume': '8661'},
                       '2021-04-21 14:30:00': {'1. open': '2267.3500', '2. high': '2268.7800', '3. low': '2264.0200',
                                               '4. close': '2265.4900', '5. volume': '11669'},
                       '2021-04-21 14:15:00': {'1. open': '2266.0050', '2. high': '2267.6900', '3. low': '2266.0050',
                                               '4. close': '2267.3500', '5. volume': '14410'},
                       '2021-04-21 14:00:00': {'1. open': '2264.5000', '2. high': '2266.8100', '3. low': '2262.6000',
                                               '4. close': '2266.0100', '5. volume': '21108'},
                       '2021-04-21 13:45:00': {'1. open': '2263.5800', '2. high': '2265.2400', '3. low': '2262.1400',
                                               '4. close': '2264.7600', '5. volume': '33359'},
                       '2021-04-21 13:30:00': {'1. open': '2263.0100', '2. high': '2264.1100', '3. low': '2261.1300',
                                               '4. close': '2263.0000', '5. volume': '10995'},
                       '2021-04-21 13:15:00': {'1. open': '2258.5300', '2. high': '2262.5700', '3. low': '2256.7000',
                                               '4. close': '2260.7100', '5. volume': '19763'},
                       '2021-04-21 13:00:00': {'1. open': '2258.6200', '2. high': '2261.2600', '3. low': '2257.3500',
                                               '4. close': '2257.9500', '5. volume': '28095'},
                       '2021-04-21 12:45:00': {'1. open': '2261.5700', '2. high': '2261.5791', '3. low': '2258.8000',
                                               '4. close': '2259.4600', '5. volume': '19902'},
                       '2021-04-21 12:30:00': {'1. open': '2261.8100', '2. high': '2263.3200', '3. low': '2260.3000',
                                               '4. close': '2260.3000', '5. volume': '17537'},
                       '2021-04-21 12:15:00': {'1. open': '2264.9200', '2. high': '2265.4800', '3. low': '2261.1000',
                                               '4. close': '2261.8500', '5. volume': '24457'},
                       '2021-04-21 12:00:00': {'1. open': '2264.8500', '2. high': '2266.2568', '3. low': '2262.4300',
                                               '4. close': '2266.2568', '5. volume': '19107'},
                       '2021-04-21 11:45:00': {'1. open': '2262.2850', '2. high': '2267.9700', '3. low': '2260.4600',
                                               '4. close': '2265.5100', '5. volume': '29086'},
                       '2021-04-21 11:30:00': {'1. open': '2256.3450', '2. high': '2263.0000', '3. low': '2256.0000',
                                               '4. close': '2262.6500', '5. volume': '31793'},
                       '2021-04-21 11:15:00': {'1. open': '2247.5300', '2. high': '2255.4200', '3. low': '2247.5300',
                                               '4. close': '2255.2400', '5. volume': '37030'},
                       '2021-04-21 11:00:00': {'1. open': '2250.1400', '2. high': '2251.9200', '3. low': '2244.8200',
                                               '4. close': '2248.0500', '5. volume': '47394'},
                       '2021-04-21 10:45:00': {'1. open': '2255.3050', '2. high': '2255.3050', '3. low': '2245.0000',
                                               '4. close': '2249.6100', '5. volume': '61736'},
                       '2021-04-21 10:30:00': {'1. open': '2252.4800', '2. high': '2256.7600', '3. low': '2248.0000',
                                               '4. close': '2255.5100', '5. volume': '51662'},
                       '2021-04-21 10:15:00': {'1. open': '2262.5300', '2. high': '2262.5300', '3. low': '2246.0000',
                                               '4. close': '2251.1000', '5. volume': '75644'}}

GOOGL_meta_data_AVantage = {'1. Information': 'Intraday (15min) open, high, low, close prices and volume',
                            '2. Symbol': 'GOOGL',
                            '3. Last Refreshed': '2021-04-23 20:00:00',
                            '4. Interval': '15min',
                            '5. Output Size': 'Compact',
                            '6. Time Zone': 'US/Eastern'}