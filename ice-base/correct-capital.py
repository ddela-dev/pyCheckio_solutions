def correct_capital(line: str) -> bool:
    if line.upper() == line:
        return True

    if line.lower() == line:
        return True

    if line[0].upper() + line[1:].lower() == line:
        return True

    return False


print("Example:")
print(correct_capital("Checkio"))

assert correct_capital("Checkio") == True
assert correct_capital("CheCkio") == False
assert correct_capital("CHECKIO") == True

print("The mission is done! Click 'Check Solution' to earn rewards!")