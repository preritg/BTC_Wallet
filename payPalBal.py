import requests
import datetime
import time

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
