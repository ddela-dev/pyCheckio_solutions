def checkio(time_string: str) -> str:
    nums = time_string.split(":")
    morse_time = ""

    hour = list(nums[0])
    if (len(hour) == 2):
        bh0 = str(bin(int(hour[0])))[2:]
        bh1 = str(bin(int(hour[1])))[2:]
    else:
        bh0 = "0"
        bh1 = str(bin(int(hour[0])))[2:]
    bin_hour0 = toBin(bh0, 2)
    bin_hour1 = toBin(bh1, 4)
    morse_hour = toMorse(bin_hour0) + " " + toMorse(bin_hour1)

    mins = list(nums[1])
    if (len(mins) == 2):
        bm0 = str(bin(int(mins[0])))[2:]
        bm1 = str(bin(int(mins[1])))[2:]
    else:
        bm0 = "0"
        bm1 = str(bin(int(mins[0])))[2:]
    bin_min0 = toBin(bm0, 3)
    bin_min1 = toBin(bm1, 4)
    morse_mins = toMorse(bin_min0) + " " + toMorse(bin_min1)

    secs = list(nums[2])
    if (len(secs) == 2):
        bs0 = str(bin(int(secs[0])))[2:]
        bs1 = str(bin(int(secs[1])))[2:]
    else:
        bs0 = "0"
        bs1 = str(bin(int(secs[0])))[2:]
    bin_sec0 = toBin(bs0, 3)
    bin_sec1 = toBin(bs1, 4)
    morse_secs = toMorse(bin_sec0) + " " + toMorse(bin_sec1)

    morse_time = morse_hour + " : " + morse_mins + " : " + morse_secs
    return morse_time


def toBin(s: str, n: int) -> str:
    aux = ""
    if (len(s) < n):
        for i in range(len(s), n):
            aux += "0"
    return aux + s


def toMorse(b: str) -> str:
    morse_str = ""
    for t in b:
        if (t == "0"):
            morse_str += "."
        else:
            morse_str += "-"
    return morse_str

    return ".- .... : .-- .--- : -.. -..-"


if __name__ == '__main__':
    print("Example:")
    print(checkio("10:37:49"))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("10:37:49") == ".- .... : .-- .--- : -.. -..-", "First Test"
    assert checkio("21:34:56") == "-. ...- : .-- .-.. : -.- .--.", "Second Test"
    assert checkio("00:1:02") == ".. .... : ... ...- : ... ..-.", "Third Test"
    assert checkio("23:59:59") == "-. ..-- : -.- -..- : -.- -..-", "Fourth Test"
    print("Coding complete? Click 'Check' to earn cool rewards!")
