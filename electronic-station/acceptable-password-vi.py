def is_acceptable_password(pswrd: str) -> bool:
    def hasnum(q: str) -> bool:
        for i in q:
            if i.isdigit():
                return True
        return False

    def haschr(q: str) -> bool:
        for i in q:
            if i.isalpha():
                return True
        return False

    def notpas(q: str) -> bool:
        i = q.lower().find('password')
        return i == -1

    def hasdiff(q: str) -> bool:
        diff = []
        for i in q:
            if i not in diff:
                diff.append(i)
        return len(diff) >= 3

    def morethan(q: str, i: int) -> bool:
        return len(q) >= i

    return morethan(pswrd, 6) and (morethan(pswrd, 9) or (hasnum(pswrd) and haschr(pswrd))) and notpas(
        pswrd) and hasdiff(pswrd)


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
    assert is_acceptable_password("aaaaaa1") == False
    assert is_acceptable_password("aaaaaabbbbb") == False
    assert is_acceptable_password("aaaaaabb1") == True
    assert is_acceptable_password("abc1") == False
    assert is_acceptable_password("abbcc12") == True
    print("Coding complete? Click 'Check' to earn cool rewards!")
