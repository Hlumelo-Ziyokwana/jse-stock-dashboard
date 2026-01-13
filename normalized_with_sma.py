import yfinance as yf
import matplotlib.pyplot as plt

# Stocks we want to analyse
tickers = ["NPN.JO", "SOL.JO", "SHP.JO", "MTN.JO"]

# Time period
period = "6mo"

for ticker in tickers:
    
    # Download stock data
    stock = yf.Ticker(ticker)
    data = stock.history(period=period)
    
    # Get closing prices
    close_prices = data["Close"]
    
    # Normalized prices so all stocks start at 100
    normalized = (close_prices / close_prices.iloc[0]) * 100
    sma_20 = normalized.rolling(20).mean()
    
    # Plot normalized prices
    plt.plot(normalized, alpha=0.4)
    # Plot moving average
    plt.plot(sma_20, label=f"{ticker} trend")

# Add graph details
plt.title("Normalized JSE Stocks with 20-Day Moving Average")
plt.xlabel("Date")
plt.ylabel("Relative Performance")
plt.legend()
plt.show()
