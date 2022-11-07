def changing_direction(ele: list) -> int:
    changes = 0

    for i in range(len(ele) - 1):
        if ele[i] == ele[i + 1]:
            continue
        if ele[i] < ele[i + 1]:
            up = True
            break
        else:
            up = False
            break

    for i in range(len(ele) - 1):
        change = False
        if ele[i] == ele[i + 1]:
            print('equ')
            continue
        if up:
            if ele[i] < ele[i + 1]:
                print('up')
                continue
            if ele[i] > ele[i + 1]:
                print('down +1')
                up = False
                change = True
        else:
            if ele[i] > ele[i + 1]:
                print('down')
                continue
            if ele[i] < ele[i + 1]:
                print('up +1')
                up = True
                change = True

        changes += 1 if change else 0
    # your code here
    print('----------')
    return changes


print("Example:")
print(changing_direction([6, 6, 6, 4, 1, 2, 5, 9, 7, 8, 5, 9, 4, 2, 6]))

assert changing_direction([1, 2, 3, 4, 5]) == 0
assert changing_direction([1, 2, 3, 2, 1]) == 1
assert changing_direction([1, 2, 2, 1, 2, 2]) == 2

print("The mission is done! Click 'Check Solution' to earn rewards!")