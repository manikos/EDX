x=input("Enter a number for x: ")
y=input("Now enter a number for y: ")
z=input("Finally enter a number for z: ")

if x%2!=0 and y%2==0 and z%2==0:
    print str(x) + ' is the greater odd number'
elif y%2!=0 and x%2==0 and z%2==0:
    print str(y) + ' is the greater odd number'
elif z%2!=0 and x%2==0 and y%2==0:
    print str(z) + ' is the greater odd number'

if x%2!=0 and y%2!=0 and z%2!=0:
    if x>y and x>z:
        print str(x) + ' is the greatest odd number1'
    if y>x and y>z:
        print str(y) + ' is the greatest odd number2'
    else:
        print str(z) + ' is the greatest odd number3'
elif x%2!=0 and y%2!=0 and z%2==0:
    if x>y:
        print str(x) + ' is the greatest odd number4'
    else:
        print str(y) + ' is the greatest odd number5'
elif x%2!=0 and y%2==0 and z%2!=0:
    if x>z:
        print str(x) + ' is the greatest odd number6'
    else:
        print str(z) + ' is the greatest odd number7'
elif x%2==0 and y%2!=0 and z%2!=0:
    if y>z:
        print str(y) + ' is the greatest odd number8'
    else:
        print str(z) + ' is the greatest odd number9'
elif x%2==0 and y%2==0 and z%2==0:
    print 'None of the above numbers are odd0'
