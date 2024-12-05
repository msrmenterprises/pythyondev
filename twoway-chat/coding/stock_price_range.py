# filename: stock_price_range.py
import yfinance as yf
import matplotlib.pyplot as plt

# Retrieve historical stock price data for Meta and Tesla
meta_data = yf.Ticker("META").history(period="1mo")
tesla_data = yf.Ticker("TSLA").history(period="1mo")

# Extract the stock prices
meta_prices = meta_data["Close"]
tesla_prices = tesla_data["Close"]

# Plot a chart comparing the stock price range for Meta and Tesla
plt.figure(figsize=(14, 7))
plt.plot(meta_prices, label='Meta', color='b')
plt.plot(tesla_prices, label='Tesla', color='r')
plt.title('Meta and Tesla Stock Price Range Comparison')
plt.xlabel('Date')
plt.ylabel('Stock Price')
plt.legend()
plt.grid(True)
plt.show()