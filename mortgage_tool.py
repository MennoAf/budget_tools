"""
@Author: Jason Bauman
@Date: 08-05-21

Just a simple mortgage tool.
"""
import pandas as pd
#import datetime

#find expected mortgage payment
#Create amortization calculator
#display the total cost of a loan (15 and 30 year?)
#Refinance option (Current amount, current term and rate, new term and rate, new assesment, break even)
#Graph of paydown (interest, principal, equity)
#snowball (extra money + target date)
#Allow it to compare 30 to 15 year and give summary savings
#Export results to 

####Demo figures dont change
apy = 3.14
term = 30
###End of Demo

class mortgageSimple:
    """Because I need to make everything a class. This will help simplify things"""



    def __init__(self,home_value,loan_amount,home_name):
        self.home_value = home_value
        self.loan_amount = loan_amount
        self.home_name = home_name



    def find_payment(self,apy,term):
        """Find the Monthly Payment on a mortgage"""
        #Will tell you what the expected mortgage payment is on that loan
        monthly_rate = apy / 100 / 12
        months = term * 12
        payment  = self.loan_amount * ( (monthly_rate * (1+monthly_rate)**months) / (((1+monthly_rate)**months)-1))
        pay = str(round(payment,2))
        return pay




    def amortization(self,apy,term):
        pass

    def total_cost():
        pass

    def refinance():
        pass

    def visualize():
        pass

    def snowball_payment():
        pass

    def snowball_target():
        pass


    def build_report():
        pass