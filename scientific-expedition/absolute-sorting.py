def checkio(values: list) -> list:
    absvalues=values[:]
    for v in range(len(values)):
        absvalues[v]=abs(values[v])
    absvalues.sort()
    for i in range(len(absvalues)):
        if(-(absvalues[i]) in values):
            absvalues[i]=-(absvalues[i])
    return absvalues


if __name__ == '__main__':
    print("Example:")
    print(checkio([-20, -5, 10, 15]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert checkio([-20, -5, 10, 15]) == [-5, 10, 15, -20]
    assert checkio([1, 2, 3, 0]) == [0, 1, 2, 3]
    assert checkio([-1, -2, -3, 0]) == [0, -1, -2, -3]
    print("Coding complete? Click 'Check' to earn cool rewards!")
