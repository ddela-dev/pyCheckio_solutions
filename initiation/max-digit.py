def max_digit(number: int) -> int:
    maxdigit=0
    for i in range(len(str(number))):
        if maxdigit<number%10:
            maxdigit=number%10
        number//=10
    return maxdigit


if __name__ == '__main__':
    print("Example:")
    print(max_digit(634))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert max_digit(0) == 0
    assert max_digit(52) == 5
    assert max_digit(634) == 6
    assert max_digit(1) == 1
    assert max_digit(10000) == 1
    print("Coding complete? Click 'Check' to earn cool rewards!")
