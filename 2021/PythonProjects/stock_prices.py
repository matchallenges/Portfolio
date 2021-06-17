import yfinance as yf

stock_info = []
current_price = []

tickerSymbol = 'WISH'


tickerData = yf.Ticker(tickerSymbol)


tickerDf = tickerData.history(period='1d')


gen = tickerDf.items()
for i in gen: stock_info.append(i)
current_price.append(stock_info[3])
print(*current_price[0][1].apply(str).str.strip())