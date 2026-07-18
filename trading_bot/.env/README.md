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
