from lbcapi import api
import datetime
import time

def lbcBalance(lbcKey, lbcSecret):
    '''usage: from lbcapi import api 
    lbcBalance(key, secret)
    returns balance as float'''
    hmac_key = lbcKey
    hmac_secret = lbcSecret
    conn = api.hmac(hmac_key, hmac_secret)
    lbcBal = conn.call('GET', '/api/wallet-balance/').json()
    ts =  datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
    balance = lbcBal["data"]['total']['balance']
    coinBalance = ['localbtc', float(balance), 'fetch time', ts]
    coinBalance = [str(ele) for ele in coinBalance]
    return ','.join(coinBalance)