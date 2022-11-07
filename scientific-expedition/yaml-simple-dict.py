def yaml(a):
    y={}
    lines=a.split('\n')
    for l in lines:
        if l =='':
            continue
        d=l.split(':')
        for i in range(len(d)):
            d[i]=d[i].strip()
            if d[i].isdigit():
                d[i]=int(d[i])
        y[d[0]]=d[1]
    return y


if __name__ == '__main__':
    print("Example:")
    print(yaml("""name: Alex
age: 12"""))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert yaml("""name: Alex
age: 12""") == {'age': 12, 'name': 'Alex'}
    assert yaml("""name: Alex Fox
age: 12

class: 12b""") == {'age': 12,
 'class': '12b',
 'name': 'Alex Fox'}
    print("Coding complete? Click 'Check' to earn cool rewards!")
