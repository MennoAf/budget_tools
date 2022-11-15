'''
@Author: Jason Bauman
@Description: Scratch Pad to test concepts in Python for creating a financial tool
'''

import pandas as pd
import yfinance as yf
from datetime import datetime
import time

goal_key = {
    '401k' : 'Retirement',
    'ira' : 'Retirement',
    'nest_egg' : 'Taxable',
    'cash' : 'Emergency_Fund'
}


class LedgerBalance:
    
    def __init__(self) -> None:
        pass
    
    def get_goal(self,account):
        return goal_key(account.lower())
    
    def get_stock_price(self,ticker):
        if ticker == "CASH":
            return 1
        else:
            t = yf.Ticker(ticker)
            return t.info['previousClose']
    
    def buy_stock(self,account,ticker,price,value):
        timestamp = time.time()
        goal = self.get_goal(account)
        dictionary_update = {
            'timestamp': timestamp,
            'account': account,
            'goal': goal,
            'ticker' : ticker,
            'buy' : value,
            'transaction_type' : price,
            'share_changes' : price / value
        }
     
     # Need to identify how to add data to database based on time stamp to identify current value compared to what exists in database. 
     # Then need a way to query data, get the current number of shares by Stock Ticker to get prices and values
