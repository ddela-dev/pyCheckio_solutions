def caps_lock(text: str) -> str:
    chars=list(text)
    new=""
    caps=False
    for c in chars:
        if c == "a":
            if caps:
                caps=False
            else:
                caps=True
        else:
            if caps:
                new+=c.upper()
            else:
                new+=c
    return new


if __name__ == "__main__":
    print("Example:")
    print(caps_lock("Why are you asking me that?"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert caps_lock("Why are you asking me that?") == "Why RE YOU sking me thT?"
    assert caps_lock("Always wanted to visit Zambia.") == "AlwYS Wnted to visit ZMBI."
    assert caps_lock("Aloha from Hawaii") == "Aloh FROM HwII"
    print("Coding complete? Click 'Check' to earn cool rewards!")
