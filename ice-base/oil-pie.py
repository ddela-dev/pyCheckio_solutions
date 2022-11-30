from fractions import Fraction as fra


def divide_pie(groups):
    d = 0
    for g in groups:
        d += abs(g)

    org = fra(d, d)

    for g in groups:
        if g > 0:
            org -= fra(abs(g), d)
        else:
            org -= org / fra(d, abs(g))

    f = str(org).split('/')

    for i in range(len(f)):
        # r.append(int(l))
        f[i] = int(f[i])

    if f[0] == 0:
        return tuple([0, 1])

    return tuple(f)


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert isinstance((2, -2), (tuple, list)), "Return tuple or list"
    assert tuple(divide_pie((2, -1, 3))) == (1, 18), "Example"
    assert tuple(divide_pie((1, 2, 3))) == (0, 1), "All know about the pie"
    assert tuple(divide_pie((-1, -1, -1))) == (8, 27), "One by one"
    assert tuple(divide_pie((10,))) == (0, 1), "All together"
