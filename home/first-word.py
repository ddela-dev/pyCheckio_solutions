def first_word(text: str) -> str:
    """
    returns the first word in a given text.
    """
    # your code here
    text=text.replace(","," ")
    text=text.replace("."," ")
    words=text.split()
    first_word=""
    for i in words:
        if "." in i:
            continue
        else:
            first_word = i
            break
    return first_word


if __name__ == "__main__":
    print("Example:")
    print(first_word("... and so on ..."))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert first_word("Hello world") == "Hello"
    assert first_word(" a word ") == "a"
    assert first_word("don't touch it") == "don't"
    assert first_word("greetings, friends") == "greetings"
    assert first_word("... and so on ...") == "and"
    assert first_word("hi") == "hi"
    assert first_word("Hello.World") == "Hello"
    print("Coding complete? Click 'Check' to earn cool rewards!")
