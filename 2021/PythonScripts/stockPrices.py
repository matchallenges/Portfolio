
# Importing packages

import pandas as pd
import datetime as dt
import pandas_datareader.data as web
import plotly.express as px
import plotly.graph_objects as go

# Data

start = dt.datetime(2019,1,1)
end = dt.datetime.now()

stocks = web.DataReader(['FB','AMZN', 'AAPL', 'NFLX', 'GOOGL', 'MSFT'], 'yahoo', start, end)
stocks_close = pd.DataFrame(web.DataReader(['FB','AMZN', 'AAPL', 'NFLX', 'GOOGL', 'MSFT'], 'yahoo', start, end)['Close'])

# Area chart

area_chart = px.area(stocks_close.AMZN, title = 'AMZN SHARE PRICE (2013-2020)')

area_chart.update_xaxes(title_text = 'Date')
area_chart.update_yaxes(title_text = 'AMZN Close Price', tickprefix = '$')
area_chart.update_layout(showlegend = False)

area_chart.show()