# JSE Stock Dashboard (Python)

This is a small learning project I built to practise working with real stock market data from the Johannesburg Stock Exchange (JSE) using Python.

The project focuses on understanding the basics of stock price data and how different companies can be compared using simple data analysis techniques.

## What this project does
- Downloads historical JSE stock data (for example NPN.JO) using the yfinance library  
- Plots stock closing prices using Matplotlib  
- Compares multiple stocks on the same graph  
- Indexes prices to a common starting point so relative performance can be compared fairly  

## Project files
- `step_1_single_stock.py`  
  Analyses one JSE stock and plots its closing price  

- `step_2_multiple_stocks.py`  
  Compares multiple JSE stocks using lists and loops  

- `step_3_normalized_stocks.py`  
  Indexes stock prices to compare relative performance over time  

## How to run the project
1. Install the required libraries:
   - pandas  
   - matplotlib  
   - yfinance  

2. Run any of the Python files, for example:
   ```bash
   python step_1_single_stock.py
