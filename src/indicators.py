"""
All technical indicator calculations for AstroSentinel V2.
"""
import ta

def add_ema(df, periods=[9, 21, 50, 200]):
    for p in periods:
        df[f'ema_{p}'] = ta.trend.ema_indicator(df['close'], window=p)
    return df

def add_macd(df):
    df['macd'] = ta.trend.macd(df['close'])
    df['macd_signal'] = ta.trend.macd_signal(df['close'])
    return df

def add_rsi(df, period=14):
    df['rsi'] = ta.momentum.rsi(df['close'], window=period)
    return df

def add_atr(df, period=14):
    df['atr'] = ta.volatility.average_true_range(df['high'], df['low'], df['close'], window=period)
    return df

def add_all_indicators(df):
    df = add_ema(df)
    df = add_macd(df)
    df = add_rsi(df)
    df = add_atr(df)
    return df
