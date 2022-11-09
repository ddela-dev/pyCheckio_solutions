from typing import List


def flipv(arr):
    return arr[::-1]


def transpose(data: List[List[int]]) -> List[List[int]]:
    at = []
    for j in range(len(data[0])):
        row = []
        for i in range(len(data)):
            row.append(data[i][j])
        at.append(row)
    return at


def get_row(arr):
    row = ''
    for aa in arr:
        for a in aa:
            row += str(a)
    return row


def get_diagonal(arr):
    n = len(arr)
    m = len(arr[0])
    res = []
    for d in range(n + m - 1):
        cur = ""
        for x in range(max(0, d - m + 1), min(n, d + 1)):
            cur = str(arr[x][d - x]) + cur
        res.append(cur)
    return res


def checkio(matrix: List[List[int]]) -> bool:
    nums = []
    for i in range(1, 10):
        nums.append(str(i) * 4)

    for n in nums:
        if n in get_row(matrix):
            return True
        if n in get_row(transpose(matrix)):
            return True
        for ns in get_diagonal(matrix):
            if n in ns:
                return True
        for sn in get_diagonal(flipv(matrix)):
            if n in sn:
                return True
    return False


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        [1, 2, 1, 1],
        [1, 1, 4, 1],
        [1, 3, 1, 6],
        [1, 7, 2, 5]
    ]) == True
    assert checkio([
        [7, 1, 4, 1],
        [1, 2, 5, 2],
        [3, 4, 1, 3],
        [1, 1, 8, 1]
    ]) == False
    assert checkio([
        [2, 1, 1, 6, 1],
        [1, 3, 2, 1, 1],
        [4, 1, 1, 3, 1],
        [5, 5, 5, 5, 5],
        [1, 1, 3, 1, 1]
    ]) == True
    assert checkio([
        [7, 1, 1, 8, 1, 1],
        [1, 1, 7, 3, 1, 5],
        [2, 3, 1, 2, 5, 1],
        [1, 1, 1, 5, 1, 4],
        [4, 6, 5, 1, 3, 1],
        [1, 1, 9, 1, 2, 1]
    ]) == True
    assert checkio([
        [2, 3, 6, 5, 6, 2, 8, 3, 7, 4],
        [6, 9, 5, 9, 7, 6, 8, 5, 1, 6],
        [6, 8, 2, 6, 1, 9, 3, 6, 6, 4],
        [5, 8, 3, 2, 3, 8, 7, 4, 6, 4],
        [2, 3, 1, 4, 5, 1, 2, 5, 6, 9],
        [5, 4, 8, 7, 5, 5, 8, 4, 9, 5],
        [9, 7, 9, 9, 5, 9, 9, 8, 1, 2],
        [5, 1, 7, 4, 8, 3, 4, 1, 8, 8],
        [5, 3, 3, 2, 6, 1, 4, 3, 8, 8],
        [4, 8, 1, 4, 5, 8, 8, 7, 4, 7]
    ]) == True
    print('All Done! Time to check!')
