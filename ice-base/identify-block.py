def rotate( m ):
    return [[m[j][i] for j in range(len(m))] for i in range(len(m[0])-1,-1,-1)]

def transpose(data):
    at = []
    for j in range(len(data[0])):
        row = []
        for i in range(len(data)):
            row.append(data[i][j])
        at.append(row)
    return at


def tobit(block):
    grid = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    bitmap = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            for b in block:
                if grid[i][j] == b:
                    bitmap[i][j] = 1
    return bitmap


def allzero(arr):
    for a in arr:
        if a != 0:
            return False
    return True


def crop(grid):
    croped=[]
    aux=[]
    for g in grid:
        if not allzero(g):
            aux.append(g)
    for a in transpose(aux):
        if not allzero(a):
            croped.append(a)
    return transpose(croped)

def identify_block(numbers):
    if numbers in [{1,4,13,16},{5,8,9,12}]:
        return None
    block_I=[[1,1,1,1]]
    block_J=[[1,1,1],[0,0,1]]
    block_L=[[0,0,1],[1,1,1]]
    block_O=[[1,1],[1,1]]
    block_S=[[0,1,1],[1,1,0]]
    block_T=[[0,1,0],[1,1,1]]
    block_Z=[[1,1,0],[0,1,1]]
    croped=crop(tobit(numbers))
    north = croped
    east = rotate(croped)
    south = rotate(rotate(croped))
    west = rotate(rotate(rotate(croped)))

    for dir in [north,east,south,west]:
        print(dir)
        if dir == block_I:
            return 'I'
        if dir == block_J:
            return 'J'
        if dir == block_L:
            return 'L'
        if dir == block_O:
            return 'O'
        if dir == block_S:
            return 'S'
        if dir == block_T:
            return 'T'
        if dir == block_Z:
            return 'Z'

    return None


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert identify_block({10, 13, 14, 15}) == 'T', 'T'
    assert identify_block({1, 5, 9, 6}) == 'T', 'T'
    assert identify_block({2, 3, 7, 11}) == 'L', 'L'
    assert identify_block({4, 8, 12, 16}) == 'I', 'I'
    assert identify_block({3, 1, 5, 8}) == None, 'None'
    print('"Run" is good. How is "Check"?')
