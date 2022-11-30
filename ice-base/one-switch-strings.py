def switch_strings(line: str, result: str) -> bool:
    line=list(line)
    result=list(result)
    for x in range(len(line)):
        for y in range(len(line)):
            aux=[]
            for l in line:
                aux.append(l)
            aux[x]=line[y]
            aux[y]=line[x]
            if result==aux:
                return True
    return False


print("Example:")
print(switch_strings("btry", "byrt"))

assert switch_strings("btry", "byrt") == True
assert switch_strings("boss", "boss") == True
assert switch_strings("solid", "disel") == False
assert switch_strings("false", "flaes") == False
assert switch_strings("true", "treu") == True

print("The mission is done! Click 'Check Solution' to earn rewards!")