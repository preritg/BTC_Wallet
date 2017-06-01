from lbcapi import api
import datetime
import time
import balWriter

def lbtcBalance(lbtcKey, lbtcSecret):
    '''usage: from lbcapi import api 
    lbcBalance(key, secret)
    returns balance as float'''
    hmac_key = lbtcKey
    hmac_secret = lbtcSecret
    conn = api.hmac(hmac_key, hmac_secret)
    lbcBal = conn.call('GET', '/api/wallet-balance/').json()
    ts =  datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
    balance = lbcBal["data"]['total']['balance']
    coinBalance = ['localbtc', 'income', float(balance), ts]
    coinBalance = [str(ele) for ele in coinBalance]
    return ','.join(coinBalance)


hmac_key = '<Key_Here>'
hmac_secret = '<Key_Here>'

balWriter.balanceWriter('localbitcoin', lbtcBalance(hmac_key, hmac_secret))
