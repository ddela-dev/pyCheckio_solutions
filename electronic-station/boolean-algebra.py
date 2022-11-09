OPERATION_NAMES = ("conjunction", "disjunction", "implication", "exclusive", "equivalence")

def boolean(x, y, operation):
    if operation =='conjunction':
        return x and y
    elif operation =='disjunction':
        return x or y
    elif operation =='implication':
        if x:
            return y
        else:
            return not x
    elif operation =='exclusive':
        if x:
            if y:
                return False
            else:
                return True
        else:
            if y:
                return True
            else:
                return False
    elif operation =='equivalence':
        return x==y

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert boolean(1, 0, "conjunction") == 0, "and"
    assert boolean(1, 0, "disjunction") == 1, "or"
    assert boolean(1, 1, "implication") == 1, "material"
    assert boolean(0, 1, "exclusive") == 1, "xor"
    assert boolean(0, 1, "equivalence") == 0, "same?"
    print('All good! Go and check the mission.')
