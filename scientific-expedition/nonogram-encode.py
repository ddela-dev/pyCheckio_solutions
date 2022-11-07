def printcol(arr):
    for a in arr:
        print(a)

def transpose(data):
    at = []
    for j in range(len(data[0])):
        row = []
        for i in range(len(data)):
            row.append(data[i][j])
        at.append(row)

    return at

def zeroboth(grid):
    aux = 0
    for g in grid:
        if len(g) > aux:
            aux = len(g)
    ret = []
    l=False
    for g in grid:
        bit = g
        for a in range(aux - len(g)):
            if l:
                bit = ' '+bit
            else:
                bit = bit+' '
            l= not l

        ret.append(bit)
    return ret

def addzero(grid):
    aux=0
    for g in grid:
        if len(g)>aux:
            aux=len(g)
    ret=[]
    for g in grid:
        bit=[]
        for a in range(aux-len(g)):
            bit.append(0)
        ret.append(bit+g)
    return ret

def extract(data):
    aa=[]
    for d in data:
        a=[]
        block=0
        for c in d:
            if c == 'X':
                block+=1
            else:
                if block != 0:
                    a.append(block)
                block=0
        if block != 0:
            a.append(block)
        aa.append(a)
    return aa

def nonogram_encode(data: list[str]) -> list:
    data = zeroboth(data)

    rowrow=extract(data)
    rowrow=addzero(rowrow)

    colcol=extract(transpose(data))
    colcol=addzero(colcol)
    colcol=transpose(colcol)

    return [colcol,rowrow]


print("Example:")
print(nonogram_encode(['XX X', ' X XXX', ' X XX ', ' XXX ', ' XXXX ', ' X ']))
print(nonogram_encode([" X X ", "X X X", " X X "]))

assert nonogram_encode([" X X ", "X X X", " X X "]) == [
    [[0, 1, 0, 1, 0], [1, 1, 1, 1, 1]],
    [[0, 1, 1], [1, 1, 1], [0, 1, 1]],
]
assert nonogram_encode(["X"]) == [[[1]], [[1]]]

print("The mission is done! Click 'Check Solution' to earn rewards!")