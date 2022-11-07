def to_camel_case(name: str) -> str:
    chars=list(name)
    new=chars[0].upper()
    skip=True
    for c in range(len(chars)):
        if skip:
            skip=False
        else:
            if chars[c]=="_":
                new+=chars[c+1].upper()
                skip=True
            else:
                new+=chars[c]
    return new

if __name__ == '__main__':
    print("Example:")
    print(to_camel_case('my_function_name'))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert to_camel_case("my_function_name") == "MyFunctionName"
    assert to_camel_case("i_phone") == "IPhone"
    assert to_camel_case("this_function_is_empty") == "ThisFunctionIsEmpty"
    assert to_camel_case("name") == "Name"
    print("Coding complete? Click 'Check' to earn cool rewards!")

