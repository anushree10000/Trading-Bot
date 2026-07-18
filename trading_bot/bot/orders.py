from bot.client import client
from bot.logging_config import logger


def place_market(symbol, side, quantity):
    try:

        logger.info(f"MARKET Request: {symbol} {side} {quantity}")

        response = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="MARKET",
            quantity=quantity
        )

        logger.info(response)

        return response

    except Exception as e:
        logger.error(str(e))
        raise


def place_limit(symbol, side, quantity, price):

    try:

        logger.info(
            f"LIMIT Request: {symbol} {side} {quantity} {price}"
        )

        response = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="LIMIT",
            quantity=quantity,
            price=price,
            timeInForce="GTC"
        )

        logger.info(response)

        return response

    except Exception as e:

        logger.error(str(e))
        raise
