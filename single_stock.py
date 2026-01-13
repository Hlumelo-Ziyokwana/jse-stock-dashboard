# We import yfinance so Python can download real stock data from the internet
# yfinance gets data from Yahoo Finance
import yfinance as yf

# We import matplotlib so we can draw graphs, pyplot is the part of matplotlib that handles plotting.
import matplotlib.pyplot as plt

# We create a stock object for Naspers.
# "NPN.JO" is the ticker symbol for Naspers on the Johannesburg Stock Exchange, ".JO" tells Yahoo Finance that this is a JSE stock
stock = yf.Ticker("NPN.JO")      # Naspers (JSE)

# We download historical price data for the stock for the last 3 months.
data = stock.history(period="3mo")

# calculate 20-day moving average
data["SMA_20"] = data["Close"].rolling(20).mean()


plt.plot(data["Close"], label = "Close Price")
plt.plot(data["SMA_20"], label ="20-Day SMA")

plt.title("Naspers Price with 20-Day Moving Average")
plt.xlabel("Date")
plt.ylabel("Price (ZAR)")
plt.legend()
plt.show()

