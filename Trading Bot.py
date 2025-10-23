import logging
from binance.client import Client
from binance.enums import *
from binance.exceptions import BinanceAPIException, BinanceOrderException
import sys


# Logging Setup

logging.basicConfig(
    filename='trading_bot.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

#Bot class
class BasicBot:
    def __init__(self, api_key, api_secret, testnet=True):
        self.client = Client(api_key, api_secret, testnet=testnet)
        if testnet:
            self.client.API_URL = 'https://testnet.binancefuture.com/fapi/v1'

    def place_order(self, symbol, side, order_type, quantity, price=None, stop_price=None):
        """
        Place an order on Binance Futures.
        :param symbol: trading pair e.g., 'BTCUSDT'
        :param side: 'BUY' or 'SELL'
        :param order_type: 'MARKET', 'LIMIT', 'STOP_LIMIT'
        :param quantity: order size
        :param price: required for LIMIT and STOP_LIMIT
        :param stop_price: required for STOP_LIMIT
        """
        try:
            if order_type == 'MARKET':
                order = self.client.futures_create_order(
                    symbol=symbol,
                    side=side,
                    type=ORDER_TYPE_MARKET,
                    quantity=quantity
                )
            elif order_type == 'LIMIT':
                order = self.client.futures_create_order(
                    symbol=symbol,
                    side=side,
                    type=ORDER_TYPE_LIMIT,
                    timeInForce=TIME_IN_FORCE_GTC,
                    quantity=quantity,
                    price=price
                )
            elif order_type == 'STOP_LIMIT':
                order = self.client.futures_create_order(
                    symbol=symbol,
                    side=side,
                    type=ORDER_TYPE_STOP,
                    quantity=quantity,
                    price=price,
                    stopPrice=stop_price,
                    timeInForce=TIME_IN_FORCE_GTC
                )
            else:
                logging.error(f"Invalid order type: {order_type}")
                return None

            logging.info(f"Order placed: {order}")
            print("Order successful:", order)
            return order

        except BinanceAPIException as e:
            logging.error(f"API Exception: {e}")
            print(f"API Error: {e}")
        except BinanceOrderException as e:
            logging.error(f"Order Exception: {e}")
            print(f"Order Error: {e}")
        except Exception as e:
            logging.error(f"Unexpected error: {e}")
            print(f"Unexpected Error: {e}")

# CLI for User Input

def run_bot():
    api_key = input("Enter your Binance API Key: ")
    api_secret = input("Enter your Binance API Secret: ")

    bot = BasicBot(api_key, api_secret)

    while True:
        print("\n--- New Order ---")
        symbol = input("Enter symbol (e.g., BTCUSDT): ").upper()
        side = input("Enter side (BUY/SELL): ").upper()
        order_type = input("Enter order type (MARKET/LIMIT/STOP_LIMIT): ").upper()
        quantity = float(input("Enter quantity: "))

        price = None
        stop_price = None
        if order_type in ['LIMIT', 'STOP_LIMIT']:
            price = float(input("Enter price: "))
        if order_type == 'STOP_LIMIT':
            stop_price = float(input("Enter stop price: "))

        bot.place_order(symbol, side, order_type, quantity, price, stop_price)

        cont = input("Place another order? (y/n): ").lower()
        if cont != 'y':
            break

if __name__ == "__main__":
    run_bot()
