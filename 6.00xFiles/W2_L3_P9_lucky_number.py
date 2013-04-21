print 'Please think of a number between 0 and 100!'

low=0
high=100
ans=(low+high)/2

print 'Is your secret number ' + str(int(ans)) + '?'
usr=raw_input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")

while usr!='c':
    if usr!='l' and usr!='h' and usr!='c':
        print 'Sorry, I did not understand your input.'
        print 'Is your secret number ' + str(int(ans)) + '?'
        usr=raw_input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
    elif usr=='l':
        low=ans
        ans=(low+high)/2
        print 'Is your secret number ' + str(int(ans)) + '?'
        usr=raw_input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
    elif usr=='h':
        high=ans
        ans=(low+high)/2
        print 'Is your secret number ' + str(int(ans)) + '?'
        usr=raw_input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
    else:
        break 

print 'Game over. Your secret number was: ' + str(int(ans))
