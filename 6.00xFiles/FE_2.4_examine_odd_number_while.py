x=[]
i=0
nul=0
while (i<10):
    x.insert(i,raw_input('Enter number: '))
    if int(x[i])%2==0:
        nul=nul+1
    i=i+1

y=[]
i=0
j=0
while (i<10):
    if int(x[i])%2!=0:
        y.insert(j,x[i])
    i=i+1

#pleon exo ston j[] ola ta mona noumera

i=0
maxi=0
while (i<len(y)):
    if int(y[i])>maxi:
        maxi=int(y[i])
    i=i+1


if nul==10:
    print 'No odd number entered'
else:
    print 'Maximum odd value is: ' + str(maxi)
        
