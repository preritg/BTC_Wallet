import cbBal
import lbtcBal
import sys
import datetime
import time
import payPalBal
import bitfinBal

cbKey = 'MggWgfNwIp5sigzq'
cbSecret = 'Y7Knb9L6sJdLSOEHhqP36xhHz0iuEiY3'

hmac_key = 'e779a9c91a1f57749578207faae87af8'
hmac_secret = '3059b0f762f67e25e907fd3d862c954db616097411a165fef5c31d4209b7d79e'

payPalUser = 'cp03308_api1.georgiasouthern.edu'
payPalPwd = '9X724CDCRUB9E299'
payPalSignature = 'AFcWxV21C7fd0v3bYYYRCpSSRl31AjrAv.pT706V74LEj3.C8QHWPABN'

bitfinexKey = 'ktooMrGqsvxWEs0UVB3f0ZYOgafCESK1szs9KsbZ4Mq'
bitfinexSecret = b'x0axXXSMhjUCQLu7kZwmpqtHe8s7UOtuLFm62WkHYRR' #the b is deliberate, encodes to bytes



f = open(sys.argv[1], 'a')
try:
    #writer = csv.writer(f)
    #bal_list = [cbBal.coinbaseBalance(cbKey, cbSecret), 
    #           lbtcBal.lbcBalance(hmac_key, hmac_secret),
    #            payPalBal.payPalBalance(payPalUser, payPalPwd, payPalSignature)
    #            ]
    #ts = time.time()
    #st =  datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    #bal_list.append(st)
    #bal = ','.join(str(x) for x in bal_list)
    f.write(cbBal.coinbaseBalance(cbKey, cbSecret))
    f.write("\n")
    f.write(lbtcBal.lbcBalance(hmac_key, hmac_secret))
    f.write("\n")
    f.write(payPalBal.payPalBalance(payPalUser, payPalPwd, payPalSignature))
    f.write("\n")
    f.write(bitfinBal.bitfinexBal(bitfinexKey, bitfinexSecret))

    #f.write(bal)
    #f.write("\n")
    #writer.writerow(bal_list)
finally:
    f.close()
