balance = 42
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
def pay_debt(balance, annualInterestRate, monthlyPaymentRate, month_number = 12):
    if month_number >0:
        up = balance - balance*monthlyPaymentRate
        M = up + annualInterestRate/12.0 * up
        pay_debt(M, annualInterestRate, monthlyPaymentRate, month_number-1)
    else:
        print("Remaining balance: {}".format(round(balance, 2)))
    




pay_debt(balance, annualInterestRate, monthlyPaymentRate)
