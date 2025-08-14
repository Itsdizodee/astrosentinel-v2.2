"""
Bot settings (markets, timeframes, risk %) for AstroSentinel V2.
"""
# Markets and pairs
MARKETS = [
    "EUR/USD", "GBP/USD", "USD/JPY", "USD/CHF", "USD/CAD", "AUD/USD", "NZD/USD",
    "EUR/GBP", "GBP/JPY", "EUR/JPY", "AUD/JPY", "GBP/AUD",
    "XAU/USD", "XAG/USD",
    "BTC/USD", "ETH/USD"
]

# Timeframes
TIMEFRAMES = ["15m", "1h", "4h"]

# Risk
RISK_PER_TRADE = 0.01  # 1% default
