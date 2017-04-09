from coinbase.wallet.client import Client
import datetime
import time


def coinbaseBalance(cbKey, cbSecret):
    '''usage from coinbase.wallet.client import Client
    coinbaseBalance(KEY, SECRET)
    it returns balance in wallet currency as float'''
    api_key = cbKey
    api_secret = cbSecret
    client = Client(api_key, api_secret)
    accInfo = client.get_accounts()
    balance = accInfo['data'][0]['native_balance']['amount']
    ts =  datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
    coinBalance = ['coinbase', float(balance), 'fetch time', ts]
    coinBalance = [str(ele) for ele in coinBalance]
    return ','.join(coinBalance)
