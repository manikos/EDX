## If the numbers 1 to 5 are written out in words: one, two, three, four, five,
## then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

## If all the numbers from 1 to 1000 (one thousand) inclusive were written out
## in words, how many letters would be used?


## NOTE: Do not count spaces or hyphens. For example,
## 342 (three hundred and forty-two) contains 23 letters and
## 115 (one hundred and fifteen) contains 20 letters.
## The use of 'and' when writing out numbers is in compliance with British usage.

NUMBER_WORDS = {0:'zero', 1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six',\
                 7:'seven', 8:'eight', 9:'nine', 10:'ten', 11:'eleven',\
                 12:'twelve', 13:'thirteen', 14:'fourteen', 15:'fifteen',\
                 16:'sixteen', 17:'seventeen', 18:'eighteen', 19:'nineteen',\
                 20:'twenty', 30: 'thirty', 40:'forty',50:'fifty', 60:'sixty',\
                70:'seventy', 80:'eighty', 90:'ninety', 100:'hundred'}
count = 0
one_nine = 0
ten_nineteen = 0
decades = 0

def speech(n):
    num = str(n)
    global NUMBER_WORDS
    if n < 21:
        return NUMBER_WORDS[n]
    elif n >= 21 and n <= 99:
        if num[1] == '0':
            return NUMBER_WORDS[ int(num[0])*10 ]
        return NUMBER_WORDS[ int(num[0])*10 ] + ' ' + NUMBER_WORDS[int( num[1] )]
    else:
        if n % 100 == 0: return NUMBER_WORDS[int(num[0])] + ' ' + NUMBER_WORDS[100]
        if num[1] == '0':
            return NUMBER_WORDS[int(num[0])] + ' ' + NUMBER_WORDS[100] + ' and ' + NUMBER_WORDS[ int(num[2]) ]
        elif (int(num[1:]) % 10 == 0) or int(num[1:]) < 21:
            return NUMBER_WORDS[int(num[0])] + ' ' + NUMBER_WORDS[100] + ' and ' + NUMBER_WORDS[ int(num[1:]) ]
        else:
            return NUMBER_WORDS[int(num[0])] + ' ' + NUMBER_WORDS[100] + ' and' + NUMBER_WORDS[ int(num[1])*10 ] + ' ' + NUMBER_WORDS[int( num[2] )]
c = 0
for i in range(1, 1000):
    s = speech(i).split(' ')
    h = ''.join(s)
    c += len(h)
c += len('onethousand')
print c


## ANSWER = 21124
