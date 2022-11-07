def checkio(words: str) -> bool:
    wl = words.split()
    wc = 0
    trio = False
    for w in wl:
        try:
            int(w)
            wc = 0
        except:
            wc += 1
            if wc == 3:
                trio = True

    return trio


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print('Example:')
    print(checkio("Hello World hello"))

    assert checkio("Hello World hello") == True, "Hello"
    assert checkio("He is 123 man") == False, "123 man"
    assert checkio("1 2 3 4") == False, "Digits"
    assert checkio("bla bla bla bla") == True, "Bla Bla"
    assert checkio("Hi") == False, "Hi"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
