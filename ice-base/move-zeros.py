def move_zeros(items: list[int]) -> list[int]:
    ret=[]
    for i in items:
        if i != 0:
            ret.append(i)
    for i in items:
        if i== 0:
            ret.append(0)
    return ret


print("Example:")
print(move_zeros([0, 1, 0, 3, 12]))

assert move_zeros([0, 1, 0, 3, 12]) == [1, 3, 12, 0, 0]
assert move_zeros([0]) == [0]

print("The mission is done! Click 'Check Solution' to earn rewards!")