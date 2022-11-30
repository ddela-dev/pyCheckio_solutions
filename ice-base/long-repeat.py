def long_repeat(line: str) -> int:
    """
        length the longest substring that consists of the same char
    """
    same=0
    maxsame=0
    if len(line)>0:
        current=line[0]
        for l in list(line):
            if current == l:
                same+=1
            else:
                current=l
                same=1
            if same>maxsame:
                maxsame=same
        return maxsame
    else:
        return 0

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert long_repeat('sdsffffse') == 4, "First"
    assert long_repeat('ddvvrwwwrggg') == 3, "Second"
    assert long_repeat('abababaab') == 2, "Third"
    assert long_repeat('') == 0, "Empty"
    print('"Run" is good. How is "Check"?')
