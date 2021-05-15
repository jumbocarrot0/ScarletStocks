import pandas_market_calendars as mcal
import pandas as pd
import datetime

# Create a calendar
asx = mcal.get_calendar('ASX')

# Show available calendars
print(mcal.get_calendar_names())

# print(asx)

local_tz = datetime.timezone(datetime.timedelta(hours=10), name='UTC+10')

early = asx.schedule(start_date=datetime.datetime.now(tz=local_tz),
                     end_date=datetime.datetime.now(tz=local_tz))
print(early)

if early.empty:
    print('Closed')
else:
    market_open = early['market_open'][0].to_pydatetime()
    market_close = early['market_close'][0].to_pydatetime()

    print(market_open)
    print(market_close)

    print(market_open <= datetime.datetime.now(tz=local_tz) <= market_close)
