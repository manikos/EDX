balance=1200
annualInterestRate=0.2

init=balance
minpaym=100

for month in range(12):
        munbal=round(balance-minpaym,2)
        minter=round(munbal*(annualInterestRate/12),2)
        balance=munbal+minter

while True:
    if balance>=0:
        balance=init
        minpaym+=10
        for month in range(12):
            munbal=round(balance-minpaym,2)
            minter=round(munbal*(annualInterestRate/12),2)
            balance=munbal+minter
    else:
        print 'Lowest Payment: ' + str(minpaym)
        break
