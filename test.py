# from tinkoff.invest import (
#     Client,
#     OrderDirection,
#     OrderExecutionReportStatus,
#     OrderType,
#     PostOrderResponse,
#     StopOrderDirection,
#     StopOrderExpirationType,
#     StopOrderType,
# )
# import json


# import json
# TOKEN = 't.raaqSpKAW7_TdXg0n6nuyKrTNGZ65ORDsOW9uWCH_zJX9KaSRwyT_wuuBZTpyRNe85M7Q8uKqV7UfKV0Dn541A'


# with Client(TOKEN) as client:
#     # print(client.users.get_info())
#     print(client.users.get_margin_attributes(account_id="2023246994").liquid_portfolio.units)
#     val=client.users.get_accounts()
#     # print((val))
#     # account_id=json.dumps(val, default=lambda o: o.__dict__ if hasattr(o, '__dict__') else str(o), indent=2)
#     # val=client.instruments.get_assets()

#     # json_data = json.dumps(val, default=lambda x: x.__dict__, ensure_ascii=False, indent=2)

#     # json_data=json.loads(json_data)

#     # ticker_figi_dict = {}
#     # for asset in json_data['assets']:
#     #     instruments = asset['instruments']
#     #     for instrument in instruments:
#     #         ticker = instrument['ticker']
#     #         figi = instrument['figi']
#     #         if ticker and figi:
#     #             ticker_figi_dict[ticker] = figi

#     # with open('figi.json', 'w') as file:
#     #     file.write(json.dumps(ticker_figi_dict))
#     # post_order_response: PostOrderResponse = client.orders.post_order(
#     # quantity=1,
#     # direction=OrderDirection.ORDER_DIRECTION_SELL,
#     # order_type=OrderType.ORDER_TYPE_MARKET,
#     # figi="BBG004730N88",
#     # account_id="2023246994"
#     # )
#     # print(post_order_response)

test="hello"
print(test.upper())