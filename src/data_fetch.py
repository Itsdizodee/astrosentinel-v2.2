"""
Fetches historical and live price data for AstroSentinel V2.
Supports Yahoo Finance; Binance for crypto (future).
"""
import yfinance as yf
import pandas as pd

def get_data(symbol, timeframe="15m"):
    symbol_map = {
        "XAU/USD": "XAUUSD=X",
        "XAG/USD": "XAGUSD=X",
        "EUR/USD": "EURUSD=X",
        "GBP/USD": "GBPUSD=X",
        "USD/JPY": "JPY=X",
        "USD/CHF": "CHF=X",
        "USD/CAD": "CAD=X",
        "AUD/USD": "AUDUSD=X",
        "NZD/USD": "NZDUSD=X",
        "EUR/GBP": "EURGBP=X",
        "GBP/JPY": "GBPJPY=X",
        "EUR/JPY": "EURJPY=X",
        "AUD/JPY": "AUDJPY=X",
        "GBP/AUD": "GBPAUD=X",
        "BTC/USD": "BTC-USD",
        "ETH/USD": "ETH-USD"
    }
    yf_sym = symbol_map.get(symbol, symbol)
    try:
        df = yf.download(yf_sym, period="60d", interval=timeframe)
        df = df.rename(columns={"Open":"open", "High":"high", "Low":"low", "Close":"close", "Volume":"volume"})
        return df.reset_index()
    except Exception as e:
        print(f"Error fetching data for {symbol}: {e}")
        return None
