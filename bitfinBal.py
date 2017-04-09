#!/usr/bin/env python3
import requests
import json
import base64
import hashlib
import time
import hmac
import datetime

bitfinexURL = 'https://api.bitfinex.com/v1/balances'

#print("BitFinex")

def bitfinexBal(key, secret):
    bitfinexKey = key
    bitfinexSecret = secret
    payloadObject = {
        'request':'/v1/balances',
        'nonce':str(time.time() * 100000), #convert to string
        'options':{}
        }
    payload_json = json.dumps(payloadObject)
    #print("payload_json: ", payload_json)
    
    payload = base64.b64encode(bytes(payload_json, "utf-8"))
    #print("payload: ", payload)

    m = hmac.new(bitfinexSecret, payload, hashlib.sha384)
    m = m.hexdigest()
    
    #headers
    headers = {
        'X-BFX-APIKEY' : bitfinexKey,
        'X-BFX-PAYLOAD' : base64.b64encode(bytes(payload_json, "utf-8")),
        'X-BFX-SIGNATURE' : m
        }
    
    r = requests.get(bitfinexURL, data={}, headers=headers)
    #print('Response Code: ' + str(r.status_code))
    #print('Response Content: '+ str(r.content))
    
    currency_json = r.json()
    currency_list = []
    for ele in currency_json:
        currency_list.append({ele["currency"].upper():float(ele["amount"])})

    coin_list = {}
    for ele in currency_dict:
        for key in ele:
            if key in coin_list.keys():
                coin_list[key] += ele[key]
            else:
                coin_list[key] = ele[key]

    ticker_url = 'https://api.bitfinex.com/v1/pubticker/'
    wallet_balance = {}

    ts =  datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')

    for coin in coin_list:
        if coin!= 'USD':
            #last_price = float(requests.get(ticker_url+coin.lower()+'usd', data={}, headers=headers).json()['last_price'])
            last_price = float(requests.get(ticker_url+coin.lower()+'usd', data={}, headers=headers).json()['bid'])
            wallet_balance[coin] = coin_list[coin]*last_price
            #print(coin, ':', last_price)
        else:
            wallet_balance[coin] = coin_list[coin]
            #print(coin, ':', 1)
    balance = sum(wallet_balance.values())
    #print (sum(wallet_balance.values()))
    coinBalance = ['bitfinex', balance, ts]
    return ','.join(coinBalance)