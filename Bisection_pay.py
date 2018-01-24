balance = 999999
annualInterestRate = 0.18
from math import pow
month_interest = annualInterestRate/12.0
pay_low = balance/12
pay_upper = (balance*pow((1 + month_interest), 12))/12.0
def pay_debt(balance, annualInterestRate, monthlyPayment, month_number = 12):
    if month_number >0:
        up = balance - monthlyPayment
        M = up + annualInterestRate/12.0 * up
        return pay_debt(M, annualInterestRate, monthlyPayment, month_number-1)
    else:
        return balance

def pay_month(balance, annualInterestRate, pay_low, pay_upper, month_number = 12):
    monthlyPayment = (pay_low+pay_upper)/2
    if pay_upper - pay_low <= 0.01:
        if pay_debt(balance, annualInterestRate, monthlyPayment) > 0:
            return pay_upper
        else:
            return pay_low
    if pay_debt(balance, annualInterestRate, monthlyPayment) > 0:
        return pay_month(balance, annualInterestRate, monthlyPayment, pay_upper)
    elif pay_debt(balance, annualInterestRate, monthlyPayment) < 0:
        return pay_month(balance, annualInterestRate, pay_low, monthlyPayment)
    else:
        return monthlyPayment
    

print("Lowest Payment: {}".format( round(pay_month(balance, annualInterestRate, pay_low, pay_upper),2) ) )
