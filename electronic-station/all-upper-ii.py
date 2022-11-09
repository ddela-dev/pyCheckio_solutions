def is_all_upper(text: str) -> bool:
    def numchar(text: str) -> bool:
        for i in text:
            if i == " ":
                continue
            if not i.isdigit():
                return True
        return False

    text = text.replace("  ", "")
    return numchar(text) and text.upper() == text and (text != "" and text != " ")


if __name__ == "__main__":
    print("Example:")
    print(is_all_upper("ALL UPPER"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_all_upper("ALL UPPER") == True
    assert is_all_upper("all lower") == False
    assert is_all_upper("mixed UPPER and lower") == False
    assert is_all_upper("     ") == False
    print("Coding complete? Click 'Check' to earn cool rewards!")