balance=4842
annualInterestRate=0.2
monthlyPaymentRate=0.04

total_paym=0

for month in range(12):
    minpaym=round(balance*monthlyPaymentRate,2)
    total_paym+=minpaym
    munbal=round(balance-minpaym,2)
    minter=round(munbal*(annualInterestRate/12),2)
    balance=munbal+minter

    print 'Month: ' + str(month+1)
    print 'Minimum monthly payment: ' + str(minpaym)
    print 'Remaining balance: ' + str(balance)

print 'Total paid: ' + str(total_paym)
print 'Remaining balance: ' + str(balance)
