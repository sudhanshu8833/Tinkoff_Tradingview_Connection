# # api key = 1965c6a0d81462b672508f92e8b4772281a99a17
# # acc id = Z4SJOT
# # username = sudhanshu_testing
# # password = Sudhanshu123

# import oandapyV20
# import oandapyV20.endpoints.instruments as instruments
# import oandapyV20.endpoints.pricing as pricing
# import oandapyV20.endpoints.accounts as accounts
# import oandapyV20.endpoints.orders as orders
# import oandapyV20.endpoints.trades as trades




# accesstoken="b4ba4a8e460a1265faaefc69ea4d4f94-8c0f1a647590f483f36ff495b9f6f5d6"

# client = oandapyV20.API(access_token=str(accesstoken))
# instrument="US500_USD"



# account_id = "101-003-21121032-001"

# params = {"instruments": str(instrument)}
# r = pricing.PricingInfo(accountID=account_id, params=params)
# rv = client.request(r)

# print(rv)


# data = {
#         "order": {

#         "timeInForce": "FOK",
#         "instrument":params,
#         "units": "1",
#         "type": "MARKET",
#         "positionFill": "DEFAULT"
#                 }
#         }

# r = orders.OrderCreate(accountID=account_id, data=data)
# rv=client.request(r)
# print(rv)

import oandapyV20.endpoints.instruments as instruments
import oandapyV20
import oandapyV20.endpoints.orders as orders
import oandapyV20.endpoints.pricing as pricing
# from oandapyV20.contrib.requests import MarketOrderRequest
import pprint
pp = pprint.PrettyPrinter(indent=4)
# Your OANDA account details
account_id = "101-003-21121032-001"
# access_token = "b4ba4a8e460a1265faaefc69ea4d4f94-8c0f1a647590f483f36ff495b9f6f5d6"
access_token="b4ba4a8e460a1265faaefc69ea4d4f94-8c0f1a647590f483f36ff495b9f6f5d6"
stop_loss_pips=25

api = oandapyV20.API(access_token=access_token,environment="practice")

# Define your trade parameters
instrument = "SPX500_USD"  # Instrument for US SPX 500
units = 1  # Number of units to trade



# Get the current market price
params = {
    "instruments": instrument
}
r = pricing.PricingInfo(accountID=account_id, params=params)
api.request(r)
price = r.response['prices'][0]['bids'][0]['price']  # Assuming you're interested in the bid price
# pp.pprint(price)
# Create a Market Order Request

# stop_loss_price = round(float(price) - stop_loss_pips * 1,1)


# market_order_data = {
#     "order": {
#         "type": "MARKET",
#         "instrument": instrument,
#         "units": units,
#         "timeInForce": "FOK",
#         "stopLossOnFill": {
#             "price": str(stop_loss_price)
#         },
#     }
# }

# # mo = MarketOrderRequest(data=market_order_data)

# # Send the order to OANDA
# r = orders.OrderCreate(accountID=account_id, data=market_order_data)
# data=api.request(r)
# pp.pprint(data)

# Check the response to ensure the order was successful
# if r.status_code == 201:
#     print("Order successfully executed!")
# else:
#     print(f"Error placing order: {r.status_code} - {r.reason}")

