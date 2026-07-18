import argparse

from bot.orders import place_market, place_limit
from bot.validators import *

parser = argparse.ArgumentParser()

parser.add_argument("--symbol", required=True)
parser.add_argument("--side", required=True)
parser.add_argument("--type", required=True)
parser.add_argument("--quantity", required=True)
parser.add_argument("--price")

args = parser.parse_args()

try:

    side = validate_side(args.side)
    order_type = validate_order_type(args.type)
    quantity = validate_quantity(args.quantity)

    print("\nOrder Summary")
    print("----------------")
    print("Symbol :", args.symbol)
    print("Side   :", side)
    print("Type   :", order_type)
    print("Qty    :", quantity)

    if order_type == "LIMIT":
        print("Price  :", args.price)

    print()

    if order_type == "MARKET":

        response = place_market(
            args.symbol,
            side,
            quantity
        )

    else:

        if not args.price:
            raise ValueError("LIMIT orders require --price")

        response = place_limit(
            args.symbol,
            side,
            quantity,
            args.price
        )

    print("\nSUCCESS\n")

    print("Order ID :", response.get("orderId"))
    print("Status   :", response.get("status"))
    print("Executed :", response.get("executedQty"))
    print("AvgPrice :", response.get("avgPrice"))

except Exception as e:

    print("\nFAILED")
    print(e)
