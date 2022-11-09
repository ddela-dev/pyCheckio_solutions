def get_neigbours(matrix,curr,mycell):
    ret=[]
    for i in range(-1,2):
        if i ==0:
            continue
        if 0 <= curr[0]+i <= len(matrix)-1:
            if matrix[curr[0]+i][curr[1]] == mycell:
                ret.append([curr[0]+i,curr[1]])
        if 0 <= curr[1]+i <= len(matrix[0])-1:
            if matrix[curr[0]][curr[1]+i] == mycell:
                ret.append([curr[0],curr[1]+i])
    return ret


def can_pass(matrix, first, second):
    first=list(first)
    second=list(second)
    mycell=matrix[first[0]][first[1]]

    path=[first]
    for p in path:
        for n in get_neigbours(matrix,p,mycell):
            if n not in path:
                path.append(n)

    print(path)
    return second in path


if __name__ == '__main__':
    assert can_pass(((0, 0, 0, 0, 0, 0),
                     (0, 2, 2, 2, 3, 2),
                     (0, 2, 0, 0, 0, 2),
                     (0, 2, 0, 2, 0, 2),
                     (0, 2, 2, 2, 0, 2),
                     (0, 0, 0, 0, 0, 2),
                     (2, 2, 2, 2, 2, 2),),
                    (3, 2), (0, 5)) == True, 'First example'
    assert can_pass(((0, 0, 0, 0, 0, 0),
                     (0, 2, 2, 2, 3, 2),
                     (0, 2, 0, 0, 0, 2),
                     (0, 2, 0, 2, 0, 2),
                     (0, 2, 2, 2, 0, 2),
                     (0, 0, 0, 0, 0, 2),
                     (2, 2, 2, 2, 2, 2),),
                    (3, 3), (6, 0)) == False, 'First example'
