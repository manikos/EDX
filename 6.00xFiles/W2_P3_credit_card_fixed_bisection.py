balance=999999
annualInterestRate=0.18

init=balance
minpaymL=balance/12.0
totalmpaym=0

for month in range(12):
        munbal=round(balance-minpaymL,2)
        minter=round(munbal*(annualInterestRate/12),2)
        balance=munbal+minter

minpaymH=balance
print '*minpaymL=' + str(minpaymL)
print '*Balance=' + str(balance)

while abs(balance)>0.1:
        minpaym=(minpaymL+minpaymH)/2.0
        balance=init
        totalmpaym=0
        for month in range(12):
            munbal=round(balance-minpaym,2)
            totalmpaym+=minpaym
            minter=round(munbal*(annualInterestRate/12),2)
            balance=munbal+minter
        print 'minpaym=' + str(minpaym) + '   Diafora=' + str(totalmpaym-balance) + '   Balance=' + str(balance)
        print 'Totalmpaym=' + str(totalmpaym)
        if balance<0:
                minpaymH=minpaym
                #print 'IF:minpaymH='+str(minpaymH)
        else:
                minpaymL=minpaym
                #print 'ELSE:minpaymL='+str(minpaymL)

print 'Lowest Payment: ' + str(round(minpaym,5))
