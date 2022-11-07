def checkio(line1: str, line2: str) -> str:
    words1=line1.split(",")
    words2=line2.split(",")
    common=[]
    both=""
    for w in words1:
        if w in words2:
            common.append(w)
    common.sort()
    for c in common:
        both+=","+c
    return both[1:]


if __name__ == '__main__':
    print("Example:")
    print(checkio('one,two,three',
 'four,five,one,two,six,three'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert checkio('hello,world', 'hello,earth') == 'hello'
    assert checkio('one,two,three', 'four,five,six') == ''
    assert checkio('one,two,three',
 'four,five,one,two,six,three') == 'one,three,two'
    print("Coding complete? Click 'Check' to earn cool rewards!")
