def frequency_sort(items):
    if (len(items)!=0):
        dic={items[0]:0}
        for i in items:
            dic[i]=0
        for i in items:
            dic[i]+=1
        dic2=dict(sorted(dic.items(),key= lambda x:x[1], reverse=True))
        newitems=[]
        for d in dic2:
            for i in range(dic2[d]):
                newitems.append(d)
        return newitems
    else:
        return items


if __name__ == '__main__':
    print("Example:")
    print(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4])) == [4, 4, 4, 4, 6, 6, 2, 2]
    assert list(frequency_sort(['bob', 'bob', 'carl', 'alex', 'bob'])) == ['bob', 'bob', 'bob', 'carl', 'alex']
    assert list(frequency_sort([17, 99, 42])) == [17, 99, 42]
    assert list(frequency_sort([])) == []
    assert list(frequency_sort([1])) == [1]
    print("Coding complete? Click 'Check' to earn cool rewards!")
