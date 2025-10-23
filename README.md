# Crypto-Trading-bot
Automated crypto trading bot built with Python and the Binance API. Features structured code design, order placement via CLI, logging of all API calls, and error handling for safer testnet trading. Ideal for developers exploring algorithmic trading systems.

# 🧠 Crypto Trading Bot (Binance Futures Testnet)

A Python-based automated trading bot built with the official **Binance API**.  
Supports **Market**, **Limit**, and **Stop-Limit** orders on the **Binance Futures Testnet (USDT-M)**.  
Includes structured code design, detailed logging, input validation, and robust error handling — perfect for developers exploring algorithmic trading systems.

---

## ⚙️ Features
-  Trade safely on Binance **Futures Testnet** (no real funds)
-  Supports **BUY** and **SELL** sides
-  Multiple order types:
  - Market  
  - Limit  
  - Stop-Limit *(optional bonus feature)*
-  Command-line interface for order input
-  Reusable modular class structure
-  Full API request/response logging
-  Exception & error handling for all trading operations

---

##  Tech Stack
- **Language:** Python 3.8+
- **Library:** [`python-binance`](https://github.com/sammchardy/python-binance)
- **Exchange:** Binance Futures Testnet (USDT-M)
- **Logging:** Built-in `logging` module

---

##  Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/<your-username>/binance-futures-trading-bot.git
cd binance-futures-trading-bot
