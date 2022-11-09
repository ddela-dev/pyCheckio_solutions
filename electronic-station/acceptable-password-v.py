def is_acceptable_password(password: str) -> bool:

    hasnum=False
    haschr=False
    haspas=password.lower().find('password')
    if haspas > -1:
        return False
    else:
        if len(password)>6:
            if len(password)>9:
                return True
            else:
                for i in password:
                    if i.isdigit():
                        hasnum=True
                    if i.isalpha():
                        haschr=True
    return hasnum and haschr


if __name__ == "__main__":
    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_acceptable_password("short") == False
    assert is_acceptable_password("short54") == True
    assert is_acceptable_password("muchlonger") == True
    assert is_acceptable_password("ashort") == False
    assert is_acceptable_password("muchlonger5") == True
    assert is_acceptable_password("sh5") == False
    assert is_acceptable_password("1234567") == False
    assert is_acceptable_password("12345678910") == True
    assert is_acceptable_password("password12345") == False
    assert is_acceptable_password("PASSWORD12345") == False
    assert is_acceptable_password("pass1234word") == True
    print("Coding complete? Click 'Check' to earn cool rewards!")
