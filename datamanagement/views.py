import logging
from django.http import HttpResponse,JsonResponse

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json
import traceback


# Create your views here.
from django.contrib import messages
import threading
import random
import string
from .models import *
import time
from datetime import datetime, date
from tinkoff.invest import (
    Client,
    OrderDirection,
    OrderExecutionReportStatus,
    OrderType,
    PostOrderResponse,
    StopOrderDirection,
    StopOrderExpirationType,
    StopOrderType,
)

errors=[]
logger = logging.getLogger('dev_log')

def place_order(client, admin,data,account_id):
    global position_opened

    try:
        figi={}
        with open("datamanagement/figi.json","r") as json_file:
            figi=json.load(json_file)

        if True:
            if data['order_type'].upper()=="BUY":
                post_order_response: PostOrderResponse = client.orders.post_order(
                    quantity=int(data['quantity']),
                    direction=OrderDirection.ORDER_DIRECTION_BUY,
                    order_type=OrderType.ORDER_TYPE_MARKET,
                    figi=figi[data["symbol"]],
                    account_id=account_id
                )
                # print(post_order_response)
                return str(post_order_response)
            else:
                post_order_response: PostOrderResponse = client.orders.post_order(
                    quantity=int(data['quantity']),
                    direction=OrderDirection.ORDER_DIRECTION_SELL,
                    order_type=OrderType.ORDER_TYPE_MARKET,
                    figi=figi[data["symbol"]],
                    account_id=account_id
                )

                return str(post_order_response)

    except Exception:

        # if str(str(traceback.format_exc())) not in errors:
        logger.info(str(traceback.format_exc()))
        errors.append(str(traceback.format_exc()))
        return str(traceback.format_exc())

        



@csrf_exempt
def tradingview_webhook(request):
    try:

        '''
        {
            "TOKEN":"t.raaqSpKAW7_TdXg0n6nuyKrTNGZ65ORDsOW9uWCH_zJX9KaSRwyT_wuuBZTpyRNe85M7Q8uKqV7UfKV0Dn541A",
            "account_id":"2023246994",
            "symbol":"RTO",
            "quantity":"1",
            "order_type":"BUY",
            "passphrase":";jfkjadweumxn",
            "price":"2187"
        }
        '''
        data = json.loads(request.body.decode("utf-8"))
        logger.info(str(data))
        logger.info(type(data))
        if request.method == "POST":        
            admin=Admin.objects.all()[0]
            passphrase=data['passphrase']
            pp = str(passphrase)
            data['Order_id']=[]
            with Client(data["TOKEN"]) as client:

                account_balance=int(client.users.get_margin_attributes(account_id=data["account_id"]).liquid_portfolio.units)
                trade=(float(data['trade'])/100)*account_balance
                data['quantity']=int(int(trade/float(data['price']))/int(data['lot_size']))

                if(data['quantity']==0):
                    return JsonResponse({"error":"quantity is coming out to be zero"})


                if pp== admin.paraphrase:
                    
                    stock=data['symbol']
                    price=data['price']

                    record=positions(symbol=stock,time=datetime.now(),price=price,order_type=data['order_type'])
                    record.save()

                    if(admin.status==True):
                        try:
                            id=place_order(client,admin,data,data['account_id'])
                            data['Order_id'].append(id)
                            logger.info(data)
                        except Exception:

                            logger.info(str(traceback.format_exc()))
                            errors.append(str(traceback.format_exc()))

                    return JsonResponse(data)

                else:
                    return JsonResponse({"error":"passphrase is wrong"})

        return JsonResponse({"error":"send a valid post request"})
        
    except Exception:

        logger.info(str(traceback.format_exc()))
        errors.append(str(traceback.format_exc()))
        return JsonResponse({"error":str(traceback.format_exc())})


