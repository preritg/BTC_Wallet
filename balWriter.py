import sys
import datetime
import time

def balanceWriter(source, balance_str):
    filename = '/home/incogrev/BTC_Wallet/datafiles/' + source.lower() + 'Balance.csv'
    f = open(filename, 'w')
    try:
        f.write(balance_str)
        f.write('\n')
    finally:
        f.close()