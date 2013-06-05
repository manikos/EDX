gs_pwr=2
root=0
pwr=0

usr=int(raw_input('Enter an integer: '))

while gs_pwr<6:
    gs_root=0

    while gs_root**gs_pwr<usr:
        gs_root+=1
        
    if gs_root**gs_pwr==usr:
        root=gs_root
        pwr=gs_pwr
        
    gs_pwr+=1

if root==0:
    print 'No pair exists'
else:
    print 'Pair is: ' + 'root=' + str(root) + ' and ' + 'pwr= ' + str(pwr)
