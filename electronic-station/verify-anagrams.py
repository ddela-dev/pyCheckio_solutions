def verify_anagrams(a, b):
    a = a.replace(' ', '')
    a = a.upper()
    la = []
    for i in a:
        la.append(i)
    la = sorted(la)
    a = ''
    for i in la:
        a += i

    b = b.replace(' ', '')
    b = b.upper()
    lb = []
    for i in b:
        lb.append(i)
    lb = sorted(lb)
    b = ''
    for i in lb:
        b += i

    return a == b


if __name__ == '__main__':
    print("Example:")
    print(verify_anagrams('Programming', 'Gram Ring Mop'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert verify_anagrams('Programming', 'Gram Ring Mop') == True
    assert verify_anagrams('Hello', 'Ole Oh') == False
    assert verify_anagrams('Kyoto', 'Tokyo') == True
    print("Coding complete? Click 'Check' to earn cool rewards!")
