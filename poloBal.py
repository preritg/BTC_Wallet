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

poloKey = '<key_here>'
poloSecret = '<secret_key_here>'


balWriter.balanceWriter('poloniex', poloniexBalance(poloKey, poloSecret))
