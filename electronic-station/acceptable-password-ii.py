def is_acceptable_password(password: str) -> bool:

    hasnum=False
    if len(password)>6:
        for i in password:
            if i.isdigit():
                hasnum=True
    return hasnum


if __name__ == "__main__":
    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_acceptable_password("short") == False
    assert is_acceptable_password("muchlonger") == False
    assert is_acceptable_password("ashort") == False
    assert is_acceptable_password("muchlonger5") == True
    assert is_acceptable_password("sh5") == False
    print("Coding complete? Click 'Check' to earn cool rewards!")
