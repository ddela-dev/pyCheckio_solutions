def getunit(arr):
    units = []
    for a in range(len(arr) - 1):
        units.append(abs(arr[a] - arr[a + 1]))
    return min(units)


def missing_number(items: list[int]) -> int:
    unit = getunit(items)
    items = sorted(items)
    expected = items[0]

    for i in items:
        if expected == i:
            expected += unit
            continue
        return expected


print("Example:")
print(missing_number([1, 4, 2, 5]))

assert missing_number([1, 4, 2, 5]) == 3
assert missing_number([2, 6, 8]) == 4

print("The mission is done! Click 'Check Solution' to earn rewards!")