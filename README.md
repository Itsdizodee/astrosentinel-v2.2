# AstroSentinel V2 – Multi-Market AI Signal Bot

A modular, 24/7 Telegram bot for automated multi-market trading signals with technical + AI logic.

## Features

- Multi-market coverage: Forex, Crypto, Commodities
- Technical indicators: EMA, MACD, RSI, ATR
- LSTM AI for price prediction (placeholder; ready for later)
- Supports 15m, 1h, 4h timeframes
- Dynamic Stop-Loss & Take-Profit
- Telegram commands: `/start`, `/signals`, `/help`
- Clear, emoji-rich alerts with entry, SL, TP1, TP2, confidence
- Designed for Render deployment

## Folder Structure

```
/src
   indicators.py   # All indicator calculations
   ai_model.py     # LSTM training & prediction (stub)
   strategy.py     # Signal generation logic
   bot.py          # Telegram bot commands & message handling
   data_fetch.py   # Data downloads
/config
   settings.py     # Markets, timeframes, risk %
requirements.txt
Procfile
README.md
```

## How to Run

1. Clone this repo and `cd` inside.
2. Install dependencies:

   ```
   pip install -r requirements.txt
   ```

3. Set your Telegram Bot token as an environment variable:
   ```
   export TELEGRAM_TOKEN=YOUR-BOT-TOKEN
   ```

4. Start the bot:
   ```
   python -m src.bot
   ```

## Deploying to Render

- Connect your GitHub repo to Render, create a new Web Service.
- Set `TELEGRAM_TOKEN` as an environment variable.
- Procfile included, so Render will start the bot automatically.

---

**Future:** Add real LSTM logic, more markets, and advanced settings.
