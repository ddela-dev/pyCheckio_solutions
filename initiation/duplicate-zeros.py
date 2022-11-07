def duplicate_zeros(donuts: list) -> list:
    ret=[]
    for d in donuts:
        if d==0:
            ret.append(d)
        ret.append(d)
    return ret


print("Example:")
print(duplicate_zeros([1, 0, 2, 3, 0, 4, 5, 0]))

assert duplicate_zeros([1, 0, 2, 3, 0, 4, 5, 0]) == [1, 0, 0, 2, 3, 0, 0, 4, 5, 0, 0]
assert duplicate_zeros([0, 0, 0, 0]) == [0, 0, 0, 0, 0, 0, 0, 0]
assert duplicate_zeros([100, 10, 0, 101, 1000]) == [100, 10, 0, 0, 101, 1000]

print("The mission is done! Click 'Check Solution' to earn rewards!")