import poloniex
import requests
import json
import datetime
import time
import balWriter

def poloniexBalance(poloKey, poloSecret):
    ''' Usage import poloniex
    poloniexBalance(key, secret)
    '''
    poloniex.Poloniex.nonce = time.time() * 1000099990
    polo = poloniex.Poloniex()
    polo.Key = poloKey
    polo.Secret = poloSecret
  
    #ticker = polo.returnTicker()
    walletBal = polo.returnCompleteBalances()
    currBTCPrice = requests.get('http://api.coindesk.com/v1/bpi/currentprice.json')
    ts =  datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')

    price_json = currBTCPrice.json()
    btc_price = price_json['bpi']['USD']['rate_float']

    balance = float(walletBal['BTC']['btcValue'])*btc_price
    coinBalance = ['poloniex', 'income', balance, ts]
    coinBalance = [str(ele) for ele in coinBalance]
    return ','.join(coinBalance)

poloKey = 'GS3YLS7O-ZJF4EDR4-XICRGQ4H-HH8TSDKZ'
poloSecret = '95b1c3ff7467c757cba4a513ea5b7b9981261b0c3910ed6ae81cf020acd9637553257fe9ff726ff6d6e32311ef98f8da3482d1a32e817240b164fe8188752217'


balWriter.balanceWriter('poloniex', poloniexBalance(poloKey, poloSecret))
