def checkio(data):
    ROMANS = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD',
              100: 'C', 90: 'XC', 50: 'L', 40: 'XL',
              10: 'X', 9: 'IX', 5: 'V', 4: 'IV',
              1: 'I'}
    roman = ""
    num = int(data)
    print(num)
    while (num > 0):
        if (num - 1000 >= 0):
            num -= 1000
            roman += ROMANS[1000]
        elif (num - 900 >= 0):
            num -= 900
            roman += ROMANS[900]
        elif (num - 500 >= 0):
            num -= 500
            roman += ROMANS[500]
        elif (num - 400 >= 0):
            num -= 400
            roman += ROMANS[400]
        elif (num - 100 >= 0):
            num -= 100
            roman += ROMANS[100]
        elif (num - 90 >= 0):
            num -= 90
            roman += ROMANS[90]
        elif (num - 50 >= 0):
            num -= 50
            roman += ROMANS[50]
        elif (num - 40 >= 0):
            num -= 40
            roman += ROMANS[40]
        elif (num - 10 >= 0):
            num -= 10
            roman += ROMANS[10]
        elif (num - 9 >= 0):
            num -= 9
            roman += ROMANS[9]
        elif (num - 5 >= 0):
            num -= 5
            roman += ROMANS[5]
        elif (num - 4 >= 0):
            num -= 4
            roman += ROMANS[4]
        elif (num - 1 >= 0):
            num -= 1
            roman += ROMANS[1]

    return roman


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(6) == 'VI', '6'
    assert checkio(76) == 'LXXVI', '76'
    assert checkio(499) == 'CDXCIX', '499'
    assert checkio(3888) == 'MMMDCCCLXXXVIII', '3888'
    print('Done! Go Check!')