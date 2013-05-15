## If the numbers 1 to 5 are written out in words: one, two, three, four, five,
## then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

## If all the numbers from 1 to 1000 (one thousand) inclusive were written out
## in words, how many letters would be used?


## NOTE: Do not count spaces or hyphens. For example,
## 342 (three hundred and forty-two) contains 23 letters and
## 115 (one hundred and fifteen) contains 20 letters.
## The use of 'and' when writing out numbers is in compliance with British usage.

NUMBER_WORDS = {0:'', 1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six',\
                 7:'seven', 8:'eight', 9:'nine', 10:'ten', 11:'eleven',\
                 12:'twelve', 13:'thirteen', 14:'fourteen', 15:'fifteen',\
                 16:'sixteen', 17:'seventeen', 18:'eighteen', 19:'nineteen',\
                 20:'twenty', 40:'forty',70:'seventy', 80:'eighty',\
                100:'hundred', 1000:'thousand'}
count = 0
one_nine = 0
ten_nineteen = 0
decades = 0
for i in range(1, 100):
    if i < 10:
        one_nine += len(NUMBER_WORDS.get(i, 0))
    if i>=10 and i<20:
        ten_nineteen += len(NUMBER_WORDS.get(i, 0))
    if i >= 20 and i < 40:
        decades += len(NUMBER_WORDS[20]) + len(NUMBER_WORDS[i-]
