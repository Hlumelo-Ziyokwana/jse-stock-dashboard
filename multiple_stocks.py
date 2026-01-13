import yfinance as yf
import matplotlib.pyplot as plt

# This list stores the stock codes we want to analyse, with each code representing a company on the JSE.
# For example: NPN.JO = Naspers ,SOL.JO = Saso, SBK.JO = Standard Bank, SHP = Shoprite, MTN = Mobile Telephone Networks.
tickers = ["NPN.JO", "SOL.JO", "SBK.JO", "SHP.JO", "MTN.JO"]


period = "3mo"

for ticker in tickers:
    
    # Create a stock object for the current ticker, this tells Python which company we are working with
    stock = yf.Ticker(ticker)
    
    # Download historical price data for the chosen time period
    data = stock.history(period=period)
    
    # Plot the closing price for this stock
    # Each stock is drawn as a separate line on the same graph
    plt.plot(data["Close"], label=ticker)

# Add graph details
plt.title("JSE Stocks – Closing Prices Over Time")
plt.xlabel("Date")
plt.ylabel("Price (ZAR)")
plt.legend()

# Display the graph on the screen
plt.show()

