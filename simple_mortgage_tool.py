"""
@Author: Jason Bauman
@Date: 12-26-2019
A Simple Mortgage Calculator
Testing what this looks like with a commit
"""


class MortgageSimple():
    """A simple mortgage tool using just loan, rate, and term"""
    def __init__(self,loan,rate,years):
        self.loan = loan
        self.rate = rate
        self.years = years

    def find_payment(self):
        #Will tell you what the expected mortgage payment is on that loan
        monthly_rate = self.rate / 100 / 12
        months = self.years * 12
        payment  = self.loan * ( (monthly_rate * (1+monthly_rate)**months) / (((1+monthly_rate)**months)-1))
        pay = str(round(payment,2))
        return pay

    def total_cost(self):
        #Will return the total cost of the loan over the term
        months = self.years * 12
        payment  = float(self.find_payment())
        total_paid = payment * months
        interest_paid = total_paid - self.loan
        paid = str(round(total_paid,2))
        return paid

    def snowball(self,extra_payment):
        #Still A WIP. Do Not Use (Yet)
        months = self.years * 12
        monthly_rate = self.rate / 100 / 12
        monthly_payment = float(self.find_payment())
        pass

    def remaining(self,months_paid):
        #Enter months_paid of how many months you've already paid on mortgage to get remaining balance
        months = self.years * 12
        monthly_rate = self.rate / 100 / 12
        monthly_payment = float(self.find_payment())
        remaining = self.loan * (((1+monthly_rate)**months-(1+monthly_rate)**months_paid) / ((1+monthly_rate)**months-1))
        remain = round(remaining,2)
        return remain

    def amortization_schedule(self):
        months = self.years * 12
        monthly_rate = self.rate / 100 / 12
        payment = float(self.find_payment())
        number = 1
        balance = self.loan
        while number <= months:
            interest = balance * monthly_rate
            principal = payment - interest
            balance = balance - principal
            interest = round(interest,2)
            principal = round(interest,2)
            simple_balance = round(balance,2)
            yield number, payment, interest, principal,simple_balance
            number += 1


    def summary(self):
        interest_paid = float(self.total_cost()) - self.loan
        interest = round(interest_paid,2)
        interest_final = interest
        #Prints out a summary of the loan, including total cost
        print(f'Total Loan amount:   ${self.loan}')
        print(f'Interest rate:       {self.rate}%')
        print(f'Monthly Payment:     $' + self.find_payment())
        print(f'Loan Term:           {self.years} Years')
        print(f'Total Cost:          $' + self.total_cost())
        print(f'Interest Paid:       ${interest_final}')

        print("This Is Your Amortization Schedule.")
        print("Month        Payment       Interest      Prinicipal       Balance")
        for x in self.amortization_schedule():
            print(f' {x[0]}          {x[1]}          {x[2]}          {x[3]}      {x[4]}')

if __name__ == '__main__':
    print("Welcome To the Simple Mortgage Calculator.")
    print("This Only Works With Fixed Rate Mortgages")
    a = 0
    b = 1
    c = 1
    while a == 0:
        try:
            print("Please enter a whole number, such as '400000'")
            loan_amount = input('How Much Is Your Loan For? ')
            loan_amount = int(loan_amount)
            a += 1
            b = 0
        except:
            print("If your loan is $350,000 please enter 350000")
            continue
    while b == 0:
        try:
            print("Please enter just the number, such as 4.13")
            annual_rate = input('What Is Your Annual Percentage Rate? ')
            annual_rate = float(annual_rate)
            b += 1
            c = 0
        except:
            print("You do not need to include the %")
            continue
    while c == 0:
        try:
            print("Please enter the number of years your mortgage is for")
            loan_term = input("How Long is your loan for?")
            loan_term = int(loan_term)
            c += 1
        except:
            print("Most loans would be either '30' or '15' years")
            continue
    test_mortgage = MortgageSimple(loan_amount,annual_rate,loan_term)
    test_mortgage.summary()
