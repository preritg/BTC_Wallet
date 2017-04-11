
# coding: utf-8

# In[174]:

import pandas as pd
import datetime as dt
import os, sys


# In[175]:

path = '/home/incogrev/BTC_Wallet/datafiles/'
dirs = os.listdir(path)
#dirs


# In[176]:

#reading all files' last record into a dataframe
dropCSV_list = ['expense.csv', 'rollingpnl.csv']

for file in dropCSV_list:
    if file in dirs:
        dirs.pop(dirs.index(file))        

dfRevenue = pd.DataFrame()
for file in dirs:
    rec = pd.read_csv(path+file).tail(1).fillna(0)
    dfRevenue = pd.concat([dfRevenue, rec])

revenue_col = ['source', 'balance', 'timestamp']
dfRevenue = dfRevenue[revenue_col]
dfRevenue = dfRevenue.reset_index(drop=True)
print("\nRevenue")
print(dfRevenue)


# In[177]:

dfRevenue['timestamp'] = pd.to_datetime(dfRevenue['timestamp'])
dfRevenue['date']  = dfRevenue['timestamp'].dt.date

dictRevenue = { 'revenue':[sum(dfRevenue['balance'],)], 'date': [max(dfRevenue['date']),]}
dfIncome = pd.DataFrame(dictRevenue)

#dictRevenue
#print("Total Revenue")
#dfIncome


# In[179]:

dfExpense = pd.read_csv(path+'expense.csv').tail(1).fillna(0)
print("\nExpenses")
print(dfExpense)


# In[180]:

dictTransaction = {'expense':[sum(dfExpense['investor_capital']+dfExpense['general_ledger']+dfExpense['customer_loans']),], 
                   'date': [max(dfExpense['date']),]}
dfTransaction = pd.DataFrame(dictTransaction)
dfTransaction['date'] = pd.to_datetime(dfTransaction['date'])
dfTransaction['date'] = dfTransaction['date'].dt.date
#print("Total Expenses")
#dfTransaction


# In[181]:

dfPnL = dfTransaction
dfPnL = dfPnL.merge(dfIncome, on = 'date')
dfPnL['PnL'] = dfPnL['revenue'] - dfPnL['expense']
#print("P/L Statement")
#dfPnL


# In[182]:

existingPnL = pd.read_csv(path+'rollingpnl.csv').fillna(0)
existingPnL['date'] = pd.to_datetime(existingPnL['date'])
existingPnL['date'] = existingPnL['date'].dt.date


# In[183]:

existingPnL = existingPnL[~existingPnL.date.isin(dfPnL.date)]


# In[184]:

existingPnL = pd.concat([existingPnL, dfPnL]).fillna(0)


# In[185]:

col_list = ['date', 'revenue', 'expense', 'PnL']
existingPnL = existingPnL[col_list]
existingPnL = existingPnL.sort_values(by = 'date').reset_index(drop = True)


# In[186]:

existingPnL['30DayRollingAvg'] = existingPnL['PnL'].rolling(window = 30).mean()


# In[187]:
print("\nP/L Statement")
print(existingPnL.tail(1))


# In[188]:

existingPnL.to_csv(path_or_buf= path + 'rollingpnl.csv')