import sys
import os

from smartConnect import SmartConnect

smartApi =SmartConnect(api_key="Your Api Key")

login = smartApi.generateSession('Your Client Id', 'Your Password')
print(login)
refreshToken = login['data']['refreshToken']
smartApi.getProfile(refreshToken)
smartApi.generateToken(refreshToken)
orderparams = {
    "variety": "NORMAL",
    "tradingsymbol": "SBIN-EQ",
    "symboltoken": "3045",
    "transactiontype": "BUY",
    "exchange": "NSE",
    "ordertype": "LIMIT",
    "producttype": "INTRADAY",
    "duration": "DAY",
    "price": "19500",
    "squareoff": "0",
    "stoploss": "0",
    "quantity": "1"
}
orderid = smartApi.placeOrder(orderparams)

modifyparams = {
    "variety": "NORMAL",
    "orderid": orderid,
    "ordertype": "LIMIT",
    "producttype": "INTRADAY",
    "duration": "DAY",
    "price": "19500",
    "quantity": "1",
    "tradingsymbol":"SBIN-EQ",
    "symboltoken":"3045",
    "exchange":"NSE"
}
smartApi.modifyOrder(modifyparams)

smartApi.cancelOrder(orderid, "NORMAL")

smartApi.orderBook()
smartApi.tradeBook()
smartApi.rmsLimit()
smartApi.position()
smartApi.holding()
exchange = "NSE"
tradingsymbol = "SBIN-EQ"
symboltoken = 3045
smartApi.ltpData("NSE", "SBIN-EQ", "3045")
params={
    "exchange": "NSE",
    "oldproducttype":"DELIVERY",
    "newproducttype": "MARGIN",
    "tradingsymbol": "SBIN-EQ",
    "transactiontype":"BUY",
    "quantity":1,
    "type":"DAY"

}

smartApi.convertPosition(params)
smartApi.terminateSession("Your Client Id")

from smartapi.smartSocket import SmartSocket
FEED_TOKEN="Your Feed Token"
CLIENT_CODE="Your Client Id"
token=None
ss = SmartSocket(FEED_TOKEN, CLIENT_CODE)
def on_tick(ws, tick):
    print("Ticks: {}".format(tick))
def on_connect(ws, response):
    a=ws.send_request(token)
    print("Back to Function",a)
def on_close(ws, code, reason):
    ws.stop()

# Assign the callbacks.
ss.on_ticks = on_tick
ss.on_connect = on_connect
ss.on_close = on_close

ss.connect( )


