def checkio(text, word):
    import numpy as np

    text = text.replace(" ", "")
    rows = text.split("\n")
    grid = []
    for r in rows:
        chars = list(r)
        grid.append(chars)
    longest = 0
    for i in grid:
        if len(i) > longest:
            longest = len(i)
    for g in grid:
        while len(g) < longest:
            g.append(0)
    grod = []
    for g in grid:
        line = ''
        for c in g:
            line += str(c)
        grod.append(line)

    print(grod)
    rownum = 0
    colnum = 0
    for r in rows:
        rownum += 1
        if (r.find(word) != -1):
            colnum = r.find(word) + 1
            print(word, rownum, colnum, rownum, colnum + len(word) - 1)
            return [rownum, colnum, rownum, colnum + len(word) - 1]

    rownum = 0
    colnum = 0
    for i in range(len(grod[0])):
        colnum += 1
        line = ''
        for j in range(len(grod)):
            line += str(grod[j][i])
        if (line.upper().find(word.upper()) != -1):
            rownum = line.upper().find(word.upper()) + 1
            return [rownum, colnum, rownum + len(word) - 1, colnum]


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("""DREAMING of apples on a wall,
And dreaming often, dear,
I dreamed that, if I counted all,
-How many would appear?""", "ten") == [2, 14, 2, 16]
    assert checkio("""He took his vorpal sword in hand:
Long time the manxome foe he sought--
So rested he by the Tumtum tree,
And stood awhile in thought.
And as in uffish thought he stood,
The Jabberwock, with eyes of flame,
Came whiffling through the tulgey wood,
And burbled as it came!""", "noir") == [4, 16, 7, 16]
print("Coding complete? Click 'Check' to earn cool rewards!")
