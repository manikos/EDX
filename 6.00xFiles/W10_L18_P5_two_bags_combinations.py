def dec2ter(dec):
    """
    Converts a decimal number into a trenary form.

    returns: a list (trenary form of a decimal number)
    """
    quotient = dec/3
    remainder = dec%3
    if dec<3:
        return str(dec)
    elif quotient<3:
        return ''.join(str(quotient) + str(remainder))
    else:
        ternary = [remainder]
        while quotient>=3:
            remainder = quotient%3
            quotient = quotient/3
            ternary.append(remainder)
    ternary.append(quotient)
    ternary.reverse()
    return ''.join(str(e) for e in ternary)


####POWER-SET. COMBINATIONS OF N-ELEMENTS TO FIT IN 2 BAGS
def yieldAllCombos(items):
    """
    Given an items object (list, tuple, string), computes all
    the possible subsets (combinations) that can be formed in order
    to fit in 2 bags. That is, an element can be either inside the
    first bag (value=1) or the second (value=2) or nowhere (value=0).

    yields: a tuple which contains the subsets
    """
    length = len(items)
    combinations = 3**length
    for dec_number in range(combinations):
        first_bag, second_bag = [], []
        ternary = dec2ter(dec_number) #ternary is in form '012', or '1201' etc.
        if len(ternary) != length:
               ternary = '0'* (length - len(ternary)) + ternary
        for test in range(len(ternary)):
            if ternary[test]=='1':
                first_bag.append(items[test])
            elif ternary[test]=='2':
                second_bag.append(items[test])
        yield (first_bag, second_bag)
