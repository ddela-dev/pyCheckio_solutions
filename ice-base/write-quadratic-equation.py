def aaa(a):
    if a == 1 or a == -1:
        a = str(a).replace('1', '')
    else:
        a = str(a) + '*'
    return str(a) + 'x**2 '


def bbb(b, a):
    r = ''
    if b == 0:
        return r
    if a > 0:
        r += '- '
    else:
        r += '+ '

    if b == 1 or b == -1:
        b = str(abs(b)).replace('1', '')
    else:
        b = str(abs(b)) + '*'

    return r + b + 'x '


def ccc(c):
    r = ''
    if c == 0:
        return r
    if c < 0:
        r += '- '
    else:
        r += '+ '

    return r + str(abs(c)) + ' '


def quadr_equation(data: list[int]) -> str:
    # your code here
    a = data[0]
    b = data[1]
    c = data[2] if len(data) > 2 else data[1]

    if data[0] == 0:
        return 0

    st = str(data[0]) + '*x**2 '

    return aaa(a) + bbb(a * (b + c), a) + ccc(a * (b * c)) + '= 0'


print("Example:")
print(quadr_equation([2, 4, 6]))

assert quadr_equation([2, 4, 6]) == "2*x**2 - 20*x + 48 = 0"
assert quadr_equation([-2, 4, 6]) == "-2*x**2 + 20*x - 48 = 0"
assert quadr_equation([2, 4, -4]) == "2*x**2 - 32 = 0"
assert quadr_equation([2, 4, 0]) == "2*x**2 - 8*x = 0"
assert quadr_equation([2, 0]) == "2*x**2 = 0"
assert quadr_equation([2, 4]) == "2*x**2 - 16*x + 32 = 0"

print("The mission is done! Click 'Check Solution' to earn rewards!")