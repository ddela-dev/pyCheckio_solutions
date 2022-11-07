import math
def split_list(items: list) -> list:
    h1=[]
    h2=[]
    half=math.ceil(len(items)/2)
    indaux=0
    for i in items:
        if indaux<half:
            h1.append(i)
        else:
            h2.append(i)
        indaux+=1
    return [h1,h2]


if __name__ == '__main__':
    print("Example:")
    print(split_list([1, 2, 3, 4, 5, 6]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert split_list([1, 2, 3, 4, 5, 6]) == [[1, 2, 3], [4, 5, 6]]
    assert split_list([1, 2, 3]) == [[1, 2], [3]]
    assert split_list([1, 2, 3, 4, 5]) == [[1, 2, 3], [4, 5]]
    assert split_list([1]) == [[1], []]
    assert split_list([]) == [[], []]
    print("Coding complete? Click 'Check' to earn cool rewards!")
