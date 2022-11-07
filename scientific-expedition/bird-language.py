def translate(text: str) -> str:
    vowels=['a','e','i','o','u','y']
    words=text.split()
    newtext=""
    skip=0
    chars=[]
    for w in words:
        chars.append(list(w))
    for letters in chars:
        newtext+=" "
        for l in letters:
            if(skip>0):
                skip-=1
                continue
            else:
                if(l in vowels):
                    newtext+=l
                    skip=2
                else:
                    newtext+=l
                    skip=1
    newtext=newtext[1:]
    return newtext


if __name__ == "__main__":
    print("Example:")
    print(translate("hoooowe yyyooouuu duoooiiine"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert translate("hieeelalaooo") == "hello"
    assert translate("hoooowe yyyooouuu duoooiiine") == "how you doin"
    assert translate("aaa bo cy da eee fe") == "a b c d e f"
    assert translate("sooooso aaaaaaaaa") == "sos aaa"
    print("Coding complete? Click 'Check' to earn cool rewards!")
