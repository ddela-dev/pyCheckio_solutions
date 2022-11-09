import re


def unix_match(filename: str, pattern: str) -> bool:
    if filename == pattern:
        return True
    if '[]' in pattern:
        return False

    pattern = pattern.replace(".", r"\.")
    pattern = pattern.replace("*", ".*")
    pattern = pattern.replace("?", ".")
    pattern = pattern.replace("!", "^")

    return re.search(pattern, filename) is not None


if __name__ == "__main__":
    print("Example:")
    print(unix_match("somefile.txt", "*"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert unix_match("somefile.txt", "somefile.txt") == True
    assert unix_match("1name.txt", "[!abc]name.txt") == True
    assert unix_match("log1.txt", "log[!0].txt") == True
    assert unix_match("log1.txt", "log[1234567890].txt") == True
    assert unix_match("log1.txt", "log[!1].txt") == False
    print("Coding complete? Click 'Check' to earn cool rewards!")
