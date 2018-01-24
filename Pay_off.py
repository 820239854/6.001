balance = 4773
annualInterestRate = 0.2
def pay_debt(balance, annualInterestRate, monthlyPayment, month_number = 12):
    if month_number >0:
        up = balance - monthlyPayment
        M = up + annualInterestRate/12.0 * up
        return pay_debt(M, annualInterestRate, monthlyPayment, month_number-1)
    else:
        return balance

def pay_month(balance, annualInterestRate, monthlyPayment=10, month_number = 12):
    while pay_debt(balance, annualInterestRate, monthlyPayment) >0:
        monthlyPayment+=10
    print("Lowest Payment: {}".format(monthlyPayment))
    
    




pay_month(balance, annualInterestRate)


















