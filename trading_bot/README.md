Include:

Setup
git clone ...
cd trading_bot

python -m venv venv

source venv/bin/activate

pip install -r requirements.txt

Create .env

API_KEY=...
API_SECRET=...

Run:

python cli.py ...
Expected Output
Order Summary

Symbol : BTCUSDT
Side : BUY
Type : MARKET
Qty : 0.001

SUCCESS

Order ID : 874920183
Status : FILLED
Executed : 0.001
AvgPrice : 118430.20
Logging

Example:

2026-07-18 12:45:21 INFO MARKET Request BTCUSDT BUY 0.001

2026-07-18 12:45:22 INFO {
    "orderId":382910,
    "status":"FILLED",
    ...
}
Bonus (recommended)

Since they only ask for one optional enhancement, the easiest high-impact choice is an enhanced CLI using Typer:

Colored success/error messages.
Interactive prompts when arguments are missing.
Better validation messages.

This takes about 10–15 minutes and makes the project feel much more polished than a plain argparse script.
