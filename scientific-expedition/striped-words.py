def checkio(line: str) -> str:
    line=line.upper()
    vows=['A', 'E', 'I', 'O', 'U', 'Y']
    cons=['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Z']
    line=line.replace(',',' ')
    line=line.replace('.',' ')
    line=line.replace('?',' ')
    line=line.replace(';',' ')
    words=line.split()
    striped=0
    for w in words:
        isStriped=False
        if len(w)>1 and w.isalpha():
            isStriped=True
            nextvow = False
            if w[0] in vows:
                nextvow=True
            for c in w:
                if nextvow:
                    if c in vows:
                        nextvow=False
                    else:
                        isStriped=False
                else:
                    if c in cons:
                        nextvow=True
                    else:
                        isStriped=False
        if isStriped:
            striped+=1
    return striped


if __name__ == '__main__':
    print("Example:")
    print(checkio('Dog,cat,mouse,bird.Human.'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert checkio('My name is ...') == 3
    assert checkio('Hello world') == 0
    assert checkio('A quantity of striped words.') == 1
    assert checkio('Dog,cat,mouse,bird.Human.') == 3
    print("Coding complete? Click 'Check' to earn cool rewards!")
