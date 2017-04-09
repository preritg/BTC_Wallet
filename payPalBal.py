import requests
import datetime
import time
import balWriter

def payPalBalance(user, pwd, signature):
	payload = {
		"USER": user,
		"PWD": pwd,
		"SIGNATURE": signature,
		"VERSION": "190",
		"METHOD": "GetBalance",
		"RETURNALLCURRENCIES": 1
	}
	url = "https://api-3t.paypal.com/nvp"
	r = requests.post(url, data=payload)
	ts =  datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
	balance_str = r.text
	balance = balance_str[balance_str.index('AMT0=')+5:balance_str.index('&')].replace('%2e','.')
	#balance = balance_str
	balance = float(balance)
	accBalance = ['paypal', balance, 'fetch time', ts]
	accBalance = [str(ele) for ele in accBalance]
	return ','.join(accBalance)

payPalUser = 'cp03308_api1.georgiasouthern.edu'
payPalPwd = '9X724CDCRUB9E299'
payPalSignature = 'AFcWxV21C7fd0v3bYYYRCpSSRl31AjrAv.pT706V74LEj3.C8QHWPABN'

balWriter.balanceWriter('paypal', payPalBalance(payPalUser, payPalPwd, payPalSignature))