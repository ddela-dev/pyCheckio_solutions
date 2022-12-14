from typing import Tuple


def follow(instructions: str) -> Tuple[int, int]:
    steps = list(instructions)
    v = 0
    h = 0
    for s in steps:
        if s == "f":
            v += 1
        elif s == "b":
            v -= 1
        elif s == "l":
            h -= 1
        elif s == "r":
            h += 1
    return (h, v)


if __name__ == '__main__':
    print("Example:")
    print(follow("fflff"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert follow("fflff") == (-1, 4)
    assert follow("ffrff") == (1, 4)
    assert follow("fblr") == (0, 0)
    print("Coding complete? Click 'Check' to earn cool rewards!")
