from typing import List


def letter_queue(commands: List[str]) -> str:
    txt=''
    for c in commands:
        if c == 'POP':
            txt=txt[1::]
        else:
            txt+=c[len(c)-1]
    return txt


if __name__ == '__main__':
    print("Example:")
    print(letter_queue(['PUSH A',
        'POP',
        'POP',
        'PUSH Z',
        'PUSH D',
        'PUSH O',
        'POP',
        'PUSH T']))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert letter_queue(['PUSH A',
        'POP',
        'POP',
        'PUSH Z',
        'PUSH D',
        'PUSH O',
        'POP',
        'PUSH T']) == 'DOT'
    assert letter_queue(['POP', 'POP']) == ''
    assert letter_queue(['PUSH H', 'PUSH I']) == 'HI'
    assert letter_queue([]) == ''
    print("Coding complete? Click 'Check' to earn cool rewards!")
