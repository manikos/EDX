bit=str(raw_input('Enter a binary number: '))
dec=0

for i in range(len(bit)):
    dec=dec+int(bit[i])*2**(len(bit)-(i+1))

print 'Decimal number of ' + str(bit) + ' is ' + str(dec)
