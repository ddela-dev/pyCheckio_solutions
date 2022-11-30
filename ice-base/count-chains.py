from typing import List, Tuple
import math


def dis(p1, p2):
    return math.sqrt(math.pow((p1[0] - p2[0]), 2) + math.pow((p1[1] - p2[1]), 2))


def sec(c1, c2):
    if c1[0] == c2[0] and c1[1] == c2[1]:
        return False
    if dis(c1, c2) + c1[2] <= c2[2] or dis(c1, c2) + c2[2] <= c1[2]:
        return False
    return dis(c1, c2) - c1[2] < c2[2]


def count_chains(c: List[Tuple[int, int, int]]) -> int:
    chains = []
    for j in c:
        chain = [j]
        for k in c:
            if j == k:
                continue
            else:
                if sec(j, k):
                    chain.append(k)
        chains.append(chain)

    for c in chains:
        c = c.sort()

    out = []
    while len(chains) > 0:
        first, *rest = chains
        first = set(first)

        lf = -1
        while len(first) > lf:
            lf = len(first)

            rest2 = []
            for r in rest:
                if len(first.intersection(set(r))) > 0:
                    first |= set(r)
                else:
                    rest2.append(r)
            rest = rest2

        out.append(first)
        chains = rest
    print(out)

    return len(out)


if __name__ == '__main__':
    print("Example:")
    print(count_chains([(0, 0, 1), (-1, 1, 1), (1, -1, 1), (-2, -2, 1)]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert count_chains([(1, 1, 1), (4, 2, 1), (4, 3, 1)]) == 2, 'basic'
    assert count_chains([(1, 1, 1), (2, 2, 1), (3, 3, 1)]) == 1, 'basic #2'
    assert count_chains([(2, 2, 2), (4, 2, 2), (3, 4, 2)]) == 1, 'trinity'
    assert count_chains([(2, 2, 1), (2, 2, 2)]) == 2, 'inclusion'
    assert count_chains([(1, 1, 1), (1, 3, 1), (3, 1, 1), (3, 3, 1)]) == 4, 'adjacent'
    assert count_chains([(0, 0, 1), (-1, 1, 1), (1, -1, 1), (-2, -2, 1)]) == 2, 'negative coordinates'
    print("Coding complete? Click 'Check' to earn cool rewards!")
