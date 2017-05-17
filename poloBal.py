import poloniex
import requests
import json
import datetime
import time
import balWriter

def poloniexBalance(poloKey, poloSecret, accNum):
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
    coinBalance = ['poloniex'+accNum, 'income', balance, ts]
    coinBalance = [str(ele) for ele in coinBalance]
    return ','.join(coinBalance)

poloKey1 = 'GS3YLS7O-ZJF4EDR4-XICRGQ4H-HH8TSDKZ'
poloSecret1 = '95b1c3ff7467c757cba4a513ea5b7b9981261b0c3910ed6ae81cf020acd9637553257fe9ff726ff6d6e32311ef98f8da3482d1a32e817240b164fe8188752217'
balWriter.balanceWriter('poloniex1', poloniexBalance(poloKey1, poloSecret1,'1'))

poloKey2 = 'PKFFQLKB-XKX356OU-V4CDE3F7-B6DXTPB8'
poloSecret2 = '6404d2ef0144103182d72bcb11781917b9d4d6eca3134751ae80451164e47a6b0b75bbe0c2028c48456a96a113b8ed174ba3796102865476817b8347634ec15a'
balWriter.balanceWriter('poloniex2', poloniexBalance(poloKey2, poloSecret2,'2'))
