def backward_string_by_word(text: str) -> str:
    words=text.split(" ")
    revtext=""
    for w in words:
        chars=list(w)
        chars.reverse()
        revword=""
        for c in chars:
            revword+=c
        if w == "":
            revtext+=" "
        else:
            revtext+=" "+revword
    revtext=revtext[1:]
    return revtext


if __name__ == '__main__':
    print("Example:")
    print(backward_string_by_word('hello   world'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert backward_string_by_word('') == ''
    assert backward_string_by_word('world') == 'dlrow'
    assert backward_string_by_word('hello world') == 'olleh dlrow'
    assert backward_string_by_word('hello   world') == 'olleh   dlrow'
    assert backward_string_by_word('welcome to a game') == 'emoclew ot a emag'
    print("Coding complete? Click 'Check' to earn cool rewards!")
