"""
Signal generation logic—combines technicals and AI model for AstroSentinel V2.
"""
from .indicators import add_all_indicators
from .ai_model import predict_lstm

def generate_signal(df, symbol, timeframe):
    df = add_all_indicators(df)
    # EMA logic
    ema_bull = df['ema_9'].iloc[-1] > df['ema_21'].iloc[-1]

    # MACD
    macd_bull = df['macd'].iloc[-1] > df['macd_signal'].iloc[-1]

    # RSI
    rsi = df['rsi'].iloc[-1]
    rsi_bull = 40 < rsi < 70
    rsi_bear = 30 < rsi < 60

    # AI prediction
    ai_trend = predict_lstm(df)

    # ATR for SL/TP
    price = df['close'].iloc[-1]
    atr = df['atr'].iloc[-1]

    # Bullish
    if ema_bull and macd_bull and rsi_bull and ai_trend == "UP":
        return {
            "symbol": symbol,
            "timeframe": timeframe,
            "signal": "BUY",
            "entry": round(price, 3),
            "sl": round(price - 1.5*atr, 3),
            "tp1": round(price + 1*atr, 3),
            "tp2": round(price + 2*atr, 3),
            "confidence": 85
        }
    # Bearish
    elif not ema_bull and not macd_bull and rsi_bear and ai_trend == "DOWN":
        return {
            "symbol": symbol,
            "timeframe": timeframe,
            "signal": "SELL",
            "entry": round(price, 3),
            "sl": round(price + 1.5*atr, 3),
            "tp1": round(price - 1*atr, 3),
            "tp2": round(price - 2*atr, 3),
            "confidence": 80
        }
    else:
        return None
