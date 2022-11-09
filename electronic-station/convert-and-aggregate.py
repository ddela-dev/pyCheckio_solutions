def conv_aggr(data: list[tuple[str, int]]) -> dict[str, int]:
    dic={}
    for d in data:
        dic[d[0]]=0
    for d in data:
        dic[d[0]]+=d[1]
    newdic={}
    for d in dic:
        if dic[d] != 0 and d != '':
            newdic[d]=dic[d]
    return newdic


print("Example:")
print(conv_aggr([("a", 5), ("", 15)]))

assert conv_aggr([("a", 7), ("b", 8), ("a", 10)]) == {"a": 17, "b": 8}
assert conv_aggr([]) == {}
assert conv_aggr([("a", 5), ("a", -5)]) == {}
assert conv_aggr([("a", 5), ("a", 5), ("a", 0)]) == {"a": 10}
assert conv_aggr([("a", 5), ("", 15)]) == {"a": 5}

print("The mission is done! Click 'Check Solution' to earn rewards!")