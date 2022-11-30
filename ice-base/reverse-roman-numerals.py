def reverse_roman(roman):
    conver = [('CM', 'DCCCC'), ('M', 'DD'), ('CD', 'CCCC'), ('D', 'CCCCC'), ('XC', 'LXXXX'), ('C', 'LL'),
              ('XL', 'XXXX'), ('L', 'XXXXX'), ('IX', 'VIIII'), ('X', 'VV'), ('IV', 'IIII'), ('V', 'IIIII')]

    for a, b in conver:
        roman = roman.replace(a, b)

    count = 0
    for r in roman:
        count += 1

    return count


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert reverse_roman('VI') == 6, '6'
    assert reverse_roman('LXXVI') == 76, '76'
    assert reverse_roman('CDXCIX') == 499, '499'
    assert reverse_roman('MMMDCCCLXXXVIII') == 3888, '3888'
    print('Great! It is time to Check your code!');