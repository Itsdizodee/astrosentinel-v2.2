"""
Telegram bot for AstroSentinel V2.
Handles /start, /signals, /settings, and inline pair selection.
"""
import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes
from src.strategy import generate_signal
from src.data_fetch import get_data

TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN")

# Inline keyboard for trading pairs
def pairs_menu():
    keyboard = [
        [InlineKeyboardButton("EUR/USD", callback_data="EUR/USD"),
         InlineKeyboardButton("GBP/USD", callback_data="GBP/USD"),
         InlineKeyboardButton("USD/JPY", callback_data="USD/JPY")],
        [InlineKeyboardButton("USD/CHF", callback_data="USD/CHF"),
         InlineKeyboardButton("USD/CAD", callback_data="USD/CAD"),
         InlineKeyboardButton("AUD/USD", callback_data="AUD/USD")],
        [InlineKeyboardButton("NZD/USD", callback_data="NZD/USD")],
        [InlineKeyboardButton("EUR/GBP", callback_data="EUR/GBP"),
         InlineKeyboardButton("GBP/JPY", callback_data="GBP/JPY"),
         InlineKeyboardButton("EUR/JPY", callback_data="EUR/JPY")],
        [InlineKeyboardButton("AUD/JPY", callback_data="AUD/JPY"),
         InlineKeyboardButton("GBP/AUD", callback_data="GBP/AUD")],
        [InlineKeyboardButton("XAU/USD", callback_data="XAU/USD"),
         InlineKeyboardButton("XAG/USD", callback_data="XAG/USD")],
        [InlineKeyboardButton("BTC/USD", callback_data="BTC/USD"),
         InlineKeyboardButton("ETH/USD", callback_data="ETH/USD")]
    ]
    return InlineKeyboardMarkup(keyboard)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "👋 <b>Welcome to AstroSentinel V2 Multi-Market AI Signal Bot!</b>\n\n"
        "💹 <b>Available Trading Pairs</b>\n\n"
        "📊 <u>Major Forex</u>\n"
        "EUR/USD • GBP/USD • USD/JPY\n"
        "USD/CHF • USD/CAD • AUD/USD\n"
        "NZD/USD\n\n"
        "🎢 <u>High-Volatility</u>\n"
        "EUR/GBP • GBP/JPY • EUR/JPY\n"
        "AUD/JPY • GBP/AUD\n\n"
        "💰 <u>Commodities</u>\n"
        "XAU/USD (Gold) • XAG/USD (Silver)\n\n"
        "🪙 <u>Crypto</u>\n"
        "BTC/USD • ETH/USD\n\n"
        "⚡ Use /signals to get analysis"
    )
    await update.message.reply_text(text, parse_mode="HTML")

async def signals(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Show pairs menu
    await update.message.reply_text(
        "Select a pair for live signal:",
        reply_markup=pairs_menu()
    )

async def on_pair_selected(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    pair = query.data
    timeframe = "15m"  # Default, can be made dynamic

    # Fetch data
    df = get_data(pair, timeframe)
    if df is None or len(df) < 30:
        await query.answer("Not enough data for this pair.")
        return

    # Generate signal
    signal = generate_signal(df, pair, timeframe)
    if signal:
        msg = (
            f"🔔 <b>{signal['signal']} Signal – {signal['symbol']} ({signal['timeframe']})</b>\n"
            f"Entry: {signal['entry']}\n"
            f"SL: {signal['sl']}\n"
            f"TP1: {signal['tp1']}\n"
            f"TP2: {signal['tp2']}\n"
            f"Confidence: {signal['confidence']}%"
        )
    else:
        msg = "No clear signal for this pair currently."

    await query.edit_message_text(msg, parse_mode="HTML")

async def help_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Commands:\n"
        "/start – Introduction\n"
        "/signals – Latest active trades\n"
        "/help – Usage guide"
    )

def main():
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("signals", signals))
    app.add_handler(CommandHandler("help", help_cmd))
    app.add_handler(CallbackQueryHandler(on_pair_selected))
    app.run_polling()

if __name__ == "__main__":
    main()
