def goes_after(word: str, first: str, second: str) -> bool:
    if (first in word):
        chars = list(word)
        for c in chars:
            if c == first:
                can = True
                break
            elif c == second:
                can = False
                break
        if can:
            for c in range(len(chars)):
                if (chars[c] == first):
                    try:
                        if (chars[c + 1] == second):
                            return True
                        else:
                            return False
                    except:
                        return False
        else:
            return False

    else:
        return False


if __name__ == "__main__":
    print("Example:")
    print(goes_after("world", "l", "o"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert goes_after("world", "w", "o") == True
    assert goes_after("world", "w", "r") == False
    assert goes_after("world", "l", "o") == False
    assert goes_after("panorama", "a", "n") == True
    assert goes_after("list", "l", "o") == False
    assert goes_after("", "l", "o") == False
    assert goes_after("list", "l", "l") == False
    assert goes_after("world", "d", "w") == False
    assert goes_after("transport", "r", "t") == False
    print("Coding complete? Click 'Check' to earn cool rewards!")
