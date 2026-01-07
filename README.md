# Multi-Timeframe Trading Strategy

A trading system that implements a multi-timeframe strategy using Python, with  backtesting  capabilities on Binance Testnet.

## Project Overview

This project implements a trading strategy that combines multiple timeframes (15-minute entries with 1-hour confirmations) to make trading decisions. The system includes backtesting capabilities using `backtesting.py` through Binance Testnet API.

### Key Features

- Multi-timeframe strategy implementation (15m entries, 1h confirmations)
- Comprehensive backtesting system with detailed trade logging
- Backtest trading integration with Binance Testnet
- Modular, class-based architecture for maintainability and extensibility

## Project Structure

```
├── README.md
├── requirements.txt
├── src/
│   ├── strategy/
│   │   ├── base.py        # Base strategy class
│   │   └── multi_tf.py    # Multi-timeframe strategy implementation
│   ├── backtesting/
│   │   ├── backtest.py    # Backtesting engine
│   │   └── analyzer.py    # Backtest results analysis
│   ├── trading/
│   │   ├── exchange.py    # Binance API wrapper
│   │   └── executor.py    # Trade execution logic
│   └── utils/
│       ├── logger.py      # Logging utilities
│       └── data.py        # Data handling utilities
└── data/
    ├── backtest_trades.csv    # Backtest trade logs
    └── live_trades.csv        # Live trading logs

```

## Strategy Details

The strategy combines signals from two timeframes:
- 15-minute timeframe for entry signals
- 1-hour timeframe for trade confirmation

Key components:
- Entry signals generated on 15m timeframe
- Trade confirmation using 1h timeframe indicators
- Risk management rules implemented at both timeframes

## Trade Logging

backtest trades are logged with:
- Timestamp
- Trade direction (long/short)
- Entry price
- Exit price
- Position size
- PnL
- Additional metadata

## Dependencies

Key packages used:
- backtesting.py
- python-binance
- pandas
- numpy
- talib 
