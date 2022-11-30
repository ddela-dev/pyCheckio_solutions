def feeded(pidgeons):
    count=0
    for p in pidgeons:
        if pidgeons[p]!=0:
            count+=1
    return count

def checkio(food: int) -> int:
    pidgeons={}
    for f in range(food):
        pidgeons[f]=0

    curr=1
    minute=1
    while food>0:
        minute+=1
        for i in range(curr):
            if food>0:
                food -= 1
                pidgeons[i]+=1
        curr+=minute

    return feeded(pidgeons)

print("Example:")
print(checkio(18))

assert checkio(1) == 1
assert checkio(3) == 2
assert checkio(5) == 3
assert checkio(10) == 6

print("The mission is done! Click 'Check Solution' to earn rewards!")
