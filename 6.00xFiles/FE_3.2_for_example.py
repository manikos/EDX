s='1.23,2.34,3.456'
total=0
tmp=''

for i in range(len(s)):
    if s[i]!=',':
        tmp+=s[i]
    else:
        total+=float(tmp)
        tmp=''

print 'Total=' + str(total+float(tmp))



