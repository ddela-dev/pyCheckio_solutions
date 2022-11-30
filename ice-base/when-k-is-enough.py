from typing import Iterable


def remove_after_kth(items: list, k: int) -> Iterable:
    ret = []
    if k == 0:
        return ret

    dic = {}
    for i in items:
        dic[i] = 0

    for i in items:
        if dic[i] < k:
            ret.append(i)
            dic[i] += 1

    return ret


print("Example:")
print(list(remove_after_kth([42, 42, 42, 42, 42, 42, 42], 3)))

assert list(remove_after_kth([42, 42, 42, 42, 42, 42, 42], 3)) == [42, 42, 42]
assert list(remove_after_kth([42, 42, 42, 99, 99, 17], 0)) == []
assert list(remove_after_kth([1, 1, 1, 2, 2, 2], 5)) == [1, 1, 1, 2, 2, 2]

print("The mission is done! Click 'Check Solution' to earn rewards!")
