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

poloKey1 = '<Key_Here>'
poloSecret1 = '<Key_Here>'
balWriter.balanceWriter('poloniex1', poloniexBalance(poloKey1, poloSecret1,'1'))

poloKey2 = '<Key_Here>'
poloSecret2 = '<Key_Here>'
balWriter.balanceWriter('poloniex2', poloniexBalance(poloKey2, poloSecret2,'2'))
