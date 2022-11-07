from typing import List


def transpose(grid):
    transgrid = []
    for g in range(len(grid)):
        transrow = []
        for c in range(len(grid[g])):
            transrow.append(grid[c][g])
        transgrid.append(list(reversed(transrow)))
    return transgrid


def bingrid(grid):
    bingrid = []
    for g in grid:
        binrow = []
        for c in g:
            if c == 'X':
                binrow.append(1)
            if c == '.':
                binrow.append(0)
        bingrid.append(binrow)
    return bingrid


def recall_password(grille: List[str], password: List[str]) -> str:
    grille = bingrid(grille)
    pwd = ''
    for a in range(4):
        for y in range(len(password)):
            for x in range(len(password[y])):
                if grille[y][x] == 1:
                    pwd += password[y][x]
        grille = transpose(grille)

    return pwd


if __name__ == '__main__':
    print("Example:")
    print(recall_password(['X...', '..X.', 'X..X', '....'],
                          ['itdf', 'gdce', 'aton', 'qrdi']))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert recall_password(['X...', '..X.', 'X..X', '....'],
                           ['itdf', 'gdce', 'aton', 'qrdi']) == 'icantforgetiddqd'
    assert recall_password(['....', 'X..X', '.X..', '...X'],
                           ['xhwc', 'rsqx', 'xqzz', 'fyzr']) == 'rxqrwsfzxqxzhczy'
    print("Coding complete? Click 'Check' to earn cool rewards!")
